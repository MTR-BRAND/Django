from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from django.conf import settings
from django.conf.urls.static import static

# Simple view for the home page
def home(request):
    return HttpResponse("<h1>Welcome to the E-commerce Site</h1>")  # Basic home page response

urlpatterns = [
    path('', home, name='home'),  # Root URL pattern
    path('admin/', admin.site.urls),
    path('products/', include('products.urls')),  # Include product URLs
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
