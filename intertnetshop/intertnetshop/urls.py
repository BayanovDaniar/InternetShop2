
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('product', include('productpage.urls')),
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('item', include('pageitem.urls')),
    path('reg', include('pageregistration.urls')),
    path('lovers', include('pagelovers.urls')),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
