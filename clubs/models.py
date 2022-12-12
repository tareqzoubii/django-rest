from django.db import models
from django.contrib.auth import get_user_model
#from accounts.models import CustomUser
#from django.urls import reverse
# Create your models here.

class Clubs(models.Model):
     club_name = models.CharField(max_length=64)
     league_name = models.CharField(max_length=64)
     club_owner = models.CharField(max_length=64)
     trophies = models.TextField()
     purchaser =models.ForeignKey(get_user_model(), on_delete = models.CASCADE)
     rank=models.IntegerField()

     def __str__(self):
        return self.club_name

     #def get_absolute_url(self):
        #return reverse('clubs-list')