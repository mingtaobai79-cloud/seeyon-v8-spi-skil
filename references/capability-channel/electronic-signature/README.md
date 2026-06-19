# 电子签章能力通道 — SPI 接口完整定义

> **Evidence: FACT ✅** — 接口签名来自 `cip-capability-api-5.5.147.jar` CFR 反编译。  
> 当前模板基线：`cip-capability-api-5.5.147.jar`；现场指定新版本时，以现场 jar/source 重新 FACT 化并局部更新。

## 场景

扩展电子签章文件、组织/用户、模板、印章、签署流程等通道。

## 接口

```java
public interface SignatureProviderService
default public CapabilityEnum getCapabilityEnum() {
default public Map<String, Object> checkToken(String token) {
default public SignatureFileApiResponseDto getSignatureViewUrl(SignatureFileApiRequestDto dto) {
default public SignatureDownApiResDto downFile(SignatureDownApiReqDto reqDto) {
default public SignatureSealApiResDto getSealInfo(SignatureSealApiReqDto reqDto) {
default public SignaturePropertiesDto getSignatureProperties() {
default public FileInfoDto uploadFile(UploadFileDto uploadFileDto) {
default public InitiateSignResultDto initiateSign(InitiateSignDto initiateSignDto) {
default public InitiateSignResultDto initiateSignFree(InitiateSignFreeDto initiateSignDto) {
default public OrganizationResultDto createOrg(OrganizationDto organizationDto) {
default public OrganizationResultDto updateOrg(OrganizationUpdateDto dto) {
default public OrganizationDetailDto detailOrg(OrganizationQueryDto dto) {
default public UserResultDto createUser(BatchCreateUserDto batchCreateUserDto) {
default public SuccessData userUpdate(UserUpdateDto dto) {
default public UserUpdateDto userDetail(UserQueryDto dto) {
default public PageData<TemplateInfoDto> selectPageByConditions(PageInfo pageInfo, TemplatePageDto params) {
default public TemplateControlResultDto getTemplateContents(TemplateBaseDto templateBaseDto) {
default public GeneratePdfResultDto generatePdfFile(GeneratePdfDto generatePdfDto) {
default public SignAreaResultDto signToolsConfig(SignAreaConfigDto dto) {
default public SignAreaDetailDto signToolsConfigDetail(SignAreaSelectDto dto) {
default public VerifySignatureResultDto verifySignature(VerifySignatureDto dto) {
default public PageData<SealDataDto> sealList(PageInfo pageInfo, SealQueryDto params) {
default public FileDownloadDto downLoadFile(FileInfoDto fileInfoDto) {
default public InvalidFlowResDto invalidFlow(InvalidFlowReqDto dto) {
default public OrganizationResultDto createOuterOrg(OuterOrganizationDto organizationDto) {
default public OrganizationResultDto updateOuterOrg(OuterOrganizationUpdateDto dto) {
default public OuterOrganizationDetailDto detailOuterOrg(OrganizationQueryDto dto) {
default public UserResultDto createOuterUser(OuterBatchCreateUserDto batchCreateUserDto) {
default public SuccessData outerUserUpdate(OuterUserUpdateDto dto) {
default public OuterUserUpdateDto outerUserDetail(UserQueryDto dto) {
default public DeleteInnerUsersResDto deleteInnerUsers(DeleteInnerUsersReqDto rsqDto) {
default public QuerySsoResDto querySsoUrl(QuerySsoReqDto reqDto) {
default public PageData<SealSignerDataDto> sealSigners(PageInfo pageInfo, SealSignerQueryDto params) {
default public String stamp(ThreePartySealIntegrationDto params) {
default public ContractResponseDto withfileupload(ThreePartySealIntegrationDto params) {
default public AgainContractResponse invalid(ThreePartySealIntegrationDto params) {
default public SingleResponse recall(ThreePartySealIntegrationDto params) {
default public SealListResultDto sealGetList(ThreePartySealIntegrationDto params) {
default public String preSign(PreSignDto preSignDto) {
default public String initPreSign(InitPreSignDto initPreSignDto) {
default public String verifySeal(VerifySealDto verifySealDto) {
default public SingleResponse finish(ContractLockRequestDto requestDto) {
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
| getCapabilityEnum | `无` | `CapabilityEnum` | default |
| checkToken | `String token` | `Map<String, Object>` | default |
| getSignatureViewUrl | `SignatureFileApiRequestDto dto` | `SignatureFileApiResponseDto` | default |
| downFile | `SignatureDownApiReqDto reqDto` | `SignatureDownApiResDto` | default |
| getSealInfo | `SignatureSealApiReqDto reqDto` | `SignatureSealApiResDto` | default |
| getSignatureProperties | `无` | `SignaturePropertiesDto` | default |
| uploadFile | `UploadFileDto uploadFileDto` | `FileInfoDto` | default |
| initiateSign | `InitiateSignDto initiateSignDto` | `InitiateSignResultDto` | default |
| initiateSignFree | `InitiateSignFreeDto initiateSignDto` | `InitiateSignResultDto` | default |
| createOrg | `OrganizationDto organizationDto` | `OrganizationResultDto` | default |
| updateOrg | `OrganizationUpdateDto dto` | `OrganizationResultDto` | default |
| detailOrg | `OrganizationQueryDto dto` | `OrganizationDetailDto` | default |
| createUser | `BatchCreateUserDto batchCreateUserDto` | `UserResultDto` | default |
| userUpdate | `UserUpdateDto dto` | `SuccessData` | default |
| userDetail | `UserQueryDto dto` | `UserUpdateDto` | default |
| selectPageByConditions | `PageInfo pageInfo, TemplatePageDto params` | `PageData<TemplateInfoDto>` | default |
| getTemplateContents | `TemplateBaseDto templateBaseDto` | `TemplateControlResultDto` | default |
| generatePdfFile | `GeneratePdfDto generatePdfDto` | `GeneratePdfResultDto` | default |
| signToolsConfig | `SignAreaConfigDto dto` | `SignAreaResultDto` | default |
| signToolsConfigDetail | `SignAreaSelectDto dto` | `SignAreaDetailDto` | default |
| verifySignature | `VerifySignatureDto dto` | `VerifySignatureResultDto` | default |
| sealList | `PageInfo pageInfo, SealQueryDto params` | `PageData<SealDataDto>` | default |
| downLoadFile | `FileInfoDto fileInfoDto` | `FileDownloadDto` | default |
| invalidFlow | `InvalidFlowReqDto dto` | `InvalidFlowResDto` | default |
| createOuterOrg | `OuterOrganizationDto organizationDto` | `OrganizationResultDto` | default |
| updateOuterOrg | `OuterOrganizationUpdateDto dto` | `OrganizationResultDto` | default |
| detailOuterOrg | `OrganizationQueryDto dto` | `OuterOrganizationDetailDto` | default |
| createOuterUser | `OuterBatchCreateUserDto batchCreateUserDto` | `UserResultDto` | default |
| outerUserUpdate | `OuterUserUpdateDto dto` | `SuccessData` | default |
| outerUserDetail | `UserQueryDto dto` | `OuterUserUpdateDto` | default |
| deleteInnerUsers | `DeleteInnerUsersReqDto rsqDto` | `DeleteInnerUsersResDto` | default |
| querySsoUrl | `QuerySsoReqDto reqDto` | `QuerySsoResDto` | default |
| sealSigners | `PageInfo pageInfo, SealSignerQueryDto params` | `PageData<SealSignerDataDto>` | default |
| stamp | `ThreePartySealIntegrationDto params` | `String` | default |
| withfileupload | `ThreePartySealIntegrationDto params` | `ContractResponseDto` | default |
| invalid | `ThreePartySealIntegrationDto params` | `AgainContractResponse` | default |
| recall | `ThreePartySealIntegrationDto params` | `SingleResponse` | default |
| sealGetList | `ThreePartySealIntegrationDto params` | `SealListResultDto` | default |
| preSign | `PreSignDto preSignDto` | `String` | default |
| initPreSign | `InitPreSignDto initPreSignDto` | `String` | default |
| verifySeal | `VerifySealDto verifySealDto` | `String` | default |
| finish | `ContractLockRequestDto requestDto` | `SingleResponse` | default |

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
com.seeyon.cip.provider.api.signature.electronic.SignatureProviderService=com.seeyon.extend.spi.capability.CustomSignatureProviderService
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

import com.seeyon.cip.provider.api.signature.electronic.SignatureProviderService;
import com.seeyon.cip.provider.enums.CapabilityEnum;

/**
 * 电子签章能力通道扩展。
 * 业务参数、供应商 SDK / HTTP API、通道 code 从 Nacos 或平台能力配置读取，不在模板中写死。
 */
public class CustomSignatureProviderService implements SignatureProviderService {

    @Override
    public String getDescription() {
        return "自定义电子签章通道";
    }

    @Override
    public CapabilityEnum getCapabilityEnum() {
        // 按 cip-capability-api 目标版本的 CapabilityEnum 实际枚举值替换；不要猜不存在的枚举。
        return null;
    }

    @Override
    public String getChannelCode() {
        return "custom-electronic-signature";
    }

    // TODO: 按目标版本 FACT 方法签名实现 required 方法；default 方法只有业务需要时覆盖。
}
```

## Evidence 摘要

| 项 | 值 |
|----|----|
| 接口 FQCN | `com.seeyon.cip.provider.api.signature.electronic.SignatureProviderService` |
| required 方法数 | 0 |
| default 方法数 | 42 |
| Contract Source | `cip-capability-api-5.5.147.jar` + CFR |
| Evidence | FACT ✅ |
