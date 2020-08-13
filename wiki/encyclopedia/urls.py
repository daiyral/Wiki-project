from django.urls import path

from . import views,util

app_name="main"
urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:entry>",views.goto,name="page"),
    path("search",views.search,name="search"),
    path("NewPage",views.new_page,name="new_page"),
    path("create_entry",views.create,name="create"),
    path("redirect/<str:title>",views.redirect,name="redirect"),
    path("edit",views.edit,name="edit"),
    path("random_page",views.random_page,name="random_page")

]
