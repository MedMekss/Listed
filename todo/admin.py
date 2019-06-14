from django.contrib import admin
from . import models

admin.sites.site.register(models.Category)
admin.sites.site.register(models.CheckList)
admin.sites.site.register(models.Item)
admin.sites.site.register(models.Messages)
