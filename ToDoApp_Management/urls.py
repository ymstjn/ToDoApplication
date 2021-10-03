from django.urls import path
from .views import signupFunc, loginFunc, todolistFunc,\
    addtodoFunc, updatetodoFunc, deletetodoFunc, completetodoFunc, orderbyFunc,\
    addcategoryFunc, updatecategoryFunc, deletecategoryFunc, logoutFunc

urlpatterns = [
    path('signup/', signupFunc, name="signup"),
    path('login/', loginFunc, name="login"),
    path('todolist/', todolistFunc, name="todolist"),
    path('addtodo/', addtodoFunc, name="addtodo"),
    path('updatetodo/<int:pk>', updatetodoFunc, name="updatetodo"),
    path('deletetodo/<int:pk>', deletetodoFunc, name="deletetodo"),
    path('completetodo/<int:pk>', completetodoFunc, name="completetodo"),
    
    path('orderby/', orderbyFunc, name="orderby"),

    path('addcategory/', addcategoryFunc, name="addcategory"),
    path('updatecategory/<int:pk>', updatecategoryFunc, name="updatecategory"),
    path('deletecategory/<int:pk>', deletecategoryFunc, name="deletecategory"),
    path('logout/', logoutFunc, name="logout"),
]