from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from stores import models
from .forms import StoreItemForm


def get_store_items(request):
    store_items: list[models.StoreItem] = list(models.StoreItem.objects.all())
    context = {
        "store_items": store_items,
    }
    return render(request, "store_item_list.html", context)

# def create_store_item(models.Model):
def create_store_item(request):
    form = StoreItemForm()

    if request.method == 'POST':
        form = StoreItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("store-item-list")

    context = {
        'form': form,
    }

    return render(request, "create-store-item.html", context)

# IN VIEW FUNCTIONS THERE SHOULD ALWAYS BE A REQUEST
# IN MODELS WE'LL USE MODELS.MODEL BECAUSE WE'RE CREATING A BLUEPRINT FOR THE DATA

def update_store_item(request, item_id):
    store_item = models.StoreItem.object.get(id=item_id)
    form = StoreItemForm(instance=store_item)

    if request.method == 'POST':
        form = StoreItemForm(request.POST, instance=store_item())
        if form.is_valid():
            form.save()
            return redirect("create-store-item")

    context = {
        'forms': form,
        'store_item': store_item
    }

    return render(request, 'update_store_item.html', context)

def delete_store_item(request, item_id):
    store_item = store_item.objects.get(id=item_id)
    store_item.delete()
    return redirect("delete-store-item")