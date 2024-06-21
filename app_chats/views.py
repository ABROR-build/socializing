# global
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.db.models import Q
from django.core.exceptions import ObjectDoesNotExist

# local
from . import models
from app_accounts.models import Accounts
from .forms import SendMessagesForm


class ListChats(View):
    def get(self, request):
        accounts = Accounts.objects.all()
        context = {
            'accounts': accounts
        }
        return render(request, 'chats/list_accounts.html', context=context)


class SendMessages(View):
    def get(self, request, account_id):
        user = request.user
        account = get_object_or_404(Accounts, id=account_id)

        messages = models.Messages.objects.filter(
            Q(sender=user, receiver=account) | Q(sender=account, receiver=user)
        ).order_by('sent_time')
        send_message_form = SendMessagesForm()

        context = {
            'account': account,
            'messages': messages,
            'send_message_form': send_message_form

        }
        return render(request, 'chats/list_chats.html', context=context)

    def post(self, request, account_id):
        send_message_form = SendMessagesForm(request.POST, request.FILES)
        if send_message_form.is_valid():
            message = send_message_form.save(commit=False)
            message.sender = request.user
            try:
                receiver_account = Accounts.objects.get(id=account_id)
                message.receiver = receiver_account
                message.save()
                return redirect(request.META.get('HTTP_REFERER', '/'))
            except Accounts.ObjectDoesNotExist:
                pass
        else:
            context = {
                'send_message_form': send_message_form
            }
            return render(request, 'chats/list_chats.html', context=context)
