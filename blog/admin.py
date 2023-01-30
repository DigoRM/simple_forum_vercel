from django.contrib import admin
from blog.models import Post, Comment, Category, Customer

class CommentItemInline(admin.TabularInline):
    model = Comment
    raw_id_fields = ['post']

class PostAdmin(admin.ModelAdmin):
    search_fields = ['title', 'intro', 'body']
    list_display = ['title','slug','created_at','category', 'status']
    list_filter = ['category', 'created_at','status']
    inlines = [CommentItemInline]
    
class CategoryAdmin(admin.ModelAdmin):
    search_fields = ['title']
    list_display = ['title']
    prepopulated_fields = {'slug':('title',)}
    
class CommentAdmin(admin.ModelAdmin):
    search_fields = ['name', 'post', 'created_at']


# Register your models here.
admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Customer)