from django.urls import path
from .views import * 

urlpatterns = [
    path('upload/', FileUploadView.as_view(), name='post'),
    path('get-csrf-token/', get_csrf_token_view, name='get_csrf_token'),
    path('user-projects/', user_projects, name='user-projects'),
    path('user-project-data/<str:project_title>/', user_project_data, name='user-project-data'),
    path('user-project/<str:project_title>/', user_project_delete, name='user-project-data-delete'),

    
    path('save-shapes/<str:project_title>/', save_shapes_view, name='save_shapes'),
    path('load-shapes/<str:project_title>/', load_shapes, name='load_shapes'),

    

  
]
