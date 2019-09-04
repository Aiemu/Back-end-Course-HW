### 开发测试环境
- python 3.7
- Django 2.2.4
- VS Code for Mac

### 测试方法
1. $ python manage.py makemigrations
2. $ python manage.py migrate
3. $ python manage.py runserver [端口]


### 文件结构
├── app  
│   ├── __init__.py  
│   ├── __pycache__  
│   │   ├── __init__.cpython-37.pyc  
│   │   ├── admin.cpython-37.pyc  
│   │   ├── models.cpython-37.pyc  
│   │   ├── urls.cpython-37.pyc  
│   │   └── views.cpython-37.pyc  
│   ├── admin.py  
│   ├── apps.py  
│   ├── migrations  
│   │   ├── 0001_initial.py  
│   │   ├── __init__.py  
│   │   └── __pycache__  
│   │       ├── 0001_initial.cpython-37.pyc  
│   │       └── __init__.cpython-37.pyc  
│   ├── models.py  
│   ├── tests.py  
│   ├── urls.py  
│   └── views.py  
├── db.sqlite3  
├── hw4  
│   ├── __init__.py  
│   ├── __pycache__  
│   │   ├── __init__.cpython-37.pyc  
│   │   ├── settings.cpython-37.pyc  
│   │   ├── urls.cpython-37.pyc  
│   │   └── wsgi.cpython-37.pyc  
│   ├── settings.py  
│   ├── urls.py  
│   └── wsgi.py  
└── manage.py  
