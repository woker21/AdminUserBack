
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('DjangoFirstApp/', include('DjangoFirstApp.urls')),
    path('admin/', admin.site.urls),
]
