from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import eZy_users
# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        users = eZy_users.objects.all()
        if(users.filter(uname=username,password=password).exists()):
            return HttpResponse('Login success')
        else:
            return HttpResponse('Login failed')
    return render(request, 'auth/login.html')

def register(request):
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        uname = request.POST['username']
        email = request.POST['email']
        phone =int( request.POST['phone'])
        age = int(request.POST['age'])
        gender = request.POST['genderOptions']
        password = request.POST['password']
        confirmPassword = request.POST['confirmPassword']
        address = request.POST.get('address')
        if(password == confirmPassword):
            print(fname,lname,uname,email,phone,age,gender,password,address)
            user = eZy_users(fname=fname,lname=lname,uname=uname,email=email,phone=phone,age=age,password=password,address=address)
            user.save()
            return HttpResponse('User registered successfully')
        else:
            print('OKokOK')
        print('Register request received')
        return redirect('login')
    return render(request, 'auth/register.html')