from django.urls import path


from . import views

app_name = 'alldays'

urlpatterns = [
    path("", views.index, name="index"),
    path("tables/<str:name>", views.tables, name="tables"),
    path("tablesdb/<str:name>", views.tablesdb, name="tablesdb"),
] 