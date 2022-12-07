"""Forms of the project."""

from things.forms import Thing
from django import forms

# Create your forms here.

class SignUpForm(forms.ModelForm):  # shows what needs to be displayed on the Signup page
    class Meta:
        model = Thing
        fields = ['name', 'description', 'quantity', 'created_at']

    
