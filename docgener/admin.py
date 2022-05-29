from django.contrib import admin

# Register your models here.
from .models import Client, Document

admin.site.register(Client)
admin.site.register(Document)