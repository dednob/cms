from django.urls import path
from . import views

app_name = 'projects'

urlpatterns = [
    path('list/', views.list),
    path('create/', views.create),
    path('details/<int:pk>', views.project_detail),
    path('byaow/<int:pk>', views.projects_by_aow),
    path('update/<int:pk>', views.update),
    path('delete/<int:pk>', views.delete),

]