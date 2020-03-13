from urllib import parse as urlparse

from django.core.paginator import Paginator, Page
from django.utils.encoding import force_str


def replace_query_param(url, key, val):
    (scheme, netloc, path, query, fragment) = urlparse.urlsplit(force_str(url))
    query_dict = urlparse.parse_qs(query, keep_blank_values=True)
    query_dict[force_str(key)] = [force_str(val)]
    query = urlparse.urlencode(sorted(list(query_dict.items())), doseq=True)
    return urlparse.urlunsplit((scheme, netloc, path, query, fragment))


def remove_query_param(url, key):
    (scheme, netloc, path, query, fragment) = urlparse.urlsplit(force_str(url))
    query_dict = urlparse.parse_qs(query, keep_blank_values=True)
    query_dict.pop(key, None)
    query = urlparse.urlencode(sorted(list(query_dict.items())), doseq=True)
    return urlparse.urlunsplit((scheme, netloc, path, query, fragment))


class RequestPage(Page):
    def __init__(self, object_list, number, paginator, request, page_query_param):
        self.request = request
        self.page_query_param = page_query_param
        super().__init__(object_list, number, paginator)

    def next_page_link(self):
        url = self.request.build_absolute_uri()
        return replace_query_param(url, self.page_query_param, self.next_page_number())

    def previous_page_link(self):
        url = self.request.build_absolute_uri()
        page_number = self.previous_page_number()
        if page_number == 1:
            return remove_query_param(url, self.page_query_param)
        return replace_query_param(url, self.page_query_param, page_number)

    def first_page_link(self):
        url = self.request.build_absolute_uri()
        return remove_query_param(url, self.page_query_param)

    def last_page_link(self):
        url = self.request.build_absolute_uri()
        return replace_query_param(url, self.page_query_param, self.paginator.num_pages)


class RequestPaginator(Paginator):
    page_query_param = 'page'

    def __init__(self, object_list, per_page, request, *args, **kwargs):
        self.request = request
        super().__init__(object_list, per_page, *args, **kwargs)

    def _get_page(self, *args, **kwargs):
        kwargs['request'] = self.request
        kwargs['page_query_param'] = self.page_query_param
        return RequestPage(*args, **kwargs)

    def get_page(self, **kwargs):
        return super().get_page(self.request.GET.get(self.page_query_param))


def replace_language_url(request, language):
    url = request.build_absolute_uri()
    (scheme, netloc, path, query, fragment) = urlparse.urlsplit(force_str(url))
    paths = path.split('/')
    paths[1] = language
    return urlparse.urlunsplit((scheme, netloc, '/'.join(paths), query, fragment))
