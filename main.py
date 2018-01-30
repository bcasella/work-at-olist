import json
from datetime import datetime
from flask import Flask, jsonify, request

from call_start_record import callStartRecord
from call_end_record import callEndRecord


app = Flask(__name__)

@app.route("/", methods=['GET'])
def example():

    csr = callStartRecord()
    csr.id = 1
    csr.type = "start"
    csr.timestamp = datetime(2018, 1, 1, 18, 00)
    csr.call_id = 1234
    csr.source = "5514991313567"
    csr.destination = "5514991212567"

    return jsonify(csr.serialize()), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

