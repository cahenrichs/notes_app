from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import SignupForm, DocumentForm
from .models import Document


# Create your views here.
def index(request):
    return render(request, 'index.html', {})

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            # messages.success(request("Success"))
            return redirect('index')
    else:
        form = SignupForm()
    return render(request, 'signup.html/', {
        'form': form
    })
    
def signin(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')   
            ...
        else:
            # messages.success(request("There was an error signing in. Try again"))
            return redirect('signin')
            ...
    else:
        return render(request, 'signin.html')

def logout_user(request):
    logout(request)
    return redirect('index')

def overview(request):
    data = Document.objects.all()
    return render(request, 'overview.html',{
        'data': data
    })
    
def notes(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST)
        if form.is_valid():
            form.save()
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']
            return redirect('index')
    else:
        form = DocumentForm()
    return render(request, 'notes.html', {
        'form': form
    })