from django.contrib import admin

# Register your models here.
from .models import DossierPost, DossierPostAdmin

admin.site.register(DossierPost, DossierPostAdmin)
