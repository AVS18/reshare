from django.contrib import admin
from .models import Profile
# Register your models here.
class ProfileRef(admin.ModelAdmin):
    list_display = ['location','profession']
    list_filter = list_display

admin.site.register(Profile,ProfileRef)