from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (ListView,
                                    DetailView,
                                    CreateView,
                                    UpdateView,
                                    DeleteView)
from django.contrib.auth.decorators import login_required
from .models import CodingIdeasPost




class PostListView(LoginRequiredMixin, ListView):
    model = CodingIdeasPost
    template_name = 'codingIdeas/codingIdeas.html'
    context_object_name = 'posts'
    ordering = ['title']
    paginate_by = 5

class PostDetailView(DetailView):
    model = CodingIdeasPost



class PostCreateView(LoginRequiredMixin, CreateView):
    model = CodingIdeasPost
    fields = ['title', 'body']

    def form_valid(self, form):

        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = CodingIdeasPost
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
    model = CodingIdeasPost
    # if everything goes well, this is a redirect url
    success_url = '/codingIdeas'
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
