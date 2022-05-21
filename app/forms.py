from dataclasses import field
from tkinter import Widget
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField, PasswordChangeForm, PasswordResetForm, SetPasswordForm
from django.contrib.auth.models import User
from django.utils.translation import gettext, gettext_lazy as _
from django.contrib.auth import password_validation
from .models import Customer


class CustomerRegistrationForm(UserCreationForm):
    email = forms.CharField(required=True, widget=forms.EmailInput(
        attrs={'class': 'form-control bg-dark text-light','placeholder':'Email *'}))
    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control bg-dark text-light','placeholder':'Username *'}))
    password1 = forms.CharField(
        label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control bg-dark text-light','placeholder':'Password *'}))
    password2 = forms.CharField(label='Confirm Password(again)',
                                widget=forms.PasswordInput(attrs={'class': 'form-control bg-dark text-light','placeholder':'Confirm Password *'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        labels = {'email': 'Email'}
        widgets = {'username': forms.TextInput(
            attrs={'class': 'form-control bg-dark text-light'})}


class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(
        attrs={'autofocus': True, 'class': 'form-control bg-dark text-light','placeholder':'Username *'}))
    password = forms.CharField(label=_("Password"), strip=False, widget=forms.PasswordInput(
        attrs={'autocomplete': 'current-password', 'class': 'form-control bg-dark text-light','placeholder':'Password *'}))


class MyPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(label=_("Old Password"), strip=False, widget=forms.PasswordInput(
        attrs={'autocomplete': 'current-password', 'autofocus': True, 'class': 'form-control bg-dark text-light'}))

    new_password1 = forms.CharField(label=_("New Password"), strip=False, widget=forms.PasswordInput(
        attrs={'autocomplete': 'new-password', 'class': 'form-control bg-dark text-light'}), help_text=password_validation. password_validators_help_text_html())

    new_password2 = forms.CharField(label=_("Confirm New Password"), strip=False, widget=forms.PasswordInput(
        attrs={'autocomplete': 'new-password', 'class': 'form-control bg-dark text-light'}))


class MyPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(label=_("Email"), max_length=254, widget=forms.EmailInput(
        attrs={'autocomplete': 'email', 'class': 'form-control bg-dark text-light'}))


class MySetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(label=_("New Password"), strip=False, widget=forms.PasswordInput(
        attrs={'autocomplete': 'new-password', 'class': 'form-control bg-dark text-light'}), help_text=password_validation. password_validators_help_text_html())

    new_password2 = forms.CharField(label=_("Confirm New Password"), strip=False, widget=forms.PasswordInput(
        attrs={'autocomplete': 'new-password', 'class': 'form-control bg-dark text-light'}))


class CustomerProfileForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'locality', 'city', 'state', 'zipcode']
        widgets = {'name': forms.TextInput(attrs={'class': 'form-control bg-dark text-light'}), 'locality': forms.TextInput(attrs={'class': 'form-control bg-dark text-light'}), 'city': forms.TextInput( attrs={'class': 'form-control bg-dark text-light'}), 
        'state': forms.Select(attrs={'class': 'form-control bg-dark text-light'}), 
        'zipcode': forms.NumberInput(attrs={'class': 'form-control bg-dark text-light'})}
