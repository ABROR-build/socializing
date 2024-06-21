from django.urls import path
from . import views


urlpatterns = [
    path('', views.ListChats.as_view(), name='rooms'),
    path('send_message/<int:account_id>/', views.SendMessages.as_view(), name='send_message'),
]
