from django.urls import path
from . import views

urlpatterns = [
    path('save/', views.save_text, name='save_text'),
    path('latest/', views.get_latest_text, name='get_latest_text'),
]