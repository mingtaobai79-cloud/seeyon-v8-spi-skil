---
title: "后端常用方法"
source: "https://www.yuque.com/seeyonkk/v8/yh43gpiq9beh16xd"
evidence: OBSERVATION
capture_method: yuque-rendered-page-copy
---

# 后端常用方法

> Source: https://www.yuque.com/seeyonkk/v8/yh43gpiq9beh16xd

作者：陈晓东

时间：2025-07-02

# 1、获取应用下的枚举信息

```
private CtpEnumAppService ctpEnumAppService;//获取枚举定义
private CtpEnumItemAppService ctpEnumItemAppService;//获取具体枚举子项
```

跨应用获取枚举需泛化调用

```
@Autowired
private DubboFactory dubboFactory;

AppServiceInvokeDto invokeDto = new AppServiceInvokeDto();
            String enumCode = "certificateType";
            invokeDto.setInterfaceName("com.seeyon.boot.starter.enums.appservice.CtpEnumItemAppService");
            // 方法名称
            invokeDto.setMethodName("selectByEnumCode");
            // 参数类型
            invokeDto.setParamType(SingleRequest.class.getName());
            invokeDto.setParamJson(JsonUtils.toJson(SingleRequest.from(enumCode)));
            invokeDto.setGenericType(enumCode.getClass().getName());
            invokeDto.setCommandId(Ids.gidString());
            AppServiceProxy appServiceProxy = dubboFactory.getProxy(AppServiceProxy.class, "organization", DubboFactory.DEFAULT_VERSION,60000);
            SingleResponse<Object> response = appServiceProxy.invokeAppService(SingleRequest.from(invokeDto));
            if (response.success()) {
                Object content = response.getData().getContent();
                List<CtpEnumItemDto> enumItemDtos = (List<CtpEnumItemDto>) content;
            } else {
                throw BusinessException.message("泛化调用失败");
            }
```

# 2、获取当前登录人相关的信息

```
Apps.getRequestContext().getTenantId();//获取当前租户Id
Apps.getRequestContext().getUserId();//获取当前用户Id
Apps.getRequestContext().getLoginOrgId();//获取当前用户所属组织Id
Apps.getAppCaption();//获取当前应用描述名称
Apps.getAppName();//获取当前服务名称
SystemVariableUtils.currentOrgId();//获取当前用户登录部门
RequestContext.get();//获取上下文 所以可以不使用Apps.getRequestContext()来获取上下文了
SystemVariableUtils.currentUserLoginName()//获取当前登录名
```

# 3、获取组织和人员信息

```
@DubboReference
private OrgMemberBaseAppService orgMemberBaseAppService;//对人员增删改查
@DubboReference
private OrgUnitBaseAppService orgUnitBaseAppService;//对组织增改查
@DubboReference
private OrgJobBaseAppService orgJobBaseAppService;//对职务增改查
@DubboReference
private OrgPostBaseAppService orgPostBaseAppService;//对岗位增改查
@DubboReference
private CtpUserCoreAppService userAppService;//获取人员信息
@DubboReference
private OrgCommonAppService orgCommonAppService; //获取下级信息selectChildrenOrgByCondition
```

# 4、文件操作

```
private FileInfoService fileInfoService;//文件信息操作（ctp_file表）
private FileService fileService;//物理文件操作，包含文件信息
```

# 5、WORD转PDF

```
@DubboReference
private DocOnlineAppService docOnlineAppService;
/**
 * word转 pdf
 * @param storageKeys 原文件key
 * @param fileDto 原文件对象
 * @return 新的PDF文件key
 */
private String wordConvert2Pdf(String storageKeys, FileDto fileDto){
    DocFileConvertDto dto = new DocFileConvertDto();
    dto.setStorageKey(storageKeys);
    dto.setFileName(fileDto.getFileName());
    dto.setTargetFileFormat("pdf");
    dto.setSceneType(1);
    dto.setSync(true);
    SingleResponse<DocFileConvertStateDto> response = docOnlineAppService.cpsOfficeConvert(SingleRequest.from(dto));
    DocFileConvertStateDto stateDto = ResponseUtils.responseResolve(response, "转版服务");
    return stateDto.getTargetStorageKey();
}
```

# 6、HTML转PDF

