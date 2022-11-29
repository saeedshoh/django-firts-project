from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import NewsForm

from .models import *



def index(request):
    news = News.objects.all()    
    return render(request, 'news/index.html', {
        'news': news,
        'title':'Список нововстей'
    })
    
def get_category(request, category_id):
    news  = News.objects.filter(category_id=category_id)
    category = Category.objects.get(pk=category_id)
    
       
    return render(request, 'news/category.html', {
        'news': news,
        'category': category
    })
    
def get_post(request, post_id):
    news = News.objects.get(pk = post_id)    
    return render(request, 'news/show.html', {
        'news': news,
    })


def add_news(request):
    if request.method == 'POST':
        form = NewsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = NewsForm()
    return render(request, 'news/create.html', {'form' : form})
    
