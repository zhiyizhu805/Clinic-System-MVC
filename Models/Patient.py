class Patient:
     # Static variable to keep track of the next available Patient ID
    nextID = 200

    def __init__(self, first_name, last_name):
        # Initializing patient attributes including a unique ID
        self.__myPatientID = Patient.nextID
        self.__myPatientFName = first_name
        self.__myPatientLName = last_name
        self.__myDoctor = []
        self.__consultations = []
        Patient.nextID += 1
        
    # Getter methods for the patient's attributes
    @property
    def Patient_ID(self):
        return self.__myPatientID
    
    @property
    def PatientFName(self):
        return self.__myPatientFName
    
    @property
    def PatientLName(self):
        return self.__myPatientLName
    
    @property
    def MyDoctor(self):
        return self.__myDoctor
    
    @property
    def Myconsultations(self):
        return self.__consultations
        
    # Method to assign a doctor to this patient
    def assign_doctor(self, doctor):
        if doctor not in self.__myDoctor:
            self.__myDoctor.append(doctor) 
            doctor.add_patient(self)
            return 1  # Also add this patient to the doctor's list
        return 0 # Return 0 if doctor is already assigned

    # Method to add a consultation for this patient
    def add_consultation(self, consultation):
        self.__consultations.append(consultation)

    # String representation of the patient
    def __str__(self):
        return f"{self.__myPatientFName} {self.__myPatientLName}"

    # Method to get detailed info about the patient, their doctors, and consultations
    def get_info(self):
        info = f"{self.__myPatientID} {self.__myPatientFName} {self.__myPatientLName}\n"
        info += '\nDoctor List:\n'
        for doctor in self.__myDoctor: 
          info += f"{doctor.Doctor_ID} {doctor}\n"
        info += "\nConsultations:\n"
        total_fee = 0
        for cons in self.__consultations:
            info += f"{cons.Doctor} {cons.Date} ${cons.Fee}\n"
            total_fee += float(cons.Fee)
        info += f"\nTotal Fees Due: ${total_fee}\n"
        return info

    # Overriding equality to compare patients based on their unique ID
    def __eq__(self, other):
        return self.__myPatientID == other.Patient_ID