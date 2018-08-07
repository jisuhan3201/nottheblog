from django.contrib import admin
from . import models

# Register your models here.

@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):

    list_display_links = (
        "title",
    )
    search_fields = (
        "title",
        "sub_title",
    )
    list_filter = (
        "title",
        "user",
        "create_at",
        "updated_at",
    )
    list_display = (
        "title",
        "sub_title",
        "intro",
        "image",
        "content",
        "user",
        "create_at",
        "updated_at",
    )


@admin.register(models.Comment)
class CommentAdmin(admin.ModelAdmin):

    list_display = (
        "message",
        "post",
        "user",
        "create_at",
        "updated_at",
    )
    list_display_links = (
        "message",
    )
    search_fields = (
        "post",
        "message",
    )
    list_filter = (
        "message",
        "user",
        "create_at",
        "updated_at",
    )


@admin.register(models.Reply)
class ReplyAdmin(admin.ModelAdmin):

    list_display_links = (
        "content",
    )
    search_fields = (
        "content",
        "user",
    )
    list_filter = (
        "content",
        "user",
        "create_at",
        "updated_at",
    )
    list_display = (
        "content",
        "comment",
        "user",
    )



@admin.register(models.Star)
class StarAdmin(admin.ModelAdmin):

    search_fields = (
        "user",
        "post",
    )
    list_filter = (
        "user",
        "post",
        "create_at",
        "updated_at",
    )
    list_display = (
        "user",
        "post",
        "create_at",
        "updated_at",
    )
