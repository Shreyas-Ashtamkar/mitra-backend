from flask import Flask, render_template
from os import makedirs, path


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app_config = [test_config, 'config.py'][test_config is None]

    try:
        if not path.exists(app.instance_path):
            makedirs(app.instance_path)
        app.config.from_pyfile(app_config)
    except OSError as o:
        print("o :", o)
    except Exception as e:
        print("e :", e)

    @app.route('/', methods=['GET'])
    def index_page():
        return render_template('index.html')

    from .views import frontend, backend
    app.register_blueprint(frontend.gui)
    app.register_blueprint(backend.api)

    return app
