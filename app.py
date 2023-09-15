import tkinter as tk
from Controllers.medical_center_controller import MedicalCenterAppController



def main():
    # Initializing the main tkinter window
    root = tk.Tk()
    # Creating an instance of the MedicalCenterAppController with the main window as its master
    app = MedicalCenterAppController(root)
    # Starting the main event loop of tkinter
    root.mainloop()


if __name__ == "__main__":
    main()
