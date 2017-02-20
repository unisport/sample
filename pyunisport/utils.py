from collections import OrderedDict
from rest_framework import pagination
from rest_framework.response import Response

class CustomPagination(pagination.PageNumberPagination):
    def get_paginated_response(self, data):
        return Response(OrderedDict([
        	('count', self.page.paginator.count),
        	('pages', self.page.paginator.num_pages),
        	('current_page', self.page.number),
        	('next', self.get_next_link()),
        	('previous', self.get_previous_link()),
        	('products', data)
        ]))