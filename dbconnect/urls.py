from django.urls import path
from . import views

urlpatterns = [
    path('check/', views.check_connection, name='check_connection'),
    path('reset/', views.reset_data, name='reset_data'),
    # ... other paths
]
