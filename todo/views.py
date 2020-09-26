from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView,DeleteView,UpdateView
from .models import TodoModel
from django.urls import reverse_lazy

#djangoでよく用いられるテンプレート CRUD
#CreateView 作成する
#ListView,DetailView　読み込む(read)（情報を取る）
#UpdateView　更新する
#DeleteVies　削除する

class TodoList(ListView):
    template_name = 'list.html'
    #使うテーブルを指示
    model = TodoModel

class TodoDetail(DetailView):
    template_name='detail.html'
    model = TodoModel
    
class TodoCreate(CreateView):
    template_name='create.html'
    #ここで指定するモデルはデータが格納される場所
    model = TodoModel
    #送信するフィールドを指定しないとエラーになる
    fields = ('title','memo','priority','duedate')
    #データを格納したあとに遷移させるURL
    #classの中ではreverse_lazyを使い、functionの中ではreverseを用いる
    #なぜ使い分けるかは明記されていない
    success_url = reverse_lazy('list')
    
class TodoDelete(DeleteView):
    template_name= "delete.html"
    model = TodoModel
    #削除後の画面を指定
    success_url = reverse_lazy('list')
    
class TodoUpdate(UpdateView):
    template_name= "update.html"
    model = TodoModel
    #更新対象のフィールドを指定
    fields = ('title','memo','priority','duedate')
    #編集後の画面を指定
    success_url = reverse_lazy('list')