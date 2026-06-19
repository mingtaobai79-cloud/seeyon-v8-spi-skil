# 通讯录 / AbstractAddressBookSpiService

> **Evidence: FACT ✅** — 接口签名、DTO 来自 `organization-facade-5.3.368.jar` CFR 反编译。

## 场景

通讯录人员字段权限控制（如隐藏手机号、邮箱等敏感字段）。

## Maven 依赖

```xml
<dependency>
  <groupId>com.seeyon</groupId>
  <artifactId>organization-facade</artifactId>
  <version>5.3.368</version>
</dependency>
```

## 接口定义 [FACT ✅]

```java
package com.seeyon.organization.spi;

import com.seeyon.organization.dto.addressbook.AddressBookMemberDto;
import java.util.List;
import java.util.Map;

public abstract class AbstractAddressBookSpiService {
    public abstract void processMembersFieldPermission(List<AddressBookMemberDto> var1);
    public abstract void processMemberCardFieldPermission(List<Map<String, String>> var1);
}
```

## 方法说明

| 方法 | 参数 | 返回 | 语义 |
|------|------|------|------|
| processMembersFieldPermission | `List<AddressBookMemberDto>` | void | 批量处理人员列表字段权限 |
| processMemberCardFieldPermission | `List<Map<String, String>>` | void | 批量处理人员卡片字段权限 |

## DTO 定义 [FACT ✅]

### AddressBookMemberDto

```java
package com.seeyon.organization.dto.addressbook;

@DtoInfo("通讯录人员信息")
public class AddressBookMemberDto extends BaseDto {
    Long id;                        // 人员id
    MemberTypeEnum memberType;      // 人员类型
    Integer sortId;                 // 排序号
    Integer topSortId;              // 置顶排序号
    BigDecimal sortNumber;          // 全局排序号（带小数可细化排序）
    BigDecimal orgSortNumber;       // 组织内排序号
    Long orgId;                     // 人员所属组织id
    OrgOnlineStatusEnum onlineStatus; // 在线状态
    String image;                   // 头像
    String name;                    // 姓名
    String mnemonic;                // 拼音
    String pinyinShort;             // 拼音首字母
    String gender;                  // 性别
    String department;              // 部门
    String fullOrg;                 // 组织
    String parentDepartment;        // 上级部门
    String post;                    // 主岗
    // ... 更多字段（手机号、邮箱等敏感字段）
}
```

## 代码骨架

```java
package com.seeyon.extend.spi.org;

import com.seeyon.organization.spi.AbstractAddressBookSpiService;
import com.seeyon.organization.dto.addressbook.AddressBookMemberDto;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import java.util.List;
import java.util.Map;

public class CustomAddressBookSpiService extends AbstractAddressBookSpiService {

    private static final Logger log = LoggerFactory.getLogger(CustomAddressBookSpiService.class);

    @Override
    public void processMembersFieldPermission(List<AddressBookMemberDto> members) {
        log.debug("[address-book] processMembersFieldPermission, count={}", members.size());
        for (AddressBookMemberDto member : members) {
            // TODO: 根据权限规则隐藏敏感字段
            // member.setPhone(null);
            // member.setEmail(null);
        }
    }

    @Override
    public void processMemberCardFieldPermission(List<Map<String, String>> cards) {
        log.debug("[address-book] processMemberCardFieldPermission, count={}", cards.size());
        for (Map<String, String> card : cards) {
            // TODO: 根据权限规则隐藏卡片敏感字段
            // card.remove("phone");
        }
    }
}
```

## Nacos 配置

本 SPI 不需要额外 Nacos 配置。

## spring.factories

```properties
com.seeyon.organization.spi.AbstractAddressBookSpiService=com.seeyon.extend.spi.org.CustomAddressBookSpiService
```

## spi_info.json

```json
{
  "name": "boot-starter-spi-customized",
  "scopes": ["organization"]
}
```

## 重启服务

organization
