import random
from django.conf import settings
from django.http import HttpResponse, Http404, JsonResponse
from django.shortcuts import render, redirect
from django.utils.http import is_safe_url

from .forms import TweetForm
from .models import Tweet

ALLOWED_HOSTS = settings.ALLOWED_HOSTS


def home_view(request, *args, **kwargs):
    return render(request, template_name="pages/home.html", context={})


def tweet_create_view(request, *args, **kwargs):
    form = TweetForm(request.POST or None)
    next_url = request.POST.get('next') or None

    if form.is_valid():
        obj = form.save(commit=False)
        obj.save()

        if request.is_ajax():
            return JsonResponse(obj.serialize(), status=201)

        if next_url != None and is_safe_url(next_url, ALLOWED_HOSTS):
            return redirect(next_url)

        form = TweetForm()

    return render(request, 'components/form.html', context={
        "form": form
    })


def tweet_list_view(request, *args, **kwargs):
    qs = Tweet.objects.all()

    return JsonResponse({
        'tweets': [tweet.serialize() for tweet in qs]
    }, status=200)


def tweet_detail_view(request, tweet_id, *args, **kwargs):
    try:
        tweet = Tweet.objects.get(id=tweet_id)
    except:
        return JsonResponse({"message": f'tweet with an id: {tweet_id}, not found'}, status=404)
    return JsonResponse({'id': tweet_id, 'content': tweet.content}, status=200)
