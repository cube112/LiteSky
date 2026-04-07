# README.MD
Just a learning record to help me understand the Flask framework and the database.  
只是一个学习记录，帮助我理解flask框架和数据库  
目前只完成了简单的文件上传和保存功能。
```
LiteSky
├─ app
│  ├─ exts.py
│  ├─ models.py
│  ├─ route
│  │  ├─ auth
│  │  │  ├─ route.py
│  │  │  └─ __init__.py
│  │  ├─ download
│  │  │  ├─ route.py
│  │  │  └─ __init__.py
│  │  ├─ index
│  │  │  ├─ route.py
│  │  │  └─ __init__.py
│  │  ├─ services
│  │  │  └─ auth_check.py
│  │  └─ upload
│  │     ├─ route.py
│  │     └─ __init__.py
│  ├─ static
│  │  ├─ css
│  │  │  ├─ auth
│  │  │  │  └─ auth.css
│  │  │  └─ base
│  │  ├─ icon
│  │  │  └─ cloud-share.svg
│  │  └─ js
│  │     ├─ base
│  │     │  ├─ base-auth.js
│  │     │  ├─ main.js
│  │     │  └─ switch_contrul.js
│  │     ├─ dowmload
│  │     │  ├─ download.js
│  │     │  └─ main.js
│  │     └─ upload
│  │        ├─ main.js
│  │        └─ upload.js
│  ├─ templates
│  │  ├─ base.html
│  │  ├─ dashboard.html
│  │  ├─ index.html
│  │  ├─ login.html
│  │  └─ upload.html
│  └─ __init__.py
├─ README.md
├─ requirements.txt
├─ run.py
└─ run_dev.py

```