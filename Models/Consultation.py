# Name : Zhiyi Zhu
# Student ID: 1152455

class Consultation:
    def __init__(self, doctor, patient, date, reason, fee):
        # Initializing the consultation with details of doctor, patient, date, reason, and fee
        self.__doctor = doctor
        self.__patient = patient
        self.__date = date
        self.__reason = reason
        self.__fee = fee
        # Adding this consultation to both the doctor's and patient's records
        doctor.add_consultation(self)
        patient.add_consultation(self)
        
     # Getter methods for the consultation's attributes
    @property
    def Doctor(self):
        return self.__doctor
    
    @property
    def Patient(self):
        return self.__patient
    
    @property
    def Date(self):
        return self.__date
    
    @property
    def Reason(self):
        return self.__reason
    
    @property
    def Fee(self):
        return self.__fee
        
    # String representation of the consultation
    def __str__(self):
        return f"{self.__date} {self.__reason} {self.__patient} ${self.__fee}"
