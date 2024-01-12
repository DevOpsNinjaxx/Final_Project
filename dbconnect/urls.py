from django.urls import path
from . import views

urlpatterns = [
    # Uncomment below to test application locally
#    path('check_sqlite/', views.check_connection_sqlite, name='check_connection_sqlite'),
    path('reset/', views.reset_data, name='reset_data'),
    path('check_rds/', views.check_connection_rds, name='check_connection_rds'),
    # ... other paths
]
