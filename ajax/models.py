from __future__ import unicode_literals

from django.db import models
from django import forms

from django.forms import ModelForm
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

# from django.core.validators import validators

# Create your models here.

def validate_name(value):
    if len(value) < 10:
        raise ValidationError(
            _('%(value)s is less than 10 characters.'),
            params={'value': value},
        )






class Student(models.Model):
	name = models.CharField(max_length = 20,validators=[validate_name] )
	password = models.CharField(max_length = 100 )
	email = models.EmailField( max_length = 50 )


class StudentForm(forms.ModelForm):
	class Meta:
		model = Student
		fields = '__all__'