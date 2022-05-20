from django.db import models
from django.conf import settings

class Temp(models.Model) :

    temp = models.TextField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    hour = models.TextField()

    def __str__(self):
            return self.temp
