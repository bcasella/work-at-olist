import json

from call_start_record import callStartRecord

csr = callStartRecord()
csr.id = 1
print(json.dumps(csr.serialize()))

