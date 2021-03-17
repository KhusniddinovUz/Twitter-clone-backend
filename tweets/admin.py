from django.contrib import admin
from .models import TweetModel, Comment


@admin.register(TweetModel)
class TweetModelAdmin(admin.ModelAdmin):
    list_display = ('username',)
    search_fields = ('username', 'text')
    ordering = ('created_at',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('owner', 'body')
    ordering = ('-created',)