```
@DubboReference
private HtmlConvertAppService htmlConvertAppService;
@DubboReference
private CtpAuthCoreAppService ctpAuthCoreAppService;
//获取cookie
public Map<String, String> buildCookie(String taskId, Long userId) {
    Map<String, String> cookieMap = new HashMap<>();

    Map<String, Object> map = new HashMap<>();
    map.put("userId", userId);
    SingleResponse<String> singleResponse = ctpAuthCoreAppService.getTempAccessToken(SingleRequest.from(map));
    if (!ErrorCode.SUCCESS.equals(singleResponse.getCode())) {
        log.error("taskId:{},userId:{},获取token信息出错了", taskId, userId);
    } else {
        cookieMap.put("SY_ACCESS_TOKEN", singleResponse.getData().getContent());
        cookieMap.put("SY_UID", String.valueOf(userId));
        cookieMap.put("HWWAFSESTIME", String.valueOf(System.currentTimeMillis()));

        log.info("taskId:{},cookie:{}", taskId, JsonUtils.toJson(cookieMap));
        return cookieMap;
    }
    return null;
}
public void html2PdfSign(Html2PdfDto html2PdfDto) {
    TransferRequestDto transferRequestDto = new TransferRequestDto();
    transferRequestDto.setCookies(buildCookie(html2PdfDto.getAffairId(),Apps.getRequestContext().getUserId()));
    transferRequestDto.setFileName(html2PdfDto.getAffairId() + ".pdf");
    transferRequestDto.setType(DocumentTypeEnum.PDF);
    transferRequestDto.setAsync(Boolean.TRUE);
    transferRequestDto.setTaskId(html2PdfDto.getAffairId());
    //URL需要使用打印页面的URL，且URL必须是完整地址(包含http://)
    transferRequestDto.setUrl(html2PdfUrl(html2PdfDto.getPageUrl()));
    htmlConvertAppService.transfer(SingleRequest.from(transferRequestDto));//异步
    //获取转换后的PDF
    FileConvertResultDto fileConvertResultDto = htmlConvertAppService.queryTransferInfo(SingleRequest.from(queryTransferRequestDto)).getData().getContent();
    //获取转换后PDF对应的storageKey    
```

# 7、缓存对象RedisTemplate 使用

```
// 声明RedisTemplate 对象
private static RedisTemplate redisTemplate = null; 
// 通过 Apps，从 Bean 池中获取redisTemplate 的 Bean
redisTemplate = (RedisTemplate) Apps.getApplicationContext().getBean("redisTemplate");

// 获取缓存值
redisTemplate.opsForValue().get(detectionCountKey);

// 设置缓存值
redisTemplate.opsForValue().set(obj);
```

# 8、获取第三方集成应用中的地址

以下以第三方集成应用中的 OA 系统为示例：

协同运营平台
海之韵DEMO
面向组织全生命周期的协同管理平台
品
组织模型
用户中心
应用中心
行政组织管理岗位职务职级管理人员及任职管理组织角色管理
用户管理角色管理授权管理
应用管理工作台设置 菜单设置|应用运行日志
多维组织管理|外部单位管理|
日志管理权限审计认证服务
理系统维管理|通讯录设置
应用效据目志
流程管理中心
门户管理
集成平台
系 流程管理  流程配置|流程达维监控
首页管理门户管理|空间管理|个性化定制/管理
基础设置 三方应用集成 开放平台(基础能力接入
栏目管理  样式库
报表中心
跨环境推送
基础设置
全局配置推送业务应用推送接收管理操作日志
系统参数 灵格设置工作时间设置消息订阅设置
推索设置常用语设置代理设置国际化
定时任务
印章管理  标签管理
务消息模板管理
节假日提醒消息推送设置
基础应用管理|敏服词管理
事项中心
事项列表 参数管理|枚举管理|性胞提升

<img width="643">

<img width="1491">

<img width="1425">

大致的内容是通过调用 LinkerAppServiceImpl的selectOneById方法，获取应用信息，请求成功后获取到 LinkerInfoDto 对象，从getMainAddress方法中获取到地址信息

# 9、通过登录名获取内部用户信息

泛化调用会经过ctpUserSpiSsoHandler中的ctpUserSpiSsoHandler方法，调用ThirdSsoHandler的getCtpUserHasTenant方法，最终到达ThirdSsoHandler的getCtpUser方法，返回内部用户的信息

# 10、通过affairId获取对应单据数据

# 11、通过affairId获取对应公文发文数据

文件下载可以通过浏览器访问：域名/service/storageKey  下载获得

例：https://xxx.com/service/storageKey

# 12、查询当前人员在组织模型中是否拥有某个角色

1、先通过角色的编码获取当前角色的 roleID

2、根据 roleId 和 memberIds 获取当前人员在哪些部门有这个角色

返回的结果为 list，结果中带有当前的角色、当前的部门 ID、拥有此角色的人员 IDs（逗号分割）

<img width="1148">

# 13、查询当前人员在用户中心中是否有某个角色

1、跟组织模型一样的查询方式，可以先根据角色编码查询角色，再根据角色和用户 ID 查询

2、区别：组织架构中的用户ID 是以逗号分割的数组例如 1,2,3,4,5，表示 5 个人

用户中心这边是以一个用户 ID 对应一个 roleID [userId:1,roleId:11],[userId:1,roleId:12]

<img width="793">
