# Yagra 功能 & 特性

- 登录、注册、登出
- 上传头像
- 密码加盐存储

# 说明

`sign_in.py sign_up.py yagra.py` 能处理 GET 和 POST 请求，对应了表单的获取和提交。

```
Method	URL						Params
GET    /cgi-bin/sign_in.py 						  # 获取登录的表单
POST   /cgi-bin/sign_in.py 	email,password  	  # 提交登录的表单
GET    /cgi-bin/sign_up.py 						  # 获取注册的表单
POST   /cgi-bin/sign_up.py  email,psw,confirm_psw # 提交注册的表单
GET    /cgi-bin/yagra.py  						  # 获取主页面
POST   /cgi-bin/yagra.py 	avatar(file) 		  # 提交上传或更新头像的表单
```

头像访问地址的 API
```python
url = "http://yagra.cc/avatar/%s" % hashlib.md5("example@163.com").hexdigest()
```

# 依赖

- Python2.7
- mysql-python
- Apache2

# Apache 配置

alias_module:
```
ScriptAlias /cgi-bin/ "/path/to/project/"
Alias /avatar "/path/to/project/file"
```

Directory:
```
<Directory "/path/to/project/">
    Options Indexes FollowSymLinks MultiViews +ExecCGI
    AllowOverride None
    Options None
    Order allow,deny
    Allow from all
</Directory>

<Directory "/path/to/project/file">
    Options Indexes MultiViews
    AllowOverride None
    Order allow,deny
    Allow from all
</Directory>
```

# MySQL 配置

1. 连上mysql

		mysql -u root -p

2. 新建一个名为 yagra 的用户，拥有 yagra 数据库下的权限

		grant all privileges on yagra.* to yagra@localhost Identified by "123456";

3. 创建yagra数据库，指定字符集

		CREATE DATABASE `yagra`
		CHARACTER SET 'utf8'
		COLLATE 'utf8_general_ci';

4. 选择 Database

	```sql
	CREATE TABLE `user` (
	  `id` int(11) NOT NULL AUTO_INCREMENT,
	  `email` varchar(255) NOT NULL,
	  `salt` varchar(255) DEFAULT NULL,
	  `token` varchar(255) DEFAULT NULL,
	  PRIMARY KEY (`id`)
	) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8;
	```

5. 修改配置文件 lib.py 中的数据库配置
