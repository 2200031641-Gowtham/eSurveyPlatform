from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import user_forms,form_questions,form_answers
from authApp.models import eZy_users
# Create your views here.
def index(request):
    return render(request, 'user/index.html')
# currentUser = eZy_users()
def create_form(request):
    if request.method == 'POST':
        return HttpResponse('Post being created by '+ currentUser.uname )
    return render(request,'user/create_form.html')
def add_question(request):
    if request.method == 'POST':
        return HttpResponse('Question add clicked')
def save_user(request):
    if request.method == 'POST':
        uname = request.POST['username'][25:]
        user = eZy_users.objects.all().filter(fname=uname)
        print(user[0].uname)
        createUser(user[0])
        return redirect('refresh_user')
def createUser(user):
    global currentUser
    currentUser = user
    print(currentUser.uname)

def refresh_user(request):
        return render(request,'user/index.html', {'ezy_user':currentUser})
    
def manage_forms(request):
    return render(request,'user/manage_forms.html')
def manage_profile(request):
    uid = currentUser.id
    user = eZy_users.objects.get(id=uid)
    print(user.fname)
    return render(request,'user/manage_profile.html',{'user':user})
def logout(request):
    currentUser = eZy_users()
    return redirect('home')
def user_grievances(request):
    return render(request,'user/user_grievances.html')

from django.contrib import messages
def update_profile(request):
    if request.method == 'POST':
        password = request.POST['password']
        cpwd = request.POST['confirmPassword']
        if password != cpwd:
            messages.error(request, 'Password does not match')
            redirect('manage_profile')
        else:
            uid = currentUser.id
            user = eZy_users.objects.get(id=uid)
            user.uname = request.POST['uname']
            user.fname = request.POST['fname']
            user.lname = request.POST['lname']
            user.email = request.POST['email']
            user.phone = request.POST['phone']
            user.age = request.POST['age']
            user.password = request.POST['password']
            user.address=request.GET['address']
            user.save()
            createUser(user)
            return redirect('refresh_user')
    return render(request,'user/manage_profile.html')