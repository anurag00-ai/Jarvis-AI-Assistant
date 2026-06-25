from django.contrib import admin
from django.urls import path
from jarvis import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('chat/', views.chat),
]