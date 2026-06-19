# Generated MQ Super SPI Audit Notes

> Session-derived reference for auditing a generated `spi-mq` Super SPI project. This is not a template; use it as a checklist when a report claims the project was generated and validated.

## First rule: verify the artifact exists

Do not trust a textual "已生成 / validator PASS" claim until the target directory exists on disk.

Expected minimal file set for an MQ-only project:

```text
pom.xml
README.md
spi-common/pom.xml
spi-mq/pom.xml
spi-mq/src/main/java/.../AliyunRocketMqOnsMessageSpi.java
spi-mq/src/main/resources/META-INF/spring.factories
spi-mq/src/main/resources/metadata/spi_info.json
spi-mq/src/main/resources/nacos/application-mq-ons-example.yml
spi-mq/docs/API_AND_CONFIG.md
VALIDATION.md
```

If the directory is absent, return `FAIL (artifact missing)` and stop. Do not discuss Java quality or validator results for a non-existent artifact.

## Static PASS criteria

A generated MQ-only Super SPI project can be marked static PASS only when all of these are true:

1. Root `pom.xml` has the expected business shape: `spi-common` + `spi-mq` modules.
2. `spi-common` has no SPI registration files:
   - no `src/main/resources/META-INF/spring.factories`
   - no `src/main/resources/metadata/spi_info.json`
3. `spi-mq` has both registration files:
   - `src/main/resources/META-INF/spring.factories`
   - `src/main/resources/metadata/spi_info.json`
4. `spi_info.json` scope is `ALL`.
5. `spring.factories` registers the FACT interface key:
   - `com.seeyon.boot.starter.mq.spi.MQMessageSpi=...`
6. Java implementation explicitly implements/uses FACT contract symbols:
   - `MQMessageSpi`
   - `MessageDto`
   - `MQSerializer`
   - `MessageListenerService`
7. Java implementation explicitly implements the four methods:
   - `send`
   - `sendBatch`
   - `subscribeTopic`
   - `unSubscribeTopic`
8. Send path serializes the full `MessageDto`, not only `messageDto.getData()`.
9. Consume path deserializes the full `MessageDto` and calls `MessageListenerService.invoke(messageDto)`.
10. No forbidden Spring annotations in Java sources:
    - `@Autowired`, `@Service`, `@Component`, `@Repository`, `@Controller`
11. No `lib/` directory or `<systemPath>` in POM files.
12. No `seeyon.ones.*` hard-coded in Java or Nacos config.

## `seeyon.ones.*` classification

`seeyon.ones.*` in active Java or Nacos config is a FAIL.

`seeyon.ones.*` in documentation is acceptable only when clearly marked as historical compatibility OBSERVATION and not recommended as the generated default.

Preferred generated keys are parameterized, e.g.:

```yaml
seeyon:
  mq:
    rocketmq-ons:
      endpoint: ${ALIYUN_ROCKETMQ_ONS_ENDPOINT:CHANGE_ME_IN_NACOS}
      accessKey: ${ALIYUN_ROCKETMQ_ONS_ACCESS_KEY:CHANGE_ME_IN_NACOS}
      secretKey: ${ALIYUN_ROCKETMQ_ONS_SECRET_KEY:CHANGE_ME_IN_NACOS}
      producerGroup: ${ALIYUN_ROCKETMQ_ONS_PRODUCER_GROUP:CHANGE_ME_IN_NACOS}
      consumerGroup: ${ALIYUN_ROCKETMQ_ONS_CONSUMER_GROUP:CHANGE_ME_IN_NACOS}
      defaultTopic: ${ALIYUN_ROCKETMQ_ONS_DEFAULT_TOPIC:CHANGE_ME_IN_NACOS}
```

## Validator rule

Always re-run the skill validator instead of trusting `VALIDATION.md` alone:

```bash
python references/generation/tools/validate_generated_spi_project.py <project-root>
```

Then compare the rerun summary to `VALIDATION.md`.

Known acceptable result for static-only environment:

```text
Summary: PASS=27 FAIL=0 WARN=1 SKIP=1
Result: PASS
```

Where:

- `WARN maven_validate: mvn not found` is an environment limitation, not a static structure failure.
- `SKIP sso_specific_checks: spi-sso not present` is expected for an MQ-only project.

Do not convert this into full compile/runtime PASS. Report scope explicitly:

- Static structure: PASS
- Super SPI registration boundary: PASS
- MQ FACT contract usage: PASS
- Case pollution: PASS
- Validator: PASS
- Maven compile: not executed if `mvn` is unavailable
- ONS runtime behavior: requires site dependencies and real RocketMQ/ONS environment

## Reporting format

Use the short final classification:

```text
结论：PASS / PARTIAL / FAIL
范围：静态结构 / validator / Maven / runtime
必修问题：...
可延后问题：...
下一步：...
```

Avoid declaring a generated project PASS before verifying the on-disk artifact and rerunning the validator.
