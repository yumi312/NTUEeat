import re
from turtle import title
from .models import Hashtag, Eatarticle
from django.contrib.auth.models import User


def Autohashtag(form):
    eatarticle = Eatarticle.objects.create(title=form["title"].data,
                                           author_name=User.objects.get(
                                               id=form["author_name"].data),
                                           snippet=form["snippet"].data,
                                           hashtag=Hashtag.objects.get(
                                               id=form["hashtag"].data),
                                           # slug=form["slug"].data,
                                           image=form["image"].data,
                                           # edit_time=form["edit_time"].data
                                           )
    contents = form["contents"].data
    tag = list(map(lambda x: x.replace(" #", ""),
                   re.findall(r" #\w+", contents)))
    new_contents = re.sub(r" #\w+", "", contents)
    eatarticle.contents = new_contents
    eatarticle.save(commit=False)

    tag, created = Hashtag.objects.get_or_create(
        title=tag[0])
    print(tag.id, tag, created)
    tag.save()
    Eatarticle.objects.filter(title=form["title"].data).update(
        hashtag=tag)
