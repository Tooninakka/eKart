from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account
# Register your models here.

class AccountAdmin(UserAdmin):
    list_display = ('email', 'firstname', 'lastname', 'username', 'date_joined', 'last_login', 'is_staff', 'is_active', 'is_admin', 'is_superuser',)
    list_display_links = ('email', 'firstname', 'lastname', )
    search_fields = ('email', 'firstname',' lastname', )
    readonly_fields = ('date_joined', 'last_login', )
    ordering = ('-date_joined', )
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(Account, AccountAdmin)
