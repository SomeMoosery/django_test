#Views are where we put the "logic" of our application -> request info from the model (say, a Post model) and pass it to a template

from django.shortcuts import render
from .models import Post
from django.utils import timezone

#Takes a request and returns a function render that puts together our template blog/post_list.html (also defined in blog/urls.py)
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts':posts})
