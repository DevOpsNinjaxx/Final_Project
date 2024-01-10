from django.shortcuts import redirect, render
from django.http import HttpResponseRedirect
from .models import ConnectionStatus
import sqlite3

def check_connection(request):
    if request.method == 'POST':
        # Check the database connection
        try:
            conn = sqlite3.connect('./database.sqlite3')
            connected = True
            conn.close()
        except sqlite3.Error:
            connected = False
        
        # Create a new entry when the button is clicked
        ConnectionStatus.objects.create(connected=connected)
        
        # Redirect to avoid form resubmission on refresh
        return HttpResponseRedirect('/check/')

    # Retrieve all statuses from the database
    statuses = ConnectionStatus.objects.all().order_by('-timestamp')
    
    return render(request, 'dbconnect/index.html', {'statuses': statuses})

def reset_data(request):
    # Delete all entries from the ConnectionStatus model
    ConnectionStatus.objects.all().delete()
    # Redirect back to the check_connection view after reset
    return redirect('check_connection')
