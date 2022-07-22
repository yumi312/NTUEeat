from django.shortcuts import redirect, render
from django.http import HttpResponse

from . import models
# Create your views here.
def index(request):
    return render(request, 'eat/index.html',)



def forum(request):
    return render(request, 'eat/forum.html',)

def top(request):
    return render(request, 'eat/top.html',)