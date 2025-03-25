from django.contrib import admin
from .models import Author, Book

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'release_date')
    list_filter = ('author', 'release_date')
    search_fields = ('title', 'author__name', 'author__surname', 'release_date')

admin.site.register(Author)
admin.site.register(Book, BookAdmin)

# Register your models here.
