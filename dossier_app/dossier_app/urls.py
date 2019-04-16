from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('dossier.urls')),
    path('blog/', include('blog.urls')),
    path('codingIdeas/',include('codingIdeas.urls')),
]
