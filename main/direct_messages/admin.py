from django.contrib import admin
from .models import DirectMessages

# Register your models here.
class DirectMessagesAdmin(admin.ModelAdmin):
    list_display = ('sender', 'receiver', 'message', 'created_at')
    

admin.site.register(DirectMessages, DirectMessagesAdmin)


