"""
URL configuration for maxdoc project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from app import views
from django.contrib import admin

urlpatterns = [
    path('', views.index_page, name='index'),
    path('save-settings/', views.save_settings, name='save_settings'),
    path('admin/', admin.site.urls),
    path('settings-table/', views.settings_table, name='settings_table'),  # Новый маршрут для таблицы настроек
]
