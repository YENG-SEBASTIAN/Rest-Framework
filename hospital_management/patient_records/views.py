from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import Person
from .serializer import PersonOrPatientSerializer
from rest_framework.parsers import JSONParser
from .forms import PatientForm

# Create your views here.
def home(request):
    if request.method == 'POST':
        patient_form = PatientForm()
        if patient_form.is_valid():
            patient_form.save()
            return HttpResponse("Data has being saved into the database")
        return render(request, 'home.html', {"patient_form":patient_form,})    
    elif request.method == "GET":
        patient_form = PatientForm()
    return render(request, 'home.html', {"patient_form":patient_form,})



def all_patient_list(request):
    #getting all the list of patient in the database

    if request.method == 'GET':   
        all_patient_qs = Person.objects.all()
        patient_serializer = PersonOrPatientSerializer(all_patient_qs, many = True)
        return JsonResponse(patient_serializer.data, safe=False)

    elif request.method == 'POST':
            data = JSONParser().parse(request)
            serializer = PersonOrPatientSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data, status = 201)
            return JsonResponse(serializer.errors, status = 400)

def patient_details(request, pk):

    try:
        patient = Person.objects.get(pk = pk)
    except Person.DoesNotExist:
        return HttpResponse("This patient does not exist in our database.")

    if request.method == 'GET':
        patient_qs = PersonOrPatientSerializer(patient)
        return JsonResponse(patient_qs.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = PersonOrPatientSerializer(patient, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        patient.delete()
        return JsonResponse(status = 204)