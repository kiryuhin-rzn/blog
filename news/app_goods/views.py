from django.shortcuts import render
from app_goods.models import Item
from .forms import UploadNewsForm
from django.http import HttpResponse
import csv
from django.forms import DecimalField
from decimal import Decimal
from csv import reader


def items_list(request):
    items = Item.objects.all()
    return render(request, 'app_goods/goods_list.html', {'items_list': items})


def update_news(request):
    if request.method == 'POST':
        form = UploadNewsForm(request.POST, request.FILES)
        if form.is_valid():
            price_file = form.cleaned_data['file'].read()
            price_str = price_file.decode('utf-8').split('\n')
            #csv_reader = reader(price_str, delimiter=",", quotechar='"')
            for row in price_str[: -1]:
                tmp = Item.objects.create()
                tmp.title = row.split(';')[0]
                tmp.text = row.split(';')[1]
                tmp.save()
            return HttpResponse(content='Цены были успешно обновлены', status=200)
    else:
        form = UploadNewsForm()

    context = {
	    'form': form
	}
    return render(request, 'app_goods/upload.html', context=context)