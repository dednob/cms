from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('home/', views.home_details),
    path('create/', views.create_home),
    path('update/<int:pk>', views.update_home),
    path('partialupdate/<int:pk>', views.partial_update_home),
    path('delete/<int:pk>', views.delete_home),

]
