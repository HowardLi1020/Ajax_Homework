from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, FileResponse
import time
import json

# Create your views here.
def index(reqeust):
    time.sleep(5)
    content='Hello!'
    # response = HttpResponse(content, 'text/plain')
    # 回傳文字內容
    response = HttpResponse(content, content_type='text/plain; charset=utf-8')
    return response
