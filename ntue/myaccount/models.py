from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')

    gender_choice = [('boy','boy'),('girl','girl'),]

    org = models.CharField(
        'Organization', max_length=128, blank=True)

    phone = models.CharField(
        'phone', max_length=50, blank=True)

    mod_date = models.DateTimeField('Last modified', auto_now=True)

    class Meta:
        verbose_name = 'User Profile'

    def __str__(self):
        return "{}'s profile".format(self.user.__str__())