from django.contrib import admin
from .models import *

class CustomUserAdmin(admin.ModelAdmin): pass

admin.site.register(CustomUser, CustomUserAdmin)

admin.site.site_header = 'система складского учёта для мастерской'
admin.site.site_title = 'site_title'
admin.site.index_title = 'admin'
