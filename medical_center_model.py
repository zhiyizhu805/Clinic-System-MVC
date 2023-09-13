
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
        # if patient not in self.myPatients:
          self.myPatients.append(patient)
        #   return 1
        # return 0

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

