from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
# being able to customize how the backend looks:
from django.contrib import admin


class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    # date that can be updated
    date_posted = models.DateTimeField(default=timezone.now)
    # this will update the time, every time a post is updated
    last_modified = models.DateTimeField(auto_now=True)
    # sets the datetime only to when the post is originally created,
    # you can never update the date posted argument
    date_original_posted = models.DateTimeField(auto_now_add=True)

    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    # this is done so that once a post is created, the user
    # is redirected directly to that detailed view
    def get_absolute_url(self):
        return reverse('blog-post-detail', kwargs={'pk':self.pk})

# how the data is shown on the backend,
# also affects how the csv is dispayed
class BlogPostAdmin(admin.ModelAdmin):
    actions = ['download_csv_file']
    list_display = ('title', 'date_original_posted', 'last_modified')

    # whatever actions we use we have to define
    def download_csv_file(self, request, queryset):
        import csv
        from django.http import HttpResponse
        from io import StringIO
        from datetime import datetime
        # writing the string as a file
        file = StringIO()
        # writing the CSV file
        writer = csv.writer(file)
        # writing the headers
        writer.writerow(["Title", "Body", "Date_Original_Posted"])

        # adding/writing whatever they add to the queryset
        # to the csv file
        for selected_set in queryset:
            writer.writerow([selected_set.title,
                            selected_set.body,
                            selected_set.date_original_posted])
        # setting the seek at the begginning of the file
        file.seek(0)
        response = HttpResponse(file, content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=wrtings.csv'
        return response

    # displaying on admin page
    download_csv_file.short_description = "Download CSV file for what's selected."
