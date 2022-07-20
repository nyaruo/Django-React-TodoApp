from django.contrib import admin
# 追加
from .models import Todo
# 追加
class TodoAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'completed')

# Register your models here.

# 追加
admin.site.register(Todo, TodoAdmin)