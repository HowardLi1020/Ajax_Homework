from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, FileResponse
import time
from .models import myMember
from django.core.files.storage import FileSystemStorage
from datetime import datetime

# Create your views here.
def index(request):
    time.sleep(5)
    content='Hello!'
    response = HttpResponse(content, content_type='text/plain; charset=utf-8')
    return response

def register(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        checkPassword = request.POST.get('checkPassword')
        age = request.POST.get('age')
        uploaded_file = request.FILES.get('avatar')

        file_name = None

        if uploaded_file:
            fs = FileSystemStorage()
            file_name = fs.save(uploaded_file.name, uploaded_file)

        if checkPassword != password:
            content = '密碼不一致'
            return HttpResponse(content, 'text/plain; charset=utf-8')
        
        myMember.objects.create(
            user_name = name,
            user_password = password, 
            user_age = age,
            user_email = email,
            user_avatar = file_name,
            last_update=datetime.now()
        )
        content = "註冊完成"
        return HttpResponse(content, 'text/plain; charset=utf-8')

def check_name(request, name):
    request.GET.get(name)
    userName = myMember.objects.filter(user_name=name).exists()
    if userName:
        content = "帳號已存在"
    else:
        content = "帳號可使用"

    return HttpResponse(content, content_type='text/plain; charset=utf-8')