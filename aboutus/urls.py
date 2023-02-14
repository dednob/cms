from django.urls import path
from . import views

app_name = 'aboutus'

urlpatterns = [
    path('list/', views.list),
    path('create/', views.create),
    path('update/<int:pk>', views.update),
    # path('partialupdate/<int:pk>', views.partial_update),
    path('delete/<int:pk>', views.delete),

    path('team/list/', views.team_list),
    path('team/create/', views.team_create),
    path('team/update/<int:pk>', views.team_update),
    # path('partialupdate/<int:pk>', views.partial_update),
    path('team/delete/<int:pk>', views.team_delete),

]
