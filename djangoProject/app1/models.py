from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class post(models.Model):
    title=models.CharField(max_length=50)
    author=models.CharField(max_length=20)
    date=models.DateTimeField(default=timezone.now)
    content=models.CharField(max_length=250)
    
    class Meta:
     ordering = ('-date',)

    def __str__(self):
      return self.author
