
from django.urls import path
from .import views
 
app_name = 'reviews'

urlpatterns = [
    
    path('list/',views.review_list , name='getReview'),
    path('create/',views.create_review , name='createReview'),
    # path('update/<int:pk>',views.update_review , name='updateReview'),
    path('delete/<int:pk>',views.delete_review , name='deleteReview'),
    
     
]