from django.shortcuts import render, redirect
from .models import Receipt, ExpenseCategory, Account
from django.contrib.auth.decorators import login_required
from .forms import ReceiptForm, ExpenseCategoryForm, AccountForm


@login_required
def receipt_list(request):
    user = request.user
    receipts = Receipt.objects.filter(purchaser=user)
    context = {
        "receipt_object": receipts
    }
    return render(request, "receipts/list.html", context)


@login_required
def create_receipt(request):
    if request.method == "POST":
        form = ReceiptForm(request.POST)
        if form.is_valid():
            receipt = form.save(False)
            receipt.purchaser = request.user
            receipt.save()
            return redirect("home")
    else:
        form = ReceiptForm
    context = {
         "form": form
    }
    return render(request, "receipts/create.html", context)


def category_list(request):
    categories = ExpenseCategory.objects.filter(owner=request.user)
    context = {
        "categories": categories,
    }
    return render(request, "receipts/category_list.html", context)


def account_list(request):
    accounts = Account.objects.filter(owner=request.user)
    context = {
        "accounts": accounts
    }
    return render(request, "receipts/account_list.html", context)


@login_required
def create_category_list(request):
    if request.method == "POST":
        form = ExpenseCategoryForm(request.POST)
        if form.is_valid():
            category = form.save(False)
            category.owner = request.user
            category.save()
            return redirect("category_list")
    else:
        form = ExpenseCategoryForm
    context = {
        "form": form,
    }
    return render(request, "receipts/create_category.html", context)


@login_required
def create_account(request):
    if request.method == "POST":
        form = AccountForm(request.POST)
        if form.is_valid():
            account = form.save(False)
            account.owner = request.user
            account.save()
            return redirect("account_list")
    else:
        form = AccountForm
    context = {
        "form": form,
    }
    return render(request, "receipts/create_account.html", context)
