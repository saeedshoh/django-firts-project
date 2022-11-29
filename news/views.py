from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import NewsForm
from django.views.generic import ListView

from .models import *

class HomeNews(ListView):
    model = News
    template_name=  'news/index.html'
    context_object_name = 'news'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    
    def get_queryset(self):
        return News.objects.filter(is_published=True)
    
class NewsBycategory(ListView):
    model = News
    template_name=  'news/index.html'
    context_object_name = 'news'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    
    def get_queryset(self):
        return News.objects.filter(is_published=True, category_id=self.kwargs['category_id'])
    
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
    
