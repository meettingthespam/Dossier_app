from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (ListView,
                                    DetailView,
                                    CreateView,
                                    UpdateView,
                                    DeleteView)
from django.contrib.auth.decorators import login_required
from .models import BlogPost



class PostListView(LoginRequiredMixin, ListView):
    model = BlogPost
    template_name = 'blog/blog.html'
    context_object_name = 'posts'
    # displays newest to oldest
    ordering = ['-date_posted']
    paginate_by = 5

class PostDetailView(DetailView):
    model = BlogPost



class PostCreateView(LoginRequiredMixin, CreateView):
    model = BlogPost
    fields = ['title', 'body']

    def form_valid(self, form):

        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = BlogPost
    fields = ['title', 'body']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin,DeleteView):
    model = BlogPost
    # if everything goes well, this is a redirect url
    success_url = '/blog'
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
