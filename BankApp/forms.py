from django import forms
from BankApp.models import Bank
class BankForm(forms.ModelForm):
    class Meta:
        model=Bank
        fields="__all__"
