from django import forms
from django.core.validators import BaseValidator
from django.db.models import fields
from django.http import request
from django.utils.regex_helper import Choice
from .models import TodoModel, CategoryModel, OrderModel

class CategoryForm(forms.ModelForm):
    class Meta:
        model = CategoryModel
        fields = ["category"]

class OrderForm(forms.ModelForm):
    class Meta:
        model = OrderModel
        fields = ["order"]

class ContentForm(forms.ModelForm):
    class Meta:
        model = TodoModel
        fields = ["content", "category", "priority", "progress", "pub_date"]

    def __init__(self, user, *args, **kwards):
        super(ContentForm, self).__init__(*args, **kwards)
        self.fields["category"] = forms.ChoiceField(
            choices = [("-", "-")] + [(item, item) for item in CategoryModel.objects.filter(user=user)],
        )