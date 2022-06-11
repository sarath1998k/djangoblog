from django.contrib import admin
from .models import Category,Blog,Comment
# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name','slug','image']
    prepopulated_fields ={'slug':('name',)}
admin.site.register(Category,CategoryAdmin)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['name','slug','image','desc','created','updated']
    list_editable = ['image','desc']
    list_per_page = 20
    prepopulated_fields ={'slug':('name',)}
admin.site.register(Blog,BlogAdmin)
admin.site.register(Comment)