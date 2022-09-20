from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


from . import models
# Create your views here.
def allgoods(request):
    return render(request, 'allgoods/allgoods.html',)