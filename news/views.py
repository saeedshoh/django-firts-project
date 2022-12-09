import json
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.views import View
from .forms import NewsForm, RegisterForm, UserLoginForm, ContactForm
from django.views.generic import ListView, DeleteView
from django.core.paginator import Paginator
from django.contrib import messages
from django.contrib.auth import login, logout
from django.core.mail import send_mail

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
     if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            mail = send_mail(form.cleaned_data['subject'], form.cleaned_data['content'], 'bsaeedshoh@gmail.com', ['saeedshoh@gmail.com', 'saeedshoh@mail.ru'])
            if mail:
                messages.success(request, 'Писмо отправлено!')
                return redirect('test')
            else:
                messages.error(request, 'Ошибка отправки!')
        else:
            messages.error(request, 'Ошибка авторзицация')
     else:
        form = ContactForm()
     return render(request, 'news/test.html', {'form': form})


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
