from django.db import models

# Create your models here.

class Record(models.Model):

    creation_date = models.DateTimeField(auto_now_add=True)
