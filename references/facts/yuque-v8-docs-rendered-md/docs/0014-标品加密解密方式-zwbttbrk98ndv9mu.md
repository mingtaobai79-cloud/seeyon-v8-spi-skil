---
title: "标品加密解密方式"
source: "https://www.yuque.com/seeyonkk/v8/zwbttbrk98ndv9mu"
evidence: OBSERVATION
capture_method: yuque-rendered-page-copy
---

# 标品加密解密方式

> Source: https://www.yuque.com/seeyonkk/v8/zwbttbrk98ndv9mu

作者：陈晓东

时间：2025-08-15

##### 1、加解密算法

目前支持 SM4，SM3，SHA1，RSA，MD5，DES，AES。

##### 2、SM4

明文: 锄禾日当午，汗滴禾下土，谁知盘中餐，粒粒皆辛苦！

采用密钥：E6C63180C2806DD1F47B859DE501C15F

SM4加密10w次耗时:1077ms

加密后的密文：WGcrOYJ47uIZYTfAGmpZppy6X5rDXY9S6/xZo8fY8/cj3jNY+4Fo29inQsiJHmv/78u8WihB7gGi66atEoWubFyg5E0rPoNDR1OWox6pQ0k=

SM4解密10w次耗时:1065ms

解密后的明文：锄禾日当午，汗滴禾下土，谁知盘中餐，粒粒皆辛苦！

```
String srcStr = "锄禾日当午，汗滴禾下土，谁知盘中餐，粒粒皆辛苦！";
// key为16进制32长度字符串
String key = "E6C63180C2806DD1F47B859DE501C15F";
// 加密
String encrypt = SM4Utils.encrypt(srcStr， key);
// 解密
String decrypt = SM4Utils.decrypt(encrypt， key);
```

##### 3、SM3

采用密钥:^((^##(&&$(UIUIEOIDJEJDOKEDE13213

SM3加密10w次耗时:582ms

带密钥加密后的密文：83994dfa458bd6f80cc367553c44c4e325b2241cc46385ee4d22adde1e7c3f3e

明文(带密钥)与密文校验结果：true

SM3加密(不带秘钥)10w次耗时:398ms

不带密钥加密后的密文：c81270579814c4bfb5ff695425a0f2661567da2a1b931826f76e6a2133c90cbd

明文(不带密钥)与密文校验结果：true

```
String srcStr = "锄禾日当午，汗滴禾下土，谁知盘中餐，粒粒皆辛苦!";
String key = "^*(*(^##*(&&$*(UIUIEOIDJEJDOKEDE13213";
//带秘钥加密
String hexStrByKey = SM3Utils.encrypt(srcStr， key);

//不带秘钥加密
String hexStrNoKey = SM3Utils.encrypt(srcStr);
```

##### 4、RSA

明文：锄禾日当午，汗滴禾下土，谁知盘中餐，粒粒皆辛苦！ 加密后的密文为：

rsa加密1000次耗时:1327ms

带密钥加密后的密文:CSdSBXQhtqgMHeCA0hzlsoihpK2nHkXeeEkIgloYtnfcpGOJhXiOArVwZkTGThrLquMu3xasU37GImJaJnRHK4LVp4+Ir8QAm+dZNaLQcutJKzycc3qGkLi+fZCmdEu57W01kOEKLe7JZqBTAstkWFfvKlb7bjUqwvb6SCBu4xk=

rsa解密1000次耗时:1193ms

密文解密后为：锄禾日当午，汗滴禾下土，谁知盘中餐，粒粒皆辛苦！

##### 5、MD5

原始信息：锄禾日当午，汗滴禾下土，谁知盘中餐，粒粒皆辛苦!

MD5加密后(密文长度16位)：bcb39866bd881302

MD5加密后(密文长度32位)：920b9868bcb39866bd881302d50318c6

32位md5加密10w次耗时:287ms

16位md5加密10w次耗时:145ms

##### 6、SHA1

SHA1加密后：de568ad5c5a0a24180fd7dbfa34a74674015abe1

SHA1加密10w次耗时:495ms

##### 7、DES

明文信息：锄禾日当午，汗滴禾下土，谁知盘中餐，粒粒皆辛苦!

采用密钥:ABCDEFGH12345678~!@#$%^&

DES加密10w次耗时:1640ms

DES加密后密文：XDQ6gKImgWxKOaSftShO9y3hV9jCjj1hJprbPtTHZugaaOtoS54b3oPfs2A5wf2qT7RXjfW75FkMtvzGpDbwpQVfO8g7nfju

DES解密10w次耗时:1000ms

解密后：锄禾日当午，汗滴禾下土，谁知盘中餐，粒粒皆辛苦!

##### 8、AES

明文：锄禾日当午，汗滴禾下土，谁知盘中餐，粒粒皆辛苦!

采用密钥:1qaz@SX#EDC4rfv

Aes加密10w次耗时:3769ms

密文: FD5341B63C9883C1B217FABF4B0642C372F0A82CD0B10C810AF11913DE84F448FC57BD8BB71AC0EE1619409FD5EDA804F91E3AC0D3F8BB9D777948CEADF8AF4E8A4B227319005DC9DE8BB4159592498E

Aes解密10w次耗时:864ms

解密后明文：锄禾日当午，汗滴禾下土，谁知盘中餐，粒粒皆辛苦!
