# 上传下载拦截 SPI 独有约束

> 公共约束：`references/spi-domain-constraints.md`

## 域特有规则

1. 🧊 **冻结**：接口 FQCN 未确认，代码无法编译。
2. 4 个方法都有 default 实现，按需覆盖。
3. beforeUpload 可修改请求（如加密文件内容）。
4. afterUpload 可修改结果（如添加元数据）。

## 禁止项

- 禁止在 beforeUpload 中返回 null（应返回原 requestDto）。
- 禁止在拦截器中做耗时操作（影响上传下载性能）。

## 索取清单

```
P0（阻塞）:
1. ❌ StorageInterceptorSpi 完整包名 — 5.3.358 不存在

P1:
2. ✅ FileSafeInterceptor → com.seeyon.boot.starter.file.safe.FileSafeInterceptor（FACT，内部实现非 SPI）
3. 需要 5.8+ 版本 jar
```
