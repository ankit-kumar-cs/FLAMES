from django import forms
from .models import Input

class InputForm(forms.ModelForm):
    class Meta:
        model=Input
        fields="__all__"
    def clean(self):
        cleaned_data = super().clean()
        x = cleaned_data.get('your_name')
        y= cleaned_data.get('person_name')
        if not(x.isalpha()) or not(y.isalpha()):
            raise forms.ValidationError(
                    "Please enter only First Name.No Spaces are allowed."
                )
