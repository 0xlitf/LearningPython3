from django.shortcuts import render

# Create your views here. url与函数的对应关系中对应的函数

from django.http import HttpResponse
from django.urls import path, re_path
from django.views.generic import RedirectView
import logging

logger = logging.getLogger(__name__)

# 如果想返回一个html页面，就要return render()
def html_test(request):
    return render(request, 'html_test.html')

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
