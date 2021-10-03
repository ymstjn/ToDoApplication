from django.contrib import admin
from .models import TodoModel, CategoryModel, OrderModel

admin.site.register(TodoModel)
admin.site.register(CategoryModel)
admin.site.register(OrderModel)