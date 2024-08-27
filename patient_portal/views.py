from django.shortcuts import render
from .models import Patient

def patient_list(request):
    patients = Patient.objects.all()
    return render(request, 'patient_portal/patient_list.html', {'patients': patients})
