from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.core import validators
from crispy_forms.bootstrap import Field, InlineRadios, TabHolder, Tab
from django.forms import ModelForm

from mysite.models import UserProfile

from .models import (
    Suggestion,
    Create_Chapter,
    Contact
)
from django.contrib.auth.forms import (
    UserCreationForm, 
    UserChangeForm
)
from django.contrib.auth import (
    authenticate, 
    get_user_model, 
    password_validation
)

#User Login Form ................
class loginForm(forms.Form):
    email = forms.CharField()
    password = forms.CharField(widget = forms.PasswordInput())

# Create Suggestion Form
class Suggestionform(forms.ModelForm):
    class Meta:
        model=Suggestion
        exclude =  [
            'user',
        ]
        
        
# Contact Form
class Contactform(forms.ModelForm):
    class Meta:
        model=Contact
        fields = (
            'name',
            'email',
            'phone',
            'message'
        )
        
# Create Chapter Form
class Chapterform(forms.ModelForm):
    class Meta:
        model=Create_Chapter
        exclude =  [
            'user',
            'approve'
        ]

class EditProfileForm(ModelForm):
    class Meta:
        model = User
        fields = (
            'email',
            'first_name',
            'last_name'
        )

class ProfileForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = (
            'address1',
            'address2',
            'postal_code',
            'country',
            'state',
            'city',
            'dob',
            'phoneNumber',
            'professionalGroup',
            'profession',
            'image'
        )