from rest_framework.test import APITestCase
from django.urls import reverse

from food_ordering.models import Restaurant, MenuItem, OrderModel
from food_ordering.models.category import Category


class TestSetUp(APITestCase):
    def setUp(self):
        self.post_order_url = reverse('order')
        self.get_menu_order_url = reverse('order-view-set')

        Category.objects.create(name='Pizza')
        Restaurant.objects.create(name='Anstella Pizza', id=1)
        MenuItem.objects.create(name='Karışık Pizza', restaurant_id=1)
        MenuItem.objects.create(name='Makarna', restaurant_id=1)
        OrderModel.objects.create(menu_items=2, user='test-user')

        self.valid_order_data = {
            "menu_items": [1]
        }
        self.invalid_order_data = {
            "menu_items": 1
        }

        return super().setUp()

    def tearDown(self):
        return super().tearDown()