from django.urls import path
from . import views

app_name = 'projects'

urlpatterns = [
    path('list/', views.list),
    path('create/', views.create),
    path('details/<str:slug>', views.project_detail),
    path('byaow/<str:slug>', views.projects_by_aow),
    path('update/<str:slugkey>', views.update),
    path('delete/<str:slug>', views.delete),
    path('featured/', views.featured_project),

]