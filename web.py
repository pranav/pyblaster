import struct
import pyblaster
import re
from flask import Flask, redirect, url_for
from flask import request
app = Flask(__name__, static_url_path='/static')


@app.route("/")
def index():
    return redirect(url_for('static', filename='index.html'))

@app.route("/set", methods=['GET'])
def set():
    if request.args.get('hex'):
        color_vals = [1-(float(int(i, 16))/255) for i in re.findall('..?', request.args.get('hex'))]
    else:
        color_vals = [1-(float(request.args.get(k)/255)) for k in ['r', 'b', 'g']]

    pyblaster.set(pyblaster.RED_GPIO, color_vals[0])
    pyblaster.set(pyblaster.GREEN_GPIO, color_vals[1])
    pyblaster.set(pyblaster.BLUE_GPIO, color_vals[2])
    return 'OK'


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')
