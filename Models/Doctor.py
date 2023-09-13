class Doctor:
    nextID = 1000
    def __init__(self, first_name, last_name, specialisation):
        self.__doctor_ID = Doctor.nextID
        self.__first_name = first_name
        self.__last_name = last_name
        self.__specialisation = specialisation
        self.__myPatients = []
        self.__myDoctorCons = []
        Doctor.nextID += 1
 
    @property
    def fname(self):
        return self.__first_name
        
    @property
    def lname(self):
        return self.__last_name
         
    @property
    def Doctor_ID(self):
        return self.__doctor_ID
    
    @property
    def Specialisation(self):
        return self.__specialisation
    
    @property
    def MyDoctorCons(self):
        return self.__myDoctorCons
    
    @property
    def Doctor_ID(self):
        return self.__doctor_ID
    
     
    def add_patient(self, patient):
          self.__myPatients.append(patient)


    def add_consultation(self, consultation):
        self.__myDoctorCons.append(consultation)


    def __str__(self):
        return f"{self.__first_name} {self.__last_name}, {self.__specialisation}"

    def get_info(self):
        info = f"{self.__doctor_ID} {self.__first_name} {self.__last_name} - {self.__specialisation}\n"
        info += "\nPatients List:\n"
        for patient in self.__myPatients:
            info += f"{patient.Patient_ID} {patient}\n"
        info += "\nConsultations:\n"
        for cons in self.__myDoctorCons:
            info += f"{cons}\n"
        return info
    
    def __eq__(self, other):
        return self.__doctor_ID == other.Doctor_ID