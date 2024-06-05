from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import Transaction

class TransactionAdmin(ModelAdmin):
    list_display = [
        'transaction_no', 
        'phone_number', 
        'checkout_request_id', 
        'description',
        'amount',
        'status',
        'receipt_no',
        'created'
    ]


admin.site.register(Transaction, TransactionAdmin)