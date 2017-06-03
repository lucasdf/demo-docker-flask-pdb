from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_pdb():
    message = 'Hello Docker'
    import pdb; pdb.set_trace()
    return message
