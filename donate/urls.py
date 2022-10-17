from django.urls import path
from . import views

app_name = 'donate'

urlpatterns = [
    path('details/', views.details),
    path('create/', views.create),
    path('update/<str:slugkey>', views.update),
    path('delete/<str:slug>', views.delete),

]