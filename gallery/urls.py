from django.urls import path
from . import views

app_name = 'gallery'

urlpatterns = [
    path('list/', views.list),
    path('create/', views.upload),
    path('details/<int:pk>', views.gallery_detail),
    path('byCampaign/<int:pk>', views.gallery_by_camp),
    # path('byaow/<int:pk>', views.projects_by_aow),
    path('update/<int:pk>', views.update),
    path('delete/<int:pk>', views.delete),

]