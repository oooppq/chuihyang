from django.shortcuts import redirect, render
from django.contrib import auth

# Create your views here.
def login(request):
    if request.method == "GET":
        return render(request, 'login.html')
    elif request.method == "POST":
        id = request.POST['username']
        pw = request.POST['password']
        user = auth.authenticate(request, username=id, password=pw)
        if user != None:
            auth.login(request, user)
            return redirect('home')
        else: return render(request, 'login.html')
        
def logout(request):
    auth.logout(request)
    return redirect('home')