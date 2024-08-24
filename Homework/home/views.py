from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'home/index.html',{'title':'Home Page'})
def show_image(request):
    return render(request, 'home/show_image.html',{'title':'取得檔案(圖)'})
def register(request):
    return render(request, 'home/register.html',{'title':'會員註冊'})