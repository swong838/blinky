import os
from flask import Flask, render_template, url_for
from lib.led import Led

template_dir = os.path.abspath('./blinky/views/templates/')
app = Flask(__name__, template_folder=template_dir, static_url_path='/static')

led_driver = Led()


@app.route("/")
def index():
    template = 'index.jinja2'
    context = {
        'app_path': url_for('static', filename='app.js')
    }
    return render_template(template, **context)


@app.route('/reset', methods=['PUT'])
def reset():
    led_driver.clearall()
    return ''


@app.route('/test', methods=['PUT'])
def cycle_test():
    led_driver.test_cycle()
    return ''


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, threaded=True, debug=True)
