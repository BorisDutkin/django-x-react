from django.http import HttpResponse, Http404, JsonResponse
from django.shortcuts import render

from .models import Tweet


def home_view(request, *args, **kargs):
    return render(request, template_name="pages/home.html", context={})


def tweet_detail_view(request, tweet_id, *args, **kargs):
    try:
        tweet = Tweet.objects.get(id=tweet_id)        
    except:
        return JsonResponse({ "message": f'tweet with an id: {tweet_id}, not found' }, status=404)
    return JsonResponse({ 'id': tweet_id, 'content': tweet.content }, status=200)
