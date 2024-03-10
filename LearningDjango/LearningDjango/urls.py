"""
URL configuration for project LearningDjango.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
import debug_toolbar
from django.contrib import admin
from django.urls import path, include  # 确保导入了include

# url路径与python函数写在一起，而非flask的装饰器形式
# 编写url与视图函数的对应关系

urlpatterns = [
    path('', include('app_main.urls')),
    path('log/', include('app_main.urls')),
    path('html_test/', include('app_main.urls')),
    path('__debug__/', include(debug_toolbar.urls)),
    path('admin/', admin.site.urls),
    path('app_main/', include('app_main.urls')),
]
