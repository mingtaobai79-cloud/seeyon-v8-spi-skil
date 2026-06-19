# 域升级检查清单

> 从 SKILL.md 下沉。用于把占位域升级为金标准域。

## 域升级检查清单（占位 → 金标准）

将域从"框架占位"升级到"金标准"时，按此清单逐项执行：

### Phase 0: Evidence Alignment Audit（先做这个！）

**在等 jar 之前，先检查已有数据是否被浪费。**

很多域的 shared/ 目录已经有 FACT 级契约（来自 jar 反编译），但 SPI 级 README.md 仍然标 OBSERVATION 且没有引用 shared/ 文件。这是文档对齐问题，不是数据缺口。

审计步骤：
1. 扫描域内所有 SPI 的 README.md，找 `OBSERVATION` 标记
2. 检查 `shared/` 目录是否有 `*-contract.md` 或 `contract.md` 文件
3. 交叉比对：SPI README 中的接口 FQCN 是否已在 shared 契约中出现
4. 如果匹配：直接升级标记为 FACT ✅，添加指向 shared 文件的引用头
5. 检查工程目录（如 auth-sso-spi-parent/）中 spring.factories 的实际 key，确认 FQCN

这个审计可以在零新 jar 的情况下把多个 SPI 从 OBSERVATION 升到 FACT。2026-06 实战：unified-auth、sso-connector、rocketmq-ons 三个域通过此方法一次性升级，契约数据早就在 shared/ 里了。

### Phase 1: 结构重组
1. 创建标准目录结构：`index.md`（纯导航）+ `shared/` + `{spi-name}/`（每个 SPI 独立文件夹）
2. `index.md` 只做路由表：SPI 文件夹索引 + scope + 重启服务 + 索取清单。**绝不塞实现细节**。
3. 删除旧的平铺 md 文件，内容合并到 `shared/README.md` 或各 SPI 的 `README.md`。

### Phase 2: SPI 文件夹内容（每个 SPI 的 README.md 必须包含）
- [ ] 场景描述 + 适用版本
- [ ] Maven 依赖
- [ ] 接口定义 [FACT ✅ 或 OBSERVATION ⚠️]
- [ ] 方法说明表格
- [ ] DTO 定义 [FACT ✅ 或 OBSERVATION ⚠️]
- [ ] 代码骨架（含 JavaDoc + SLF4J 日志 + 错误处理）
- [ ] Nacos 配置模板
- [ ] spring.factories 注册示例
- [ ] **spi_info.json**（scope = 该 SPI 对应的微服务应用名）
- [ ] 重启服务

### Phase 3: constraints.md（每个 SPI 独有约束）
- [ ] 域特有规则
- [ ] 禁止项
- [ ] 索取清单（P0/P1 分级，已有项标 ✅）

### Phase 4: 验证
- [ ] 金标准段落检查：代码骨架、Nacos、spring.factories、spi_info.json、Maven 全部命中
- [ ] 更新 SKILL.md 路由表
- [ ] 更新 SKILL.md References 区域

### spi_info.json scope 规则
scope 值 = 该 SPI 部署到的微服务应用名，不是域名也不是模块名：

| SPI 域 | scope 值 | 说明 |
|--------|----------|------|
| auth-sso 模式 A/B | `ctp-user` | 认证服务 |
| auth-sso 模式 C | `cip-connector` | 连接器服务 |
| MQ | `ALL` | 全系统生效 |
| todo-batch | `ctp-affair` | 待办服务 |
| api-auth | `cip-connector` | 连接器服务 |
| org-sync-middle-table | `cip-connector` | 连接器服务 |
| system-variable | `ALL`（兜底） | UDC 应用，具体 scope 待确认 |

**规律**：同一个微服务下的多个 SPI 共享同一个 scope 值。新增 SPI 时先确认它部署到哪个微服务，再填 scope。
