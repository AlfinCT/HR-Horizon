from django.db import models

# Create your models here.
class Employe(models.Model):
    name=models.CharField(max_length=250)
    last_name=models.CharField(max_length=250)
    age=models.IntegerField()
    post=models.CharField(max_length=250)
    salary=models.IntegerField()

    def __str__(self):
        return self.name