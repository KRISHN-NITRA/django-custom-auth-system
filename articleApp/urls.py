from django.urls import path, include
from .views import ArticleCRUD

urlpatterns = [
    path("crud/", ArticleCRUD.as_view(), name="crud"),
    path("crud/<int:pk>", ArticleCRUD.as_view(), name="crudPk"),
    ]