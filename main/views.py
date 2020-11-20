from django.shortcuts import render, redirect
from django.http import HttpResponse
# Create your views here.

def dashboard(response):
    return render(response, 'main/dashboard.html', {})

def add_patient(response):
    return render(response, 'main/add_patient.html', {})

def patient(response):
    return render(response, 'main/patient.html', {})
