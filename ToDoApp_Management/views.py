# from typing_extensions import Required
# from django import forms
from typing import Counter
from django.db.models import Count
from itertools import chain
import datetime
from django.db.models.base import Model
from django.db.models.expressions import OrderBy
from django.db.models.fields import PositiveBigIntegerField
from django.shortcuts import render, redirect
from .models import CategoryModel, OrderModel, TodoModel
from .forms import ContentForm, CategoryForm, OrderForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.contrib.auth import authenticate, login, logout
from django.db.models import Q

# 新規登録のための機能
def signupFunc(request):
    errorCheck = False

    if request.method == 'POST':
        if str(request.POST["username"]) != "":
            username = request.POST['username']
            password = request.POST['password']
            
            try:
                # ユーザーの新規作成
                user = User.objects.create_user(username, '', password)

                # 並べ替えのModelを作成
                orderBy = OrderModel(user=user, order="asc")
                orderBy.save()

                return redirect('login')
            # ユーザー名が使用されている場合エラーを返す
            except IntegrityError:
                errorCheck = True
        else:
            errorCheck = True
    return render(request, 'ToDoApp_Management/signup.html', {"errorCheck": errorCheck})

# ログイン機能
def loginFunc(request):
    errorLogin = False

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('todolist')
        else:
            errorLogin = True

    return render(request, 'ToDoApp_Management/login.html', {"errorLogin": errorLogin})

# カテゴリーの数順に並べる
def sort_CategoryCount(sample_data, owner):
    ctg_dict = {}

    for d in sample_data.annotate(reviews=Count('category')):
        try:
            ctg = str(d.category)
        except:
            ctg = "None"

        if ctg not in ctg_dict:
            ctg_dict[ctg] = 1
        else:
            ctg_dict[ctg] += 1

    ctg_dict = dict(sorted(ctg_dict.items(), key=lambda x: x[0], reverse=True))
    ctg_dict = dict(sorted(ctg_dict.items(), key=lambda x: x[1], reverse=True))

    last = False
    if "None" in ctg_dict:
        last_data = sample_data.filter(category=None)
        del ctg_dict["None"]
        last = True
    
    return_data = TodoModel.objects.none()

    obj = CategoryModel.objects.filter(user=owner)    
    for k in ctg_dict.keys():
        try:
            ctg_id = obj.get(category=k)
        except:
            ctg_id = None
        return_data = chain(return_data, sample_data.filter(category=ctg_id))
    
    if last:
        return_data = chain(return_data, last_data)
    
    return return_data

# ToDoリストの一覧を表示
@login_required
def todolistFunc(request):

    id = OrderModel.objects.filter(user=request.user)[0].id
    order_obj = OrderModel.objects.get(pk=id)

    data = TodoModel.objects.filter(user=request.user)

    if str(order_obj) == "asc" or str(order_obj) == "ctg_asc":    
        data = data.order_by("pub_date")
    if str(order_obj) == "desc" or str(order_obj) == "ctg_desc":
        data = data.order_by("-pub_date")

    data_sta = data.filter(progress="start")
    data_ini = data.filter(Q(progress="quarter")| Q(progress="half")| Q(progress="thrquarter"))
    data_fin = data.filter(progress="finish")

    if str(order_obj) == "ctg_asc" or str(order_obj) == "ctg_desc":
        data_sta = sort_CategoryCount(data_sta, request.user)
        data_ini = sort_CategoryCount(data_ini, request.user)
        data_fin = sort_CategoryCount(data_fin, request.user)
    
    initial_dict = {
        "order": order_obj
    }

    params = {
        'form': OrderForm(initial=initial_dict),
        'data_sta': data_sta,
        'data_ini': data_ini,
        'data_fin': data_fin,
    }

    return render(request, 'ToDoApp_Management/todolist.html', params)

@login_required
def addtodoFunc(request):
    params = {
        'form': ContentForm(request.user)
    }
    if request.method == "POST":
        con = request.POST["content"]

        # この場合、categoryのnameが返ってくる。
        # そのため、categorynameからidを取得してから入力するのが良い。
        # categoryの名前が異なる人と被る可能性があるため
        # 先にユーザーで特定する
        obj = CategoryModel.objects.filter(user=request.user)
        try:
            cat_id = obj.get(category=request.POST['category'])
        except:
            cat_id = None
        
        pri = request.POST["priority"]
        pro = request.POST["progress"]
        
        li = list(request.POST["pub_date"].split("-"))
        try:
            d = datetime.date(int(li[0]), int(li[1]), int(li[2]))
            pub = request.POST["pub_date"]
        except:
            pub = "0001-01-01"

        todo = TodoModel(user=request.user, category=cat_id, content=con, priority=pri, progress=pro, pub_date=pub)
        todo.save()

        return redirect("todolist")

    return render(request, 'ToDoApp_Management/addtodo.html', params)

