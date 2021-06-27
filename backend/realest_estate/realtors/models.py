from django.db import models
from datetime import datetime

class Realtor(models.Model):
    name = models.CharField(max_length=200)
    photo = models.ImageField(upload_to = 'photos/%y/%m/%d/')
    description = models.TextField(blank=True)
    phone = models.CharField(max_length=23)
    email = models.EmailField(max_length=180)
    top_seller = models.BooleanField(default=False)
    date_hired = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.name

