# Name : Zhiyi Zhu
# Student ID: 1152455

import tkinter as tk
import tkinter.messagebox as messagebox
from Models.Doctor import Doctor
from Models.Patient import Patient
from Models.Consultation import Consultation
from Views.medical_center_view import MedicalCenterAppView

        
class MedicalCenterAppController:
    def __init__(self, master):
        # Initialize view and various lists for doctors, patients, consultations.
        self.view = MedicalCenterAppView(master)
        self.__myDoctors = []
        self.__myPatients = []
        self.__myConsultations = []
        self.__filteredDoctors = []
        self.__filteredPatients = []
        
        # Load doctor and patient data from respective files
        self.load_doctors_from_file()
        self.load_patients_from_file()
        
        # Update the view with loaded data
        self.update_doctor_list()
        self.update_patient_list()

        # Bind GUI buttons to their respective functionalities
        self.view.assign_btn.config(command=self.assign_doctor)
        self.view.consult_btn.config(command=self.add_consultation)
        self.view.btn_show_doctor_info.config(command=self.show_doctor_info)
        self.view.btn_show_patient_info.config(command=self.show_patient_info)
        self.view.btn_show_consultation_report.config(command=self.show_consultation_report)
        
    """getter for attributes"""
    @property
    def myDoctors(self):
        return self.__myDoctors
    
    @property
    def myPatients(self):
        return self.__myPatients
    
    @property
    def myConsultations(self):
        return self.__myConsultations
    
    @property
    def filteredDoctors(self):
        return self.__filteredDoctors
    
    @property
    def filteredPatients(self):
        return self.__filteredPatients
    

    """ create doctor instance """
    def create_doctor(self, first_name, last_name, specialisation):
        doctor = Doctor(first_name, last_name, specialisation)
        self.__myDoctors.append(doctor)
        return doctor

    """ create patient instance """
    def create_patient(self, first_name, last_name):
        patient = Patient(first_name, last_name)
        self.__myPatients.append(patient)
        return patient

    """ create consultation instance """
    def create_consultation(self, doctor, patient, date, reason, fee):
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
    
 
    """search doctor function: please call this function with doctor's name as variable"""
    def searchDoctors(self, userInput):
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

    """search patients function: please call this function with patient's name as variable"""
    def searchPatients(self, userInput):
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
        
    """ create function to load doctor's data """
    def load_doctors_from_file(self, filename="Data/Doctor.txt"):
        try:
            with open(filename, "r") as file:
                for line in file:
                    first_name, last_name, specialty = line.strip().split(",")
                    self.create_doctor(first_name, last_name, specialty)
        except FileNotFoundError:
            tk.messagebox.showerror("Error", f"❗️ File '{filename}' not found!")
       
    """ create function to load patient's data """     
    def load_patients_from_file(self, filename="Data/Patient.txt"):
        try:
            with open(filename, "r") as file:
                for line in file:
                    first_name, last_name = line.strip().split(",")
                    self.create_patient(first_name, last_name)
        except FileNotFoundError:
            tk.messagebox.showerror("Error", f"❗️ File '{filename}' not found!")
        
    """ update the view of doctor list"""
    def update_doctor_list(self):
        self.view.doctor_listbox.delete(0, tk.END)
        for doctor in self.myDoctors:
            self.view.doctor_listbox.insert(tk.END, doctor)

    """ update the view of patient list"""
    def update_patient_list(self):
        self.view.patient_listbox.delete(0, tk.END)
        for patient in self.myPatients:
            self.view.patient_listbox.insert(tk.END, patient)

    """function for assigning a doctor to a patient"""
    def assign_doctor(self):
        selected_doctor_index = self.view.doctor_listbox.curselection()
        selected_patient_index = self.view.patient_listbox.curselection()

        # validation : cannot double assigned
        if not selected_doctor_index or not selected_patient_index: 
            messagebox.showerror("Error", "❗️ Please select both a doctor and a patient!")
            return

        doctor = self.myDoctors[selected_doctor_index[0]]
        patient = self.myPatients[selected_patient_index[0]]
        assign_patient_to_doctor = patient.assign_doctor(doctor)
        if assign_patient_to_doctor == 1:
          messagebox.showinfo("Success",f"✅ Doctor {doctor} has been assigned to patient {patient}!")
        else:
          messagebox.showerror("Error", f"❌ Doctor {doctor} cannot be double-assigned to patient {patient}!")

    """function for adding a consultation record between a doctor and a patient"""
    def add_consultation(self):
        # get user input
        date = self.view.date_entry.get()
        reason = self.view.reason_entry.get()
        fee = self.view.fee_entry.get()

        # user input validation 
        if not date or not reason or not fee:
            messagebox.showerror("Error", "❗️ Please fill in all consultation details!")
            return
        if not self.view.validate_date(date) :
            return 
        if not self.view.validate_fee(fee):
            return
        
        # get user input
        selected_doctor_index = self.view.doctor_listbox.curselection()
        selected_patient_index = self.view.patient_listbox.curselection()

        # user input validation 
        if not selected_doctor_index or not selected_patient_index:
            messagebox.showwarning("warning", "❗️ Please select both a doctor and a patient!")
            return
        
        # get user input
        doctor = self.myDoctors[selected_doctor_index[0]]
        patient = self.myPatients[selected_patient_index[0]]
         
        # user input validation 
        if doctor in patient.MyDoctor:
            consultation = self.create_consultation(doctor, patient, date, reason, fee)
            messagebox.showinfo("Success", f"✅  Consultation with Doctor {doctor} has been made to patient {patient} on {date}!")
        else:
            messagebox.showerror("Error", f"❗️ Please assign {doctor} to {patient} first!")
            
        
    """ function for showing doctor's information """
    def show_doctor_info(self):
        selected_doctor_index = self.view.doctor_listbox.curselection()
        if not selected_doctor_index:
            messagebox.showerror("Error", "❗️ Please select a doctor!")
            return
        
        doctor = self.myDoctors[selected_doctor_index[0]]
        info = doctor.get_info()
        self.show_info("👨🏼‍⚕️ Doctor Information", info)

    def show_patient_info(self):
        selected_patient_index = self.view.patient_listbox.curselection()
        if not selected_patient_index:
            messagebox.showerror("Error", "❗️ Please select a patient!")
            return
        
        patient = self.myPatients[selected_patient_index[0]]
        info = patient.get_info()
        self.show_info("Patient Information", info)

    def show_consultation_report(self):
        report = self.get_consultation_report()
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
   
        
# """ test case : search doctor and patients function"""
# root = tk.Tk()
# test = MedicalCenterAppController(root)
# print(test.searchDoctors('laura vivi'))
# print(test.searchPatients('Misha'))

