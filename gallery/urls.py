from django.urls import path
from . import views

app_name = 'gallery'

urlpatterns = [
    path('list/', views.list),
    path('create/', views.upload),
    path('details/<str:slug>', views.gallery_detail),
    path('byCampaign/<str:slug>', views.gallery_by_camp),
    # path('byaow/<int:pk>', views.projects_by_aow),
    path('update/<str:slugkey'
         '>', views.update),
    path('delete/<str:slug>', views.delete),

]