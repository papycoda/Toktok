from django.contrib import admin
from .models import Toks

# Register your models here.

class TokAdmin(admin.ModelAdmin):
    list_display = ('id', 'created_by', 'tok', 'created_at')
    list_display_links = ('id', 'created_by')
    search_fields = ('created_by', 'tok')
    list_filter = ('created_by', 'tok')
    list_per_page = 25


admin.site.register(Toks, TokAdmin)