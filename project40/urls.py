"""project40 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path,re_path
from app.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',home.as_view(),name='home'),
    path('School_list/',School_list.as_view(),name='School_list'),
    path('school_create/',school_create.as_view(),name='school_create'),

    re_path('^delete/(?P<pk>\d+)/',schooldelete.as_view(),name='schooldelete'),
    re_path('^update/(?P<pk>\d+)/',schoolupdate.as_view(),name='schoolupdate'),
    re_path('(?P<pk>\d+)/',school_detail.as_view(),name='detailview'),
]
