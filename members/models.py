from django.db import models
from django.core.validators import RegexValidator

# Create your models here.
class Member(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    phone = models.CharField(
        max_length=15, 
        null=True,
        validators=[RegexValidator(r'^\+?\d{10,15}$', 'Enter a valid phone number')]
    )
    joined_date = models.DateField(null=True)

    def __str__(self):
        return f"{self.firstname} {self.lastname}"