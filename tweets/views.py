import random
from django.http import HttpResponse, Http404, JsonResponse
from django.shortcuts import render


from .forms import TweetForm
from .models import Tweet


def home_view(request, *args, **kwargs):
    return render(request, template_name="pages/home.html", context={})


def tweet_create_view(request, *args, **kwargs):
    form = TweetForm(request.POST or None)

    if form.is_valid():
        obj = form.save(commit=False)
        obj.save()
        form = TweetForm()

    return render(request, 'components/form.html', context={
        "form": form
    })


def tweet_list_view(request, *args, **kwargs):
    qs = Tweet.objects.all()

    return JsonResponse({
        'tweets': [{'id': tweet.id, 'content': tweet.content, 'likes': random.randint(0, 120)} for tweet in qs]
    }, status=200)


def tweet_detail_view(request, tweet_id, *args, **kwargs):
    try:
        tweet = Tweet.objects.get(id=tweet_id)
    except:
        return JsonResponse({"message": f'tweet with an id: {tweet_id}, not found'}, status=404)
    return JsonResponse({'id': tweet_id, 'content': tweet.content}, status=200)
