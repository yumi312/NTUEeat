from re import template
from unicodedata import category
from xml.etree.ElementTree import Comment
from django.urls import reverse
from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import ListView,DetailView,CreateView
from .form import ArticleForm
from .models import Hashtagforum, Eatforum, Categoryforum

from django.contrib.auth.decorators import permission_required

def likeforum(request, pk):
    eatforum = get_object_or_404(Eatforum, id=request.POST.get('eatforum_id'))
    if eatforum.likes.filter(id=request.user.id).exists():
        eatforum.likes.remove(request.user)
    else:
        eatforum.likes.add(request.user)
    return HttpResponseRedirect(reverse('detailforum', eatforum.pk))

"""class forum(ListView):
    model = Eatforum
    template_name = 'eatforum/forum.html'

class detailforum(DetailView):
    model = Eatforum
    template_name = 'eatforum/detail.html'

"""
def forum(request):
    q = request.GET.get('q', None)
    items = ""
    if q is None or q == "":
        eatforums = Eatforum.objects.all()
        hashtagforums = Hashtagforum.objects.all()
        categoryforums = Categoryforum.objects.all()
    elif q is not None:
        eatforums = Eatforum.objects.filter(title__contains=q)
        hashtagforums = Hashtagforum.objects.filter(title__contains=q)
        categoryforums = Categoryforum.objects.all()
    return render(request, 'eatforum/forum.html', {'eatforums': eatforums, 'hashtagforums': hashtagforums, 'categoryforums': categoryforums})

def detailforum(request, slug=None):  # < here
    eatforum = get_object_or_404(Eatforum, slug=slug)
    hashtagforum = Hashtagforum.objects.all()
    categoryforum = Categoryforum.objects.all()
    return render(request, 'eatforum/detail.html', {'eatforum': eatforum, 'hashtagforum': hashtagforum,'categoryforum':categoryforum})

def hashtagforum(request, slug=None):
    eatforum = Eatforum.objects.filter(hashtag__slug=slug)
    hashtagforum = Hashtagforum.objects.all()
    categoryforum = Categoryforum.objects.all()
    return render(request, 'eatforum/forum.html', {'eatforums': eatforum, 'hashtagforums': hashtagforum,'categoryforums':categoryforum})

def categoryforum(request, slug=None):
    eatforum = Eatforum.objects.filter(hashtag__slug=slug)
    hashtagforum = Hashtagforum.objects.all()
    categoryforum = Categoryforum.objects.all()
    return render(request, 'eatforum/forum.html', {'eatforums': eatforum, 'hashtagforums': hashtagforum,'categoryforums':categoryforum})
# 發文

""" class AddCommentView(CreateView):
    model = Comment
    template_name: 'eatarticle/detail.html'
    fields: '__all__' """

@permission_required('forum.add_forum')
def createforum(request):
    if request.method == "POST":
        # 如果失敗 ->(request.POST, request.FILES)
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/eat/forum")
    else:
        form = ArticleForm
    return render(request, "eatforum/edit.html", {'form': form})
# 修改


@permission_required('forum.change_forum')
def editforum(request, pk=None):
    # 判斷物件存不存在，存在就傳回，不存在就404
    a = get_object_or_404(Eatforum, pk=pk)
    if request.method == "POST":
        form = ArticleForm(request.POST or None,
                           request.FILES, instance=a)   # 修了這行
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/eat/forum")
    else:
        form = ArticleForm(instance=a)
    return render(request, "eatforum/edit.html", {'form': form})
# 刪除


@permission_required('forum.delete_forum')
def deleteforum(request, pk=None):
    a = get_object_or_404(Eatforum, pk=pk)
    a.delete()
    return HttpResponseRedirect("/eat/forum")