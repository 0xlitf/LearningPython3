from django.shortcuts import render

# Create your views here. url与函数的对应关系中对应的函数

from django.http import HttpResponse
from django.urls import path, re_path
from django.views.generic import RedirectView
import logging

logger = logging.getLogger(__name__)

# 如果想返回一个html页面，就要return render()
def html_test(request):
    return render(request, 'html_test.html')  # 并非从当前templates目录U型你找，而是根据app的注册顺序，逐一去找templates目录，比如在根目录templates也有同名文件，会从当前app的templates目录中寻找
# 如果在项目的settings.py中有指定'DIRS': [BASE_DIR / 'templates']，那么就会优先从根目录的templates中寻找
# 在开发过程中，一般将css、图片、js或者插件都会当作静态文件处理，

def log(request):
    logger.debug('This is a debug message for log')
    logger.info('This is an info message for log')
    logger.warning('This is a warning message for log')
    logger.error('This is an error message for log')
    logger.critical('This is a critical message for log')
    return HttpResponse("log")


def root(request):
    logger.debug('This is a debug message')
    logger.info('This is an info message')
    logger.warning('This is a warning message')
    logger.error('This is an error message')
    logger.critical('This is a critical message')
    return HttpResponse("welcome")


def home(request):
    logger.debug('This is a debug message')
    logger.info('This is an info message')
    logger.warning('This is a warning message')
    logger.error('This is an error message')
    logger.critical('This is a critical message')
    return HttpResponse("欢迎来到我的应用首页！")

def redirect(request):
    return HttpResponse("no page found, redirect to this page")
