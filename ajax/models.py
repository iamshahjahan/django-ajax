from __future__ import unicode_literals

from django.db import models
from django import forms

from django.forms import ModelForm

# Create your models here.

class Student(models.Model):
	name = models.CharField(max_length = 20 )
	password = models.CharField(max_length = 10 )
	email = models.CharField( max_length = 10 )


class StudentForm(forms.ModelForm):
	class Meta:
		model = Student
		fields = '__all__'	

		labels = {
            'name': ('Name'),
        }
        help_texts = {
            'name': ('Some useful help text.'),
        }
        error_messages = {
            'name': {
                'max_length': ("This writer's name is too long."),
            },
        }		
		