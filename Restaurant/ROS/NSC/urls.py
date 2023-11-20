from django.urls import path
from . import views

urlpatterns = [
    path('NSC/', views.NSC, name='NSC'),
]
