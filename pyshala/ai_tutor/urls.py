from django.urls import path
from . import views

urlpatterns = [
    path('', views.ai_tutor, name='ai_tutor'),
    path('ask/', views.ask_ai, name='ask_ai'),
]
