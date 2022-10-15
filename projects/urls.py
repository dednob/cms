from django.urls import path
from . import views

app_name = 'projects'

urlpatterns = [
    path('projects/', views.list),
    path('create/', views.create),
    path('update/<int:pk>', views.update),
    path('partialupdate/<int:pk>', views.partial_update),
    path('delete/<int:pk>', views.delete),

]