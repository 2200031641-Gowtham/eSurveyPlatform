from django.shortcuts import render,redirect

# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        print(username,password)
        return redirect('home')
        
    return render(request, 'auth/login.html')
def register(request):
    if request.method == 'POST':
        print('Register request received')
        return redirect('login')
    return render(request, 'auth/register.html')