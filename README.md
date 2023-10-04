# Flask-Repo-Template
This is a template repository of a Flask App

## Directory Tree :
```
Flask-Repo-Template/
├── instance
│   └── config.py
├── mainapp
│   ├── __init__.py
│   ├── static
│   │   ├── css
│   │   │   ├── style.css
│   │   │   ├── bootstrap.min.css
│   │   │   └── bootstrap.min.css.map
│   │   ├── js
│   │   │   ├── main.js
│   │   │   ├── bootstrap.bundle.min.js
│   │   │   └── bootstrap.bundle.min.js.map
│   │   └── media
│   ├── templates
│   │   ├── index.html
│   │   ├── frontend.html
│   │   └── backend.html
│   ├── utils
│   │   └── __init__.py
│   └── views
│       ├── __init__.py
│       ├── frontend.py
│       └── backend.py
├── run_app.py
├── prepare_app.sh
├── prepare_app.bat
├── requirements.txt
├── README.md
└── LICENSE
```

## TO Run :
- If you want to broadcast on Localhost
    ```
    waitress-serve --listen=localhost:5000 run:app
    ```

- If you want to broadcast on 0.0.0.0
    ```
    waitress-serve --listen=*:5000 run:app
    ```
