"""hw4 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('logon', views.log_on),
    path('login', views.log_in),
    path('logout', views.log_out),
    path('record/add', views.add_record),
    path('record/<slug:id_num>/delete', views.delete_record),
    path('record/<slug:id_num>/update', views.update_record),
    path('record/<int:id_num>', views.get_record),
    path('record/query', views.search_record),
]
