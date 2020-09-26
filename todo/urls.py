from django.conf.urls import url, include
from django.contrib import admin
from .views import TodoList,TodoDetail,TodoCreate,TodoDelete,TodoUpdate

urlpatterns = [
    #nameを指定することでそのnameを使って遷移を任意の場所で呼び出せる
    #今回はviews.pyのreverse_lazyで用いる
    #宛先を空欄にすると他に該当しなければ自動でここに誘導される
    url('list/',TodoList.as_view(), name='list'),
    #DetailViewを呼ぶにはPrimaly Key(pk)と一緒に呼び出す必要がある
    #記事とPrimaly Keyの紐付けは管理画面のURLから確認できる
    url('detail/(?P<pk>\d+)',TodoDetail.as_view(),name='detail'),
    url('create/',TodoCreate.as_view(),name='create'),
    #削除する項目のpkを指定
    url('delete/(?P<pk>\d+)',TodoDelete.as_view(),name='delete'),
    url('update/(?P<pk>\d+)',TodoUpdate.as_view(),name='update')
    
]
