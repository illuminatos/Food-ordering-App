from drf_yasg.utils import swagger_auto_schema
from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_200_OK
from rest_framework.views import APIView
from food_ordering.models import MenuItem
from food_ordering.models.order import OrderModel
import logging

from food_ordering.tasks import food_ordering_task

logger = logging.getLogger(__name__)


# simple serializer for order
class OrderForm(serializers.Serializer):
    menu_items = serializers.JSONField(required=True)

    def validate_items(self, value):
        if not isinstance(value, list):
            raise serializers.ValidationError("it is not a list")
        return value


class MenuOrderHook(APIView):

    @swagger_auto_schema(request_body=OrderForm)
    def post(self, request, *args, **kwargs):
        """
        :param request: takes payload with data as
        {"menu_items": [3,4]} ->  3, 4 are id of menu item or
        {"menu_items": [1]}
        that was selected by user. in near future :) UI must send payload such like
        :param args:
        :param kwargs:
        :return:
        """
        serializer = OrderForm(data=request.data)
        if serializer.is_valid():
            order_data = serializer.data.get('menu_items')
            order_result = {}

            try:
                index = 0
                for datum in order_data:

                    menu_item = MenuItem.objects.get(id=int(datum))
                    order_datum = {
                        'id': menu_item.id,
                        'name': menu_item.name,
                        'category': menu_item.category.instance.name,
                        'restaurant': menu_item.restaurant.name,
                    }
                    order_result.update({index: order_datum})
                    index += 1
                order = OrderModel.objects.create(user=request.user.username, menu_items=order_result)
                order_result.update({'obj_id': order.id})
                food_ordering_task.publish_message(order_result)

            except Exception as e:
                logger.error(e)
                return Response("Ordering is not completed since %s" % str(e), status=HTTP_400_BAD_REQUEST)

            return Response("Ordering is completed successfully",
                        status=HTTP_200_OK)

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)





