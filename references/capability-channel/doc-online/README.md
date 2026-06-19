# 在线文档能力通道 — SPI 接口完整定义

> **Evidence: FACT ✅** — 接口签名来自 `cip-capability-api-5.5.147.jar` CFR 反编译。  
> 当前模板基线：`cip-capability-api-5.5.147.jar`；现场指定新版本时，以现场 jar/source 重新 FACT 化并局部更新。

## 场景

扩展在线文档预览、编辑、转换、清理、水印、合并等通道。

## 接口

```java
public interface DocOnlineProviderService
public Map<String, Object> checkToken(String var1);
public FilePropertiesDto getDocOnlineProperties();
default public DocUrlDto getOfficeViewUrl(FileViewDto fileViewDto) throws BusinessException {
default public DocUrlDto getOfficeEditUrl(FileEditDto fileEditDto) throws BusinessException {
default public FileOperateCleanDto cpsOfficeOperateClean(FileOperateCleanDto fileOperateDto) throws BusinessException {
default public List<String> cpsCleanSupportFileFormat() {
default public FileOperateTextWatermarkDto cpsOfficeOperateTextWatermark(FileOperateTextWatermarkDto fileOperateDto) throws BusinessException {
default public FileOperateImageWatermarkDto cpsOfficeOperateImageWatermark(FileOperateImageWatermarkDto fileOperateDto) throws BusinessException {
default public FileConvertDto cpsOfficeConvert(FileConvertDto fileConvertDto) throws BusinessException {
default public FileConvertResultDto cpsDownload(Map<String, Object> map) throws BusinessException {
default public FileConvertResultDto cpsTaskQuery(String taskId) throws BusinessException {
default public FileConvertDto getDocumentTemplateTab(FileConvertDto officialTemplateDto) throws BusinessException {
default public FileWrapHeaderDto cpsWrapHeader(FileWrapHeaderDto officialTemplateDto) throws BusinessException {
default public FileSetBookmarkPermissionsApiDto setBookmarkPermissions(FileSetBookmarkPermissionsApiDto apiDto) throws BusinessException {
default public FileMergeResDto cpsMerge(FileMergeDto fileMergeDto) throws BusinessException {
default public DocExtractPicApiResDto extractPictures(DocExtractPicApiReqDto reqDto) throws BusinessException {
default public DocFileUrlApiResDto getFileUrl(DocFileUrlApiReqDto apiReqDto) throws BusinessException {
default public DocCloseFileApiResDto closeFile(DocCloseFileApiReqDto apiReqDto) throws BusinessException {
default public String fileFormat() {
default public CapabilityEnum getCapabilityEnum() {
```

## 基接口：ProviderService

所有能力通道接口均继承或遵循 `com.seeyon.cip.provider.api.ProviderService`：

```java
public interface ProviderService {
    String getDescription();
    CapabilityEnum getCapabilityEnum();
    String getChannelCode();
}
```

## 方法说明

| 方法 | 参数 | 返回 | 类型 |
|------|------|------|------|
| checkToken | `String var1` | `Map<String, Object>` | required |
| getDocOnlineProperties | `无` | `FilePropertiesDto` | required |
| getOfficeViewUrl | `FileViewDto fileViewDto` | `DocUrlDto` | default |
| getOfficeEditUrl | `FileEditDto fileEditDto` | `DocUrlDto` | default |
| cpsOfficeOperateClean | `FileOperateCleanDto fileOperateDto` | `FileOperateCleanDto` | default |
| cpsCleanSupportFileFormat | `无` | `List<String>` | default |
| cpsOfficeOperateTextWatermark | `FileOperateTextWatermarkDto fileOperateDto` | `FileOperateTextWatermarkDto` | default |
| cpsOfficeOperateImageWatermark | `FileOperateImageWatermarkDto fileOperateDto` | `FileOperateImageWatermarkDto` | default |
| cpsOfficeConvert | `FileConvertDto fileConvertDto` | `FileConvertDto` | default |
| cpsDownload | `Map<String, Object> map` | `FileConvertResultDto` | default |
| cpsTaskQuery | `String taskId` | `FileConvertResultDto` | default |
| getDocumentTemplateTab | `FileConvertDto officialTemplateDto` | `FileConvertDto` | default |
| cpsWrapHeader | `FileWrapHeaderDto officialTemplateDto` | `FileWrapHeaderDto` | default |
| setBookmarkPermissions | `FileSetBookmarkPermissionsApiDto apiDto` | `FileSetBookmarkPermissionsApiDto` | default |
| cpsMerge | `FileMergeDto fileMergeDto` | `FileMergeResDto` | default |
| extractPictures | `DocExtractPicApiReqDto reqDto` | `DocExtractPicApiResDto` | default |
| getFileUrl | `DocFileUrlApiReqDto apiReqDto` | `DocFileUrlApiResDto` | default |
| closeFile | `DocCloseFileApiReqDto apiReqDto` | `DocCloseFileApiResDto` | default |
| fileFormat | `无` | `String` | default |
| getCapabilityEnum | `无` | `CapabilityEnum` | default |

## Maven 依赖

```xml
<dependency>
  <groupId>com.seeyon</groupId>
  <artifactId>cip-capability-api</artifactId>
  <version>${cip-capability-api.version}</version>
</dependency>
```

已 FACT 版本：`5.5.147`。父 POM 平台版本、boot starter 版本、SPI 契约包版本必须分别参数化。

## spring.factories

```properties
com.seeyon.cip.provider.api.doc.DocOnlineProviderService=com.seeyon.extend.spi.capability.CustomDocOnlineProviderService
```

## spi_info.json

```json
{
  "name": "boot-starter-spi-customized",
  "scopes": ["cip-capability"]
}
```

## 重启服务

cip-capability

## 代码骨架

```java
package com.seeyon.extend.spi.capability;

import com.seeyon.cip.provider.api.doc.DocOnlineProviderService;
import com.seeyon.cip.provider.enums.CapabilityEnum;

/**
 * 在线文档能力通道扩展。
 * 业务参数、供应商 SDK / HTTP API、通道 code 从 Nacos 或平台能力配置读取，不在模板中写死。
 */
public class CustomDocOnlineProviderService implements DocOnlineProviderService {

    @Override
    public String getDescription() {
        return "自定义在线文档通道";
    }

    @Override
    public CapabilityEnum getCapabilityEnum() {
        // 按 cip-capability-api 目标版本的 CapabilityEnum 实际枚举值替换；不要猜不存在的枚举。
        return null;
    }

    @Override
    public String getChannelCode() {
        return "custom-doc-online";
    }

    // TODO: 按目标版本 FACT 方法签名实现 required 方法；default 方法只有业务需要时覆盖。
}
```

## Evidence 摘要

| 项 | 值 |
|----|----|
| 接口 FQCN | `com.seeyon.cip.provider.api.doc.DocOnlineProviderService` |
| required 方法数 | 2 |
| default 方法数 | 18 |
| Contract Source | `cip-capability-api-5.5.147.jar` + CFR |
| Evidence | FACT ✅ |
