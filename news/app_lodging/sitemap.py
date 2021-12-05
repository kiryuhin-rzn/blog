from django.contrib.sitemaps import Sitemap
from app_lodging.models import Lodging, News
from django.contrib import sitemaps
from django.urls import reverse


class LodgingSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.9

    def items(self):
        return Lodging.objects.filter(is_published=True).all()

    def lastmod(self, obj: Lodging):
        return obj.published_at

class NewsSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.9

    def items(self):
        return News.objects.all()

    def lastmod(self, obj: News):
        return obj


class StaticViewSitemap(sitemaps.Sitemap):
    priority = 0.5
    changefreq = 'daily'

    def items(self):
        return ['contacts', 'about']

    def location(self, item):
        return reverse(item)