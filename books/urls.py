from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('books/', include('book_api.urls')),
]
