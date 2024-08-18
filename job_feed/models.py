from django.db import models
#from django.utils import timezone
#from django.contrib.auth.models import User


# Create your models here.
class JobPost(models.Model):
    name=models.CharField(max_length=100)
    type=models.CharField(max_length=100)
    title=models.CharField(max_length=300)
    description=models.TextField(max_length=1000)
    fulldescription=models.TextField(max_length=1000)
    work=models.TextField(max_length=1000)
    email=models.EmailField(max_length=100)
    address = models.CharField(max_length=500)
    sector=models.TextField(max_length=1000)
    experience=models.CharField(max_length=100)
    position=models.CharField(max_length=100)
    date=models.DateField()

    def __str__(self):
        return self.name



class JobApply(models.Model):
    letter=models.TextField(max_length=1000)
    
    def __str__(self):
        return self.letter