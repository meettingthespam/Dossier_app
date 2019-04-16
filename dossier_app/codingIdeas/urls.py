from django.urls import path
from . import views

from .views import (PostListView,
                    PostDetailView,
                    PostCreateView,
                    PostUpdateView,
                    PostDeleteView)


urlpatterns = [
    path('', PostListView.as_view(), name='codingIdeas'),
    path('codingIdeas_post/<int:pk>/', PostDetailView.as_view(), name='codingIdeas-post-detail'),
    path('codingIdeas_post/new/', PostCreateView.as_view(), name='codingIdeas-post-create'),
    path('codingIdeas_post/<int:pk>/update', PostUpdateView.as_view(), name='codingIdeas-post-update'),
    path('codingIdeas_post/<int:pk>/delete', PostDeleteView.as_view(), name='codingIdeas-post-delete')

]
