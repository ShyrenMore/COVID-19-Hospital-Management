from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import *
from .filters import PatientFilter
# PatientFilter = OrderFilter

# Create your views here.

def dashboard(request):
    patients = Patient.objects.all()
    patient_count = patients.count()
    patients_recovered = Patient.objects.filter(status="Recovered")
    patients_deceased = Patient.objects.filter(status="Deceased")
    deceased_count = patients_deceased.count()
    recovered_count = patients_recovered.count()
    beds = Bed.objects.all()
    beds_available = Bed.objects.filter(occupied=False).count()
    context = {
        'patient_count': patient_count,
        'recovered_count': recovered_count,
        'beds_available': beds_available,
        'deceased_count':deceased_count,
        'beds':beds
    }
    print(patient_count)
    return render(request, 'main/dashboard.html', context)

def add_patient(request):
    beds = Bed.objects.filter(occupied=False)

    if request.method == "POST":
        name = request.POST['name']
        phone_num = request.POST['phone_num']
        patient_relative_name = request.POST['patient_relative_name']
        patient_relative_contact = request.POST['patient_relative_contact']
        address = request.POST['address']
        symptoms = request.POST['symptoms']
        prior_ailments = request.POST['prior_ailments']
        bed_num_sent = request.POST['bed_num']
        bed_num = Bed.objects.get(bed_number=bed_num_sent)
        dob = request.POST['dob']
        status = request.POST['status']
        print(request.POST)
        patient = Patient.objects.create(
            name = name,
        phone_num = phone_num,
        patient_relative_name = patient_relative_name,
        patient_relative_contact = patient_relative_contact, 
        address = address, 
        symptoms = symptoms, 
        prior_ailments = prior_ailments, 
        bed_num = bed_num,
        dob = dob, 
        status = status 
        )
        patient.save()

        bed = Bed.objects.get(bed_number=bed_num_sent)
        bed.occupied = True
        bed.save()
        id = patient.id
        return redirect(f"/patient/{id}")
        
    context = {
        'beds': beds
    }
    return render(request, 'main/add_patient.html', context)

def patient(request, pk):
    patient = Patient.objects.get(id=pk)
    context = {
        'patient': patient
    }
    return render(request, 'main/patient.html', context)


def patient_list(request):
    patients = Patient.objects.all()

    # filtering
    myFilter = PatientFilter(request.GET, queryset=patients)

    patients = myFilter.qs
    context = {
        'patients': patients,
        'myFilter': myFilter
    }

    return render(request, 'main/patient_list.html', context)

'''
def autocomplete(request):
    if patient in request.GET:
        name = Patient.objects.filter(name__icontains=request.GET.get(patient))
        name = ['js', 'python']
        
        names = list()
        names.append('Shyren')
        print(names)
        for patient_name in name:
            names.append(patient_name.name)
        return JsonResponse(names, safe=False)
    return render (request, 'main/patient_list.html')
'''

def autosuggest(response):
    query_original = response.GET.get('term')
    queryset = Patient.objects.filter(name=query_original)
    mylist = []
    mylist += [x.name for x in queryset]
    return JsonResponse(mylist, safe=False)