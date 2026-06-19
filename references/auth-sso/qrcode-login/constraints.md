# 二维码登录 SPI 独有约束

> 公共约束：`references/spi-domain-constraints.md`

## 状态机

```
GENERATED → ROUND → SCANNED → (登录成功)
    ↓
  EXPIRED
```

## 索取清单

```
P0:
1. AbstractLoginQrCodeService 完整反编译源码
2. CtpLoginQrCodeDto / QrcodeResultDto / QrcodeStatusEnum 完整定义
3. spring.factories 注册示例

P1:
4. BaiChengLoginQrCodeServiceImpl 示例
5. ctp-user-api 版本
```

## 域特有规则

1. 三个方法都是 abstract，必须全部实现。
2. `getQrCodeAuthenticationType()` 返回认证类型标识。
3. `generateQrCode()` 生成二维码数据。
4. `roundScanResult()` 轮询扫码结果。

## 禁止项

- 禁止 `generateQrCode()` 返回 null。
- 禁止在 `roundScanResult()` 中做阻塞等待（平台会轮询）。
- 禁止使用 `@Autowired`、`@Service` 等 Spring 注解。
