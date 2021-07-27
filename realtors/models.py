from django.db import models

# Create your models here.

class Realtor(models.Model):
    name = models.CharField(max_length=120)
    photo = models.ImageField(upload_to='realtors' )
    description =models.TextField(blank=True)
    phone = models.CharField(max_length=13)
    email=models.CharField(max_length=30)
    is_mvp=models.BooleanField(default=False)
    hire_date = models.DateTimeField(null=True,blank=True)

    def __str__(self):
        return self.name 