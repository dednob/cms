from django.urls import path
from . import views

app_name = 'donate'

urlpatterns = [
    path('details/', views.details),
    path('create/', views.create),
    path('update/<int:pk>', views.update),
    path('delete/<int:pk>', views.delete),

]