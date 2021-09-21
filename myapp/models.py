from django.db import models

# Create your models here.
class Photo(models.Model):
    ph = models.ImageField(upload_to = 'myphoto')
    date = models.DateTimeField(auto_now_add=True)
