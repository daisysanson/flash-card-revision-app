from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, get_user_model
from django.contrib import messages
from django.utils.http import is_safe_url
from .forms import RegistrationForm, LoginForm


User=get_user_model()

def registration_view(request):
    form = RegistrationForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password1")
        password2 = form.cleaned_data.get("password2")
        try:
            user = User.objects.create_user(username, email, password)
        except:
            user = None
        if user != None:
            login(request, user)
            return redirect("/")
        else:
            request.session['register_error'] = 1 # 1 == True
    return render(request, "register.html", {"form": form})

def profile_view(request):
  username = request.user.username
  return render(request, 'profile.html', {'username': request.user.username})


def login_view(request):
    form=LoginForm(request.post or None)
    if form.is_valid():
        username=form.cleaned_data.get("username")
        password=form.cleaned_data.get("password")
        print(password)
        user = authenticate(request,username=username,
        password=password)
        return is_safe_url('/profile/')
        if user== None:
            # attempt = request.session.get("attempt") or 0
            # request.session['attempt'] + 1
            # return redirect("/invalid-password")
            return render(request,"forms.html", {"form" : form, 
            "invalid_user": True})