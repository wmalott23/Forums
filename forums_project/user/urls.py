from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_info_list),
    path ('<int:pik>/', views.user_info_detail)]
