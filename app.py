import tkinter as tk
from Controllers.medical_center_controller import MedicalCenterAppController
from Controllers.medical_center_controller import Clinic

def main():
    clinic = Clinic()
    # Load data from files
    with open("Data/Doctor.txt", "r") as file:
        for line in file:
            first_name, last_name, specialty = line.strip().split(",")
            clinic.create_doctor(first_name, last_name, specialty)

    with open("Data/Patient.txt", "r") as file:
        for line in file:
            first_name, last_name = line.strip().split(",")
            clinic.create_patient(first_name, last_name)

    root = tk.Tk()
    app = MedicalCenterAppController(root, clinic)
    root.mainloop()

if __name__ == "__main__":
    main()
