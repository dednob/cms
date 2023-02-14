from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('view/', views.home_view),
    path('detail/<int:pk>', views.home_details),

    path('list/', views.home_list),
    path('active/toggle/<int:pk>', views.toggle_active_status),
    path('create/', views.create_home),
    path('experience/', views.experience_details),
    path('update/<int:pk>', views.update),
    path('delete/<int:pk>', views.delete_home),
    path('count/', views.work_list_count),

    path('achievement/view/', views.achievement_view),
    path('achievement/detail/<int:pk>', views.achievement_details),
    path('achievement/list/', views.achievement_list),
    path('achievement/active/toggle/<int:pk>', views.toggle_achievement_active_status),
    path('achievement/create/', views.create_achievement),
    # path('achievement/experience/', views.experience_details),
    path('achievement/update/<int:pk>', views.update_achievement),
    # path('partialupdate/<int:pk>', views.partial_update_home),
    path('achievement/delete/<int:pk>', views.delete_achievement),

]
