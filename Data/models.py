from django.db import models
from datetime import datetime
from django.core.validators import MaxValueValidator

# Create your models here.

class EnergieTerug(models.Model):
    Jaartal = models.IntegerField(default=datetime.now().year)
    Maand = models.IntegerField(default=datetime.now().month, validators=[MaxValueValidator(12)])
    Tijdstip = models.CharField(max_length=10, unique=True, primary_key=True)
    Waarde = models.DecimalField(max_digits=7, decimal_places=2)

    class Meta:
        verbose_name = "Teruggeleverd Energie"
        verbose_name_plural = "Teruggeleverd Energie"
    
    def __str__(self):
        return f"{self.Tijdstip}: {self.Waarde} kWh"

class CSVBestanden(models.Model):
    CSVBestand = models.FileField(upload_to='CSV/')