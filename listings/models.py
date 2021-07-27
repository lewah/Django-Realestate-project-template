from realtors.models import Realtor
from django.db import models

# Create your models here.


class Listing(models.Model):
    PROPTYPE = [
        ('House','House'),
        ('Land','Land'),
        ('Office','Office')
    ]
    PROPSTATUS =[
        ('Sale','sale'),
        ('Rent','rent')
    ]
    COUNTIES =[ 
    ('Nairobi', 'Nairobi'),
    ('Mombasa', 'Mombasa'),
    ('Lamu', 'Lamu'),
    ('Kwale', 'Kwale'),
    ('Kilifi', 'Kilifi'),
    ('Kiambu', 'Kiambu'),
    ('Nakuru', 'Nakuru'),
    ('Tana River' , 'Tana River'),
    ('Taita/Taveta' ,'Taita/Taveta'),
    ('Garissa ','Garissa '),
    ('Wajir ','Wajir '),
    ('Mandera','Mandera'),
    ('Marsabit','Marsabit'),
    ('Isiolo','Isiolo'),
    ('Meru','Meru'),
    ('Tharaka-Nithi','Tharaka-Nithi'),
    ('Embu','Embu'),
    ('Kitui','Kitui'),
    ('Machakos','Machakos'),
    ('Makueni','Makueni'),
    ('Nyandarua','Nyandarua'),
    ('Nyeri','Nyeri'),
    ('Kirinyaga','Kirinyaga'),
    ('Muranga','Muranga'),
    ('Turkana','Turkana'),
    ('West Pokot','West Pokot'),
    ('Samburu','Samburu'),
    ('Trans Nzoia','Trans Nzoia'),
    ('Uasin Gishu','Uasin Gishu'),
    ('Elgeyo/Marakwet','Elgeyo/Marakwet'),
    ('Nandi','Nandi'),
    ('Baringo','Baringo'),
    ('Laikipia','Laikipia'),
    ('Nakuru','Nakuru'),
    ('Narok','Narok'),
    ('Kajiado','Kajiado'),
    ('Kericho','Kericho'),
    ('Bomet','Bomet'),
    ('Kakamega','Kakamega'),
    ('Vihiga','Vihiga'),
    ('Bungoma','Bungoma'),
    ('Busia','Busia'),
    ('Siaya','Siaya'),
    ('Kisumu','Kisumu'),
    ('Homa Bay','Homa Bay'),
    ('Migori','Migori'),
    ('Kisii','Kisii'),
    ('Nyamira','Nyamira'),
    ]

    realtor = models.ForeignKey(Realtor,on_delete=models.CASCADE)
    title = models.CharField(max_length=120)
    address = models.CharField(max_length=60)
    area = models.CharField(max_length=20)
    county =  models.CharField(max_length=20,choices=COUNTIES,default='Kiambu')  #choices
    zipcode = models.CharField(max_length=13)
    description =models.TextField(blank=True)
    price = models.CharField(max_length=20)
    bedrooms = models.CharField(max_length=20) 
    bathrooms = models.CharField(max_length=20)
    garage = models.CharField(max_length=20)
    sqft = models.CharField(max_length=20)
    lot_size = models.CharField(max_length=20)
    property_type = models.CharField(max_length=10,choices=PROPTYPE,default='HS')   #choices: house,office,land
    status = models.CharField(max_length=10,choices=PROPSTATUS,default='RNT')  # choices sale,rent
    photo_main = models.ImageField(upload_to='listings')
    photo_1 = models.ImageField(upload_to='listings',blank=True)
    photo_2 = models.ImageField(upload_to='listings',blank=True)
    photo_3 = models.ImageField(upload_to='listings',blank=True)
    photo_4 = models.ImageField(upload_to='listings',blank=True)
    photo_5 = models.ImageField(upload_to='listings',blank=True)
    photo_6 = models.ImageField(upload_to='listings',blank=True)
    is_published = models.BooleanField(default=False)
    list_date = models.DateTimeField(null=True,blank=True)

    def __str__(self):
        return self.title


