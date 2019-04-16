from django.urls import path
from . import views

from .views import (#PostListView,
                    PostDetailView,
                    PostCreateView,
                    PostUpdateView,
                    PostDeleteView)


urlpatterns = [
    path('', views.dossier, name='dossier'),
    path('dossier_post/<int:pk>/', PostDetailView.as_view(), name='dossier-post-detail'),
    path('dossier_post/new/', PostCreateView.as_view(), name='dossier-post-create'),
    path('dossier_post/<int:pk>/update', PostUpdateView.as_view(), name='dossier-post-update'),
    path('dossier_post/<int:pk>/delete', PostDeleteView.as_view(), name='dossier-post-delete')

]
