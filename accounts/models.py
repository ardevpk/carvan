from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.



class CustomUser(AbstractUser):
    TYPES = (
        ('Manager', 'Manager'),
        ('Cleaner', 'Cleaner'),
        ('Washer', 'Washer'),
        )
    type = models.CharField(max_length=254, choices=TYPES, verbose_name='Type', help_text='Which type of this user is?', null=True, blank=True)

    STATUS = (
        ('Employee', 'Employee'),
        ('Self', 'Self'),
        )
    status = models.CharField(max_length=254, choices=STATUS, verbose_name='Status', help_text='Is this user self or employee?')
    def __str__(self):
        return self.username