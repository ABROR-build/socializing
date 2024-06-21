from django.db import models
from app_accounts.models import Accounts


class Messages(models.Model):
    sender = models.ForeignKey(Accounts, on_delete=models.CASCADE, related_name='message_sender')
    message = models.TextField()
    image = models.ImageField(upload_to='sent/', null=True, blank=True)
    sent_time = models.TimeField(auto_now=True)
    receiver = models.ForeignKey(Accounts, on_delete=models.CASCADE, related_name='message_receiver')

    class Meta:
        db_table = "Messages"
