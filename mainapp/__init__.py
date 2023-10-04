from flask import Flask

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app_config = [test_config, 'config.py'][test_config is None]

    try:
        app.config.from_pyfile(app_config)
    except OSError as o:
        print("o :", o)
    except Exception as e:
        print("e :", e)

    from .views import frontend, backend
    
    app.register_blueprint(frontend.gui)
    app.register_blueprint(backend.api)

    return app
