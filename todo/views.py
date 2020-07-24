from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import CreateView
from django.views.generic import DeleteView
from django.views.generic import UpdateView
from django.urls import reverse_lazy
from .models import TodoModel

# Create your views here.

# list/を踏むとこのクラスからオブジェクト生成
class TodoList(ListView):
    template_name = 'list.html'
    model = TodoModel

class TodoDetail(DetailView):
    template_name = 'detail.html'
    model = TodoModel

class TodoCreate(CreateView):
    template_name = 'create.html'
    model = TodoModel
    fields = ('title', 'memo', 'priority', 'duedate')
    # クラスの場合はreverse_lazy、メソッド(関数)の場合はreverse
    # POSTが成功したらlist.htmlにリダイレクト
    success_url = reverse_lazy('list')

class TodoDelete(DeleteView):
    template_name = 'delete.html'
    model = TodoModel
    success_url = reverse_lazy('list')

class TodoUpdate(UpdateView):
    template_name = 'update.html'
    model = TodoModel
    # テーブル上の全領域にアクセス可能
    fields = ('title', 'memo', 'priority', 'duedate')
    success_url = reverse_lazy('list')