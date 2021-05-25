from django import forms
class OrderForm(forms.Form):
    first_name = forms.CharField(max_length=150, label="Nom")
    last_name = forms.CharField(max_length=150, label="Prénom")
    adresse = forms.CharField(max_length=250, label="Adresse")
    phone_number = forms.IntegerField(label='Numéro de téléphone')
