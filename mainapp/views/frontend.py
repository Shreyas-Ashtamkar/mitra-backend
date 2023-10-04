from flask import Blueprint, render_template

gui = Blueprint('frontend', __name__, url_prefix='/gui')


@gui.route('/', methods=['GET'])
def index_page():
    return render_template('frontend.html')
