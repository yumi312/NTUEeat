from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect

from .form import ArticleForm
from .models import Hashtag, Eatarticle

from django.contrib.auth.decorators import permission_required
# Create your views here.
def article(request):
    q = request.GET.get('q', None)
    items = ""
    if q is None or q == "":
        eatarticles = Eatarticle.objects.all()
        hashtags = Hashtag.objects.all()
    elif q is not None:
        eatarticles = Eatarticle.objects.filter(title__contains=q)
        hashtags = Hashtag.objects.filter(title__contains=q)
    return render(request, 'eatarticle/article.html',{'eatarticles':eatarticles, 'hashtags':hashtags})


def detail(request, slug=None):  # < here
    eatarticle = get_object_or_404(Eatarticle, slug=slug)
    hashtag = Hashtag.objects.all()
    print(eatarticle.slug)
    return render(request, 'eatarticle/detail.html', {'eatarticle':eatarticle, 'hashtag':hashtag})

#放在eat/article.html頁面的
def hashtag(request, slug=None):
    eatarticle = Eatarticle.objects.filter(hashtag__slug=slug)
    hashtag = Hashtag.objects.all()
    return render(request, 'eatarticle/article.html', {'eatarticle':eatarticle, 'hashtag':hashtag}) 
#發文
@permission_required('article.add_article')
def create(request):
    if request.method == "POST":
        # 如果失敗 ->(request.POST, request.FILES)
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/eat/article")
    else:
        form = ArticleForm
    return render(request, "eatarticle/edit.html", {'form': form})
#修改
@permission_required('article.change_article')
def edit(request, pk=None):
    # 判斷物件存不存在，存在就傳回，不存在就404
    a = get_object_or_404(Eatarticle, pk=pk)
    if request.method == "POST":
        form = ArticleForm(request.POST, instance=a)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/eat/article")
    else:
        form = ArticleForm(instance=a)
    return render(request, "eatarticle/edit.html", {'form': form})
#刪除
@permission_required('article.delete_article')
def delete(request, pk=None):
    a = get_object_or_404(Eatarticle, pk=pk)
    a.delete()
    return HttpResponseRedirect("/eat/article")