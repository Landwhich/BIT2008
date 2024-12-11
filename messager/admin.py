from django.contrib import admin
from .models import Text

@admin.register(Text)
class ChatMessageAdmin(admin.ModelAdmin):
    list_display = ('room', 'content', 'date')

# Register your models here.
