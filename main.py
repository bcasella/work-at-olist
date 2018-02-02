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
def example():

    try:
        values = request.get_json()
        phone_number = values.get('number')
        phones = Phone(phone_number).query.all()
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


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
