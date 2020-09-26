from django.contrib import admin
from .models import TodoModel
# Register your models here.

#管理画面でモデルを操作できるように設定する
admin.site.register(TodoModel)