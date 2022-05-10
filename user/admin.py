from django.contrib import admin
from .models import User


class UsersAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email',
                    'created_at', 'is_active', 'is_staff')
    list_display_links = ('id', 'username', 'email')
    search_fields = ('id', 'username', 'email')
    list_editable = ('is_staff',)
    list_filter = ('is_active', 'is_staff')


admin.site.register(User, UsersAdmin)
