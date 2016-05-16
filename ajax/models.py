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
	name = models.CharField(max_length = 20)	
	password = models.CharField(max_length = 100 )
	repeat_password = models.CharField(max_length = 100 )
	email = models.EmailField( max_length = 50 )

# custom validation of the above form





class StudentForm(forms.ModelForm):
	class Meta:
		model = Student
		fields = '__all__'

	def clean(self):
		form_data = self.cleaned_data

		if len(form_data['name']) > 5:
			self.errors['name'] = ["Your name is more than 5 characters."]

		if form_data['password'] != form_data['repeat_password']:
			self.errors['repeat_password'] = ["Please enter the same password as above."]

		return form_data
