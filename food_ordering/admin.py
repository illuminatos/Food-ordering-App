from django.contrib import admin
from .models import MenuItem, Category, Restaurant, OrderModel


admin.site.register(MenuItem)
admin.site.register(Category)
admin.site.register(Restaurant)
admin.site.register(OrderModel)
