# MQ 消息队列 SPI 域

> 本目录整合了 Super SPI 和旧版本 SPI 的 MQ 扩展内容，按 SPI 类型组织为独立文件夹。

## 目录结构

```
mq/
├── index.md                    ← 本文件（总索引）
├── shared/                     ← 共享资源（契约、部署、健康检查等）
└── rocketmq-ons/               ← 阿里云 RocketMQ / ONS SPI
```

## SPI 文件夹索引

| SPI 文件夹 | 场景 | 接口 | Scope | 重启服务 |
|-----------|------|------|-------|----------|
| [rocketmq-ons/](rocketmq-ons/README.md) | 阿里云 RocketMQ / ONS 消息中间件扩展 | `MQMessageSpi` | boot-starter-mq | 全部 |

## 共享资源

所有 MQ SPI 共享以下资源，位于 [shared/](shared/) 目录：

| 文件 | 用途 |
|------|------|
| [contract.md](shared/contract.md) | MQMessageSpi / MessageDto 反编译契约（FACT ✅） |
| [deployment-guide.md](shared/deployment-guide.md) | MQ SPI 工程落点、注册、部署与 Nacos 配置 |
| [health-check-rules.md](shared/health-check-rules.md) | 生成后静态检查与现场验证清单 |
| [closeout.md](shared/closeout.md) | MQ 子域收敛记录 / 冻结边界 |
| [generated-project-validation.md](shared/generated-project-validation.md) | MQ SPI 示例工程生成形态与静态验证清单 |

## 每个 SPI 文件夹的标准结构

```
{spi-name}/
├── README.md              ← 场景描述、实现规则、代码骨架
├── constraints.md         ← 该 SPI 的独有约束
└── {extra}.md             ← 补充资料（仅限归一化契约/规则，不放一次性案例）
```

## 执行流程

1. 识别用户场景，定位到具体 SPI 文件夹
2. 读取该 SPI 的 `README.md` 了解场景和实现规则
3. 读取 `constraints.md` 了解独有约束
4. 如需共享资源（契约、部署、健康检查），查阅 `shared/` 目录
5. 生成代码前先读 `references/spi-domain-constraints.md`（全局公共约束）

## 公共方法双查规则

生成、改造或标注 SPI 方法时必须同时查询两类来源：

1. 子域契约：本目录对应 SPI 的 `README.md` / `constraints.md` / `shared/*contract*`，只用于接口 FQCN、SPI 方法签名、DTO、枚举、scope、spring.factories。
2. 平台公共方法：`references/platform-standard-library/index.md` 和 `references/platform-standard-library/decompiled/`，用于 boot-core / boot-starter-web / boot-starter-spi 的 JSON、HTTP、加密、BeanCopy、Transport Response/Request、RequestContext、BusinessException 等公共能力。

规则：凡是代码中要使用或标注公共 helper / Response / Request / 工具类方法，先查平台标准库；凡是 SPI 接口与 DTO，先查本子域契约。两边都查完再生成，禁止把平台公共类型误报成子域缺口，也禁止把子域契约包提升为全局公共方法。

## Evidence 状态

| SPI | 接口 Evidence | DTO Evidence | 样例 Evidence | 契约来源 | 状态 |
|-----|--------------|--------------|--------------|----------|------|
| rocketmq-ons | FACT ✅ | FACT ✅ | OBSERVATION ⚠️ | shared/contract.md (反编译) + rocketmq-ons/README.md (已归一化 OBSERVATION) | ✅ |

## 关键边界

1. MQ 是 SSO 后的第二子域，不是 SSO 的补丁。
2. MQ 生效范围是全系统，部署说明必须写"重启所有服务"。
3. 只有用户明确要求"生成代码/改工程/补模块"时，才创建 `spi-mq`。
4. 版本不同，泛化 jar 结论意义有限；优先使用目标现场反编译接口代码。
