import json
from datetime import datetime

from call_start_record import callStartRecord
from call_end_record import callEndRecord

csr = callStartRecord()
csr.id=1
csr.type = "start"
csr.timestamp = datetime(2018, 1, 1, 18, 00)
csr.call_id = 1234
csr.source = "5514991313567"
csr.destination = "5514991212567"

print(json.dumps(csr.serialize()))

