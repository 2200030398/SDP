from django.shortcuts import *
from .models import *
# Create your views here.
def home(request):
    return render(request,'home.html')

def login(request):
    return render(request,'login.html')

def gir(request):
    return render(request,'gir.html')

def signup(request):
    return render(request,'signup.html')

def signup1(request):
    if request.method=="POST":
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        confirmpassword=request.POST.get('confirmpassword')

        if Userinfo.objects.filter(email=email).exists():
            return HttpResponse("Email is already Registered Please try with another Email")

        Userinfo.objects.create(username=username,email=email,password=password,confirmpassword=confirmpassword)
        return redirect('home')
    return render(request,'login.html')