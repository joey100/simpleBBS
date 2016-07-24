"""simpleBBS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from bbs import views
urlpatterns = [
    url(r'^$',views.index),
    url(r'^category/(\d+)/$', views.category, name='category'),
    url(r'^articleDetail/(\d+)/$', views.articleDetail, name='articleDetail'),
    url(r'^comment/$', views.postComments, name='postComments'),
    url(r'^getComments/(\d+)/$', views.getComments, name='getComments'),
    url(r'^inputArticle/$', views.inputArticle, name='inputArticle'),
    url(r'^postArticle/$', views.postArticle, name='postArticle'),
    url(r'^fileUpload/$', views.fileUpload, name='fileUpload'),
    url(r'^getLatestArticleCount/$', views.getLatestArticleCount, name='getLatestArticleCount'),
]
