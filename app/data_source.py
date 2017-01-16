import json
import urllib2
from app.models import Product


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
            yield Product(**item)

    @staticmethod
    def url_stream_factory(url):
        return StreamDataSource(
            urllib2.urlopen(url)
        )
