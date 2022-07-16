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
from groupbuy import views as groupbuy_views

from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', eat_views.index),
    #eat/home 要改上面 base.html也要改兩個地方 base1.html改一個
    path('eat/article/', eat_views.article),
    path('eat/forum/', eat_views.forum),
    path('eat/top/', eat_views.top),
    path('groupbuy/', groupbuy_views.groupbuy),
    path('accounts/', include('allauth.urls')),
    #path('accounts/', include('myaccount.urls')),
]
