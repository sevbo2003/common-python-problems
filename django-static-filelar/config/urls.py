from django.contrib import admin
from django.urls import path
from blog.views import Home
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Home.as_view())
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)
