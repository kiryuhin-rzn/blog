from django.contrib.syndication.views import Feed
from django.db.models import QuerySet
from django.urls import reverse
from app_lodging.models import Lodging, News

class LatestLodgingFeed(Feed):
    title = "Police beat site news"
    link = "/sitenews/"
    description = "Updates on changes and additions to police beat central."

    def items(self) -> QuerySet:
        return Lodging.objects.order_by('-published_at')[:5]

    def item_title(self, item: Lodging) -> str:
        return item.name

    def item_description(self, item: Lodging) -> str:
        return item.description

    # item_link is only needed if NewsItem has no get_absolute_url method.
    def item_link(self, item: Lodging) -> str:
        return reverse('lodging_detail', args=[item.pk])


class LatestNewsFeed(Feed):
    title = "Бла бла бла"
    link = "/sitenews/"
    description = "Бла бла бла"

    def items(self) -> QuerySet:
        return News.objects.order_by('-date_publication')[:5]

    def item_title(self, item: News) -> str:
        return item.title

    def item_description(self, item: News) -> str:
        return item.text

    # item_link is only needed if NewsItem has no get_absolute_url method.
    def item_link(self, item: News) -> str:
        return reverse('news_detail', args=[item.pk])
