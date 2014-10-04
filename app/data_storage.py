import json


class DataStorage(object):

    def save_data(self, data):
        raise NotImplementedError


class StreamDataStorage(object):

    def __init__(self, write_stream):
        self.write_stream = write_stream

    def save_data(self, data):
        self.write_stream.write(
            json.dumps({
                "latest": [product.__dict__ for product in data]
            })
        )
