from argparse import _MutuallyExclusiveGroup
import pstats
from django.db import models

# Create your models here.
class Perfume(models.Model):
    name = models.CharField(max_length=50)
    brand = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name

