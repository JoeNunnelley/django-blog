from django.contrib import admin
from blogging.models import Post, Category


class CategoryAdmin(admin.ModelAdmin):
    exclude = ('posts',)


class CategoryInline(admin.TabularInline):
    model = Category.posts.through


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'text', 'author',  'created_date', 'published_date')
    list_filter = ('created_date',)
    date_hierarchy = 'created_date'
    ordering = ('-created_date',)
    fields = ('title', 'text', 'author', )
    inlines = [ CategoryInline, ]
    exclude = ('posts',)


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
