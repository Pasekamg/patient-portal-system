from django.test import TestCase
from .models import Patient

class PatientModelTest(TestCase):

    def test_string_representation(self):
        patient = Patient(first_name="John", last_name="Doe")
        self.assertEqual(str(patient), "John Doe")

    def test_patient_creation(self):
        patient = Patient.objects.create(
            first_name="Jane", last_name="Doe", birth_date="1990-01-01", email="jane.doe@example.com"
        )
        self.assertEqual(patient.first_name, "Jane")
