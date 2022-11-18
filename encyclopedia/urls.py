from django.urls import path

from . import views

# app_name = "wiki"

urlpatterns = [
    path("", views.index, name ="index"),
    path("<str:name>", views.show, name = "show"),
    path("wiki/<str:name>", views.show, name = "show"),
    path("search/", views.search, name = "search"),
    path("newentry/", views.newentry, name = "newentry"),
    path("editentry/<str:name>", views.editentry, name = "editentry"),
    path("randome/", views.randome, name = "randome"),
]
