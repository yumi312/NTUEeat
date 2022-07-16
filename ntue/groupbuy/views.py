from django.shortcuts import render
from django.http import HttpResponse

from . import models
# Create your views here.
def groupbuy(request):
    return render(request, 'groupbuy/groupbuy.html',)
