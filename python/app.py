from flask import Flask


app = Flask(__name__);

@app.route('/test/', methods=['GET'])
def get_test():
    return "Hello World"
