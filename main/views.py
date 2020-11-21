from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import *
from .filters import PatientFilter
# PatientFilter = OrderFilter

# Create your views here.

def dashboard(response):
    return render(response, 'main/dashboard.html', {})

def add_patient(response):
    return render(response, 'main/add_patient.html', {})

def patient(response):
    return render(response, 'main/patient.html', {})


def paitent_list(response):
    patients = Patient.objects.all()

    # filtering
    myFilter = PatientFilter(response.GET, queryset=patients)

    patients = myFilter.qs
    context = {
        'patients': patients,
        'myFilter': myFilter
    }

    return render(response, 'main/patient_list.html', context)

'''
def autocomplete(response):
    if patient in response.GET:
        name = Patient.objects.filter(name__icontains=response.GET.get(patient))
        name = ['js', 'python']
        
        names = list()
        names.append('Shyren')
        print(names)
        for patient_name in name:
            names.append(patient_name.name)
        return JsonResponse(names, safe=False)
    return render (response, 'main/patient_list.html')
'''