from django.urls import path
from . import views

app_name = 'campaigns'

urlpatterns = [
    path('list/', views.list),
    path('create/', views.create),
    path('details/<int:pk>', views.campaign_detail),
    path('byproject/<int:pk>', views.campaigns_by_projects),
    path('update/<int:pk>', views.update),
    path('delete/<int:pk>', views.delete),
    

]