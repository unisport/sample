from django.core.paginator import Paginator
from unisample.api.api_common.utils import safe_int



#-----------------------------------------------------------------------------------------------------------------------
class PaginatingMixin(object):

    def paginate(self, item_list, paginate_by=10, url_param_name='page'):
        '''
        Method for getting current page number from request
        and leave only the relevant items

        :param item_list: list for splitting
        :param paginate_by: items per page
        :param url_param_name: name of the param ign GET request data
        :return: Page object which can be used as iterable through items
        '''
        if url_param_name not in self.request.REQUEST:
            return item_list

        paginator = Paginator(item_list, paginate_by)

        current_page = safe_int(self.request.REQUEST.get(url_param_name), 1)
        current_page = min(current_page, paginator.num_pages)

        page = paginator.page(current_page)
        return page
