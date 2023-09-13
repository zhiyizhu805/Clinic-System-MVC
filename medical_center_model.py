
class Doctor:
    def __init__(self, first_name, last_name, specialisation):
        self.first_name = first_name
        self.last_name = last_name
        self.specialisation = specialisation
        self.myPatients = []
        self.myDoctorCons = []
        
    # @property
    # def first_name(self):
    #     return self.first_name
    
     
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
        info = f"{self.first_name} {self.last_name} - {self.specialisation}\n"
        info += "Patients List:\n"
        for patient in self.myPatients:
            info += f"{patient}\n"
        info += "Consultations:\n"
        for cons in self.myDoctorCons:
            info += f"{cons}\n"
        return info
    def __eq__(self, other):
        return self.first_name == other.first_name

class Patient:
    nextID = 1

    def __init__(self, first_name, last_name):
        self.myPatientID = Patient.nextID
        Patient.nextID += 1
        self.myPatientFName = first_name
        self.myPatientLName = last_name
        self.myDoctor = []
        self.consultations = []

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
        info = f"{self.myPatientFName} {self.myPatientLName}\n"
        info += f"Doctor: {self.myDoctor}\n"
        info += "Consultations:\n"
        total_fee = 0
        for cons in self.consultations:
            info += f"{cons}\n"
            total_fee += float(cons.fee)
        info += f"Total Fees Due: ${total_fee}\n"
        return info
    
    def __eq__(self, other):
        return self.first_name == other.first_name

class Consultation:
    def __init__(self, doctor, patient, date, reason, fee):
        self.doctor = doctor
        self.patient = patient
        self.date = date
        self.reason = reason
        self.fee = fee
        doctor.add_consultation(self)
        patient.add_consultation(self)

    def __str__(self):
        return f"{self.date} {self.reason} {self.patient} ${self.fee}"

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
            report += f"{cons}\n"
            total_fee += float(cons.fee)
        report += f"Total Fees: ${total_fee}\n"
        return report
