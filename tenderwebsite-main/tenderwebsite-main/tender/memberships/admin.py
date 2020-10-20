from django.contrib import admin
from .models import Membership, UserMembership, Subscription


class UserMembershipAdmin(admin.ModelAdmin):
    date_hierarchy = 'membership_created_at'
    list_display = ['user', 'membership', 'membership_until', 'membership_created_at']
    search_fields = ['user', 'membership']
    readonly_fields = ['membership_created_at', 'membership_until']
    list_filter = ['membership_until', 'membership']
    list_editable = ['membership_until', 'membership']


admin.site.register(Membership)
admin.site.register(UserMembership, UserMembershipAdmin)
admin.site.register(Subscription)

