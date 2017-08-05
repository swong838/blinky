import os
from flask import Flask, render_template

template_dir = os.path.abspath('./blinky/views/templates/')
app = Flask(__name__, template_folder=template_dir)


@app.route("/")
def index():
    template = 'index.jinja2'
    return render_template(template)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, threaded=True, debug=True)
