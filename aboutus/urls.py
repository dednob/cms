from django.urls import path
from . import views

app_name = 'aboutus'

urlpatterns = [
    path('view/', views.about_view),
    path('create/', views.update_aboutus),
    # path('delete/<int:pk>', views.delete),
    # path('detail/<int:pk>', views.about_details),
    # path('list/', views.list),
    
    # path('update/<int:pk>', views.update),
    # path('partialupdate/<int:pk>', views.partial_update),
    # path('active/toggle/<int:pk>', views.toggle_aboutus_active_status),
    

    path('team/list/', views.team_list),
    path('team/create/', views.team_create),
    path('team/update/<int:pk>', views.team_update),
    # path('partialupdate/<int:pk>', views.partial_update),
    path('team/delete/<int:pk>', views.team_delete),

]
