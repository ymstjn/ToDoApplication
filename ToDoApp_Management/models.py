from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from django.forms.models import ModelForm
from django.http import request

orderCHOICES = (("asc", "早い順"), ("desc", "遅い順"), ("ctg_asc", "早い順（カテゴリー毎）"), ("ctg_desc", "遅い順（カテゴリー毎）"))
priorityCHOICES = (("normal", '普通'), ("important", '重要'))
progressCHOICES = (("start", 0), ("quarter", 25), ("half", 50), ("thrquarter", 75), ("finish", 100))

class CategoryModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='category_user')
    category = models.CharField(max_length=15)

    def __str__(self):
        return str(self.category)

class OrderModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='order_user')
    order = models.CharField(max_length=10, choices=orderCHOICES, default="期限昇順")

    def __str__(self):
        return str(self.order)

class TodoModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    # on_delete=models.SET_NULLは外部キー(カテゴリー)が削除された時に
    # categoryの値がNULLになる設定。null=Trueが必要。
    category = models.ForeignKey(CategoryModel, on_delete=models.SET_NULL, null=True, blank=True)
    content = models.CharField(max_length=40)
    priority = models.CharField(max_length=20, choices=priorityCHOICES, default="普通")
    progress = models.CharField(max_length=20, choices=progressCHOICES, default=0)
    pub_date = models.DateField(null=False, blank=False)

    def __str__(self):
        return "(" + str(self.id) + ") " + str(self.user) + " : " + str(self.content) + " <" + str(self.category) + ">" 

    class Meta:
        ordering = ('pub_date',)



