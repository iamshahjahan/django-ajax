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

	    # student.name = request.POST.get('name')
	    # student.email = request.POST.get('email')
	    # student.password = request.POST.get('password')


	    # student.name = name
	    # student.email = email
	    # student.password = password

	    student.save()

	    data = {"status" : "success"}
	    return JsonResponse(data)
	else:
		data = {"status" : "failure"}
       
		return JsonResponse(data)