from rest_framework.pagination import PageNumberPagination


class UnisportPagination(PageNumberPagination):
    page_size_query_param = "page"
    page_size = 10
