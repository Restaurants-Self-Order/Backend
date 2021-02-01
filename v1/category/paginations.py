from rest_framework.pagination import LimitOffsetPagination, PageNumberPagination

class SmallPagesPagination(PageNumberPagination):  
    page_size = 3

class SmallOffsetPagination(LimitOffsetPagination):  
    default_limit = 2