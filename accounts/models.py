from django.db import models
from django.contrib.auth.models import User
from services.models import Pet

# Create your models here.
class Default_value(models.Model):
    owners=models.OneToOneField(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=30,blank=True)
    pet_name=models.CharField(max_length=30,blank=True)
    # pet_type=models.OneToOneField(Pet,on_delete=models.CASCADE)
    def __str__(self) -> str:
        return self.name

