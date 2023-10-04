from flask import Blueprint, render_template

api = Blueprint('backend', __name__, url_prefix='/api')


@api.route('/', methods=['GET'])
def index_page():
    return render_template('backend.html')
