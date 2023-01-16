from django.contrib import admin
from .models import *


@admin.register(Post)
class FileUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'is_published', 'title', 'is_main')


admin.site.register(Tag)
admin.site.register(Block)
admin.site.register(Category)


