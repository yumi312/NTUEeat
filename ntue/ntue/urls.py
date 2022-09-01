"""ntue URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from eat import views as eat_views
from myaccount import views as myaccount_views
from eatarticle import views as eatarticle_views
from eatforum import views as eatforum_views
from groupbuy import views as groupbuy_views

from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', eat_views.index),
    #eat/home 要改上面 base.html也要改兩個地方 base1.html改一個
    path('eat/article/', eatarticle_views.article),
    path('eat/article/create/', eatarticle_views.create),
    path('eat/article/edit/<int:pk>', eatarticle_views.edit, name="edit"),
    path('eat/article/delete/<int:pk>/', eatarticle_views.delete, name="delete"),
    path('eat/article/detail/<slug:slug>/', eatarticle_views.detail,name="detail"),
    path('eat/article/hashtags/<slug:slug>/', eatarticle_views.hashtag),
    #path('like/<int:pk>/',eatarticle_views.like ,name='blog_posts'),   
    
    path('eat/forum/', eatforum_views.forum),
    #path('eat/forum/', eatforum_views.forum.as_view(),name="forum"),
    path('eat/forum/create/', eatforum_views.createforum),
    path('eat/forum/edit/<int:pk>/', eatforum_views.editforum, name="editforum"),
    path('eat/forum/delete/<int:pk>/', eatforum_views.deleteforum, name="deleteforum"),
    path('eat/forum/detail/<slug:slug>/', eatforum_views.detailforum,name="detailforum"),
    #path('eat/forum/detail/<int:pk>/', eatforum_views.detailforum.as_view(),name="detailforum"),
    path('eat/forum/like/', myaccount_views.like,name="like"),
    path('eat/forum/hashtags/<slug:slug>/', eatforum_views.hashtagforum),
    path('eat/forum/categoryforum/<slug:slug>/', eatforum_views.categoryforum),

    path('eat/map/', eat_views.map),
    path('eat/top/', eat_views.top),
    path('groupbuy/', groupbuy_views.groupbuy),

    path('accounts/', include('allauth.urls')),
    path('accounts/', include('myaccount.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
