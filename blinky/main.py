import os
from flask import Flask, render_template, url_for, request, abort
from lib.effects import Effects

template_dir = os.path.abspath('./blinky/views/templates/')
app = Flask(__name__, template_folder=template_dir, static_url_path='/static')

led_driver = Effects()


@app.route("/")
def index():
    template = 'index.jinja2'
    context = {
        'app_path': url_for('static', filename='compiled/app.js'),
        'css_path': url_for('static', filename='css/picker.css')
    }
    return render_template(template, **context)


@app.route('/reset', methods=['PUT'])
def reset():
    led_driver.clearall()
    return ''


@app.route('/test', methods=['PUT'])
def cycle_test():
    led_driver.test_cycle
    return ''


@app.route('/setcolor', methods=['POST'])
def set_color():
    values = request.get_json()
    led_driver.setrgb(r=values['r'], g=values['g'], b=values['b'])
    return ''


@app.route('/effect/<effect_name>', methods=['PUT'])
def apply_effect(effect_name):
    if hasattr(led_driver, effect_name):
        getattr(led_driver, effect_name)
    else:
        abort(404)
    return ''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, threaded=True, debug=True)
