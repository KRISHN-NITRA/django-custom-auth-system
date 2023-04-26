from django.urls import path, include
from .views import ArticleInsetUpdate, ArticleDispay

urlpatterns = [
    path("show/", ArticleDispay.as_view(), name="show"),
    path("show/<int:pk>", ArticleDispay.as_view(), name="show"),
    path("insert-update/", ArticleInsetUpdate.as_view(), name="insert_update"),
    path("insert-update/<int:pk>", ArticleInsetUpdate.as_view(), name="insert_update"),
    ]