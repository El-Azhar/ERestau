from django import forms
from django.contrib.auth import password_validation
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class SignUpForm(UserCreationForm):
  email = forms.EmailField(max_length=250)
  first_name = forms.CharField(max_length=150, label="Nom")
  last_name = forms.CharField(max_length=150, label="Prénom")
  password1 = forms.CharField(
    label=("Mot de passe"),
    strip=False,
    widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
    help_text=password_validation.password_validators_help_text_html(),
  )
  password2 = forms.CharField(
    label=("Confirmation du mot de passe"),
    widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
    strip=False,
    help_text=("Enter the same password as before, for verification."),
  )
  class Meta:
    model = User
    fields = ('email', 'first_name', 'last_name', 'password1', 'password2')
    labels = {
      'first_name': ('Nom'),
      'last_name': 'Prénom',
      'password1': 'Mot de passe',
      'password2': 'Confirmation du mot de passe',
    }
  def clean_email(self):
    email = self.cleaned_data['email'].lower()
    if User.objects.filter(email=email):
      raise ValidationError("This email address already exists.")
    return email


  class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=250)
  first_name = forms.CharField(max_length=150, label="Nom")
  last_name = forms.CharField(max_length=150, label="Prénom")
  password1 = forms.CharField(
    label=("Mot de passe"),
    strip=False,
    widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
    help_text=password_validation.password_validators_help_text_html(),
  )
  password2 = forms.CharField(
    label=("Confirmation du mot de passe"),
    widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
    strip=False,
    help_text=("Enter the same password as before, for verification."),
  )
  class Meta:
    model = User
    fields = ('email', 'first_name', 'last_name', 'password1', 'password2')
    labels = {
      'first_name': ('Nom'),
      'last_name': 'Prénom',
      'password1': 'Mot de passe',
      'password2': 'Confirmation du mot de passe',
    }
  def clean_email(self):
    email = self.cleaned_data['email'].lower()
    if User.objects.filter(email=email):
      raise ValidationError("This email address already exists.")
    return email







