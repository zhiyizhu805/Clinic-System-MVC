import tkinter as tk
from Controllers.medical_center_controller import MedicalCenterAppController
# from Controllers.medical_center_controller import Clinic

def main():
    # clinic = Clinic()
    root = tk.Tk()
    app = MedicalCenterAppController(root)
    root.mainloop()

if __name__ == "__main__":
    main()
