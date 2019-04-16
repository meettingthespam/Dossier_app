from django.urls import path
from . import views

from .views import (PostListView,
                    PostDetailView,
                    PostCreateView,
                    PostUpdateView,
                    PostDeleteView)


urlpatterns = [
    path('', PostListView.as_view(), name='blog'),
    path('blog_post/<int:pk>/', PostDetailView.as_view(), name='blog-post-detail'),
    path('blog_post/new/', PostCreateView.as_view(), name='blog-post-create'),
    path('blog_post/<int:pk>/update', PostUpdateView.as_view(), name='blog-post-update'),
    path('blog_post/<int:pk>/delete', PostDeleteView.as_view(), name='blog-post-delete')

]
