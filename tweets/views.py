from django.shortcuts import render
from django.http import HttpResponse


def home_view(request, *args, **kargs):    
    return HttpResponse('Hello World!')

def tweet_detail_view(request, tweet_id, *args, **kargs):        
    return HttpResponse(f'Tweet Id: {tweet_id}')
