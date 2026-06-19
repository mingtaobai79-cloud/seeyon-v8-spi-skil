import json
import tempfile
import unittest
from pathlib import Path

import sys

ROOT = next(p for p in Path(__file__).resolve().parents if (p / "SKILL.md").exists())
sys.path.insert(0, str(ROOT / "references" / "contract-index" / "tools"))

import decompile_jar


SAMPLE_JAVA = r'''
package com.seeyon.ctp.user.api.sso;

@CtpUserComment("统一认证服务")
public interface CtpUserSsoAuthProviderService {
    @CtpUserComment("参数 key")
    public String getRequestParaKey();

    @CtpUserComment("获取用户信息")
    public CtpUserSpiLoginUserInfoDto getUserLoginInfo(HttpServletRequest request, String encodeRedirectUrl) throws CtpUserSpiSsoException, SpiAuthContinueException;

    default void setServerEnv(CtpUserSpiServerEnvDto env) {
    }
}
'''

DTO_JAVA = r'''
package com.seeyon.ctp.user.dto;

public class CtpAvoidLoginUserInfoDto {
    @DtoAttribute(value="三方用户编码")
    private String thirdUserCode;
}
'''


class JarContractIndexTests(unittest.TestCase):
    def test_parse_artifact_and_version_from_common_jar_name(self):
        parsed = decompile_jar.parse_artifact_version("ctp-user-api-5.3.351.jar")
        self.assertEqual(parsed["artifact_id"], "ctp-user-api")
        self.assertEqual(parsed["version"], "5.3.351")

    def test_extract_contracts_returns_structured_methods_and_fields(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            src = root / "com" / "seeyon" / "ctp" / "user" / "api" / "sso"
            dto = root / "com" / "seeyon" / "ctp" / "user" / "dto"
            src.mkdir(parents=True)
            dto.mkdir(parents=True)
            (src / "CtpUserSsoAuthProviderService.java").write_text(SAMPLE_JAVA, encoding="utf-8")
            (dto / "CtpAvoidLoginUserInfoDto.java").write_text(DTO_JAVA, encoding="utf-8")

            contracts = decompile_jar.extract_contracts(str(root))
            by_name = {c["name"]: c for c in contracts}

            service = by_name["CtpUserSsoAuthProviderService"]
            self.assertEqual(service["fqn"], "com.seeyon.ctp.user.api.sso.CtpUserSsoAuthProviderService")
            self.assertEqual(service["domain_hint"], "sso.unifiedauth")
            self.assertTrue(any(m["method_name"] == "getUserLoginInfo" for m in service["methods"]))
            method = next(m for m in service["methods"] if m["method_name"] == "getUserLoginInfo")
            self.assertEqual(method["return_type"], "CtpUserSpiLoginUserInfoDto")
            self.assertEqual([p["type"] for p in method["params"]], ["HttpServletRequest", "String"])
            self.assertEqual(method["throws"], ["CtpUserSpiSsoException", "SpiAuthContinueException"])

            dto_contract = by_name["CtpAvoidLoginUserInfoDto"]
            self.assertTrue(any(f["field_name"] == "thirdUserCode" for f in dto_contract["fields"]))

    def test_index_writer_creates_queryable_jsonl_files(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            index_root = root / "indexes"
            jar = root / "ctp-user-api-5.3.351.jar"
            jar.write_bytes(b"fake jar bytes")
            java_root = root / "decompiled"
            java_pkg = java_root / "com" / "seeyon" / "ctp" / "user" / "api" / "sso"
            java_pkg.mkdir(parents=True)
            (java_pkg / "CtpUserSsoAuthProviderService.java").write_text(SAMPLE_JAVA, encoding="utf-8")

            meta = decompile_jar.index_decompiled_dir(str(jar), str(java_root), str(index_root))

            jar_dir = index_root / "by-sha256" / meta["sha256"]
            self.assertTrue((jar_dir / "jar-meta.json").exists())
            self.assertTrue((jar_dir / "contracts.jsonl").exists())
            self.assertTrue((jar_dir / "methods.jsonl").exists())
            self.assertTrue((jar_dir / "contract.md").exists())

            symbol_hits = decompile_jar.query_index(str(index_root), symbol="CtpUserSsoAuthProviderService")
            self.assertEqual(len(symbol_hits["symbols"]), 1)
            method_hits = decompile_jar.query_index(str(index_root), method="getUserLoginInfo")
            self.assertEqual(len(method_hits["methods"]), 1)


if __name__ == "__main__":
    unittest.main()
