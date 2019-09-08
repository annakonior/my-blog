from django.shortcuts import render
from django.utils import timezone
from .models import Post
def post_list(request): #request-wszystko co otrzymujemy od użytkowanika internetu
    posts=Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date') #posts to nazwa QuerySetu
    return render(request, 'myblog/post_list.html', {'posts':posts})
#{} jest miejscem, w którym możemy dodać parę rzeczy do wykorzystania w szablonie


