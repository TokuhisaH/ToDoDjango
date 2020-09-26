from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    #管理画面にログインするユーザー名はpython3 manege.py createsuperuserから
    url(r'^admin/', admin.site.urls),
    #宛先を空欄(localhost:8000)にすると他に該当しなければ自動でここに誘導される
    url('',include('todo.urls'))
]
