from django.contrib import admin
from .models import Invoice,InvoiceDetail
# Register your models here.

@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    list_display = ('invoice_number', 'customer_name', 'date')
    search_fields = ('invoice_number', 'customer_name',)
    list_filter = ('date',)

@admin.register(InvoiceDetail)
class InvoiceDetailAdmin(admin.ModelAdmin):
    list_display = ('invoice', 'description', 'quantity', 'unit_price', 'line_total')
    search_fields = ('description',)
    list_filter = ('invoice',)
    