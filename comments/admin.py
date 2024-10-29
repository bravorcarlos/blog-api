from django.contrib import admin
from .models import Comment

# Register your models here.

class CommentAdmin(admin.ModelAdmin):
    list_display = ['short_content', 'user', 'post', 'created_at']
    
    def short_content(self, obj):
        return obj.content[:15] + '...' if len(obj.content) > 10 else obj.content
    
    short_content.short_description = 'Content'

admin.site.register(Comment, CommentAdmin)