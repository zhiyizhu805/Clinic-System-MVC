import tkinter as tk
from Controllers.medical_center_controller import MedicalCenterAppController


def main():
    root = tk.Tk()
    app = MedicalCenterAppController(root)
    root.mainloop()

if __name__ == "__main__":
    main()
