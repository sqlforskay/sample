# 概述

[![](https://img.shields.io/badge/github-issues-%2365A30D?style=flat-square&logo=github)](https://github.com/sqlforskay/sample/issues)
[![](https://img.shields.io/badge/github-traffic-green)](https://github.com/sqlforskay/sample/graphs/traffic)

#### 简体中文 | [English](/README.md)

****

**极速**建站,我选**sample**-Flask! **Python**网站开发者的福音!🔥🔥🔥

**sample**是一个高度封装的Flask Demo.

它集成了各种代码,用于web开发目的第三方包，route Demo，templates Demo(存放html的文件)等等。

这是全网 **最方便** , **教程易读** 的Flask Sample, **一键** 安装, **一键** 运行.
## 安装

- 在根目录运行 ```pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple``` 去安装所需模块，或者运行 **install.cmd / install.sh** 安装所需模块。( ```chmod +x install.sh && ./install.sh``` )

## 运行

- 在linux下运行```chmod +x script.sh && ./script.sh```。在Windows上点击 **script.bat** 运行.

## 开始使用

- 在 ```project/templates/``` 路径下添加或修改静态HTML,JS,CSS文件.( **可选** )
- 在 ```project/routes/``` 文件夹以修改 **.py** 的路由文件.( **可选** )
- 如果需要用到Mysql数据库,在 ```sample/project/config.py``` 修改Mysql数据库的连接参数.( **可选** )
- 如果需要用到Mysql数据库,模仿 Mysql [ORM 例子](https://github.com/sqlforskay/sample/) 创建新的 Mysql 代码.( **可选** )
- 模仿 Routes [例子](https://github.com/sqlforskay/sample/) 创建新的 routes 代码.( **可选** )
- 在linux下运行```chmod +x script.sh && ./script.sh```。在Windows上点击 **script.bat** 运行.

## 所需环境 

- Python 2.7以上 版本, 最好是 3.6 版本.
- Mysql.( **可选** )

## 优势
- 安装运行简易,一步到位.
- 代码轻量,易读,优美.
- BUG少,相较其他难遇到.
- 减少开发工作量,距离动态网站更近一步.
- 教程详细,易找.
- **非常适合用不来,用不习惯,没学过SQLAlchemy的开发者**,封装了mysql相关函数,因为mysql大量用于生成环境.弥补了flask官方文档中SQLAlchemy只能使用sqlite或者mongodb的不足.
- 定义了一个相对标准的flask文件结构,让复杂的动态网站开发有迹可循.

## 项目结构

  ```
  ├── .github
  │   ├── workflows
  │   │   ├── codeql-analysis.yml
  │   ├── FUNDING.yml
  ├── project
  │   ├── models
  │   │   ├── __init__.py
  │   │   ├── sql.py
  │   │   ├── user.py
  │   ├── routes
  │   │   ├── __init__.py 
  │   │   ├── admin.py
  │   │   ├── auth.py
  │   │   ├── index.py
  │   ├── services
  │   │   ├── __init__.py 
  │   │   ├── external_functions.py
  │   │   ├── external_objects.py
  │   ├── templates
  │   │   ├── PutHtmlCodeThere.md
  │   ├── venv
  │   │   ├──......
  │   ├── __init__.py
  │   ├── database.py 
  │   ├── config.py 
  ├── LICENSE
  ├── README_CN.md
  ├── README.md
  ├── install.cmd
  ├── install.sh
  ├── manage.py
  ├── script.cmd
  ├── script.sh
  ├── requirements.txt
  ```

## 加入我们
你的帮助很受欢迎！ 甚至只是打开一个[问题](https://github.com/sqlforskay/sample/issues)，提出一个问题可能会极大地帮助他人。
