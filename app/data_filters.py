class BaseFilter(object):
    def apply(self, data):
        raise NotImplementedError


class PaginationFilter(BaseFilter):
    def __init__(self, page_num, per_page):
        self.page_num = page_num
        self.per_page = per_page

    def apply(self, data):
        iter_data = iter(data)

        for x in xrange(self.per_page * self.page_num):
            next(iter_data)

        for x in xrange(self.per_page):
            yield next(iter_data)


class SortingFilter(BaseFilter):
    ASC = 'asc'
    DESC = 'desc'

    def __init__(self, asc=ASC, key=None):
        self.ordering = asc
        self.key = key

    def apply(self, data):
        return sorted(
            data,
            key=lambda item: getattr(item, self.key),
            reverse=self.ordering == self.DESC,
        )


class KeyValueFilter(BaseFilter):
    def __init__(self, key, value, inverse=False):
        self.key = key
        self.value = value
        self.inverse = inverse

    def apply(self, data):
        for item in data:
            if self.inverse:
                if getattr(item, self.key) != self.value:
                    yield item
            else:
                if getattr(item, self.key) == self.value:
                    yield item


class CompositeFilter(BaseFilter):
    def __init__(self, *filters):
        self.filters = filters

    def apply(self, data):
        for filter_item in self.filters:
            data = filter_item.apply(data)

        return data
