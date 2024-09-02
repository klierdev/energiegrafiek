from django.contrib import admin
from django.contrib.auth.models import Group
from .models import EnergieTerug#, CSVBestanden



admin.site.unregister(Group)

admin.site.register(EnergieTerug)

#admin.site.register(CSVBestanden)