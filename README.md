# myplatform
1、集成一些在安全漏洞审核中比较方便的小工具。flatform基于flask。目前还很简陋，后续慢慢完善。  
2、在漏洞审核过程中，存在几个问题。这个list不断更新中，  
    ①白帽子提供了csrf_poc，审核人员需要复制poc到html文件，较为繁琐。  
    ②白帽子没有提供csrf_poc，只提供了csrf的action和参数，需要手动生成poc。  
    ③目前poc处于“用完就删”的状态，不利于管理。它们并不是一次性用完就可以扔掉了，后续复测、统计也需要。  
   

## 20190520提交

**在这个520的日子，别人在秀恩爱，我却在提交一行代码 :)**

写了一个csrf测试小平台，功能如下：  
1、根据csrf-url和csrf-params生成csrf-form表单。可选form-method为get和post  
页面入口地址：/csrf/index  
生成csrf_poc的接口地址：/csrf/createpoc  

2、查看当前平台上生成的所有csrf_poc  
页面入口地址：/csrf/pocs/allpocs  
查看某个具体的poc：/csrf/pocs/<poc_name>  

3、给某个poc重命名  
页面入口地址：/csrf/pocs/allpocs  
重命名接口：/csrf/renamepoc  

Todo：  
1、删除某个Poc  
2、增加使用ajax提交csrf_params的方式。目前只支持form表单。  
3、增加伪造referer等http请求头的功能。（需要调研一下可行性）  
