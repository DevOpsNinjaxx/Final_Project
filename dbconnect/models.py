from django.db import models

class ConnectionStatus(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    connected = models.BooleanField(default=False)
