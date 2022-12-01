from django.contrib import admin
from .models import User, Profile
from django.contrib.auth.models import Group

admin.site.unregister(Group)

# Register your models here.
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'bio', 'followers_count',)
    list_display_links = ('user',)
    search_fields = ('user',)
    list_filter = ('user',)
    list_per_page = 25

admin.site.register(User)
admin.site.register(Profile, ProfileAdmin)





