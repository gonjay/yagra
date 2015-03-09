# 功能 & 特性

- 登录、注册、登出
- 上传头像
- 密码加盐存储

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
