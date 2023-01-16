from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
import django_filters
from django.views.generic import CreateView, ListView
from django.contrib.auth import logout, login

from . import models
from . import forms


class ProductFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='contains')

    class Meta:
        model = models.Post
        fields = ['title', ]


def index(request):
    posts1 = models.Post.objects.filter(is_published=True).order_by('-time_create')[:3]
    posts2 = models.Post.objects.all()
    posts = models.Post.objects.all().order_by('-time_create')[:11]
    cats = models.Category.objects.all().order_by('-title')[:5]
    return render(request, 'magazine/home.html', {'posts': posts, 'posts1': posts1, 'posts2': posts2, 'cats': cats})


def search(request):
    f = ProductFilter(request.GET, queryset=models.Post.objects.all())
    cats = models.Category.objects.all()
    return render(request, 'magazine/search.html', {'filter': f, 'cats': cats})


class ShowPost(ListView):
    model = models.Post
    template_name = 'magazine/show_post.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        cats = models.Category.objects.all()
        context['cats'] = cats
        return context

    def get_queryset(self):
        return models.Post.objects.get(slug=self.kwargs['slug'])


class ShowCategory(ListView):
    model = models.Category
    template_name = 'magazine/show_cat.html'
    context_object_name = 'category'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        cats = models.Category.objects.all()
        context['cats'] = cats
        return context

    def get_queryset(self):
        return models.Category.objects.get(slug=self.kwargs['slug'])


class RegisterUser(CreateView):
    form_class = forms.Registration
    template_name = "magazine/registration.html"
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


class LoginUser(LoginView):
    form_class = forms.LoginUserForm
    template_name = 'magazine/login.html'

    def get_success_url(self):
        return reverse_lazy('home')


def logout_me(request):
    logout(request)
    return redirect('home')
