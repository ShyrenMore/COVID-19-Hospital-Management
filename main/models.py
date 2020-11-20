from django.db import models

# Create your models here.

class Patient(models.Model):
    name = models.CharField(max_length=50)
    phone_num = models.CharField(max_length=15)
    address = models.TextField()
    # symptoms = 
    prior_ailments = models.TextField()
    bed_num = models.CharField(max_length=5)
    dob = models.DateField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return self.name
        