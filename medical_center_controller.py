
import tkinter as tk
from tkinter import messagebox
from medical_center_model import Clinic, Doctor, Patient, Consultation
from medical_center_view import ImprovedMedicalCenterAppViewV2 as MedicalCenterAppView

class MedicalCenterAppController:
    def __init__(self, master, clinic):
        self.view = MedicalCenterAppView(master)
        self.clinic = clinic

        # Bind buttons to methods
        self.view.assign_btn.config(command=self.assign_doctor)
        self.view.consult_btn.config(command=self.add_consultation)
        self.view.btn_show_doctor_info.config(command=self.show_doctor_info)
        self.view.btn_show_patient_info.config(command=self.show_patient_info)
        self.view.btn_show_consultation_report.config(command=self.show_consultation_report)

        self.update_doctor_list()
        self.update_patient_list()

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
            messagebox.showerror("Error", "Please select both a doctor and a patient!")
            return

        doctor = self.clinic.myDoctors[selected_doctor_index[0]]
        patient = self.clinic.myPatients[selected_patient_index[0]]
        patient.assign_doctor(doctor)
        messagebox.showinfo("Success", f"Doctor {doctor} assigned to patient {patient}!")

    def add_consultation(self):
        date = self.view.date_entry.get()
        reason = self.view.reason_entry.get()
        fee = self.view.fee_entry.get()

        if not date or not reason or not fee:
            messagebox.showerror("Error", "Please fill in all consultation details!")
            return

        selected_doctor_index = self.view.doctor_listbox.curselection()
        selected_patient_index = self.view.patient_listbox.curselection()

        if not selected_doctor_index or not selected_patient_index:
            messagebox.showerror("Error", "Please select both a doctor and a patient!")
            return

        doctor = self.clinic.myDoctors[selected_doctor_index[0]]
        patient = self.clinic.myPatients[selected_patient_index[0]]

        consultation = self.clinic.add_consultation(doctor, patient, date, reason, fee)
        messagebox.showinfo("Success", f"Consultation added for doctor {doctor} and patient {patient} on {date}!")

    def show_doctor_info(self):
        selected_doctor_index = self.view.doctor_listbox.curselection()
        if not selected_doctor_index:
            messagebox.showerror("Error", "Please select a doctor!")
            return
        
        doctor = self.clinic.myDoctors[selected_doctor_index[0]]
        info = doctor.get_info()
        self.show_info("Doctor Information", info)

    def show_patient_info(self):
        selected_patient_index = self.view.patient_listbox.curselection()
        if not selected_patient_index:
            messagebox.showerror("Error", "Please select a patient!")
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

# main function to run the app
def main():
    clinic = Clinic()

    # Load data from files
    with open("Doctor.txt", "r") as file:
        for line in file:
            first_name, last_name, specialty = line.strip().split(",")
            clinic.create_doctor(first_name, last_name, specialty)

    with open("Patient.txt", "r") as file:
        for line in file:
            first_name, last_name = line.strip().split(",")
            clinic.create_patient(first_name, last_name)

    root = tk.Tk()
    app = MedicalCenterAppController(root, clinic)
    root.mainloop()

if __name__ == "__main__":
    main()