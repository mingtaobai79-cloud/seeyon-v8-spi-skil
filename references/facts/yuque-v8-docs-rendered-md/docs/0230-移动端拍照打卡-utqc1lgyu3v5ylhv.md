操作步骤：  
1.使用具有可以看到低代码定制平台的账号登录OA导入udc应用

<img src="https://cdn.nlark.com/yuque/0/2026/png/900375/1780381939883-20037229-5dba-4cf7-8c12-ce915fa6e33f.png" width="416" title="" crop="0,0,1,1" id="u45e259ea" class="ne-image">

2.导入成功后，需要将移动端拍照打卡应用进行构建

<img src="https://cdn.nlark.com/yuque/0/2026/png/900375/1780381946763-78bc45aa-d7aa-4f6b-8659-c04d996f7caa.png" width="416" title="" crop="0,0,1,1" id="ued4a33e5" class="ne-image">

3.再将custom-frontend\extend-components\new-locationPhotography-button\目录下的文件全部提交到system-admin账号登录后OA，菜单：客开管理-前端扩展-工程里面，并将代码提交到对应的1.0分支，点击构建按钮，进行构建，看到构建状态：构建成功 ，就表示次组件已部署到本环境里面。

<img src="https://cdn.nlark.com/yuque/0/2026/png/900375/1780381951822-b6089fae-9ed7-4e15-ab2c-5fe4685e5f41.png" width="416" title="" crop="0,0,1,1" id="uff44c1cb" class="ne-image">

<img src="https://cdn.nlark.com/yuque/0/2026/png/900375/1780381958454-377fcfe5-85e2-4990-be23-0229fad9c31c.png" width="416" title="" crop="0,0,1,1" id="uf50e9664" class="ne-image">

<img src="https://cdn.nlark.com/yuque/0/2026/png/900375/1780381962225-68d39fb9-acf2-41d3-9ea0-0c2a76522503.png" width="416" title="" crop="0,0,1,1" id="u8d113e5c" class="ne-image">

4.切换到后台管理，找到需要使用移动端拍照定位组件的应用，先将组件引入，再拖到搭建页面里面

<img src="https://cdn.nlark.com/yuque/0/2026/png/900375/1780381971326-b5ba0638-a549-480d-82f8-be63ccd4c74e.png" width="416" title="" crop="0,0,1,1" id="u197fdfd0" class="ne-image">

若是组件依赖区域里面没有搜索到“定位拍照打卡按钮”组件，组件依赖-前端组件-添加依赖-移动端 进行搜索对应的组件名称添加到应用里面

<img src="https://cdn.nlark.com/yuque/0/2026/png/900375/1780381977743-49653d9e-cfc3-4417-8f39-02954316a736.png" width="416" title="" crop="0,0,1,1" id="uf2a1366a" class="ne-image">

<img src="https://cdn.nlark.com/yuque/0/2026/png/900375/1780381983838-71da3122-3ffc-45fa-809c-470719823152.png" width="416" title="" crop="0,0,1,1" id="uaf7a1005" class="ne-image">

5. 配置完毕后构建即可，到对应的运行态看对应的效果



[移动端拍照打卡源码及操作.zip](https://www.yuque.com/attachments/yuque/0/2026/zip/900375/1780382005285-2eb8e262-59b9-487b-9923-5fe42e3333b5.zip)
