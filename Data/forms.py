from django import forms
from Data.models import CSVBestanden

class CSVForm(forms.ModelForm):
    class Meta:
        model = CSVBestanden
        fields = ['CSVBestand']
        widgets = {
            "CSVBestand": forms.FileInput(attrs={'accept': '.csv'})
        }