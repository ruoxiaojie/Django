博客地址:
        http://www.cnblogs.com/liujiliang/p/7492622.html

作业功能：

        1、由原js校验输入内容是否合法 改为ajax + form表单验证形式

        2、主机列表的增、删、改、查(通过业务线可以跳转查看当前业务线有多少管理员)

        3、分页功能(搜索分页搜索的部分) 搜索为空白时,显示所有书籍

        4、左侧主机管理，可以添加主机,添加业务线(采用左右互选框形式选择管理员)

        5、基于session和cookie登录认证与注销功能 (注册内容为管理员信息)

执行方法：
        进入liujiliang目录,
                执行python manage.py runserver 127.0.0.1:9999
                首页访问url：http://127.0.0.1:9999/index.html  (第一次会跳转到login)

                参考帐号: 帐号:  alex    密码: 123456
                         帐号:  dragon  密码:123456



-------------------------------------------------------------------------------------

作业：主机管理

	用户表(id, user,pwd,email,mm)
	业务线(id, name) # 用户表_set
	主机表(id host port FK(业务线))
	用户业务线关系表(id  uid  bid)   ******


	1. 登录（Ajax POST，密码加密）
	2. 用户登录基于Session
	3. 装饰器
	4. 主机列表
			host  port  <a>业务线名称</a>
			host  port  业务线名称
			host  port  业务线名称
			host  port  业务线名称
			host  port  业务线名称

			分页

			PS: 模态对话框编辑
	5. 新页面： 当前业务线所有的管理员列表






