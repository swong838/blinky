from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello c World!"

app.run(host='0.0.0.0', port=8000, threaded=True)

