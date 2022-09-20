from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


UserAdmin.fieldsets[2][1]['fields'] = (
    'is_active',
    'is_staff',
    'is_superuser',
    'is_author',
    'special_user',
    'groups',
    'user_permissions','photo'

)
UserAdmin.list_display += ('is_author','is_special_user')
UserAdmin.list_display_links += ('username','email')
admin.site.register(User,UserAdmin)


