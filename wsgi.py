#!/usr/bin/python3
from os import getenv
from web_flask import app as application


HOST = getenv('STINGRAY_HOST', '0.0.0.0')
PORT = getenv('STINGRAY_PORT', '5000')

if __name__ == "__main__":
    application.run(host=HOST, port=int(PORT), threaded=True)

