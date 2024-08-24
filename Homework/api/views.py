from django.shortcuts import render
from django.http import HttpResponse
import time
import json
from django.core.files.storage import FileSystemStorage
# Create your views here.
def index(reqeust):
    time.sleep(5)
    content='Hello!'
    # response = HttpResponse(content, 'text/plain')
    # 回傳文字內容
    response = HttpResponse(content, content_type='text/plain; charset=utf-8')
    return response

# /api/register/?name=Tom&email=Tom@company.com&age=30
def register(request):
#    接收GET傳過來的資料
#    取得 ?id=3 的資料
#    name = request.GET.get('name', 'Guest')
#    email = request.GET.get('email', 'Guest@company.com')
#    age = request.GET.get('age', 30)
# 接收POST傳過來FormData的資料
   name = request.POST.get('name', 'Guest')
   email = request.POST.get('email', 'Guest@company.com')
   age = request.POST.get('age', 30)

#  接收傳過來的檔案
   uploaded_file = request.FILES.get('avatar')
#    把檔案寫進uploads資料夾
   if uploaded_file:
       fs = FileSystemStorage()
       file_name = fs.save(uploaded_file.name, uploaded_file)

   content = f"{name} 您好，電子郵件是 {email}，{age} 歲了. {file_name}"

   return HttpResponse(content, 'text/plain')

def check_name(request):
    # filter(name='Tom').exists()
    pass

def register1(request):
    user = json.loads(request.body) # 將JSON字串反序列化成dict物件
    name = user.get('name')
    email = user.get('email')
    age = user.get('age')
    content = f"{name} 您好，電子郵件是 {email}，{age} 歲了. "
    return HttpResponse(content, 'text/plain')
