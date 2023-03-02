from django.shortcuts import render
from .models import Account, Receipt, ExpenseCategory


def receipt_list(request):
    receipts = Receipt.objects.all()
    context = {
        "receipt_object": receipts
    }
    return render(request, "receipts/list.html", context)
