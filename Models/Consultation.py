class Consultation:
    def __init__(self, doctor, patient, date, reason, fee):
        self.__doctor = doctor
        self.__patient = patient
        self.__date = date
        self.__reason = reason
        self.__fee = fee
        doctor.add_consultation(self)
        patient.add_consultation(self)
        
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
        

    def __str__(self):
        return f"{self.__date} {self.__reason} {self.__patient} ${self.__fee}"
