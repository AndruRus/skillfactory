from django.contrib import admin

from core.models import Book


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    pass
