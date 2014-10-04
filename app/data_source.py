import json
import urllib2
from app.models import Document


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
    def url_stream_factory(url):
        return StreamDataSource(
            urllib2.urlopen(url)
        )

    @staticmethod
    def file_stream_factory(file_path):
        return StreamDataSource(
            open(file_path)
        )
