from django.db import models

# Create your models here.
class Transactions(models.Model):
    '''
    Table to represent individual reference transactions

    Transaction fields:
    id (auto added), type, location, format, datetime
    '''

    ''' 
    Model Field Choices
    '''
    class TypeChoices(models.TextChoices):
        INFORMATION_SERVICES = 'information services'
        DIGITAL_RESOURCES = 'digital resources'

    
    type = models.CharField(max_length=64, choices=TypeChoices)
    location = models.CharField(max_length=64)
    format = models.CharField(max_length=64)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Transaction {self.id} | Type {self.type} | Location {self.location} | Format {self.format} | Date {self.date}"
