from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('permission/', include('permission.urls')),
    path('home/', include('home.urls')),
    path('areaofwork/', include('areaofwork.urls')),
    path('projects/', include('projects.urls')),


]
