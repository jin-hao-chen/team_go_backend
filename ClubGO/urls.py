"""ClubGO URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path, re_path, include
from django.views.static import serve
from ClubGO.settings import MEDIA_ROOT

from users.views import LoginView
from users.views import RegisterView
from clubs.views import ClubListView

from rest_framework.routers import DefaultRouter

import xadmin


router = DefaultRouter()

# 不能有下划线, 只能是单一路径
router.register(r'clubs', ClubListView)

urlpatterns = [
    re_path(r'^api/v1/', include(router.urls)),
    re_path(r'^xadmin/', xadmin.site.urls),
    re_path(r'^media/(?P<path>.*)', serve, {'document_root': MEDIA_ROOT}),
    re_path(r'^ueditor/', include('DjangoUeditor.urls')),
    re_path(r'^api/v1/login/', LoginView.as_view()),
    re_path(r'^api/v1/register/', RegisterView.as_view())
]
