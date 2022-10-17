from django.db import models
from djmoney.models.fields import MoneyField

# Create your models here.

ROLE = (
    ("SOFTWARE ENGINEER"), ("SOFTWARE ENGINEER"),
    ("MECHANICAL ENGINEER"), ("MECHANICAL ENGINEER")
)

class Salary(models.Model):
    fullname = models.CharField(max_length=50)
    role = models.CharField(max_length=50, choices=ROLE)
    amount = MoneyField(max_digits=14, decimal_places=2, default_currency='USD')

    def __str__(self):
        return self.fullname
        
    
