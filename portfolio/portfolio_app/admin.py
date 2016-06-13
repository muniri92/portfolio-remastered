from django.contrib import admin

# Register your models here.

from .models import About, Portfolio, Education, Experience

admin.site.register(About)
admin.site.register(Portfolio)
admin.site.register(Education)
admin.site.register(Experience)
