import json
from datetime import datetime
from flask import Flask, jsonify, request
from sqlalchemy.exc import IntegrityError, InvalidRequestError

from call_start_record import callStartRecord
from call_end_record import callEndRecord

from sqlalchemy_db.database import *
from sqlalchemy_db.models import *

app = Flask(__name__)

@app.route("/phone/getall", methods=['GET'])
def getall_phone():

    try:
        phones = Phone().query.all()
        phones_dict = {phones.index(phone): phone.number for phone in phones}
        db_session.commit()
    except IntegrityError as e:
        print(e)
        return "ERRO, PK", 400
    except InvalidRequestError as e:
        print(e)
        return "Invalid request", 400
    except Exception as e:
        print(e)
        return "Internal server error", 400

    return jsonify(phones_dict), 200

@app.route("/phone/insert", methods=['POST'])
def insert_phone():
    try:
        values = request.get_json()
        phone_number = values.get('number')
        phone = Phone(number=phone_number)
        db_session.add(phone)
        db_session.commit()
    except IntegrityError as e:
        print(e)
        return "ERRO, PK", 400
    except InvalidRequestError as e:
        print(e)
        return "Invalid request", 400
    except Exception as e:
        print(e)
        return "Internal server error", 400

    return jsonify("it worked"), 200

@app.route("/phone/delete", methods=['POST'])
def delete_phone():
    try:
        values = request.get_json()
        phone_number = values.get('number')
        Phone(phone_number).query.filter_by(number=f"{phone_number}").delete()
        db_session.commit()

    except IntegrityError as e:
        print(e)
        return "ERRO, PK", 400
    except InvalidRequestError as e:
        print(e)
        return "Invalid request", 400
    except Exception as e:
        print(e)
        return "Internal server error", 400

    return jsonify("it worked"), 200


@app.route("/phone/update", methods=['POST'])
def update_phone():
    try:
        values = request.get_json()
        old_phone_number = values.get('old_number')
        new_phone_number = values.get('new_number')
        Phone(old_phone_number).query.filter_by(number=f"{old_phone_number}").\
            update({Phone.number: new_phone_number})
        db_session.commit()

    except IntegrityError as e:
        print(e)
        return "ERRO, PK", 400
    except InvalidRequestError as e:
        print(e)
        return "Invalid request", 400
    except Exception as e:
        print(e)
        return "Internal server error", 400

    return jsonify("it worked"), 200

###############################################################################

@app.route("/call/getall", methods=['GET'])
def getall_calls():

    try:
        calls = Call().query.all()
        calls_dict = {}
        calls_list = []
        for call in calls:
            calls_dict["id"] = call.id
            calls_dict["type_start"] = call.type_start
            calls_dict["timestamp"] = call.timestamp
            calls_dict["call_id"] = call.call_id
            calls_dict["source"] = call.source
            calls_dict["destination"] = call.destination
            calls_list.append(calls_dict)

        db_session.commit()

    except IntegrityError as e:
        print(e)
        return "ERRO, PK", 400
    except InvalidRequestError as e:
        print(e)
        return "Invalid request", 400
    except Exception as e:
        print(e)
        return "Internal server error", 400

    return jsonify(calls_list), 200

@app.route("/call/delete", methods=['POST'])
def delete_call():

    try:
        values = request.get_json()
        call_id = values.get('id')
        Call().query.filter_by(id=f"{call_id}").delete()

        db_session.commit()
    except IntegrityError as e:
        print(e)
        return "ERRO, PK", 400
    except InvalidRequestError as e:
        print(e)
        return "Invalid request", 400
    except Exception as e:
        print(e)
        return "Internal server error", 400

    return "It Worked", 200


@app.route("/call/insert", methods=['POST'])
def insert_call():
    try:
        values = request.get_json()
        call = Call()
        call.type_start = values.get('type_start')
        call.call_id = values.get('call_id')
        call.source = values.get('source')
        call.destination = values.get('destination')

        db_session.add(call)
        db_session.commit()
    except IntegrityError as e:
        print(e)
        return "ERRO, PK", 400
    except InvalidRequestError as e:
        print(e)
        return "Invalid request", 400
    except Exception as e:
        print(e)
        return "Internal server error", 400

    return jsonify("it worked"), 200

@app.route("/call/update", methods=['POST'])
def update_call():
    try:
        values = request.get_json()
        call = Call()
        call.id = values.get('id')

        if "type_start" in values.keys():
            call.type_start = values.get('type_start')
            call.query.filter_by(id=f"{call.id}"). \
                update({Call.type_start: call.type_start})

        if "call_id" in values.keys():
            call.call_id = values.get('call_id')
            call.query.filter_by(id=f"{call.id}"). \
                update({Call.call_id: call.call_id})

        if "source" in values.keys():
            call.source = values.get('source')
            call.query.filter_by(id=f"{call.id}"). \
                update({Call.source: call.source})

        if "destination" in values.keys():
            call.destination = values.get('destination')
            call.query.filter_by(id=f"{call.id}"). \
                update({Call.destination: call.destination})

        db_session.commit()
    except IntegrityError as e:
        db_session.rollback()
        print(e)
        return "ERRO, PK", 400
    except InvalidRequestError as e:
        db_session.rollback()
        print(e)
        return "Invalid request", 400
    except Exception as e:
        db_session.rollback()
        print(e)
        return "Internal server error", 400

    return jsonify("it worked"), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)