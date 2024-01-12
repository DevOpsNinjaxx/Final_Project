from django.shortcuts import render, redirect
from .models import ConnectionStatus
from django.db import connection

def check_connection_rds(request):
    if request.method == 'POST':
        # Check the database connection only when the form is submitted
        try:
            with connection.cursor() as cursor:
                cursor.execute("SELECT 1")
            connected = True
        except Exception as e:
            connected = False

        # Create a new entry in the ConnectionStatus model
        ConnectionStatus.objects.create(connected=connected)

    # Retrieve all statuses from the database
    statuses = ConnectionStatus.objects.all().order_by('-timestamp')

    return render(request, 'dbconnect/index.html', {'statuses': statuses})

def reset_data(request):
    # Delete all entries from the ConnectionStatus model
    ConnectionStatus.objects.all().delete()
    # Redirect back to the check_connection_rds view after reset
    return redirect('check_connection_rds')
