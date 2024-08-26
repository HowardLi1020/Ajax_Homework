from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'home/index.html',{'title':'Home Page'})
def register(request):
    return render(request, 'home/register.html',{'title':'會員註冊'})