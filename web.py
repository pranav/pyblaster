
import pyblaster
from flask import Flask
from flask import request
app = Flask(__name__, static_url_path='/static')


@app.route("/set", methods=['GET'])
def set():
    color_vals = []
    for k in ['r', 'b', 'g']:
        color_vals.append(request.args.get(k))

    pyblaster.set(pyblaster.RED_GPIO, color_vals[0])
    pyblaster.set(pyblaster.BLUE_GPIO, color_vals[1])
    pyblaster.set(pyblaster.GREEN_GPIO, color_vals[2])

    return 'OK'


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')
