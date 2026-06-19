# Seeyon V8 语雀索引（本地 SPI 子集 + 远程检索）

## 口径

- 本地：`docs/` 只保留 SPI / Super SPI / ProviderService / 生成工程相邻规范子集。
- 远程：完整语雀来源为 `https://www.yuque.com/seeyonkk/v8`。本地无命中、非 SPI 文档、或用户给具体 URL 时，用 `tools/yuque_fetch.py` 查远程。
- Evidence：语雀结果最高为 OBSERVATION；接口签名、DTO、artifact 仍需 jar / 源码 / OpenAPI exact match 才能升 FACT。

## 本地索引

```text
docs/*.md       # 本地 SPI 子集正文
manifest.json   # local_file <-> remote_url 映射
tools/yuque_fetch.py # 远程语雀检索 / 指定 URL 获取
```

## 数量

```text
local_spi_docs=85
remote_book=https://www.yuque.com/seeyonkk/v8
removed_non_spi_docs=145  # 已移出 active skill tree；需要时走远程脚本
```

## 使用

本地快查：

```bash
python references/contract-index/tools/query_yuque_local_index.py "MQ扩展"
```

远程/URL 查：

```bash
python references/facts/yuque-v8-docs-rendered-md/tools/yuque_fetch.py --query "<关键词>" --max-results 8
python references/facts/yuque-v8-docs-rendered-md/tools/yuque_fetch.py --query "<关键词>" --url "https://www.yuque.com/seeyonkk/v8/<slug>" --max-results 8
```

## 本地文档清单

