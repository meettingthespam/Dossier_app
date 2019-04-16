from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (ListView,
                                    DetailView,
                                    CreateView,
                                    UpdateView,
                                    DeleteView)
from django.contrib.auth.decorators import login_required
from .models import DossierPost

# search imports
# (encapsulates our database)
from django.db.models import Q

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


@login_required
def dossier(request):
    """
    Adding a search bar at navbar just for Dossier 
    """
    html_title = "/dossier"
    posts_list = DossierPost.objects.all()
    search_term=''

    if 'search' in request.GET:
        search_term = request.GET['search']
        posts = posts_list.filter(name__icontains=search_term)
    else:
        posts = posts_list

    page = request.GET.get('page', 1)

    paginator = Paginator(posts, 10)

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    context = {
        'html_title' : html_title,
        'posts': posts,
        'search_term': search_term
    }
    return render(request, 'dossier/dossier.html', context)


class PostDetailView(DetailView):
    model = DossierPost



class PostCreateView(LoginRequiredMixin, CreateView):
    model = DossierPost
    fields = ['name', 'hobbies', 'appearance', 'discussions']

    def form_valid(self, form):

        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = DossierPost
    fields = ['name', 'hobbies', 'appearance', 'discussions']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin,DeleteView):
    model = DossierPost
    # if everything goes well, this is a redirect url
    success_url = '/dossier'
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
