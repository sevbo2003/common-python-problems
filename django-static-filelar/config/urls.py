from django.contrib import admin
from django.urls import path
from blog.views import Home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Home.as_view())
]
