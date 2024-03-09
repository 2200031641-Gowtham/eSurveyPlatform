from django.shortcuts import render,redirect
from django.http import HttpResponse
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
        return redirect('user_index')
def createUser(user):
    global currentUser
    currentUser = user
    print(currentUser.uname)