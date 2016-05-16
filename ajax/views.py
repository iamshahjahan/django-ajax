from django.shortcuts import render

from django.http import HttpResponse

from django.http import JsonResponse
from ajax.models import StudentForm
# Create your views here.

def index(request):

	student = StudentForm()
	return render(request,'index.html',{'form' : student})

def apply(request):

	data = {'hello' : 'hi'}
	return JsonResponse(data)	