from django.shortcuts import render
from .models import Account, Receipt, ExpenseCategory
from django.contrib.auth.decorators import login_required


@login_required
def receipt_list(request):
    user = request.user
    receipts = Receipt.objects.filter(purchaser=user)
    context = {
        "receipt_object": receipts
    }
    return render(request, "receipts/list.html", context)
