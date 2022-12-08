import json
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.views import View
from .forms import NewsForm, RegisterForm, UserLoginForm
from django.views.generic import ListView, DeleteView
from django.core.paginator import Paginator
from django.contrib import messages
from django.contrib.auth import login, logout

from .models import *


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, 'Вы успешно зарегистривовались')
            return redirect('login')
        else:
            messages.error(request, 'Ошибка авторзицация')

    else:
        form = RegisterForm()
    return render(request, 'news/register.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('login')


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Ошибка авторзицация')
    else:
        form = UserLoginForm()
    return render(request, 'news/login.html', {'form': form})


def test(request):
    objects = ['item1', 'item2', 'item3', 'item4',
               'item5', 'item6', 'item7', 'item8', ]
    paginator = Paginator(objects, 2)
    page_num = request.GET.get('page', 1)
    page_objects = paginator.get_page(page_num)
    return render(request, 'news/test.html', {'page_obj': page_objects})


class HomeNews(ListView):
    model = News
    template_name = 'news/index.html'
    context_object_name = 'news'
    paginate_by = 2

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get_queryset(self):
        return News.objects.filter(is_published=True).select_related('category')


class NewsBycategory(ListView):
    model = News
    template_name = 'news/index.html'
    context_object_name = 'news'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get_queryset(self):
        return News.objects.filter(is_published=True, category_id=self.kwargs['category_id'])


class GetPostView(DeleteView):
    model = News
    template_name = 'news/show.html'
    pk_url_kwarg = 'news_id'


def get_post(request, post_id):
    news = News.objects.get(pk=post_id)
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
    return render(request, 'news/create.html', {'form': form})


class TestBaseView(View):

    def get(self, request):
        query = News.objects.all().values()
        print(query)
        return JsonResponse({"key1": list(query)})
