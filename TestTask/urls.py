from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("", include('django.contrib.auth.urls')),
    path("register/", views.register, name="register"),
    path("users", views.users_list, name="usersList"),
    path("users/<int:pk>", views.user_page, name="userPage"),
    path("users/update/<int:pk>", views.user_update_page, name="userPageUpdate"),
]
