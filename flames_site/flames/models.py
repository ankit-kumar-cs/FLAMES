from django.db import models

# Create your models here.
class Input(models.Model):
    your_name=models.CharField(help_text="Enter Your First Name",max_length=100)
    person_name=models.CharField(help_text="Second Person First Name",max_length=100)
    def __str__(self):
        return self.your_name
