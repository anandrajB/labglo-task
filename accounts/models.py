from django.db import models
from accounts.utils.base import hex_code , GenderTextChoies

class University(models.Model):
    uid = models.UUIDField(primary_key=True, default=hex_code, editable=False)
    name = models.CharField(max_length=100 , unique=True)
    ranking = models.IntegerField()
    address=  models.TextField()
    established_year = models.IntegerField()
    def __str__(self):
        return self.name


    class Meta:
        ordering = ['name']
        verbose_name_plural = "Universities"
        indexes = [models.Index(fields=["uid" ,"name"])]



class Student(models.Model):
    uid = models.UUIDField(primary_key=True, default=hex_code, editable=False)
    name = models.CharField(max_length=100)
    university = models.ForeignKey(University , on_delete= models.CASCADE)
    age = models.IntegerField()
    address = models.TextField()
    gender = models.CharField(choices = GenderTextChoies.choices, max_length=100)
    enrollment_date = models.DateField()

    def __str__(self):
        return f"{self.name} - {self.university.name} - {self.gender.capitalize()}"
    
    class Meta:
        ordering = ['name']
        verbose_name_plural = "Students"
        indexes = [models.Index(fields=["uid" ,"name"])]

