from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('detail/', views.home_details),
    path('list/', views.home_list),
    path('active/toggle/<int:pk>', views.toggle_active_status),
    path('create/', views.create_home),
    path('experience/', views.experience_details),
    path('update/<str:slugkey>', views.update),
    # path('partialupdate/<int:pk>', views.partial_update_home),
    path('delete/<str:slug>', views.delete_home),

]
