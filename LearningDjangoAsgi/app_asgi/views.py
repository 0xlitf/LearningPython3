from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, HttpResponse
from django.views.decorators.http import require_http_methods


@require_http_methods(["GET"])
def hello_asgi(request):
    return HttpResponse('{\"name\":\"hello_asgi --reload 2\"}', content_type="application/json;charset=utf-8")
