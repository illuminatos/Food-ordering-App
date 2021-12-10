from .test_setup import TestSetUp


class TestMenuOrderViewSet(TestSetUp):
    def test_get_menu_order(self):
        res = self.client.get(self.get_menu_order_url)
        self.assertEqual(res.data.get('count'), 1)