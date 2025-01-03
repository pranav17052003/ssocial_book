from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


#Register your models here
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    fieldsets = UserAdmin.fieldsets + (
        ('Additional Info', {'fields': ('public_visibility', 'age', 'birth_year', 'address')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Additional Info', {'fields': ('public_visibility', 'birth_year', 'address')}),
    )

admin.site.register(CustomUser, CustomUserAdmin)
