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

class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'profile'

class UserAdmin(admin.ModelAdmin):
    inlines = [ProfileInline, ]
    list_display = ('id', 'username', 'email', 'first_name', 'last_name', 'created_at',)
    list_display_links = ('id', 'username',)
    search_fields = ('username', 'email', 'first_name', 'last_name',)
    list_filter = ('username', 'email', 'first_name', 'last_name',)
    list_per_page = 25


admin.site.register(User, UserAdmin)





