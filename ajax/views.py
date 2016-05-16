from django.shortcuts import render

from django.http import HttpResponse

from django.http import JsonResponse
from ajax.models import StudentForm
# Create your views here.

def index(request):

	student = StudentForm()
	return render(request,'index.html',{'form' : student})

def apply(request):

	if request.method == 'POST':
		student = StudentForm(request.POST)
		if student.is_valid():
			student.save()
			data = {"status" : "success"}
			return JsonResponse(data)
		else:
			data = {
				"status" : "failure",
				"errors" : student.errors
				}
			return HttpResponse(JsonResponse(data))

				
	
	return JsonResponse({'status' : 'failure'})