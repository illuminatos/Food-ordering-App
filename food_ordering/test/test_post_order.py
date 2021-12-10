from .test_setup import TestSetUp
from ..models import Category, Restaurant, MenuItem


class TestPostOrder(TestSetUp):
    def test_post_order_with_no_data(self):
        res = self.client.post(self.post_order_url)
        self.assertEqual(res.status_code, 400)

    def test_post_order_with_invalid_data(self):
        res = self.client.post(self.post_order_url, self.invalid_order_data, format="json")
        self.assertEqual(res.status_code, 400)

    def test_get_category(self):
        category = Category.objects.get(id=1)
        print("category id: " + str(category.id))
        self.assertEqual(category.name, 'Pizza')

    def test_get_restaurant(self):
        restaurant = Restaurant.objects.get(id=1)
        print("restaurant id: " + str(restaurant.id))
        self.assertEqual(restaurant.name, 'Anstella Pizza')

    def test_get_menu_item(self):
        menu_item = MenuItem.objects.get(id=1)
        print("menu item id: " + str(menu_item.id))
        self.assertEqual(menu_item.name, 'Karışık Pizza')

    def test_post_order_with_valid_data(self):
        # in setup create 1 order and now post another
        post_res = self.client.post(self.post_order_url, self.valid_order_data, format="json")
        self.assertEqual(post_res.status_code, 200)
        get_res = self.client.get(self.get_menu_order_url)
        self.assertEqual(get_res.data.get('count'), 2)



