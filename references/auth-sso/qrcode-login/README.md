# M5 扫码登录 PC / AbstractLoginQrCodeService

> Evidence: FACT ✅ 用户提供的反编译接口源码 + BaiChengLoginQrCodeServiceImpl 示例。语雀 `0093-M5扫描三分二维码登录PC端-to23xvuwpby5fx7m.md` 为 OBSERVATION。

## 场景

M5 移动端扫描三方二维码登录 PC 端。V8 生成二维码，M5 扫码后轮询状态，确认后 PC 端登录。

## Maven 依赖

```xml
<dependency>
  <groupId>com.seeyon</groupId>
  <artifactId>ctp-user-api</artifactId>
  <version>3.12.1</version>
</dependency>
```

## 接口定义 [FACT ✅]

```java
package com.seeyon.ctp.user.api.qrcode;

public abstract class AbstractLoginQrCodeService {
    /**
     * 获取二维码认证类型标识
     * @return 认证类型字符串
     */
    public abstract String getQrCodeAuthenticationType();

    /**
     * 生成二维码
     * @return CtpLoginQrCodeDto 包含二维码值、图片、过期时间等
     */
    public abstract CtpLoginQrCodeDto generateQrCode();

    /**
     * 轮询扫码结果
     * @param qrValue 二维码值
     * @return QrcodeResultDto 包含扫码状态和用户 ID
     */
    public abstract QrcodeResultDto roundScanResult(String qrValue);
}
```

## DTO 定义 [FACT ✅]

### CtpLoginQrCodeDto

```java
package com.seeyon.ctp.user.dto;

public class CtpLoginQrCodeDto {
    /** 二维码值（唯一标识） */
    private String qrValue;
    
    /** 对象 ID */
    private Long objectId;
    
    /** 过期时间 */
    private Date expireTime;
    
    /** 存储 key */
    private String storageKey;
    
    /** 二维码图片（支持 data:image/png;base64,...） */
    private String imageStr;
}
```

### QrcodeResultDto

```java
package com.seeyon.ctp.user.dto;

public class QrcodeResultDto {
    /** 扫码状态 */
    private QrcodeStatusEnum status;
    
    /** 用户 ID（扫码成功时返回） */
    private Long userId;
}
```

### QrcodeStatusEnum

```java
package com.seeyon.ctp.user.enums;

public enum QrcodeStatusEnum {
    /** 二维码已生成，等待扫码 */
    GENERATED,
    
    /** 轮询中，尚未扫码 */
    ROUND,
    
    /** 已扫码，等待确认 */
    SCANNED,
    
    /** 二维码已过期 */
    EXPIRED
}
```

## 方法说明

| 方法 | 作用 | 调用时机 |
|------|------|----------|
| `getQrCodeAuthenticationType()` | 返回二维码认证类型标识 | 框架选择 QR 服务时调用 |
| `generateQrCode()` | 生成二维码（调用三方 API 或本地生成） | PC 端请求二维码时调用 |
| `roundScanResult(qrValue)` | 轮询扫码结果（调用三方 API 或本地存储） | PC 端轮询时调用 |

## 状态机

```
GENERATED → ROUND → SCANNED → (登录成功)
    ↓
  EXPIRED
```

- `GENERATED`：二维码刚生成，等待扫码。
- `ROUND`：轮询中，尚未扫码或已扫码未确认。
- `SCANNED`：已扫码并确认，可以登录。
- `EXPIRED`：二维码过期，需要重新生成。

## Nacos 配置

```yaml
# ctp-user 微服务 Nacos 配置
seeyon:
  qrcode:
    {qr_type}:  # 如 baicheng / custom
      enabled: true
      expire-seconds: 300  # 二维码有效期（秒）
      poll-interval-ms: 2000  # 轮询间隔（毫秒）
      third-api-url: https://third.example.com/qrcode  # 三方二维码 API
      third-poll-url: https://third.example.com/qrcode/poll  # 三方轮询 API
      api-key: CHANGE_ME_IN_NACOS
      api-secret: CHANGE_ME_IN_NACOS
```

## spring.factories

```properties
com.seeyon.ctp.user.api.qrcode.AbstractLoginQrCodeService=\
com.seeyon.extend.spi.{project_id}.{Prefix}LoginQrCodeService
```

## 代码骨架

