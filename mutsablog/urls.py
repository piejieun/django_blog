"""mutsablog URL Configuration

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
from django.urls import path
import jieun.views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', jieun.views.home, name='home'),
    path('blog/<int:blog_id>/',jieun.views.detail, name='detail'),
    path('jieun/new/', jieun.views.new, name='new'),
    path('jieun/make/', jieun.views.make, name='make'),
    path('jieun/count/', jieun.views.count, name='count'),
    path('jieun/result/', jieun.views.result, name='result'),
]
