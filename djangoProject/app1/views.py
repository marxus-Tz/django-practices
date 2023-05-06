from django.shortcuts import render
from .models import post

# Create your views here.

# posts = [
#     {
#         'author': 'Anna',
#         'title': 'Blog post 1',
#         'content': 'First post content',
#         'date': 'August 10, 2020'
#     },
#     {
#         'author': 'Jane',
#         'title': 'Blog post 1',
#         'content': 'First post content',
#         'date': 'August 1, 2020'
#     }
# ]

def index(request):
    context = {
        'posts': post.objects.all()# "posts":"posts" if fetching data from the view it sel using example  codes commented above
    }
    return render(request, 'blog/index.html', context)