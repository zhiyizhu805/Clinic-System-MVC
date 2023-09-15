import tkinter as tk
import tkinter.messagebox as messagebox
import datetime
import re

class MedicalCenterAppView:
    def __init__(self, master):
        self.master = master
        self.master.title("Medical Center Application")

        # Frame for doctors and patients listbox
        self.listbox_frame = tk.Frame(self.master, padx=10, pady=10)
        self.listbox_frame.pack(pady=20)

        # Patient Label and Listbox
        self.patient_label = tk.Label(self.listbox_frame, text="All Patients")
        self.patient_label.grid(row=0, column=1, padx=10)
        self.patient_listbox = tk.Listbox(self.listbox_frame, width=40, height=10, exportselection=False)
        self.patient_listbox.grid(row=1, column=1, padx=10)
        
        # Doctor Label and Listbox
        self.doctor_label = tk.Label(self.listbox_frame, text="All Doctors")
        self.doctor_label.grid(row=0, column=0, padx=10)
        self.doctor_listbox = tk.Listbox(self.listbox_frame, width=40, height=10, exportselection=False)
        self.doctor_listbox.grid(row=1, column=0, padx=10)

        # Consultation Frame
        self.cons_frame = tk.LabelFrame(self.master, text="Consultation Details", padx=10, pady=10)
        self.cons_frame.pack(padx=15, pady=15, fill="x")

        # Date Entry with validation
        self.date_label = tk.Label(self.cons_frame, text="Date")
        self.date_label.grid(row=0, column=0, padx=10)
        self.validate_date_cmd = self.master.register(self.validate_date)
        self.date_entry = tk.Entry(self.cons_frame, validate="focusout", validatecommand=(self.validate_date_cmd, '%P'))
        self.date_entry.grid(row=0, column=1, padx=10)

        # Reason Entry
        self.reason_label = tk.Label(self.cons_frame, text="Reason")
        self.reason_label.grid(row=1, column=0, padx=10)
        self.reason_entry = tk.Entry(self.cons_frame)
        self.reason_entry.grid(row=1, column=1, padx=10)

        # Fee Entry with validation
        self.fee_label = tk.Label(self.cons_frame, text="Fee")
        self.fee_label.grid(row=2, column=0, padx=10)
        self.validate_fee_cmd = self.master.register(self.validate_fee)
        self.fee_entry = tk.Entry(self.cons_frame, validate="focusout", validatecommand=(self.validate_fee_cmd, '%P'))
        self.fee_entry.grid(row=2, column=1, padx=10)

        # Action Buttons Frame
        self.assign_frame = tk.LabelFrame(self.master, text="Actions", padx=10, pady=10)
        self.assign_frame.pack(padx=15, pady=15, fill="x")
        
        # Assign doctor & Add consultation buttons
        self.assign_btn = tk.Button(self.assign_frame, text="Assign Doctor")
        self.assign_btn.pack(side=tk.LEFT, padx=5)

        self.consult_btn = tk.Button(self.assign_frame, text="Add Consultation")
        self.consult_btn.pack(side=tk.LEFT, padx=5)

        # Info Buttons Frame
        self.info_frame = tk.LabelFrame(self.master, text="Information", padx=10, pady=10)
        self.info_frame.pack(padx=15, pady=15, fill="x")
        
        self.btn_show_doctor_info = tk.Button(self.info_frame, text="Doctor Information")
        self.btn_show_doctor_info.pack(side=tk.LEFT, padx=5)

        self.btn_show_patient_info = tk.Button(self.info_frame, text="Patient Information")
        self.btn_show_patient_info.pack(side=tk.LEFT, padx=5)

        self.btn_show_consultation_report = tk.Button(self.info_frame, text="Consultation Report")
        self.btn_show_consultation_report.pack(side=tk.LEFT, padx=5)



    def validate_date(self, date_str):
        """Validate date format."""
        # Regex to validate complete date format
        if re.match(r'^(0?[1-9]|[12][0-9]|3[01])/(0?[1-9]|1[0-2])/\d{4}$', date_str):
            # Try to create a date object to check if the date is valid
            try:
                datetime.datetime.strptime(date_str, '%d/%m/%Y')
                return True
            except ValueError:
                # If the creation of the date object fails, it's an invalid date
                messagebox.showwarning("Invalid date","❗️ Please enter a valid date in dd/mm/yyyy format")
                return False
        else:
            messagebox.showwarning("Invalid date","❗️ Please enter a valid date in dd/mm/yyyy format")
            return False



    def validate_fee(self, fee_str):
        """Validate fee format."""
        import re
        # Regex allows partial matches to accommodate for progressive input
        if re.match(r'^\d*(\.\d{0,2})?$', fee_str) or not fee_str:
            return True
        else:
            messagebox.showwarning("Invalid Fee", "❗️ Please enter a valid fee (e.g., 100 or 100.50).")
            return False
    