- V8知识大纲进度跟踪表 | local: `docs/0001-V8知识大纲进度跟踪表-mhhl2p4uxo8fdp08.md` | remote: https://www.yuque.com/seeyonkk/v8/mhhl2p4uxo8fdp08
- 开发准备 | local: `docs/0002-开发准备-fqdmdrodt7x7p6no.md` | remote: https://www.yuque.com/seeyonkk/v8/fqdmdrodt7x7p6no
- nacos开关 | local: `docs/0005-nacos开关-lw1x44oiovko3ybv.md` | remote: https://www.yuque.com/seeyonkk/v8/lw1x44oiovko3ybv
- 日志扩展 | local: `docs/0012-日志扩展-vu83q687l6skhpk9.md` | remote: https://www.yuque.com/seeyonkk/v8/vu83q687l6skhpk9
- 标品加密解密方式 | local: `docs/0014-标品加密解密方式-zwbttbrk98ndv9mu.md` | remote: https://www.yuque.com/seeyonkk/v8/zwbttbrk98ndv9mu
- MQ组件 | local: `docs/0015-MQ组件-hs96yt55xze6xydg.md` | remote: https://www.yuque.com/seeyonkk/v8/hs96yt55xze6xydg
- Nacos和应用参数获取方式 | local: `docs/0016-Nacos和应用参数获取方式-lzbghrhioxhhd31r.md` | remote: https://www.yuque.com/seeyonkk/v8/lzbghrhioxhhd31r
- Dubbo接口说明 | local: `docs/0020-Dubbo接口说明-dubbo.md` | remote: https://www.yuque.com/seeyonkk/v8/dubbo
- 公式组件(暂不支持扩展) | local: `docs/0021-公式组件(暂不支持扩展)-vcvg1gny9rp8tplv.md` | remote: https://www.yuque.com/seeyonkk/v8/vcvg1gny9rp8tplv
- 平台技术白皮书 | local: `docs/0022-平台技术白皮书-khioi6tyczlxno45.md` | remote: https://www.yuque.com/seeyonkk/v8/khioi6tyczlxno45
- 后端常用方法 | local: `docs/0023-后端常用方法-yh43gpiq9beh16xd.md` | remote: https://www.yuque.com/seeyonkk/v8/yh43gpiq9beh16xd
- 工程结构 | local: `docs/0056-工程结构-zy37084h3lxylfy9.md` | remote: https://www.yuque.com/seeyonkk/v8/zy37084h3lxylfy9
- 接口规范 | local: `docs/0058-接口规范-wpinkgn5ggfwmkta.md` | remote: https://www.yuque.com/seeyonkk/v8/wpinkgn5ggfwmkta
- MQ消息规范 | local: `docs/0066-MQ消息规范-vdlfzwdaafl67yr9.md` | remote: https://www.yuque.com/seeyonkk/v8/vdlfzwdaafl67yr9
- Rest规范 | local: `docs/0067-Rest规范-lkrzaod5edg33r8k.md` | remote: https://www.yuque.com/seeyonkk/v8/lkrzaod5edg33r8k
- 平台页面js/css/jssdk扩展 | local: `docs/0077-平台页面js_css_jssdk扩展-fch83t5fwntnm4zy.md` | remote: https://www.yuque.com/seeyonkk/v8/fch83t5fwntnm4zy
- 扩展插槽 | local: `docs/0082-扩展插槽-zngrgup351qls4gv.md` | remote: https://www.yuque.com/seeyonkk/v8/zngrgup351qls4gv
- 自定义行为扩展 | local: `docs/0083-自定义行为扩展-vfs0bxnr8msg4152.md` | remote: https://www.yuque.com/seeyonkk/v8/vfs0bxnr8msg4152
- SPI扩展 | local: `docs/0085-SPI扩展-nizgyacv5x4oh0wh.md` | remote: https://www.yuque.com/seeyonkk/v8/nizgyacv5x4oh0wh
- 三方事项栏目自动刷新 | local: `docs/0089-三方事项栏目自动刷新-zyxzukrgg38n6svy.md` | remote: https://www.yuque.com/seeyonkk/v8/zyxzukrgg38n6svy
- 批处理三方待办事项 | local: `docs/0090-批处理三方待办事项-gonq0zusief36hit.md` | remote: https://www.yuque.com/seeyonkk/v8/gonq0zusief36hit
- 自定义租户、机构登录人数控制 | local: `docs/0092-自定义租户、机构登录人数控制-lbtxv6th0m01v9im.md` | remote: https://www.yuque.com/seeyonkk/v8/lbtxv6th0m01v9im
- 登录扩展 | local: `docs/0094-登录扩展-ix6conpzm43saumy.md` | remote: https://www.yuque.com/seeyonkk/v8/ix6conpzm43saumy
- 菜单导航添加三方菜单 | local: `docs/0095-菜单导航添加三方菜单-ingocx5774cym2xs.md` | remote: https://www.yuque.com/seeyonkk/v8/ingocx5774cym2xs
- ticket认证返回人员信息自定义 | local: `docs/0096-ticket认证返回人员信息自定义-pazygl1cot73gavl.md` | remote: https://www.yuque.com/seeyonkk/v8/pazygl1cot73gavl
- 登录前门户 | local: `docs/0098-登录前门户-np2eldavkvhybzzy.md` | remote: https://www.yuque.com/seeyonkk/v8/np2eldavkvhybzzy
- 公文扩展接口 | local: `docs/0099-公文扩展接口-ss8h88xen6x2al43.md` | remote: https://www.yuque.com/seeyonkk/v8/ss8h88xen6x2al43
- 事项中心流程扩展 | local: `docs/0100-事项中心流程扩展-bykkpxgxntm6cltm.md` | remote: https://www.yuque.com/seeyonkk/v8/bykkpxgxntm6cltm
- 注册中心 | local: `docs/0101-注册中心-qc6siuqr3xa5ti0c.md` | remote: https://www.yuque.com/seeyonkk/v8/qc6siuqr3xa5ti0c
- 配置中心 | local: `docs/0102-配置中心-etln83yguiz4k0pd.md` | remote: https://www.yuque.com/seeyonkk/v8/etln83yguiz4k0pd
- MQ扩展 | local: `docs/0103-MQ扩展-qii2f3ybtoq43pnz.md` | remote: https://www.yuque.com/seeyonkk/v8/qii2f3ybtoq43pnz
- 上传下载文件扩展 | local: `docs/0104-上传下载文件扩展-ibmhcc3391u12fsg.md` | remote: https://www.yuque.com/seeyonkk/v8/ibmhcc3391u12fsg
- 散列加密 | local: `docs/0105-散列加密-htbbndul0hfirkdu.md` | remote: https://www.yuque.com/seeyonkk/v8/htbbndul0hfirkdu
- 对称加密 | local: `docs/0106-对称加密-wqgtvw7hlnaqwage.md` | remote: https://www.yuque.com/seeyonkk/v8/wqgtvw7hlnaqwage
- 系统变量扩展 | local: `docs/0107-系统变量扩展-xynmcgh1igvh01n2.md` | remote: https://www.yuque.com/seeyonkk/v8/xynmcgh1igvh01n2
- 认证系统接入 | local: `docs/0108-认证系统接入-uevxy4zvbfi6bs11.md` | remote: https://www.yuque.com/seeyonkk/v8/uevxy4zvbfi6bs11
- 三方单点到V8 | local: `docs/0109-三方单点到V8-v8-ctp-user-api-ctpavoidloginmiddlepageproviderservice.md` | remote: https://www.yuque.com/seeyonkk/v8/v8-ctp-user-api-ctpavoidloginmiddlepageproviderservice
- V8单点到三方 | local: `docs/0110-V8单点到三方-v8-cip-connector-api-ssoservice.md` | remote: https://www.yuque.com/seeyonkk/v8/v8-cip-connector-api-ssoservice
- V8接入三方App | local: `docs/0111-V8接入三方App-rx8blahmz6zt2u4d.md` | remote: https://www.yuque.com/seeyonkk/v8/rx8blahmz6zt2u4d
- 集成接口鉴权 | local: `docs/0112-集成接口鉴权-nks3s8agdgi1im3z.md` | remote: https://www.yuque.com/seeyonkk/v8/nks3s8agdgi1im3z
- 文件操作 | local: `docs/0113-文件操作-hl17w2x7p9wu11t0.md` | remote: https://www.yuque.com/seeyonkk/v8/hl17w2x7p9wu11t0
- 能力通道扩展 | local: `docs/0114-能力通道扩展-glpgswl2kflo5850.md` | remote: https://www.yuque.com/seeyonkk/v8/glpgswl2kflo5850
- 数据源扩展 | local: `docs/0115-数据源扩展-wkew2iynh3d3rauh.md` | remote: https://www.yuque.com/seeyonkk/v8/wkew2iynh3d3rauh
- 组织同步中间表扩展 | local: `docs/0116-组织同步中间表扩展-wthi6ignkwu033ok.md` | remote: https://www.yuque.com/seeyonkk/v8/wthi6ignkwu033ok
- AI | local: `docs/0135-AI-ai.md` | remote: https://www.yuque.com/seeyonkk/v8/ai
- 短信 | local: `docs/0136-短信-smsproviderservice.md` | remote: https://www.yuque.com/seeyonkk/v8/smsproviderservice
- 电子邮件 | local: `docs/0137-电子邮件-lonl0sev2do5sswq.md` | remote: https://www.yuque.com/seeyonkk/v8/lonl0sev2do5sswq
- 在线文档 | local: `docs/0138-在线文档-hnoy0cnu8t5rl97o.md` | remote: https://www.yuque.com/seeyonkk/v8/hnoy0cnu8t5rl97o
- WPS配置及常见问题 | local: `docs/0139-WPS配置及常见问题-rw2kc8wvokon654l.md` | remote: https://www.yuque.com/seeyonkk/v8/rw2kc8wvokon654l
- 版式文档 | local: `docs/0140-版式文档-dygyzew5otosm4pc.md` | remote: https://www.yuque.com/seeyonkk/v8/dygyzew5otosm4pc
- 智能文档 | local: `docs/0141-智能文档-cz2vt0hclv76regl.md` | remote: https://www.yuque.com/seeyonkk/v8/cz2vt0hclv76regl
- 合合 | local: `docs/0142-合合-xq1twzblp4640vob.md` | remote: https://www.yuque.com/seeyonkk/v8/xq1twzblp4640vob
- 简历解析 | local: `docs/0143-简历解析-gdzts8d29pbzxcvf.md` | remote: https://www.yuque.com/seeyonkk/v8/gdzts8d29pbzxcvf
- OCR识别 | local: `docs/0144-OCR识别-ocr.md` | remote: https://www.yuque.com/seeyonkk/v8/ocr
- 视频会议 | local: `docs/0145-视频会议-ivwplr4wwg33w8sp.md` | remote: https://www.yuque.com/seeyonkk/v8/ivwplr4wwg33w8sp
- 商旅服务 | local: `docs/0146-商旅服务-shortl2okuort02z.md` | remote: https://www.yuque.com/seeyonkk/v8/shortl2okuort02z
- 企业征信 | local: `docs/0147-企业征信-sgtn67nnga2dei8l.md` | remote: https://www.yuque.com/seeyonkk/v8/sgtn67nnga2dei8l
- 启信宝 | local: `docs/0148-启信宝-lf6ug4tttyywm7fg.md` | remote: https://www.yuque.com/seeyonkk/v8/lf6ug4tttyywm7fg
- 发票服务 | local: `docs/0149-发票服务-dsbmug3v87eqheii.md` | remote: https://www.yuque.com/seeyonkk/v8/dsbmug3v87eqheii
- 物理印章 | local: `docs/0150-物理印章-guror8p6i1x1srye.md` | remote: https://www.yuque.com/seeyonkk/v8/guror8p6i1x1srye
- 电子签章 | local: `docs/0151-电子签章-kmkvpvbvzpsnyp1k.md` | remote: https://www.yuque.com/seeyonkk/v8/kmkvpvbvzpsnyp1k
- 翻译服务 | local: `docs/0152-翻译服务-hi342ylk3b8ghz3r.md` | remote: https://www.yuque.com/seeyonkk/v8/hi342ylk3b8ghz3r
- 天气预报 | local: `docs/0153-天气预报-sunh9n2l44py9s08.md` | remote: https://www.yuque.com/seeyonkk/v8/sunh9n2l44py9s08
- 天气查询 | local: `docs/0154-天气查询-gs3o2l75fd8kkfd2.md` | remote: https://www.yuque.com/seeyonkk/v8/gs3o2l75fd8kkfd2
- GIS服务 | local: `docs/0155-GIS服务-gis.md` | remote: https://www.yuque.com/seeyonkk/v8/gis
- 地理位置 | local: `docs/0156-地理位置-sr99gd076pshgxip.md` | remote: https://www.yuque.com/seeyonkk/v8/sr99gd076pshgxip
- 离线消息 | local: `docs/0157-离线消息-qhix1g6uzquoy08a.md` | remote: https://www.yuque.com/seeyonkk/v8/qhix1g6uzquoy08a
- 离线消息配置 | local: `docs/0158-离线消息配置-xgzdb06lbk09z1gv.md` | remote: https://www.yuque.com/seeyonkk/v8/xgzdb06lbk09z1gv
- 标签打印 | local: `docs/0159-标签打印-by4kq17m1o7br277.md` | remote: https://www.yuque.com/seeyonkk/v8/by4kq17m1o7br277
- 银企直连 | local: `docs/0160-银企直连-xkoabytfxo4xdzg2.md` | remote: https://www.yuque.com/seeyonkk/v8/xkoabytfxo4xdzg2
- 全文检索 | local: `docs/0161-全文检索-xrw76qgaotqc0gvv.md` | remote: https://www.yuque.com/seeyonkk/v8/xrw76qgaotqc0gvv
- 语音技术 | local: `docs/0162-语音技术-gx3fls0f39yvk5lq.md` | remote: https://www.yuque.com/seeyonkk/v8/gx3fls0f39yvk5lq
- 移动日程 | local: `docs/0163-移动日程-hby563h7pvqaacgb.md` | remote: https://www.yuque.com/seeyonkk/v8/hby563h7pvqaacgb
- 档案系统 | local: `docs/0164-档案系统-doa9ya5tvl6btiuq.md` | remote: https://www.yuque.com/seeyonkk/v8/doa9ya5tvl6btiuq
- 人脸识别 | local: `docs/0165-人脸识别-hzsivn6xp8eca6ii.md` | remote: https://www.yuque.com/seeyonkk/v8/hzsivn6xp8eca6ii
- 敏感词 | local: `docs/0166-敏感词-hng30tufn8fktv7i.md` | remote: https://www.yuque.com/seeyonkk/v8/hng30tufn8fktv7i
- 在线支付 | local: `docs/0167-在线支付-rusz6cfbw81h67ty.md` | remote: https://www.yuque.com/seeyonkk/v8/rusz6cfbw81h67ty
- 3.15之前的版本扩展代码如何构建 | local: `docs/0183-3.15之前的版本扩展代码如何构建-zcormguidgprgedl.md` | remote: https://www.yuque.com/seeyonkk/v8/zcormguidgprgedl
- 扩展代码-添加菜单 | local: `docs/0188-扩展代码-添加菜单-yuihf5rrtk0qs1kl.md` | remote: https://www.yuque.com/seeyonkk/v8/yuihf5rrtk0qs1kl
- BPM平台 | local: `docs/0193-BPM平台-vhkpt9byr8p32zy3.md` | remote: https://www.yuque.com/seeyonkk/v8/vhkpt9byr8p32zy3
- BPM功能扩展 | local: `docs/0195-BPM功能扩展-bpm.md` | remote: https://www.yuque.com/seeyonkk/v8/bpm
- 流程触发方法 | local: `docs/0196-流程触发方法-bf8agor08ia7u045.md` | remote: https://www.yuque.com/seeyonkk/v8/bf8agor08ia7u045
- 流程按钮扩展行为 | local: `docs/0197-流程按钮扩展行为-xuimob9dd26fwdb6.md` | remote: https://www.yuque.com/seeyonkk/v8/xuimob9dd26fwdb6
- 正文组件技术说明文档 | local: `docs/0199-正文组件技术说明文档-zfbeqyeoyh6x5onl.md` | remote: https://www.yuque.com/seeyonkk/v8/zfbeqyeoyh6x5onl
- 正文自定义事件操作步骤 | local: `docs/0200-正文自定义事件操作步骤-cyxo4l4xfenm0cyz.md` | remote: https://www.yuque.com/seeyonkk/v8/cyxo4l4xfenm0cyz
