# CP_XM_unitest
# 首先这是根据selenium+unitest+pom分层的项目
## Base层（对象库层）：page页面一些公共的方法。如：初始化、元素定位、点击、输入、获取文本、截图等方法；

## Page层（操作层）：封装对元素的操作。将每个涉及的元素操作单独封装一个操作方法，然后根据需求组装操作步骤，如登录方法=输入帐号+输入密码+点击登录三个操作进行组装；

## scripts层（业务层）：导包调用 page页面，将一个或多个操作组合起来完成一个业务功能。如：实现登录，直接调用page组装的登陆方法即可；

# 三者的关系：page层继承base层，scripts层调用page层

## tool 文件夹下存放了工具，例如导入、导出检测、生成日志、生成报告

## data 文件夹下是操作数据（暂时没用）

## image 文件夹下存放了异常截图

## log 文件夹下存放了运行日志

## report 文件夹下存放了测试报告
