from django.urls import path
from . import views

app_name = 'areaofwork'

urlpatterns = [
    path('list/', views.aow_list),
    path('detail/<int:pk>', views.aow_detail),
    path('create/', views.create),
    path('update/<int:pk>', views.update),
    path('delete/<int:pk>', views.delete),

]