from django.contrib import admin
from .models import BookModel,CategoryModel,BookReview
# Register your models here.
class BookAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('title',)}
    
admin.site.register(BookModel,BookAdmin)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
admin.site.register(CategoryModel,CategoryAdmin)

admin.site.register(BookReview)