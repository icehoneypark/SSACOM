from django.db import models
from django.conf import settings

# Create your models here.
class faq(models.Model):
    title = models.CharField(max_length=255)
    content = models.CharField(max_length=255)

    def __str__(self):
        return self.title