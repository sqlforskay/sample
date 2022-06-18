# Overview

[![](https://img.shields.io/badge/github-issues-%2365A30D?style=flat-square&logo=github)](https://github.com/sqlforskay/sample/issues)
[![](https://img.shields.io/badge/github-traffic-green)](https://github.com/sqlforskay/sample/graphs/traffic)

#### English | [简体中文](/README_CN.md)

****

How to Build dynamic web **rapidly**? We choose **sample** based on Flask. 

**sample** is a highly packaged Flask Demo which following Flask official documentation.

It's intergrates various code ,function for web development purposes.

It's the **easiest** way and **fastest** way to create Flask dynamic website.

## Install

- Run ```pip install -r requirements.txt``` to install required module or Run **install.cmd / install.sh** to install  required module ( ```chmod +x install.sh && ./install.sh``` ) .

## Run

- Run  ```chmod +x script.sh && ./script.sh``` on Linux. Run **script.cmd** on Windows.

## How to Use

- MVC architecture, easy to get started.
- Change ```project/templates/``` folder to add or modify static **html**,**css**,**js** file.( **Optional** )
- Change ```project/routes/``` folder to modify **route** file with **.py** suffix.( **Optional** )
- If Mysql Database is needed,change ```sample/project/config.py``` file to edit Mysql config argument.( **Optional** )
- If Mysql Database is needed,follow Mysql [ORM Example](https://github.com/sqlforskay/flask-sample/blob/main/project/models/user.py#L13) to create new Mysql code.( **Optional** )
- Follow Routes [Example](https://github.com/sqlforskay/flask-sample/blob/main/project/routes/index.py#L56) to create new routes code.( **Optional** )
- Run  ```chmod +x script.sh && ./script.sh``` on Linux. Run **script.cmd** on Windows.

## Required Environment

- Python 2.7+ version, better 3.6 version
- Mysql( **Optional** )

## Project Structure

  ```
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

## Join us

Your help is more than welcome! Even just open an [issue](https://github.com/sqlforskay/sample/issues) to give a enhanced suggestion or ask a question may greatly help others.
