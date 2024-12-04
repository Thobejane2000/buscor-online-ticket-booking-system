# admins.py
from django.contrib import admin
from .models import Message, Ticket
admin.site.register(Message)
#admin.site.register(Ticket)

@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ('ticket_number', 'user', 'destination', 'pickup', 'distance', 'rate')
    fields = ('user', 'ticket_number', 'qr_code', 'destination', 'pickup', 'distance')
