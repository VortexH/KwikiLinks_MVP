#!/usr/bin/python3
"""
starts a Flask web application
"""
from flask import Flask, render_template, send_from_directory, jsonify, abort, request
from os import getenv
from werkzeug.exceptions import BadRequest
import bfs

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/css/<path:path>')
def static_css(path):
    """ static css path """
    return send_from_directory('static/css', path)


@app.route('/js/<path:path>')
def static_js(path):
    """ static css path """
    return send_from_directory('static/js', path)


@app.route('/img/<path:path>')
def static_img(path):
    """ static imp path """
    return send_from_directory('static/img', path)


@app.route('/vendor/<path:path>')
def static_vendor(path):
    """ static vendor misc path """
    return send_from_directory('static/vendor', path)


@app.route('/', methods=['get'])
def index():
    print('we gettin')
    """ basic index """
    return render_template('index.html')


@app.route('/kwiklinks', methods=['POST'])
def post_kwiklinks():
    """ makes a new place """
    if request.mimetype != 'application/json':
        return jsonify(error="Not a JSON"), 400
    try:
        kwik_json = request.get_json()
        response = bfw.BFS(kwik_json["firstw"], kwik_json["lastw"])
    except BadRequest:
        return jsonify(error="Not a JSON"), 400

    print(kwik_json)

    return response

HOST = getenv('STINGRAY_HOST', '0.0.0.0')
PORT = getenv('STINGRAY_PORT', '5000')

if __name__ == "__main__":
    app.run(host=HOST, port=int(PORT), threaded=True)
