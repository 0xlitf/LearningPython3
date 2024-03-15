# myapp/urls.py
from django.urls import path
from django.urls import path, re_path
from django.views.generic import RedirectView
from . import views
from django.templatetags.static import static  # Not from django.conf.urls.static
from django.views.generic.base import RedirectView

urlpatterns = [
    path('', views.root, name='root'),
    path('log/', views.log, name='log'),
    path('home/', views.home, name='home'),
    path('signal_test/', views.signal_test, name='signal_test'),
    path('html_test/', views.html_test, name='html_test'),
    path('favicon.ico', RedirectView.as_view(url=static('favicon.ico'))),
    path('redirect/', views.redirect, name='redirect'),
    re_path(r'^.*$', RedirectView.as_view(url='redirect/', permanent=False)),
]
