---
title: "Excel读写"
source: "https://www.yuque.com/seeyonkk/v8/hv4w7hges85wn2k3"
evidence: OBSERVATION
capture_method: yuque-rendered-page-copy
---

# Excel读写

> Source: https://www.yuque.com/seeyonkk/v8/hv4w7hges85wn2k3

作者：陈晓东

时间：2025-08-15

提供excel读写能力，支持注解描述excel样式，支持读取数据到指定类型JavaBean。

暂不支持同时写入多sheet和合并单元格。

```java
public class ExcelUtils {
    /**
     * 读取第一个sheet
     *
     * @param fileName excel文件全路径
     * @param rowModel
     * @param <T>      行数据封装bean
     * @return
     */
    public static <T> List<T> readExcel(String fileName, Class<T> rowModel) {
    }

    /**
     * 读取指定sheet
     *
     * @param fileName excel文件全路径
     * @param rowModel
     * @param sheetNo
     * @param <T>      行数据封装bean
     * @return
     */
    public static <T> List<T> readExcel(String fileName, Class<T> rowModel, int sheetNo) {
    }

    /**
     * 读取第一个sheet
     *
     * @param excelFile excel文件全路径
     * @param rowModel
     * @param <T>       行数据封装bean
     * @return
     */
    public static <T> List<T> readExcel(File excelFile, Class<T> rowModel) {
    }

    /**
```

示例

```java
/**
*描述Excel的JavaBean，导入时可不描述样式仅描述列头即可。
**/
@ExcelHeadStyle(verticalAlignment = VerticalAlignment.CENTER,rowHeight = 25,
        borderRight = BorderStyle.DOUBLE, borderTop = BorderStyle.DOUBLE, borderLeft = BorderStyle.DOUBLE, borderBottom = BorderStyle.DOUBLE,
        bottomBorderColor = IndexedColors.ROYAL_BLUE, leftBorderColor = IndexedColors.ROYAL_BLUE, rightBorderColor = IndexedColors.ROYAL_BLUE, topBorderColor = IndexedColors.ROYAL_BLUE,
        fillForegroundColor = IndexedColors.PINK1
)//设置头部区样式
@ExcelHeadFontStyle(fontName = "隶书", fontHeightInPoints = 20, color = IndexedColors.BROWN)//设置头部区字体样式
@ExcelContentStyle(wrapped = true,rowHeight = 30,
        borderBottom = BorderStyle.DOUBLE, borderLeft = BorderStyle.DOUBLE, borderTop = BorderStyle.DOUBLE, borderRight = BorderStyle.DOUBLE,
        leftBorderColor = IndexedColors.BLUE,rightBorderColor = IndexedColors.MAROON,topBorderColor = IndexedColors.LIGHT_GREEN,bottomBorderColor = IndexedColors.BLACK,
        fillForegroundColor = IndexedColors.RED
)//设置内容区样式
@ExcelContentFontStyle(fontName = "楷体", fontHeightInPoints = 10, color = IndexedColors.LIGHT_GREEN)//统一设置内容区字体样式
@ExcelColumnWidth(20)//统一设置cell的宽度
public class ExcelTestBean {

    @ExcelContentStyle(wrapped = true,
            borderBottom = BorderStyle.DOTTED, borderLeft = BorderStyle.DOTTED, borderTop = BorderStyle.DOTTED, borderRight = BorderStyle.DOTTED,
            leftBorderColor = IndexedColors.RED1,rightBorderColor = IndexedColors.RED1,topBorderColor = IndexedColors.RED1,bottomBorderColor = IndexedColors.RED1,
            fillForegroundColor = IndexedColors.GREEN
    )
    @ExcelContentFontStyle(fontName = "宋体", fontHeightInPoints = 18, color = IndexedColors.LIGHT_GREEN)//姓名列单独设置内容字体样式
    @ExcelColumn(value = {"姓名","名字","英文名","曾用名"})//多列头
    private String v11;
    @ExcelContentFontStyle(fontName = "仿宋", fontHeightInPoints = 13, color = IndexedColors.BRIGHT_GREEN)
    @ExcelColumn(value = "年龄",width = 8)//年龄这列单独设置宽度
    private int v21;
    @ExcelColumn(value = "分数")
    private double v13;
    private String v41;

}
public class ExcelUtilsExample {
```
