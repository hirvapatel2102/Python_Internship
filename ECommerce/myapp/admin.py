from django.contrib import admin
from .models import about_us, watch, contact

# Register your models here.
admin.site.register(watch)
admin.site.register(about_us)
admin.site.register(contact)