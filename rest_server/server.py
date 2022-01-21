#!/usr/bin/env python

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
  return json.dumps(robot_data)

if __name__ == '__main__':
    api.run() 
