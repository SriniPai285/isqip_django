from django.shortcuts import redirect,render
from posts.models import Post

# Create your views here.
def posts_list(request):
    posts=Post.objects.filter(is_active=True)
    return render(request,'posts/posts_list.html',{'posts':posts})