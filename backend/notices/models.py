from django.db import models
from django.conf import settings

# Create your models here.
class notices(models.Model):
    title = models.CharField(max_length=255)
    content = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title