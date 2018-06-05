
from django.contrib.auth import authenticate, login, get_user_model, logout
from django.shortcuts import render, HttpResponseRedirect
from .froms import UserCreationForm, UserLoginForm

User = get_user_model()


def register(request, *args, **kwargs):
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/login')
    return render(request, 'accounts/register.html', {'form': form})


def login_view(request, *args, **kwargs):
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username_ = form.cleaned_data.get('username')
        user_obj = User.objects.get(username__iexact=username_)
        login(request, user_obj)
        return HttpResponseRedirect("/")
    return render(request, "accounts/login.html", {"form": form})


def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/login')