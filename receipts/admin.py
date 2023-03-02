from django.contrib import admin
from .models import Receipt, Account, ExpenseCategory


@admin.register(ExpenseCategory)
class ExpenseCateogyAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "owner",
    )


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "number",
        "owner",
    )


@admin.register(Receipt)
class ReceiptAdmin(admin.ModelAdmin):
    list_display = (
        "vendor",
        "total",
        "tax",
        "date",
    )
