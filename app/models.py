from django.db import models

# Create your models here.
from django.urls import reverse
class School(models.Model):
    name=models.CharField(max_length=100)
    principal=models.CharField(max_length=100)
    location=models.CharField(max_length=100)

    def get_absolute_url(self):
        return reverse('detailview',kwargs={'pk':self.pk})

    def __str__(self) -> str:
        return self.name
    

class Student(models.Model):
    name=models.ForeignKey(School,on_delete=models.CASCADE,related_name='students')
    sname=models.CharField(max_length=100)
    age=models.IntegerField()

    