from django.contrib import admin

from .models import CodingIdeasPost, CodingIdeasPostAdmin

admin.site.register(CodingIdeasPost, CodingIdeasPostAdmin)
