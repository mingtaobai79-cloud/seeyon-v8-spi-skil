# CFR 反编译与 Jar 发现工作流

> 从 SKILL.md 下沉。用于 Contract First 时从 jar/class 提取 FACT 契约。

## CFR 反编译工作流（Windows 实战）

**关键：必须先提取 .class 文件，再反编译。直接传 jar 给 CFR 会输出全部内容（13000+ 行）。**

```python
import subprocess, os, tempfile

skill_root = os.environ.get("SEEYON_V8_SPI_SKILL_ROOT", "<seeyon-v8-spi-skill-root>")
cfr = os.path.join(skill_root, "references", "contract-index", "tools", "cfr.jar")
jar = r"${LOCAL_MAVEN_REPO}\com\seeyon\boot-starter-file\5.3.358\boot-starter-file-5.3.358.jar"
tmpdir = tempfile.mkdtemp()

# 1. 列出 jar 内容，找到目标 class
result = subprocess.run(['jar', 'tf', jar], capture_output=True, text=True, timeout=30)
entries = result.stdout.strip().split('\n')
target = [e for e in entries if 'StorageSpi' in e and e.endswith('.class')][0]

# 2. 提取 class 到临时目录
subprocess.run(['jar', 'xf', jar, target], cwd=tmpdir, capture_output=True, timeout=30)

# 3. 反编译提取的 class 文件
cls_path = os.path.join(tmpdir, target)
r = subprocess.run(['java', '-jar', cfr, cls_path], capture_output=True, text=True, timeout=60)
print(r.stdout)
```

## Jar 发现路径

Jar 路径是现场输入，不写死用户本地环境。优先级：

1. 用户提供的源码 / jar / 反编译结果。
2. 目标工程 POM / `.idea` / Maven settings 中可发现的本地仓库或私服。
3. 用户明确提供的 Artifactory/Nexus URL。
4. 项目 `lib` / `third-jar` 等随工程交付目录。

占位符示例：`${LOCAL_MAVEN_REPO}\com\seeyon\{artifactId}\{version}\{artifactId}-{version}.jar`。
