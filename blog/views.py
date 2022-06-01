from asyncio.windows_events import NULL
from dataclasses import fields
from unicodedata import name
from urllib import request
from django import forms
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from django.urls import reverse
from .forms import CreateNewPost


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5

class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html'
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')

class TiketPostListView(ListView):
    model = Post
    template_name = 'blog/tiket_post.html'
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        return Post.objects.filter(author=self.request.user).order_by('-date_posted')

class PostDetailView(DetailView):
    model = Post

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content', 'foto_1']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['foto_2', 'teknisi', 'status']

    def form_valid(self, form):
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author or self.request.user.groups.filter(name='admin'):
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author or self.request.user.groups.filter(name='admin'):
            return True
        return False

class TeknisiListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    template_name = 'blog/teknisi.html'
    context_object_name = 'posts'
    paginate_by = 5

    def test_func(self):
        return self.request.user.groups.filter(name='teknisi')
    
    def get_queryset(self):
        return Post.objects.filter(teknisi=self.request.user).order_by('-date_posted')

class TeknisiNoneListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    template_name = 'blog/teknisi_none.html'
    context_object_name = 'posts'
    paginate_by = 5

    def test_func(self):
        return self.request.user.groups.filter(name='admin')
    
    def get_queryset(self):
        return Post.objects.filter(teknisi__isnull=True).order_by('-date_posted')

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})