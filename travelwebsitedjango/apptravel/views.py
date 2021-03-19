from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
# from .forms import *
from .models import *


def index_page(request):
    # if request.method == "POST":
    #     form = SignUpForm(request.POST, request.FILES)
    #     if form.is_valid():
    #         form.save()
    #         user = form.cleaned_data.get('id_program')
    #         messages.success(request, user)
    #         username = form.cleaned_data.get('username')
    #         password = form.cleaned_data.get('password1')
    #         account = authenticate(username=username, password=password)
    #         login(request, account)
    #
    #         return redirect('login')
    #     else:
    #         context = {'form': form}
    # else:
    #     form = SignUpForm()
    #     context = {'form': form}
    return render(request, 'index.html')


def profile_page(request):
    return render(request, 'profile.html')


def forum_page(request):
    return render(request, 'forum.html')