# FanRuan FineReport public SSO notes

> Session-derived reference for generating Seeyon V8 -> FineReport SSO connector implementations.

## Scope

Use this when the user asks for V8 / Seeyon / 致远 to single-sign-on into FanRuan FineReport / 帆软 / 决策平台.

Route to:

- Auth-SSO domain
- V8 -> third-party SSO / `SsoService`
- Super SPI module: `spi-sso`
- Runtime scope: `cip-connector`

## Evidence levels

| Item | Evidence | Source / locator |
|---|---|---|
| Seeyon `SsoService` signature, `spring.factories` key, `cip-connector` scope | FACT | `references/auth-sso/sso-connector/README.md` / `cip-connector-api` contract |
| FineReport frontend SSO endpoint shape | OBSERVATION | FanRuan public help doc `doc-view-884`, title: 前台单点登录接口 |
| Token/cookie behavior after FineReport login | OBSERVATION | FanRuan public help doc `doc-view-884` |

Do not mark FineReport public doc observations as FACT unless a site jar/source/OpenAPI/plugin contract confirms them.

## Public FineReport frontend SSO endpoint

The public frontend SSO interface observed in FanRuan docs is:

```text
GET /webroot/decision/login/cross/domain?fine_username=XX&fine_password=XX&validity=-2&callback=
```

Common full URL form:

```text
http://<host>:<port>/webroot/decision/login/cross/domain?fine_username=<user>&fine_password=<password>&validity=-2&callback=
```

Notes from the public doc:

- `fine_username` is required.
- `fine_password` is required.
- `validity` is commonly shown as `-2`.
- Login success writes token/cookie in the browser context.
- URL credentials should be URL-encoded.
- Embedded iframe / cross-domain usage may require FineReport security settings changes such as content sniffing / clickjacking protection, depending on site policy.

## Generation pattern

For Seeyon V8 -> FineReport:

1. Generate a Super SPI project, not a loose single-module project.
2. Implement `com.seeyon.cip.connector.api.sso.SsoService` in `spi-sso`.
3. Register with:

```properties
com.seeyon.cip.connector.api.sso.SsoService=\
com.seeyon.extend.spi.sso.connector.finereport.finereportSsoServiceImpl
```

4. Keep `spi_info.json` scoped to `cip-connector` for this connector scenario, even if the generic validator warns that `ALL` is the broad default.
5. Class name must equal `getName() + "SsoServiceImpl"`. If `getName()` returns `finereport`, the class name should be exactly `finereportSsoServiceImpl`.
6. Do not put SPI registration files in `spi-common`.
7. Avoid Spring stereotype/injection annotations and avoid unverified third-party helpers.

## Credential boundary / pitfall

FineReport's public frontend SSO interface requires a password. Seeyon `SsoService.login(...)` usually receives user binding data in `userMap`, not a native plaintext password.

Therefore generated implementations should parameterize password source instead of hardcoding a single assumption:

- `config:passwordFixedValue`
- `extendParams:<key>`
- `userMap:<key>`

Production warning:

- Long-term plaintext password in connector config is weak and should be called out in `VALIDATION.md`.
- Prefer a site-approved credential channel, FineReport backend SSO/plugin mode, or a shared account/password strategy explicitly confirmed by the customer.

## Validation notes

Minimum checks after generation:

```bash
python references/generation/tools/validate_generated_spi_project.py <project-root> --maven false
```

A `spi_info_scopes_acceptable` WARN for `scopes=['cip-connector']` is acceptable for this scenario if the Auth-SSO connector reference says the service runs in `cip-connector`.

Maven compile should only be run after collecting the site's Maven executable, settings.xml, repository/private mirror, and actual `cip-connector-api` / boot versions.