```java
package com.seeyon.extend.spi.{project_id};

import com.seeyon.ctp.user.api.qrcode.AbstractLoginQrCodeService;
import com.seeyon.ctp.user.dto.CtpLoginQrCodeDto;
import com.seeyon.ctp.user.dto.QrcodeResultDto;
import com.seeyon.ctp.user.enums.QrcodeStatusEnum;
import com.seeyon.ctp.user.util.CtpUserSpiUtils;
import lombok.extern.slf4j.Slf4j;

import java.util.Date;
import java.util.UUID;

/**
 * {project_name_cn} M5 扫码登录 PC
 *
 * 场景：M5 移动端扫描三方二维码登录 PC 端
 * V8 调用时机：
 *   1. PC 端请求二维码时调用 generateQrCode()
 *   2. PC 端轮询扫码状态时调用 roundScanResult(qrValue)
 * 三方系统：{third_system_name}
 * 返回语义：
 *   - generateQrCode() 返回二维码值、图片、过期时间
 *   - roundScanResult() 返回扫码状态（ROUND/SCANNED/EXPIRED）和用户 ID
 */
@Slf4j
public class {Prefix}LoginQrCodeService extends AbstractLoginQrCodeService {

    @Override
    public String getQrCodeAuthenticationType() {
        return "{qr_type}";  // 二维码认证类型标识
    }

    @Override
    public CtpLoginQrCodeDto generateQrCode() {
        try {
            log.info("[qrcode] {project_name_cn} 生成二维码");

            // 1. 生成唯一二维码值
            String qrValue = UUID.randomUUID().toString().replace("-", "");

            // 2. 计算过期时间
            int expireSeconds = Integer.parseInt(
                CtpUserSpiUtils.getPropertyByName("seeyon.qrcode.{qr_type}.expire-seconds")
            );
            Date expireTime = new Date(System.currentTimeMillis() + expireSeconds * 1000L);

            // 3. 调用三方 API 生成二维码图片（或本地生成）
            String imageStr = generateQrCodeImage(qrValue);

            // 4. 构建返回
            CtpLoginQrCodeDto dto = new CtpLoginQrCodeDto();
            dto.setQrValue(qrValue);
            dto.setExpireTime(expireTime);
            dto.setImageStr(imageStr);
            dto.setStorageKey("qrcode:" + qrValue);

            log.info("[qrcode] 二维码生成成功, qrValue: {}, 过期时间: {}", qrValue, expireTime);
            return dto;

        } catch (Exception e) {
            log.error("[qrcode] 生成二维码失败", e);
            throw new RuntimeException("生成二维码失败: " + e.getMessage(), e);
        }
    }

    @Override
    public QrcodeResultDto roundScanResult(String qrValue) {
        try {
            log.info("[qrcode] 轮询扫码结果, qrValue: {}", qrValue);

            // 1. 检查二维码是否过期
            // TODO: 从存储中读取过期时间，判断是否过期
            // if (isExpired(qrValue)) {
            //     return new QrcodeResultDto(QrcodeStatusEnum.EXPIRED, null);
            // }

            // 2. 调用三方 API 查询扫码状态
            // TODO: 调用三方轮询接口
            // String pollUrl = CtpUserSpiUtils.getPropertyByName("seeyon.qrcode.{qr_type}.third-poll-url");
            // PollResult result = callThirdPollApi(pollUrl, qrValue);

            // 3. 根据三方返回构建结果
            // 示例逻辑（参考 BaiChengLoginQrCodeServiceImpl）：
            //   - 未扫码 → ROUND
            //   - 已扫码未确认 → ROUND 或 SCANNED
            //   - 已确认 → SCANNED + userId
            //   - 过期 → EXPIRED

            // 保守模板：返回 ROUND（等待扫码）
            QrcodeResultDto result = new QrcodeResultDto();
            result.setStatus(QrcodeStatusEnum.ROUND);
            result.setUserId(null);

            log.info("[qrcode] 轮询结果, status: {}", result.getStatus());
            return result;

        } catch (Exception e) {
            log.error("[qrcode] 轮询扫码结果失败", e);
            throw new RuntimeException("轮询扫码结果失败: " + e.getMessage(), e);
        }
    }

    // ===== 私有方法 =====

    private String generateQrCodeImage(String qrValue) {
        // TODO: 调用三方 API 生成二维码图片，或本地生成
        //
        // 方式 1：调用三方 API
        // String apiUrl = CtpUserSpiUtils.getPropertyByName("seeyon.qrcode.{qr_type}.third-api-url");
        // return callThirdQrCodeApi(apiUrl, qrValue);
        //
        // 方式 2：本地生成（需要 ZXing 等库）
        // return generateLocalQrCodeImage(qrValue);
        //
        // 返回格式：data:image/png;base64,{base64_encoded_image}
        return "data:image/png;base64,TODO";
    }
}
```

## BaiCheng 示例参考逻辑

```java
// generateQrCode() 调用三方 QR API：
//   1. 请求三方生成二维码接口
//   2. 解码/存储/返回 qrValue、imageStr、expireTime

// roundScanResult(qrValue) 调用三方轮询 API：
//   1. 请求三方轮询接口
//   2. 根据返回状态判断：
//      - expired → EXPIRED
//      - waiting → ROUND
//      - recognized user → SCANNED + userId
```

## spi_info.json

```json
{
  "name": "boot-starter-spi-customized",
  "scopes": ["ctp-user"]
}
```

## 重启服务

`ctp-user`
