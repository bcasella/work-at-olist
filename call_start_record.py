from datetime import datetime
class callStartRecord:

    id = None
    type = None
    timestamp = None
    call_id = None
    source = None
    destination = None

    def serialize(self):
        if isinstance(self.timestamp, datetime):
            self.timestamp = self.timestamp.isoformat()
        dic = {'id': self.id,
               'type': self.type,
               'timestamp': self.timestamp,
               'call_id': self.call_id,
               'source': self.source,
               'destination': self.destination,
               }

        return dic