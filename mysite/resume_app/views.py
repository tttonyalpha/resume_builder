from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Resume
from .forms import ResumeForm
from django.template import RequestContext
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.views import LoginView
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib import messages
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.decorators import login_required
from django.db import connection, connections
from django.http import Http404

from django.template import loader

import pdfkit
import io


def index(request):
    return HttpResponse("Welcome to the resume builder website. Here you can create a perfect resume for you")


@login_required(login_url='/login/')
def create_resume(request, *args, **kwargs):
    #    user = User.objects.get(pk=2)
    user = request.user
    if request.method == 'POST':
        form = ResumeForm(request.POST, request.FILES)
        if form.is_valid():
            resume = form.save(commit=False)
            resume.author = user
            resume.save()
            # url = question.get_url()
            return HttpResponseRedirect('/resume/' + str(resume.id))
    else:
        form = ResumeForm()
    return render(request, 'create_resume.html', {'form': form})


@login_required(login_url='/login/')
def resumes_list(request, *args, **kwargs):
    user = request.user
#    user = User.objects.get(pk=2)
    resumes = Resume.objects.new().filter(author=user)
    return render(request, 'resumes_list_template.html', {'resumes': resumes})


@login_required(login_url='/login/')
def download_resume(request, id):
    user = request.user
    try:
        resume = Resume.objects.get(id=id)
    except Resume.DoesNotExist:
        return HttpResponse('<p><h1>Resume does not exist</h1></p>', status=404)
        #form.question_id = id
    template = loader.get_template('single_resume_template.html')
    html = template.render({'resume': resume})

 #   html = render(request, 'single_resume_template.html', {'resume': resume})
    option = {'page-size': 'Letter', 'encoding': 'UTF-8'}
    pdf = pdfkit.from_string(html, False, option)
    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = 'attachments'
    return response


@login_required(login_url='/login/')
def single_resume(request, id):
    user = request.user
    try:
        resume = Resume.objects.get(id=id)
    except Resume.DoesNotExist:
        return HttpResponse('<p><h1>Resume does not exist</h1></p>', status=404)
        #form.question_id = id
    return render(request, 'single_resume_template.html', {'resume': resume})


def register(request, *args, **kwargs):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=raw_password)
            auth_login(request, user)
        return HttpResponseRedirect('/resumes/')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return HttpResponseRedirect('/resumes/')
        else:
            messages.info(request, 'Login or password is incorrect')
    form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


def logout_user(request):
    logout(request)
    return HttpResponseRedirect('/login/')
