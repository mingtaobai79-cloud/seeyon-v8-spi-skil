# integration-sync 域独有约束

> 公共约束：`references/spi-domain-constraints.md`。

## 域特有规则

1. 三者都属于"三方集成过程中的数据/请求同步和处理"。
2. 生成代码时必须分三类模块/包：`todo-batch`、`api-auth`、`org-sync-middle-table`。
3. `0111-V8接入三方App` 可交叉引用本域，但主归 `references/auth-sso/mobile-app/`。

## 禁止项

- 禁止把三个场景合并到一个实现类。
- 禁止在待办批处理里直接调用三方 API 而不做异常隔离。
