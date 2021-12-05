"""news URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from app_news import views as app_news_views
import debug_toolbar
from django.contrib.sitemaps.views import sitemap
from app_lodging.sitemap import LodgingSitemap, StaticViewSitemap


sitemaps = {
    'lodging': LodgingSitemap,
    #'news': NewsSitemap,
    'static': StaticViewSitemap,
}

schema_view = get_schema_view(
    openapi.Info(
        title='Items API',
        default_version='v1',
        description='Описание проекта',
        terms_of_service='https://www.google.com/policies/terms',
        contact=openapi.Contact(email='admin@company.local'),
        license=openapi.License(name=''),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('admin/doc/', include('django.contrib.admindocs.urls')),
    path('admin/', admin.site.urls),
    path('', include('app_news.urls')),
    path('users/', include('app_users.urls')),
    path('market/', include('app_market.urls')),
    #path('goods/', include('app_goods.urls')),
    path('i18n', include('django.conf.urls.i18n')),
    path('api/', include('app_goods.urls')),
    path('sample/', app_news_views.sample_view),
    path('__debug__/', include(debug_toolbar.urls)),
    path('swagger', schema_view.with_ui('swagger', cache_timeout=0), name='shema-swagger-ui'),
    path('lodging/', include('app_lodging.urls')),
    path('rss/', include('app_rss.urls')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


'''urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns'''