@login_required
def updatetodoFunc(request, pk):
    data = TodoModel.objects.get(id=pk)
    
    if request.method == "POST":
        data.content = request.POST["content"]
        obj = CategoryModel.objects.filter(user=request.user)
        try:
            cat_id = obj.get(category=request.POST['category'])
        except:
            cat_id = None

        data.category = cat_id
        data.priority = request.POST["priority"]
        data.progress = request.POST["progress"]
        # data.pub_date = request.POST["pub_date"]
        li = list(request.POST["pub_date"].split("-"))
        try:
            d = datetime.date(int(li[0]), int(li[1]), int(li[2]))
            data.pub_date = request.POST["pub_date"]
        except:
            data.pub_date = "0001-01-01"
        
        data.save()

        return redirect("todolist")

    else:
        if request.user == TodoModel.objects.get(id=pk).user:
            initial_dict = {
                "content": data.content,
                "category": data.category,
                "priority": data.priority,
                "progress": data.progress,
                "pub_date": data.pub_date
            }
            params = {
                "id": pk,
                "form": ContentForm(request.user, initial=initial_dict) 
            }
            return render(request, "ToDoApp_Management/updatetodo.html", params)
        # 当ユーザでない人が変更を行おうとした時
        return redirect('login')

# 並べ替え機能
@login_required
def orderbyFunc(request):
    id = OrderModel.objects.filter(user=request.user)[0].id
    order_obj = OrderModel.objects.get(pk=id)
    print(order_obj, request.POST["order"])
    order_obj.order = request.POST["order"]
    order_obj.save()
    
    return redirect("todolist")

@login_required
def deletetodoFunc(request, pk):
    # 万が一のために他のユーザの整合性の確認
    if request.user == TodoModel.objects.get(id=pk).user:
        data = TodoModel.objects.get(id=pk)
        data.delete()
    return redirect("todolist")

# 完了ボタンーprogressを100にする
@login_required
def completetodoFunc(request, pk):
    # 万が一のために他のユーザの整合性の確認
    if request.user == TodoModel.objects.get(id=pk).user:
        data = TodoModel.objects.get(id=pk)
        data.progress = "finish"
        data.save()

    return redirect("todolist")

@login_required
def addcategoryFunc(request):
    params = {
        'data': CategoryModel.objects.filter(user=request.user),
        'form': CategoryForm()
    }
    if request.method == "POST":
        cat = request.POST["category"]
        category_list = list(CategoryModel.objects.filter(user=request.user).values_list('category', flat=True))

        if cat not in category_list:
            ctgy = CategoryModel(user=request.user, category=cat)
            ctgy.save()
            return render(request, 'ToDoApp_Management/addcategory.html', params)
        # 重複したカテゴリーの不許可
    return render(request, 'ToDoApp_Management/addcategory.html', params)

@login_required
def updatecategoryFunc(request, pk):
    data = CategoryModel.objects.get(id=pk)
    
    if request.method == "POST":
        category_list = list(CategoryModel.objects.filter(user=request.user).values_list('category', flat=True))

        if request.POST["category"] not in category_list:
            data.category = request.POST["category"]
            data.save()
        return redirect("addcategory")

    else:
        if request.user == CategoryModel.objects.get(id=pk).user:
            initial_dict = {
                "category": data.category,
            }
            params = {
                "id": pk,
                "form": CategoryForm(initial=initial_dict) 
            }
            return render(request, "ToDoApp_Management/updatecategory.html", params)
        # 当ユーザでない人が変更を行おうとした時
        return redirect('login')


@login_required
def deletecategoryFunc(request, pk):
    # 万が一のために他のユーザの整合性の確認
    if request.user == CategoryModel.objects.get(id=pk).user:
        data = CategoryModel.objects.get(id=pk)
        data.delete()

    return redirect("addcategory")

# ログアウト機能
def logoutFunc(request):
    logout(request)
    return redirect("login")