from django.db import models
from django.conf import settings

class temp(models.Model) :

    temp = models.TextField()
    message = models.TextField()

    def __str__(self):
            return self.temp