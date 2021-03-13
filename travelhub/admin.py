from django.contrib import admin
from .models import Country, City, Image, Asset, Category, Tag, Place, Comment, Reply

class ReplyInline(admin.StackedInline):
    model = Reply
    extra = 5


class CommentAdmin(admin.ModelAdmin):
    inlines = [ReplyInline]


class PostAdmin(admin.ModelAdmin):
    search_fields = ('name', 'slug')
    list_display = ['name', 'is_public', 'updated_at', 'created_at', 'title_len']
    list_filter = ['is_public', 'tags']
    ordering = ('-updated_at',)

    def title_len(self, obj):
        return len(obj.name)

    title_len.short_description = 'タイトルの文字数'

admin.site.register(Country, PostAdmin)
admin.site.register(City, PostAdmin)
admin.site.register(Image)
admin.site.register(Asset)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Place)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Reply)
