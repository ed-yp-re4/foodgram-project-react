from rest_framework.pagination import PageNumberPagination


class PageNumberCustomPaginator(PageNumberPagination):

    page_size_query_param = 'limit'
