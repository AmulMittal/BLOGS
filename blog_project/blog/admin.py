from django.contrib import admin
from .models import Post, Comment

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published_date')
    search_fields = ('title', 'content', 'author__username')

class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'author', 'created_date')
    search_fields = ('post__title', 'author', 'text')

admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
