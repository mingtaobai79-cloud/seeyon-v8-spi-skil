# 三方菜单 SPI 独有约束

> 公共约束：`references/spi-domain-constraints.md`

## 域特有规则

1. position() 有默认实现（TAIL），只需 override 需要改位置的情况。
2. selectThirdMenu 是 abstract，必须实现。
3. 返回的菜单支持树形结构（children 字段）。

## 禁止项

- 禁止在 selectThirdMenu 中做耗时操作（影响导航加载速度）。
- 禁止返回 null（应返回空 List）。

## 索取清单

```
P0:
1. ✅ AbstractThirdMenuService FQCN → com.seeyon.ctp.user.api.menu.AbstractThirdMenuService（FACT）
2. ✅ ThirdMenuParamDto FQCN → com.seeyon.ctp.user.dto.menu.ThirdMenuParamDto（FACT）
3. ✅ CtpUserThirdNavFrontDto FQCN → com.seeyon.ctp.user.dto.menu.CtpUserThirdNavFrontDto（FACT）
4. ✅ MenuPositionEnum → HEAD(0), TAIL(2)（FACT）

P1:
5. 示例实现类
```
