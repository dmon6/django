from django.shortcuts import render

posts = [
    {
        'author': 'Dennis',
        'title': 'Blog post 1 ',
        'content': 'First post content',
        'date_posted': 'March 11, 2019'
    },
    {
        'author': 'Kathy',
        'title': 'Blog post 1 ',
        'content': 'Second post content',
        'date_posted': 'March 12, 2019'
    }
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'} )
