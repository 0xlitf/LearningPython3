# myapp/urls.py
from django.urls import path
from django.urls import path, re_path
from django.views.generic import RedirectView
from . import views


urlpatterns = [
    path('', views.root, name='root'),
    path('log/', views.log, name='log'),
    path('home/', views.home, name='home'),
    path('html_test/', views.html_test, name='html_test'),
    path('redirect/', views.redirect, name='redirect'),
    re_path(r'^.*$', RedirectView.as_view(url='redirect/', permanent=False)),
]
