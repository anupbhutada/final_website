from django.contrib.auth.models import User
from models import *
from django import forms

class RegisterForm(forms.ModelForm):

	class Meta:
		model = Register
		fields = ['name','idno','contact','email', 'title', 'objective', 'abstract']
		widgets = {
          'abstract': forms.Textarea(attrs={'rows':4, 'cols':15}),
          'objective': forms.Textarea(attrs={'rows':2, 'cols':15}),
        }

