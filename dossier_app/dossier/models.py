from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
# being able to customize how the backend looks:
from django.contrib import admin


class DossierPost(models.Model):
    name = models.CharField(max_length=100)
    hobbies = models.CharField(max_length=200, blank=True)
    appearance = models.CharField(max_length=200, blank=True)

    discussions = models.TextField(blank=True)

    # date that can be updated
    date_posted = models.DateTimeField(default=timezone.now)
    # this will update the time, every time a post is updated
    last_modified = models.DateTimeField(auto_now=True)
    # sets the datetime only to when the post is originally created,
    # you can never update the date posted argument
    date_original_posted = models.DateTimeField(auto_now_add=True)

    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    # this is done so that once a post is created, the user
    # is redirected directly to that detailed view
    def get_absolute_url(self):
        return reverse('dossier-post-detail', kwargs={'pk':self.pk})

# how the data is shown on the backend,
# also affects how the csv is dispayed
class DossierPostAdmin(admin.ModelAdmin):
    actions = ['download_csv_file']
    list_display = ('name', 'hobbies', 'appearance', 'discussions')

    # whatever actions we use we have to define
    def download_csv_file(self, request, queryset):
        import csv
        from django.http import HttpResponse
        from io import StringIO
        # writing the string as a file
        file = StringIO()
        # writing the CSV file
        writer = csv.writer(file)
        # writing the headers
        writer.writerow(["Name", "Hobbies", "Appearance", "Discussions"])

        # adding/writing whatever they add to the queryset
        # to the csv file
        for selected_set in queryset:
            writer.writerow([selected_set.name,
                            selected_set.hobbies,
                            selected_set.appearance,
                            selected_set.discussions])
        # setting the seek at the begginning of the file
        file.seek(0)
        response = HttpResponse(file, content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=dossier.csv'
        return response



    # displaying on admin page
    download_csv_file.short_description = "Download CSV file for what's selected."
