from django.contrib import admin
from accounts.models import Profile

# ds/ds


class ProfileAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_at'
    list_display = ['user', 'company_name', 'created_at', 'contact_person_name', 'created_at']
    search_fields = ['user', 'company_name', 'allowed_memberships']
    readonly_fields = ['created_at', 'updated_at']
    list_filter = ['created_at', 'allowed_memberships']


admin.site.register(Profile, ProfileAdmin)
