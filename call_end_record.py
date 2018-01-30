class callEndRecord:

    id = None
    type = None
    timestamp = None
    call_id = None

    def serialize(self):

        dic = {'id': self.id,
               'type': self.type,
               'timestamp': self.timestamp,
               'call_id': self.call_id,
               }
        return dic