# 文件操作 SPI 独有约束

> 公共约束：`references/spi-domain-constraints.md`

## 域特有规则

1. 9 个方法中 6 个必须实现（无 default），`delete` 有 default 实现。
2. 桶名称参数可能为空（标品 bug），实现时需兜底处理。
3. download 有两个重载：一个写 HttpServletResponse，一个返回 InputStream。
4. copy 参数顺序：srcKey, srcBucket, destKey, destBucket。

## 禁止项

- 禁止使用 OSS 方式加载。
- 禁止通过客开管理直接提交代码。
- 禁止在 upload 中返回 null。

## 索取清单

```
P0:
1. ✅ StorageSpi FQCN → com.seeyon.boot.starter.file.spi.StorageSpi（FACT）
2. ✅ SpiUploadRequestDto → com.seeyon.boot.starter.file.spi.dto.SpiUploadRequestDto（FACT）
3. ✅ UploadResultDto → com.seeyon.boot.starter.file.dto.response.UploadResultDto（FACT）

P1:
4. UnifyFileService 示例代码
5. Nacos 配置项（桶名称 bug 修复）
```
