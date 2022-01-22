#!/usr/bin/env python

import flask
import random
from flask import Flask, json

robot_data = {
    "motor1" : {
        "voltage": 5.2,
        "speed": 10.3
    },
    "motor2" : {
        "voltage": 4.9,
        "speed": 4.1
    }
}

api = Flask(__name__)

@api.route('/robot', methods=['GET'])
def get_data():
  robot_data["motor1"]["speed"] = random.randrange(1, 10)
  resp = flask.Response(json.dumps(robot_data))
  resp.headers['Access-Control-Allow-Origin'] = '*'
  return resp

if __name__ == '__main__':
    api.run() 
