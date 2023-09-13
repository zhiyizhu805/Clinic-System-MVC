class Patient:
    nextID = 200

    def __init__(self, first_name, last_name):
        self.myPatientID = Patient.nextID
        self.myPatientFName = first_name
        self.myPatientLName = last_name
        self.myDoctor = []
        self.consultations = []
        Patient.nextID += 1
        
    @property
    def Patient_ID(self):
        return self.myPatientID
        
    def assign_doctor(self, doctor):
        if doctor not in self.myDoctor:
            self.myDoctor.append(doctor) 
            doctor.add_patient(self)
            return 1
        return 0

    def add_consultation(self, consultation):
        self.consultations.append(consultation)

    def __str__(self):
        return f"{self.myPatientFName} {self.myPatientLName}"

    def get_info(self):
        info = f"{self.myPatientID} {self.myPatientFName} {self.myPatientLName}\n"
        info += '\nDoctor List:\n'
        for doctor in self.myDoctor: 
          info += f"{doctor.Doctor_ID} {doctor}\n"
        info += "\nConsultations:\n"
        total_fee = 0
        for cons in self.consultations:
            info += f"{cons.Doctor} {cons.Date} {cons.Fee}\n"
            total_fee += float(cons.Fee)
        info += f"\nTotal Fees Due: ${total_fee}\n"
        return info

    
    def __eq__(self, other):
        return self.myPatientID == other.Patient_ID