from django.contrib import admin

from public.models import EarlyAccess


class EarlyAccessAdmin(admin.ModelAdmin):
    list_display = ('email_address', 'sign_up_date')


admin.site.register(EarlyAccess, EarlyAccessAdmin)
