import unittest
import json

from datetime import datetime

from call_end_record import callEndRecord
from call_start_record import callStartRecord

class TestJsonSerialization(unittest.TestCase):

    def testCallEndRecordSerialization(self):

        result = '{"id": null, "type": null, "timestamp": null, "call_id": null}'
        call_end = callEndRecord()
        self.assertEqual(json.dumps(call_end.serialize()), result)

    def testCallStartRecordSerialization(self):

        result = '{"id": null, "type": null, "timestamp": null, "call_id": null, "source": null, "destination": null}'

        call_start = callStartRecord()
        self.assertEqual(json.dumps(call_start.serialize()), result)

    def testCallEndRecordSerialization2(self):

        result = '{"id": 1, "type": "start", "timestamp": "2018-01-01T18:00:00", "call_id": 1234}'
        call_end = callEndRecord()

        call_end.id = 1
        call_end.type = "start"
        call_end.timestamp = datetime(2018, 1, 1, 18, 00)
        call_end.call_id = 1234

        self.assertEqual(json.dumps(call_end.serialize()), result)

    def testCallStartRecordSerialization2(self):

        result = '{"id": 1, "type": "start", "timestamp": "2018-01-01T18:00:00", "call_id": 1234, "source": "5514991313567", "destination": "5514991212567"}'

        call_start = callStartRecord()
        call_start.id = 1
        call_start.type = "start"
        call_start.timestamp = datetime(2018, 1, 1, 18, 00)
        call_start.call_id = 1234
        call_start.source = "5514991313567"
        call_start.destination = "5514991212567"

        self.assertEqual(json.dumps(call_start.serialize()), result)

unittest.main()
