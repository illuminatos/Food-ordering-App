
from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import PageNumberPagination
from food_ordering.models.order import OrderModel
from food_ordering.rest.serializers.menu_order import MenuOrderSerialization


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 256
    page_size_query_param = 'page_size'
    max_page_size = 1000


class MenuOrderViewSet(ModelViewSet):
    pagination_class = StandardResultsSetPagination
    queryset = OrderModel.objects.all()
    serializer_class = MenuOrderSerialization

    def get_queryset(self):
        queryset = self.queryset.all()
        return queryset


