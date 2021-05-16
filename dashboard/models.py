from django.db import models
from django.contrib.auth.models import User
from django_clamd import validators
from django_clamd.validators import validate_file_infection
from django_cryptography.fields import encrypt

# Create your models here.
class Profile(models.Model):
    profile_image = models.ImageField(upload_to="profile",validators=[validate_file_infection])
    location = encrypt(models.CharField(max_length=200))
    profession = encrypt(models.CharField(max_length=200))
    mobile = encrypt(models.BigIntegerField())
    user = models.OneToOneField(User,on_delete=models.CASCADE)

class Resource(models.Model):
    user = models.ForeignKey(User,on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=50,default='')
    upload = models.FileField(upload_to='resources',validators=[validate_file_infection])
    description = models.CharField(max_length=400)
    branch = models.CharField(choices=(('ALL',"ALL"),('ECE','ECE'),('CSE','CSE'),('MECH','MECH'),("CIVIL","CIVIL"),('OTHER','OTHER')),max_length=10)
    year = models.CharField(choices=(('ANY','ANY'),('1','1'),('2','2'),('3','3'),('4','4')),max_length=5)
    addedAt = models.DateTimeField(auto_now_add=True)

