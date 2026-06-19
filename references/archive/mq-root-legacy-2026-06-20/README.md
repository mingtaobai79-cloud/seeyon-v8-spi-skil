# MQ root legacy archive

这些文件从 `references/mq/` 根目录移入可恢复归档，原因：MQ 金标准结构只保留 `index.md`、`shared/` 和 `rocketmq-ons/` 子目录作为 active 路由。

归档文件：

- `deployment-guide.md` → active: `references/mq/shared/deployment-guide.md`
- `health-check-rules.md` → active: `references/mq/shared/health-check-rules.md`
- `generated-project-validation.md` → active: `references/mq/shared/generated-project-validation.md`
- `rocketmq-ons.md` → active: `references/mq/rocketmq-ons/README.md` + `constraints.md`

不要从 active 文档重新引用本目录；仅用于可恢复历史对照。
