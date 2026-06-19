# 通讯录 SPI 独有约束

> 公共约束：`references/spi-domain-constraints.md`

## 域特有规则

1. 抽象类（非接口），用 `extends` 而非 `implements`。
2. 两个方法都是批量处理，入参是 List。
3. 人员卡片用 `Map<String, String>` 表示，key 是字段名。
4. 隐藏字段的方式：设为 null 或从 Map 中 remove。

## 禁止项

- 禁止修改 List 结构（不要 add/remove 元素，只修改元素内容）。
- 禁止在循环中做数据库查询。

## 索取清单

```
P0:
1. ✅ AbstractAddressBookSpiService FQCN → com.seeyon.organization.spi.AbstractAddressBookSpiService（FACT）
2. ✅ AddressBookMemberDto → com.seeyon.organization.dto.addressbook.AddressBookMemberDto（FACT）

P1:
3. AddressBookMemberDto 完整字段列表（jar 反编译截断）
4. spring.factories key 确认
```
