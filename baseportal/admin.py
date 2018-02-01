from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from baseportal.models import PublishedJournal
# Register your models here.

admin.site.site_header = 'Ejournal administration'

admin.site.unregister(User)

@admin.register(User)
class MyUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_active', 'is_staff')
    actions = ['activate_user', 'deactivate_user']

    def activate_user(self, request, queryset):
        queryset.update(is_active=True)
    activate_user.short_description = "Activate selected Users"

    def deactivate_user(self, request, queryset):
        queryset.update(is_active=False)
    deactivate_user.short_description = "Deactivate selected Users"

admin.site.register(PublishedJournal)
