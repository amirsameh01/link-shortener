from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm, RegisterForm

class UserLoginView(View):

    def get(self, request):
        
        if request.user.is_authenticated:
            return redirect('home')
        
        form = LoginForm()
        return render(request, 'login.html', {'form': form})

    def post(self, request):
        form = LoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            passwored = form.cleaned_data['password']

            user = authenticate(request, username=username, password=passwored)
            if user:
                login(request, user)
                return redirect('home')
            
        messages.error(request,f'username or password is incorrect')
        return render(request, 'login.html', {'form': form})


class UserRegisterView(View):
    def get(self, request):
        form = RegisterForm()
        return render(request, 'register.html', {'form': form})

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'register.html', {'form': form})
        

def logout_view(request):
    logout(request)
    return redirect('login')
