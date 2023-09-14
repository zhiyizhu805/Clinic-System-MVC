import tkinter as tk
import tkinter.messagebox as messagebox
from tkcalendar import Calendar



class MedicalCenterAppView:
    def __init__(self, master):
        self.master = master
        self.master.title("Medical Center Application")

        # Container frame for doctors and patients listbox
        self.listbox_frame = tk.Frame(self.master, padx=10, pady=10)
        self.listbox_frame.pack(pady=20)

        # Label and Listbox for patients (side by side with doctor listbox)
        self.patient_label = tk.Label(self.listbox_frame, text="All Patients")
        self.patient_label.grid(row=0, column=1, padx=10)
        self.patient_listbox = tk.Listbox(self.listbox_frame, width=40, height=10, exportselection=False)
        self.patient_listbox.grid(row=1, column=1, padx=10)
        
        # Label and Listbox for doctors (side by side with patient listbox)
        self.doctor_label = tk.Label(self.listbox_frame, text="All Doctors")
        self.doctor_label.grid(row=0, column=0, padx=10)
        self.doctor_listbox = tk.Listbox(self.listbox_frame, width=40, height=10, exportselection=False)
        self.doctor_listbox.grid(row=1, column=0, padx=10)

        # Consultation Frame with border
        self.cons_frame = tk.LabelFrame(self.master, text="Consultation Details", padx=10, pady=10)
        self.cons_frame.pack(pady=20, fill="x")


        # Date Entry with validation
        self.date_label = tk.Label(self.cons_frame, text="Date")
        self.date_label.grid(row=0, column=0, padx=10)
        self.validate_date_cmd = self.master.register(self.validate_date)
        self.date_entry = tk.Entry(self.cons_frame, validate="key", validatecommand=(self.validate_date_cmd, '%P'))
        self.date_entry.grid(row=0, column=1, padx=10)

        # Reason Entry
        self.reason_label = tk.Label(self.cons_frame, text="Reason")
        self.reason_label.grid(row=1, column=0, padx=10)
        self.reason_entry = tk.Entry(self.cons_frame)
        self.reason_entry.grid(row=1, column=1, padx=10)

        # Fee Entry
        self.fee_label = tk.Label(self.cons_frame, text="Fee")
        self.fee_label.grid(row=2, column=0, padx=10)
        self.fee_entry = tk.Entry(self.cons_frame)
        self.fee_entry.grid(row=2, column=1, padx=10)

        # Buttons Frame for Assign and Consultation
        self.assign_frame = tk.LabelFrame(self.master, text="Actions", padx=10, pady=10)
        self.assign_frame.pack(pady=10, fill="x")
        
        # Assign doctor & Add consultation buttons
        self.assign_btn = tk.Button(self.assign_frame, text="Assign Doctor")
        self.assign_btn.pack(side=tk.LEFT, padx=5)

        self.consult_btn = tk.Button(self.assign_frame, text="Add Consultation")
        self.consult_btn.pack(side=tk.LEFT, padx=5)

        # Buttons Frame for Doctor, Patient and Consultation Info
        self.info_frame = tk.LabelFrame(self.master, text="Information", padx=10, pady=10)
        self.info_frame.pack(pady=10, fill="x")
        
        self.btn_show_doctor_info = tk.Button(self.info_frame, text="Doctor Information")
        self.btn_show_doctor_info.pack(side=tk.LEFT, padx=5)

        self.btn_show_patient_info = tk.Button(self.info_frame, text="Patient Information")
        self.btn_show_patient_info.pack(side=tk.LEFT, padx=5)

        self.btn_show_consultation_report = tk.Button(self.info_frame, text="Consultation Report")
        self.btn_show_consultation_report.pack(side=tk.LEFT, padx=5)

    def validate_date(self, date_str):
        import re
        # Updated regex to allow partial date input while being typed
        if re.match(r'(\d{1,2}/?)?(\d{1,2}/?)?(\d{0,4})?$', date_str) or not date_str:
            return True
        else:
            messagebox.showwarning("Invalid Date", "❗️ Please enter date in dd/mm/yyyy format")
            return False
    
    

