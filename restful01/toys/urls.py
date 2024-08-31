from django.urls import path
from . import views

urlpatterns = [
    path("toys/", views.toy_list),
    path("toys/<int:pk>", views.toy_detail),
]
