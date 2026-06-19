---
title: "集成接口鉴权"
source: "https://www.yuque.com/seeyonkk/v8/nks3s8agdgi1im3z"
evidence: OBSERVATION
capture_method: yuque-rendered-page-copy
---

# 集成接口鉴权

> Source: https://www.yuque.com/seeyonkk/v8/nks3s8agdgi1im3z

作者：杨映海
最后更新：2025-04-18

## 1. 应用场景

在配置集成应用接口时，有些业务接口通过标品无法成功配置时可以通过扩展SPI方式来完成接口鉴权（通过扩展代码调用接口方式来完成 相关 heaer,body,query 参数设置）

## 2. 接口说明

接口名称：com.seeyon.cip.connector.api.authentication.LinkerSecurityService

```xml
<dependency>
    <groupId>com.seeyon</groupId>
    <artifactId>cip-connector-api</artifactId>
    <!-- 请以实际环境的依赖版本号为准-->
    <version>3.8.211</version>
</dependency>
```

## 3.接口实现

spi代码仓库获取及工程初始化请参考：
开发准备

```java
package com.seeyon.cip.connector.domain.service.auth.impl;

import com.seeyon.boot.transport.BaseDto;
import com.seeyon.boot.util.JsonUtils;
import com.seeyon.cip.connector.api.authentication.LinkerSecurityService;
import com.seeyon.cip.connector.common.utils.WojiaCloudServiceUtil;
import com.seeyon.cip.connector.dto.authentication.AuthEventDto;
import com.seeyon.cip.connector.dto.authentication.AuthenticationDto;
import com.seeyon.cip.connector.enums.AuthInfoModeEnum;
import lombok.Getter;
import lombok.Setter;
import lombok.extern.slf4j.Slf4j;
import org.springframework.stereotype.Service;

import javax.validation.constraints.NotBlank;
import java.util.Date;
import java.util.HashMap;
import java.util.Map;

/**
 */
@Slf4j
@Service
public class WojiacloudSecurityServiceImpl implements LinkerSecurityService {
    @Override
    public String getName() {
        return "wojiacloud";
    }

    @Override
    public String getTypeCaption() {
        return "金蝶认证-我家云";
    }

    @Override
    public AuthInfoModeEnum getMode() {
```

注意：完成接口开发并构建成功后需要重启【cip-connector】服务才能进行后续功能验证

## 4.参数配置

<img src="https://cdn.nlark.com/yuque/0/2025/png/26748915/1745724499466-9cbf0f8c-60da-40d2-bd91-39d1765d8e31.png" width="1489.5">
