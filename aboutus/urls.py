from django.urls import path
from . import views

app_name = 'aboutus'

urlpatterns = [
    path('aboutus/', views.list),
    path('create/', views.create),
    path('update/<str:slug>', views.update),
    # path('partialupdate/<int:pk>', views.partial_update),
    path('delete/<str:slug>', views.delete),

]
