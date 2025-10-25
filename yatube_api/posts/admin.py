from django.contrib import admin
from .models import Post, Group, Comment, Follow

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'text', 'pub_date', 'author', 'group')
    list_filter = ('pub_date', 'author', 'group')
    search_fields = ('text',)
    empty_value_display = '-пусто-'

@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug', 'description')
    search_fields = ('title', 'description')
    empty_value_display = '-пусто-'

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'post', 'author', 'text', 'created')
    list_filter = ('created', 'author')
    search_fields = ('text',)
    empty_value_display = '-пусто-'

@admin.register(Follow)
class FollowAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'following')
    list_filter = ('user', 'following')
    empty_value_display = '-пусто-'