from django.db import models

class Job(models.Model):
    image = models.ImageField(upload_to='images/')
    summary = models.CharField(max_length=400)
    link = models.CharField(max_length=50, null=True)