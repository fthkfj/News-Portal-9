from django.contrib import admin
from .models import Author, Category, Post, PostCategory, Comment


class AuthorAdmin(admin.ModelAdmin):
    list_display = ['users', 'rating']
    list_editable = ['rating']


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['category']


class PostAdmin(admin.ModelAdmin):
    list_display = ['authors', 'CategoryType', 'DateCreation', 'ratings']
    list_editable = ['CategoryType', 'ratings']


class PostCategoryAdmin(admin.ModelAdmin):
    list_display = ['PostTrough', 'CategoryTrough']


class CommentAdmin(admin.ModelAdmin):
    list_display = ['CommentPost', 'CommentUser', 'text', 'DateCreation', 'ratings']


admin.site.register(Author, AuthorAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(PostCategory, PostCategoryAdmin)
admin.site.register(Comment, CommentAdmin)
