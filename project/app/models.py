from django.db import models
from datetime import datetime
import uuid
from phonenumber_field.modelfields import PhoneNumberField
gender_field=(
    ("Male","male"),
    ("Female","female"),
    ("other","other")
)
# Create your models here.
class Student(models.Model):
    ischeck=models.BooleanField(default=True,verbose_name="it is an checkbox")
    name=models.CharField(max_length=30,verbose_name="enter your name")
    email=models.EmailField(null=True,unique=True)
    text=models.TextField(blank=True)
    image=models.ImageField(null=True)
    date=models.DateField(default=datetime.now())
    date1=models.DateTimeField(default=datetime.now())
    created_date=models.DateField(auto_now_add=True,null=True)
    update_date=models.DateField(auto_now=True,null=True)
    url=models.URLField(default="www.facebook.com")
    decimal=models.DecimalField(max_digits=8,decimal_places=3,default=0)
    var=models.UUIDField(default=uuid.uuid4,editable=False)
    gender=models.CharField(choices=gender_field,max_length=50,null=True)
    phone=PhoneNumberField(blank=True)

class Interested(models.Model):
    title=models.CharField(max_length=200)
    
    def _str_(self) -> str:
        return self.title
    
class City(models.Model):
    title=models.CharField(max_length=200)
    def _str_(self) -> str:
        return self.title
    
class Person(models.Model):
    name=models.CharField(max_length=50)
    age=models.IntegerField()
    interest=models.ManyToManyField(Interested)
    
    def _str_(self) -> str:
        return self.name
    
class personDetail(models.Model):
    person=models.OneToOneField(Person,on_delete=models.CASCADE)
    city=models.ForeignKey(City, on_delete=models.CASCADE)
    room_no=models.CharField(max_length=200)
    





