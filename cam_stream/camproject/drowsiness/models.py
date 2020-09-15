from django.db import models
from django.contrib.auth.models import User

class Sound(models.Model) :
    title = models.CharField(max_length=100)
    alarm = models.FileField(upload_to="./sound", blank=True)



