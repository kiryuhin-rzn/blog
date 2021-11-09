from rest_framework.response import Response
from rest_framework.views import APIView
from app_goods.models import Author, Book
from app_goods.serializers import AuthorSerializer, BookSerializer
from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin, UpdateModelMixin, RetrieveModelMixin, DestroyModelMixin
from django.db.models import Q


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 1
    page_size_query_param = 'page_size'
    max_page_size = 10


class AuthorList(ListModelMixin, CreateModelMixin, GenericAPIView):
    """Представление для получения списка авторов книг и добавления авторов книг в библиотеку."""
    serializer_class = AuthorSerializer
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        queryset = Author.objects.all()
        author_name = self.request.query_params.get('name')
        if author_name:
            queryset = queryset.filter(name=author_name)
        return queryset

    def get(self, request):
        return self.list(request)

    def post(self, request, format=None):
        return self.create(request)


class BookList(ListModelMixin, CreateModelMixin, GenericAPIView):
    """Представление для получения списка книг и добавления книг в библиотеку."""
    serializer_class = BookSerializer
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        queryset = Book.objects.all()
        book_title = self.request.query_params.get('title')
        author_name = self.request.query_params.get('author')
        book_pages = self.request.query_params.get('pages__gt')
        book_pages2 = self.request.query_params.get('pages__lt')
        book_pages3 = self.request.query_params.get('pages')
        #pages = self.request.query_params.get('pages')
        #pages = self.request.query_params.get('pages')
        #pages__lt = self.request.query_params.get('pages')
        #book_pages = Book.objects.get(

        if author_name:
            queryset = queryset.filter(author__name=author_name)
        if book_title:
            queryset = queryset.filter(title=book_title)
        if book_pages:
            queryset = queryset.filter(pages__gt=book_pages)
        if book_pages2:
            queryset = queryset.filter(pages__lt=book_pages2)
        if book_pages3:
            queryset = queryset.filter(pages=book_pages3)
        '''elif book_pages:
            queryset = queryset.filter(pages__lt=book_pages)
        elif book_pages:
            queryset = queryset.filter(pages=book_pages)'''
            #queryset = queryset.filter(pages__lt=book_pages)


        return queryset

    def get(self, request):
        return self.list(request)

    def post(self, request, format=None):
        return self.create(request)


class BookDetail(UpdateModelMixin, RetrieveModelMixin, DestroyModelMixin, GenericAPIView):
    """Представление для получения детальной информации о книге,
    а также ее редактирования и удаления."""
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


'''
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

'''