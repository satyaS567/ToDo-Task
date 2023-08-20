from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Tasklist(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=40)
    description = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.title