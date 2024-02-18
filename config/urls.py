from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, include
from django.contrib.sitemaps.views import sitemap

from post.sitemaps import PostSitemap

sitemaps = {
    'post': PostSitemap
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('post.urls')),
    path('aut/', include('account.urls')),
    path('social-auth/', include('social_django.urls', namespace='social')),
    path('api/', include('api.urls')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap')

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)