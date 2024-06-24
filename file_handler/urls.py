from django.urls import path
from .views import * 

urlpatterns = [
    path('upload/', FileUploadView.as_view(), name='post'),
    path('get-csrf-token/', get_csrf_token_view, name='get_csrf_token'),

    path('data/', get_data),
    path('data/top10/', get_data_top10),
    path('data/buttontwo/', get_data_two),
    path('data/buttonthree/', get_data_three),
    path('labels/', get_labels),
    
]
