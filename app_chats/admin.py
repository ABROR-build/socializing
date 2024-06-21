from django.contrib import admin
from . import models


class MessagesAdmin(admin.ModelAdmin):
    list_display = ['sender', 'message', 'sent_time', 'receiver']


admin.site.register(models.Messages, MessagesAdmin)
