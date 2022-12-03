from django.contrib import admin
from .models import *

# Register your models here.
class CommentsInline(admin.StackedInline):
    model = TokComment
    can_delete = True
    verbose_name_plural = 'Comments'

class TokAdmin(admin.ModelAdmin):
    inlines = [CommentsInline,]
    list_display = ('id', 'created_by', 'tok', 'created_at')
    list_display_links = ('id', 'created_by')
    search_fields = ('created_by', 'tok')
    list_filter = ('created_by', 'tok')
    list_per_page = 25


admin.site.register(Toks, TokAdmin)