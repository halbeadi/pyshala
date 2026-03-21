from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('accounts/', include('accounts.urls')),
    path('courses/', include('courses.urls')),
    path('interpreter/', include('interpreter.urls')),
    path('quiz/', include('quiz.urls')),
    path('ai-tutor/', include('ai_tutor.urls')),
]