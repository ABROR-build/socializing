from django.contrib import admin
from . import models


class AccountsAdmin(admin.ModelAdmin):
    list_display = ['username']


admin.site.register(models.Accounts, AccountsAdmin)
