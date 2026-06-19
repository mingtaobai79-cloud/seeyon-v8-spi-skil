---
title: "前端接口请求规范"
source: "https://www.yuque.com/seeyonkk/v8/gteqkvkkfw5sd9op"
evidence: OBSERVATION
capture_method: yuque-rendered-page-copy
---

# 前端接口请求规范

> Source: https://www.yuque.com/seeyonkk/v8/gteqkvkkfw5sd9op

```
import { ajax } from "@seeyon/global";
```

```
//流程预测数据
export const getPredictionResult = async(params: any ) =>{
  const res = await ajax.post(`/bpm/simulation/process-prediction`,
                              params
                             )
  return res.data;
}

//获取表单的意见区数据
//http://175.178.251.177:8808/service/bpm/graphql?bpmSummarySelectOpinionByDimensionPost
export const getBpmSummarySelectOpinionByDimensionPost = async(params: any ) =>{
  const res = await ajax.post(`/bpm/summary/select-opinion-by-dimension`,
                              params
                             )
  return res.data;
}
```

备注：原有grapghql接口规范不推荐使用
