from django.db import models


# Create your models here.
class user(models.Model):
    email=models.EmailField()
    password1=models.CharField(max_length=10)
    username=models.CharField(max_length=220)
    # adress=models.CharField(max_length=255)
    def __str__(self):
        return self.email
    

