from django.db import models
from .constants import GENDER_TYPE
from django.contrib.auth.models import User
# Create your models here.
class UserDetailsModel(models.Model):
    user = models.OneToOneField(User,related_name='account',on_delete=models.CASCADE)
    gender = models.CharField(choices=GENDER_TYPE,max_length=50)
    birth_date = models.DateTimeField()
    account_no = models.BigIntegerField()
    balance = models.DecimalField(default=0,max_digits=12,decimal_places=2)
    address = models.CharField(max_length=200)
    country = models.CharField(max_length=50)
    
    def __str__(self) -> str:
        return self.user.username
    
    
