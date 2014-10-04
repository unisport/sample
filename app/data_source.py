import json
import urllib2
from app.models import Document
import os


class DataSource(object):
    def get_data(self):
        """Should return iterable, generator preffered, as it give an
        ability not to load all data in memory"""
        raise NotImplementedError


class StreamDataSource(DataSource):

    def __init__(self, stream):
        self.stream = stream

    def get_data(self):
        json_data = self.stream.read()
        data = json.loads(json_data)

        for item in data["latest"]:
            yield Document(**item)

    @staticmethod
    def unisport_url_stream_factory():
        return StreamDataSource(
            urllib2.urlopen('http://www.unisport.dk/api/sample/')
        )

    @staticmethod
    def file_stream_factory():
        return StreamDataSource(
            open("{path}/data.json".format(
                path=os.path.dirname(os.path.realpath(__file__))
            ))
        )
