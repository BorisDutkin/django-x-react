from django.http import HttpResponse, Http404

from .models import Tweet


def home_view(request, *args, **kargs):
    return HttpResponse('Hello World!')


def tweet_detail_view(request, tweet_id, *args, **kargs):
    try:
        tweet = Tweet.objects.get(id=tweet_id)        
    except:
        raise Http404
    return HttpResponse(f'Tweet Id: {tweet_id}, {tweet.content}')
