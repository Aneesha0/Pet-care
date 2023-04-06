from django.db import models
from django.contrib.auth.models import User
import datetime
from django.utils import timezone

# class Pet(models.Model):
#     animal=models.CharField(max_length=10)
#     def __str__(self) -> str:
#         return self.animal

class Service(models.Model):
    services_name = models.CharField(max_length=200)
    cost=models.IntegerField(default=500)
    def __str__(self) -> str:
        return self.services_name

class Status(models.Model):
    status=models.CharField(max_length=10)
    def __str__(self) -> str:
        return self.status

class Book(models.Model):
    owners=models.ForeignKey(User,on_delete=models.CASCADE)
    user=User.objects.all()
    services=models.ForeignKey(Service,on_delete=models.CASCADE)
    statuses=models.ForeignKey(Status,on_delete=models.CASCADE)
    owner=models.CharField(max_length=10)
    pet_name=models.CharField(max_length=10)
    # animal=models.ForeignKey(Pet,on_delete=models.CASCADE)
    date = models.DateField(default=datetime.date.today)

    def __str__(self) -> str:
        return self.owner
