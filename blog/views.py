from django.shortcuts import render, get_object_or_404

from .models import Blog

# Create your views here.
def allblogs(request):
    posts = Blog.objects
    return render(request, 'blog/allblogs.html', {'posts' : posts})

def details(request, blog_id):
    details = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/details.html', {'post':details,"id":blog_id})
