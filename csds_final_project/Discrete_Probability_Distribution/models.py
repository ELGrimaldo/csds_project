from django.db import models

# Create your models here.
class TableValues(models.Model):
    xValue = models.CharField(max_length=200)
    pOfX = models.CharField(max_length=200)
    xPofX = models.CharField(max_length=200)
    xRaiseTwo = models.CharField(max_length=200)
    xRaiseTwoPofX = models.CharField(max_length=200)

