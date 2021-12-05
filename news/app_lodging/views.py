from django.views import generic
from app_lodging.models import Lodging, News
from django.views.generic.base import TemplateView
from django.views.generic import DetailView


class LodgingListView(generic.ListView):
    model = Lodging
    context_object_name = 'lodging_list'
    queryset = News.objects.order_by('-date_publication')


class LodgingDetailView(DetailView):
    model = Lodging
    template_name = "app_lodging/lodging_detail.html"


class AboutView(TemplateView):

    template_name = "app_lodging/about.html"

    def get_context_data(self, **kwargs):
        context = super(AboutView, self).get_context_data(**kwargs)
        context['name'] = 'Сайт продажи жилья "Пентхаус"'
        context['description'] = 'Самый лучший сайт для продажи и покупки жилья'
        return context


class ContactsView(TemplateView):

    template_name = "app_lodging/contacts.html"

    def get_context_data(self, **kwargs):
        context = super(ContactsView, self).get_context_data(**kwargs)
        context['address'] = 'г. Москва, ул. Ленина, д. 59'
        context['telephone'] = '8(800)352-45-89'
        context['e_mail'] = 'salelodging@gmail.com'
        return context


class NewsListView(generic.ListView):
    model = News
    context_object_name = 'news_list'


class NewsDetailView(DetailView):
    model = News
    template_name = "app_lodging/news_detail.html"
