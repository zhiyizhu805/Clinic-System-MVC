import tkinter as tk
import tkinter.messagebox as messagebox
from Models.Doctor import Doctor
from Models.Patient import Patient
from Models.Consultation import Consultation
from Views.medical_center_view import MedicalCenterAppView

class Clinic:
    def __init__(self):
        self.__myDoctors = []
        self.__myPatients = []
        self.__myConsultations = []
        self.__filteredDoctors = []
        self.__filteredPatients = []
        
        
        
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
        for cons in self.__myConsultations:
            report += f"\n{cons.Patient} {cons.Date} {cons.Reason} ${cons.Fee}\n"
            total_fee += float(cons.Fee)
        report += f"\nTotal Fees: ${total_fee}\n"
        return report
    
 
    def searchDoctors(self, userInput):
        """search doctor function: please call this function with doctor's name as variable"""
        # Clear the filtered list before each search
        self.__filteredDoctors.clear()  
        
        for doctor in self.__myDoctors:
            if userInput in f'{doctor.fname} {doctor.lname}':
                self.__filteredDoctors.append(doctor) 
        
        # If there are any filtered doctors
        if self.__filteredDoctors:
            print(f'\n>>>>user input:{userInput}\n>>>>filterd doctors:')
            return '\n'.join([f"{doc.fname} {doc.lname}" for doc in self.__filteredDoctors])
        else:
            print(f'\n>>>>user input:{userInput}')
            return "No doctors found matching your criteria."

    def searchPatients(self, userInput):
        """search patients function: please call this function with patient's name as variable"""
        # Clear the filtered list before each search
        self.__filteredPatients.clear()  
        
        for patient in self.__myPatients:
            if userInput in f'{patient.PatientFName} {patient.PatientLName}':
                self.__filteredPatients.append(patient)

        # If there are any filtered patients
        if self.__filteredPatients:
            print(f'\n>>>>user input:{userInput}\n>>>>filterd patients:')
            return '\n'.join([f"{pat.PatientFName} {pat.PatientLName}" for pat in self.__filteredPatients])
        else:
            print(f'\n>>>>user input:{userInput}')
            return "No patients found matching your criteria."

                    
        
        


class MedicalCenterAppController:
    def __init__(self, master):
        self.view = MedicalCenterAppView(master)
        self.clinic = Clinic()
        # Load data from files
        with open("Data/Doctor.txt", "r") as file:
            for line in file:
                first_name, last_name, specialty = line.strip().split(",")
                self.clinic.create_doctor(first_name, last_name, specialty)

        with open("Data/Patient.txt", "r") as file:
            for line in file:
                first_name, last_name = line.strip().split(",")
                self.clinic.create_patient(first_name, last_name)

        # Bind buttons to methods
        self.view.assign_btn.config(command=self.assign_doctor)
        self.view.consult_btn.config(command=self.add_consultation)
        self.view.btn_show_doctor_info.config(command=self.show_doctor_info)
        self.view.btn_show_patient_info.config(command=self.show_patient_info)
        self.view.btn_show_consultation_report.config(command=self.show_consultation_report)

        self.update_doctor_list()
        self.update_patient_list()

        # test case:
        # search doctor and patients
        print(self.clinic.searchDoctors('laura vivi'))
        print(self.clinic.searchPatients('Misha'))
        

    def update_doctor_list(self):
        self.view.doctor_listbox.delete(0, tk.END)
        for doctor in self.clinic.myDoctors:
            self.view.doctor_listbox.insert(tk.END, doctor)

    def update_patient_list(self):
        self.view.patient_listbox.delete(0, tk.END)
        for patient in self.clinic.myPatients:
            self.view.patient_listbox.insert(tk.END, patient)

    def assign_doctor(self):
        selected_doctor_index = self.view.doctor_listbox.curselection()
        selected_patient_index = self.view.patient_listbox.curselection()

        if not selected_doctor_index or not selected_patient_index: 
            messagebox.showerror("Error", "❗️ Please select both a doctor and a patient!")
            return

        doctor = self.clinic.myDoctors[selected_doctor_index[0]]
        patient = self.clinic.myPatients[selected_patient_index[0]]
        assign_patient_to_doctor = patient.assign_doctor(doctor)
        if assign_patient_to_doctor == 1:
          messagebox.showinfo("Success",f"✅ Doctor {doctor} has been assigned to patient {patient}!")
        else:
          messagebox.showerror("Error", f"❌ Doctor {doctor} cannot be double-assigned to patient {patient}!")

    def add_consultation(self):
        date = self.view.date_entry.get()
        reason = self.view.reason_entry.get()
        fee = self.view.fee_entry.get()

        if not date or not reason or not fee:
            messagebox.showerror("Error", "❗️ Please fill in all consultation details!")
            return
        if not self.view.validate_date(date) :
            return 
        if not self.view.validate_fee(fee):
            return
            
        selected_doctor_index = self.view.doctor_listbox.curselection()
        selected_patient_index = self.view.patient_listbox.curselection()

        if not selected_doctor_index or not selected_patient_index:
            messagebox.showwarning("warning", "❗️ Please select both a doctor and a patient!")
            return

        doctor = self.clinic.myDoctors[selected_doctor_index[0]]
        patient = self.clinic.myPatients[selected_patient_index[0]]
        
        if doctor in patient.MyDoctor:
            consultation = self.clinic.add_consultation(doctor, patient, date, reason, fee)
            messagebox.showinfo("Success", f"✅  Consultation with Doctor {doctor} has been made to patient {patient} on {date}!")
        else:
            messagebox.showerror("Error", f"❗️ Please assign {doctor} to {patient} first!")
            
        

    def show_doctor_info(self):
        selected_doctor_index = self.view.doctor_listbox.curselection()
        if not selected_doctor_index:
            messagebox.showerror("Error", "❗️ Please select a doctor!")
            return
        
        doctor = self.clinic.myDoctors[selected_doctor_index[0]]
        info = doctor.get_info()
        self.show_info("👨🏼‍⚕️ Doctor Information", info)

    def show_patient_info(self):
        selected_patient_index = self.view.patient_listbox.curselection()
        if not selected_patient_index:
            messagebox.showerror("Error", "❗️ Please select a patient!")
            return
        
        patient = self.clinic.myPatients[selected_patient_index[0]]
        info = patient.get_info()
        self.show_info("Patient Information", info)

    def show_consultation_report(self):
        report = self.clinic.get_consultation_report()
        self.show_info("Consultation Report", report)

    def show_info(self, title, info):
        info_window = tk.Toplevel(self.view.master)
        info_window.title(title)
        txt = tk.Text(info_window, wrap=tk.WORD, width=60, height=20)
        txt.pack(padx=20, pady=20)
        txt.insert(tk.END, info)
        txt.config(state=tk.DISABLED)
        btn_close = tk.Button(info_window, text="Close", command=info_window.destroy)
        btn_close.pack(pady=10)

