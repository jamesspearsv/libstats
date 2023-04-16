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
    type_choices = (
        ("information services", "Information Services"), ("digital resources", "Digital Resources"), ("directional", "Directional"), 
        ("tech help", "Tech Help"))
    location_choices = (
        ("circ", "Circulation"),
        ("ref", "Reference"), 
        ("childrens", "Childrens"))
    format_choices = (
        ("in-person", "In-Person"),
        ("virtual", "Virtual"),
        ("phone", "Phone"))

    
    type = models.CharField(
        max_length=64, 
        choices=type_choices)
    location = models.CharField(
        max_length=64, 
        choices=location_choices)
    format = models.CharField(
        max_length=64,
        choices=format_choices)
    date = models.DateTimeField(
        auto_now_add=True)

    def __str__(self):
        return f"Transaction {self.id} | Type {self.type} | Location {self.location} | Format {self.format} | Date {self.date}"
