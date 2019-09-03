from django.db import models
from django.contrib.auth.models import User

class Records(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    name = models.TextField(max_length=64, default="")
    time = models.BigIntegerField(max_length=64, default="")
    content = models.TextField(max_length=2000, default="")
