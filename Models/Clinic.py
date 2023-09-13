from Models.Consultation import Consultation
from Models.Patient import Patient
from Models.Doctor import Doctor

class Clinic:
    def __init__(self):
        self.__myDoctors = []
        self.__myPatients = []
        self.__myConsultations = []
        
    @property
    def myDoctors(self):
        return self.__myDoctors
    
    @property
    def myPatients(self):
        return self.__myPatients
    
    @property
    def myConsultations(self):
        return self.__myConsultations
    

    def create_doctor(self, first_name, last_name, specialisation):
        # create doctor instance
        doctor = Doctor(first_name, last_name, specialisation)
        self.__myDoctors.append(doctor)
        return doctor

    def create_patient(self, first_name, last_name):
        # create patient instance
        patient = Patient(first_name, last_name)
        self.__myPatients.append(patient)
        return patient

    def add_consultation(self, doctor, patient, date, reason, fee):
        # create consultation instance
        consultation = Consultation(doctor, patient, date, reason, fee)
        self.__myConsultations.append(consultation)
        return consultation

    def get_consultation_report(self):
        report = "Consultation Report for XYZ Medical Center\n"
        total_fee = 0
        for cons in self.myConsultations:
            report += f"\n{cons.Patient} {cons.Date} {cons.Reason} {cons.Fee}\n"
            total_fee += float(cons.Fee)
        report += f"\nTotal Fees: ${total_fee}\n"
        return report