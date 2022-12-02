import json
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.views import View
from .forms import NewsForm
from django.views.generic import ListView, DeleteView

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



class GetPostView(DeleteView):
    model = News
    template_name=  'news/show.html'
    pk_url_kwarg =  'news_id'


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

class TestBaseView(View):

    def get(self, request):
        query = News.objects.all().values()
        print(query)
        return JsonResponse({"key1": list(query)})
    
