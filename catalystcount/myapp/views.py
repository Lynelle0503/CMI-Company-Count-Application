from django.shortcuts import render
from allauth.account.forms import LoginForm, SignupForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView
from django.contrib.auth.models import User 

# Create your views here.

def uploadFile(request):
    return render(request, "uploadPage.html")
    

def qbPage(request):
    return render(request, "QBuildPage.html")
    