from xml.etree.ElementTree import Comment
from django.urls import reverse
from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import DetailView, CreateView
from .form import ArticleForm
from .models import Hashtag, Eatarticle
from .utils import Autohashtag

from django.contrib.auth.decorators import permission_required
# Create your views here.


def like(request, pk):
    eatarticle = get_object_or_404(Eatarticle, id=request.POST.get('post_id'))
    print('555')
    if eatarticle.likes.filter(id=request.user.id).exists():
        eatarticle.likes.remove(request.user)
    else:
        eatarticle.likes.add(request.user)
        print('123')

    return HttpResponseRedirect(reverse('detail', args=[str(pk)]))


def article(request):
    q = request.GET.get('q', None)
    items = ""
    if q is None or q == "":
        eatarticles = Eatarticle.objects.all()
        hashtags = Hashtag.objects.all()
    elif q is not None:
        eatarticles = Eatarticle.objects.filter(title__contains=q)
        hashtags = Hashtag.objects.filter(title__contains=q)
    return render(request, 'eatarticle/article.html', {'eatarticles': eatarticles, 'hashtags': hashtags})


# 放在eat/article.html頁面的
""" class BlogPostDetailView(DetailView):
    model = Eatarticle
    template_name: 'eatarticle/detail.html'
    context_object_name = 'object'
    print("1") """


def detail(request, slug=None):  # < here
    eatarticle = get_object_or_404(Eatarticle, slug=slug)
    hashtag = Hashtag.objects.all()
    print(eatarticle.slug)
    return render(request, 'eatarticle/detail.html', {'eatarticle': eatarticle, 'hashtag': hashtag})
    """ def get_context_data(self,*args,**kwargs):
        context = super(BlogPostDetailView,self).get_context_data(*args,**kwargs)
        likes_connected = get_object_or_404(Eatarticle, id=self.kwargs['pk'])
        liked = False
        if likes_connected.likes.filter(id=self.request.user.id).exists():
            liked = True
        context['number_of_likes'] = likes_connected.number_of_likes()
        context['post_is_liked'] = liked
        print("2")
        return context """


def hashtag(request, slug=None):
    eatarticle = Eatarticle.objects.filter(hashtag__slug=slug)
    hashtag = Hashtag.objects.all()
    return render(request, 'eatarticle/article.html', {'eatarticles': eatarticle, 'hashtags': hashtag})
# 發文


""" class AddCommentView(CreateView):
    model = Comment
    template_name: 'eatarticle/detail.html'
    fields: '__all__' """


@permission_required('article.add_article')
def create(request):
    if request.method == "POST":
        # 如果失敗 ->(request.POST, request.FILES)
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            Autohashtag(form)
            # form.save()
            return HttpResponseRedirect("/eat/article")
    else:
        form = ArticleForm
    return render(request, "eatarticle/edit.html", {'form': form})
# 修改


@permission_required('article.change_article')
def edit(request, pk=None):
    # 判斷物件存不存在，存在就傳回，不存在就404
    a = get_object_or_404(Eatarticle, pk=pk)
    if request.method == "POST":
        form = ArticleForm(request.POST or None,
                           request.FILES, instance=a)   # 修了這行
        if form.is_valid():
            Autohashtag(form)
            # form.save()
            return HttpResponseRedirect("/eat/article")
    else:
        form = ArticleForm(instance=a)
    return render(request, "eatarticle/edit.html", {'form': form})
# 刪除


@permission_required('article.delete_article')
def delete(request, pk=None):
    a = get_object_or_404(Eatarticle, pk=pk)
    a.delete()
    return HttpResponseRedirect("/eat/article")
