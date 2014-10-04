import json


class DataStorage(object):

    def save_data(self, data):
        raise NotImplementedError


class StreamDataStorage(DataStorage):

    def __init__(self, write_stream):
        self.write_stream = write_stream

    def save_data(self, data):
        self.write_stream.seek(0)
        self.write_stream.truncate(0)
        self.write_stream.write(
            json.dumps({
                "latest": [product.__dict__ for product in data]
            })
        )

    def file_stream_factory(self, file_path):
        return StreamDataStorage(
            open(file_path, "r+")
        )

