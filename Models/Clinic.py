from Models.Consultation import Consultation
from Models.Patient import Patient
from Models.Doctor import Doctor

class Clinic:
    def __init__(self):
        self.myDoctors = []
        self.myPatients = []
        self.myConsultations = []

    def create_doctor(self, first_name, last_name, specialisation):
        doctor = Doctor(first_name, last_name, specialisation)
        self.myDoctors.append(doctor)
        return doctor

    def create_patient(self, first_name, last_name):
        patient = Patient(first_name, last_name)
        self.myPatients.append(patient)
        return patient

    def add_consultation(self, doctor, patient, date, reason, fee):
        consultation = Consultation(doctor, patient, date, reason, fee)
        self.myConsultations.append(consultation)
        return consultation

    def get_consultation_report(self):
        report = "Consultation Report for XYZ Medical Center\n"
        total_fee = 0
        for cons in self.myConsultations:
            report += f"\n{cons.Patient} {cons.Date} {cons.Reason} {cons.Fee}\n"
            total_fee += float(cons.Fee)
        report += f"\nTotal Fees: ${total_fee}\n"
        return report