from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('detail/', views.home_details),
    path('create/', views.create_home),
    path('update/<str:slugkey>', views.update),
    # path('partialupdate/<int:pk>', views.partial_update_home),
    path('delete/<str:slug>', views.delete_home),

]
