from django.urls import path
from . import views

urlpatterns = [ path('topic/', views.topic_list),
                path('topic/<int:pk>/', views.topic_detail)]