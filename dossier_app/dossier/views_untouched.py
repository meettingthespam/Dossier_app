from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (ListView,
                                    DetailView,
                                    CreateView,
                                    UpdateView,
                                    DeleteView)
from django.contrib.auth.decorators import login_required
from .models import DossierPost





@login_required
def dossier(request):

    context = {
        'html_title' : 'dossier',
        'posts': DossierPost.objects.all()
    }
    return render(request, 'dossier/dossier.html', content)





class PostListView(ListView):
    model = DossierPost
    template_name = 'dossier/dossier.html'
    context_object_name = 'posts'
    # displays newest to oldest
    ordering = ['name']
    paginate_by = 15

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
