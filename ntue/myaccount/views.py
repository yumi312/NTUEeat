from django.shortcuts import render, get_object_or_404


from .models import UserProfile
from eatforum.models import Eatforum
from .forms import ProfileForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
import json


@login_required
def profile(request):
    user = request.user
    return render(request, 'account/profile.html', {'user': user})


@login_required
def profile_update(request):
    user = request.user
    user_profile = get_object_or_404(UserProfile, user=user)

    if request.method == "POST":
        form = ProfileForm(request.POST)
        # form表單驗證提交資料的正確性
        if form.is_valid():
            # 獲取篩選後的資料，參考django的form表單
            user.first_name = form.cleaned_data['first_name'] 
            user.last_name = form.cleaned_data['last_name']
            user.save()
            user_profile.phone = form.cleaned_data['phone']
            user_profile.save()

            return HttpResponseRedirect(reverse('myaccount:profile'))
    else:
        default_data = {'first_name': user.first_name, 'last_name': user.last_name,'phone': user_profile.phone, }
        form = ProfileForm(default_data)

    return render(request, 'account/profile_update.html', {'form': form, 'user': user})

@login_required
def like(request):
    if request.POST.get('action') == 'eatforum':
        result = ''
        id = int(request.POST.get('eatforumid'))
        eatforum = get_object_or_404(Eatforum,id=id)
        if eatforum.likes.filter(id=request.user.id).exists():
            eatforum.likes.remove(request.user)
            eatforum.like_count -= 1
            result = eatforum.like_count
            eatforum.save()
        else:
            eatforum.likes.add(request.user)
            eatforum.like_count += 1
            result = eatforum.like_count
            eatforum.save()
        
        return JsonResponse({'result':result,})


# Create your views here.
