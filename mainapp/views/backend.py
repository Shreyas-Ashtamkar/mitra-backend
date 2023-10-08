from flask import Blueprint, render_template
from twilio.twiml.messaging_response import MessagingResponse

api = Blueprint('backend', __name__, url_prefix='/api')

@api.route('/', methods=['GET'])
def index_page():
    return render_template('backend.html')

@api.route('/hello', methods=['GET'])
def hello():
    return "Hello World"

@api.route('/chatbot', methods=['GET', 'POST'])
def chatbot():
    resp = MessagingResponse()
    msg  = resp.message()
    msg.body("This is cool, this has been sent by my server.")
    # msg.media('https://example.com/path/image.jpg')
    return str(resp)


