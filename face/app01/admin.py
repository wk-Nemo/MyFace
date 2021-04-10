from django.contrib import admin

# Register your models here.

from .models import user_native,user_part

admin.site.register(user_native)
admin.site.register(user_part)