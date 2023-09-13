class Doctor:
    nextID = 1000
    def __init__(self, first_name, last_name, specialisation):
        self.doctor_ID = Doctor.nextID
        self.first_name = first_name
        self.last_name = last_name
        self.specialisation = specialisation
        self.myPatients = []
        self.myDoctorCons = []
        Doctor.nextID += 1
 
    @property
    def fname(self):
        return self.first_name
        
    @property
    def lname(self):
        return self.last_name
         
    @property
    def Doctor_ID(self):
        return self.doctor_ID
    
     
    def add_patient(self, patient):
          self.myPatients.append(patient)


    def add_consultation(self, consultation):
        self.myDoctorCons.append(consultation)


    def __str__(self):
        return f"{self.first_name} {self.last_name}, {self.specialisation}"

    def get_info(self):
        info = f"{self.doctor_ID} {self.first_name} {self.last_name} - {self.specialisation}\n"
        info += "\nPatients List:\n"
        for patient in self.myPatients:
            info += f"{patient.Patient_ID} {patient}\n"
        info += "\nConsultations:\n"
        for cons in self.myDoctorCons:
            info += f"{cons}\n"
        return info
    
    def __eq__(self, other):
        return self.doctor_ID == other.Doctor_ID