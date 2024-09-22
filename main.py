import tkinter as tk
from Screens import NMITPortal

def run_portal():
    root = tk.Tk()
    root.title("https://nmit.EduTrack.in/")
    app = NMITPortal(root)
    app.create_choose_screen()
    root.mainloop()  # Start the Tkinter event loop
    

if __name__ == "__main__":
    run_portal()

































