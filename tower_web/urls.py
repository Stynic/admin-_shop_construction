from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'', include('main_page.urls')),
    url(r'^blog', include('blog.urls')),
    url(r'^gallery/', include('gallery.urls')),
    url(r'^admin/', admin.site.urls),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
