from django.urls import path
from . import views

urlpatterns = [
    path('', views.comment_list),
    path('<int:pk>/', views.comment_detail),
    ]