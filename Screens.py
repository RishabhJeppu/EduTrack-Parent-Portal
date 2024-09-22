import tkinter as tk
from tkinter import ttk, messagebox
from DBMS import get_db_connection  # Updated to use the MySQL connection function
from PIL import Image, ImageTk
import mysql.connector
import sqlite3
from tkcalendar import DateEntry
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class NMITPortal:
    
    def __init__(self, root):
        self.root = root
        self.header_font = ("Helvetica", 18, "bold")
        self.subheader_font = ("Helvetica", 14)
        self.notice_font = ("Helvetica", 12)
        
        # Set fullscreen
        self.root.attributes('-fullscreen', True)
        
        # Bind the Escape key to exit fullscreen mode
        self.root.bind("<Escape>", self.exit_fullscreen)
        
        self.create_choose_screen()


    # Teacher Student Page
    def create_choose_screen(self):
        # Clear the current screen
        for widget in self.root.winfo_children():
            widget.destroy()

        # Left section (1/2 of the screen)
        left_frame = tk.Frame(self.root, bg="#2d3748", padx=20, pady=20)
        left_frame.pack(side="left", fill="both", expand=True)

        # Right section (1/2 of the screen)
        right_frame = tk.Frame(self.root, bg="#2b6cb0", padx=20, pady=20)
        right_frame.pack(side="right", fill="both", expand=True)

        # Left section content
        header_frame = tk.Frame(left_frame, bg="#2d3748")
        header_frame.pack(anchor="w", pady=10)
        tk.Label(header_frame, text="Nitte Meenakshi Institute of Technology", font=self.header_font, fg="white", bg="#2d3748").pack(anchor="w")
        tk.Label(header_frame, text="Bengaluru-560064", font=self.subheader_font, fg="white", bg="#2d3748").pack(anchor="w")

        tk.Label(left_frame, text="Welcome to NMIT", font=self.header_font, fg="white", bg="#2d3748", pady=20).pack(anchor="w")
        tk.Label(left_frame, text="""Nitte Meenakshi Institute of Technology is an autonomous engineering college in Bangalore, Karnataka,\nIndia affiliated to the Visvesvaraya Technological University, Belagavi.""", wraplength=600, font=self.subheader_font, fg="white",
                 bg="#2d3748", pady=20, anchor="w", justify="left").pack(anchor="w")

        notice_board_frame = tk.Frame(left_frame, bg="white", padx=20, pady=20, relief="raised")
        notice_board_frame.pack(anchor="w", pady=20, fill="x")
        tk.Label(notice_board_frame, text="Notice Board", font=self.header_font, fg="black", bg="white").pack(anchor="w")
        tk.Label(notice_board_frame, text="Welcome to the preview of the new mobile friendly parent portal", wraplength=600,
                 font=self.notice_font, fg="black", bg="white").pack(anchor="w", pady=10)

        # Right section content
        button_frame = tk.Frame(right_frame, bg="#2c5282", padx=20, pady=20, relief="raised")
        button_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)  # Center the frame

        student_button = tk.Button(button_frame, text="Student", font=self.header_font, bg="#dd6b20", fg="white",
                                   command=self.student_login_screen, width=25, height=4)  # Increased button size
        student_button.pack(pady=10, fill="x")

        teacher_button = tk.Button(button_frame, text="Teacher", font=self.header_font, bg="#dd6b20", fg="white",
                                   command=self.teacher_login_screen, width=25, height=4)  # Increased button size
        teacher_button.pack(pady=10, fill="x")


    def student_login_screen(self):
        # Clear the current screen
        for widget in self.root.winfo_children():
            widget.destroy()

        # Left section (2/3 of the screen)
        left_frame = tk.Frame(self.root, bg="#2d3748", padx=20, pady=20)
        left_frame.grid(row=0, column=0, sticky="nsew")

        # Right section (1/3 of the screen)
        right_frame = tk.Frame(self.root, bg="#2b6cb0", padx=20, pady=20)
        right_frame.grid(row=0, column=1, sticky="nsew")

        # Left section content
        header_frame = tk.Frame(left_frame, bg="#2d3748")
        header_frame.pack(anchor="w", pady=10)
        tk.Label(header_frame, text="Nitte Meenakshi Institute of Technology", font=self.header_font, fg="white", bg="#2d3748").pack(anchor="w")
        tk.Label(header_frame, text="Bengaluru-560064", font=self.subheader_font, fg="white", bg="#2d3748").pack(anchor="w")

        tk.Label(left_frame, text="Welcome to NMIT", font=self.header_font, fg="white", bg="#2d3748", pady=20).pack(anchor="w")
        tk.Label(left_frame, text="""Nitte Meenakshi Institute of Technology is an autonomous engineering college in Bangalore, Karnataka,\nIndia affiliated to the Visvesvaraya Technological University, Belagavi.""", wraplength=600, font=self.subheader_font, fg="white",
                bg="#2d3748", pady=20, anchor="w", justify="left").pack(anchor="w")

        notice_board_frame = tk.Frame(left_frame, bg="white", padx=20, pady=20, relief="raised")
        notice_board_frame.pack(anchor="w", pady=20, fill="x")
        tk.Label(notice_board_frame, text="Notice Board", font=self.header_font, fg="black", bg="white").pack(anchor="w")
        tk.Label(notice_board_frame, text="Welcome to the preview of the new mobile friendly parent portal", wraplength=600,
                font=self.notice_font, fg="black", bg="white").pack(anchor="w", pady=10)

        # Right section content
        login_frame = tk.Frame(right_frame, bg="#2c5282", padx=20, pady=20, relief="raised")
        login_frame.pack(anchor="e", pady=20, fill="x")
        tk.Label(login_frame, text="Login to Your Account", font=self.header_font, fg="white", bg="#2c5282").pack(anchor="w")

        tk.Label(login_frame, text="Username", font=self.subheader_font, fg="white", bg="#2c5282").pack(anchor="w", pady=10)
        self.username_entry = tk.Entry(login_frame, bg="white", fg="black", font=self.subheader_font)
        self.username_entry.pack(anchor="w", fill="x")

        tk.Label(login_frame, text="Password", font=self.subheader_font, fg="white", bg="#2c5282").pack(anchor="w", pady=10)
        password_frame = tk.Frame(login_frame, bg="#2c5282")
        password_frame.pack(anchor="w", fill="x")

        days = [str(day).zfill(2) for day in range(1, 32)]
        months = [str(month).zfill(2) for month in range(1, 13)]
        years = [str(year) for year in range(1980, 2025)]

        self.day_combobox = ttk.Combobox(password_frame, values=days, font=self.subheader_font)
        self.day_combobox.set("Day")
        self.day_combobox.pack(side="left", padx=2, fill="x", expand=True)
        self.month_combobox = ttk.Combobox(password_frame, values=months, font=self.subheader_font)
        self.month_combobox.set("Month")
        self.month_combobox.pack(side="left", padx=2, fill="x", expand=True)
        self.year_combobox = ttk.Combobox(password_frame, values=years, font=self.subheader_font)
        self.year_combobox.set("Year")
        self.year_combobox.pack(side="left", padx=2, fill="x", expand=True)

        login_button = tk.Button(login_frame, text="LOGIN", font=self.header_font, bg="#dd6b20", fg="white", command=self.student_page)
        login_button.pack(anchor="w", pady=20, fill="x")

        # Back button
        back_button = tk.Button(right_frame, text="Back", font=self.header_font, bg="#dd6b20", fg="white", command=self.create_choose_screen)
        back_button.pack(anchor="se", pady=10)

        # Configure grid weights for responsiveness
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=2)
        self.root.grid_columnconfigure(1, weight=1)


    def student_page(self):
        username = self.username_entry.get()
        day = self.day_combobox.get()
        month = self.month_combobox.get()
        year = self.year_combobox.get()
        password = f"{day}/{month}/{year}"

        conn = get_db_connection()
        if conn:
            cursor = conn.cursor()
            name_query = "SELECT Name FROM student where USN=%s"
            query = "SELECT * FROM student WHERE USN=%s AND password=%s"
            cursor.execute(query, (username, password))
            result = cursor.fetchone()
            cursor.execute(name_query, (username,))
            name = cursor.fetchone()
            name = name[0] if name else None

            if result:
                self.main_student_page(name, username)  # Call main_page function upon successful login
            else:
                messagebox.showerror("Login", "Incorrect username or password")

            cursor.close()
            conn.close()
        else:
            messagebox.showerror("Login", "Database connection failed") 

    # Teacher login screen
    def teacher_login_screen(self):
        # Clear the current screen
        for widget in self.root.winfo_children():
            widget.destroy()
        
        # Left section (1/2 of the screen)
        left_frame = tk.Frame(self.root, bg="#2d3748", padx=20, pady=20)
        left_frame.grid(row=0, column=0, sticky="nsew")

        # Right section (1/2 of the screen)
        right_frame = tk.Frame(self.root, bg="#2b6cb0", padx=20, pady=20)
        right_frame.grid(row=0, column=1, sticky="nsew")

        # Left section content
        header_frame = tk.Frame(left_frame, bg="#2d3748")
        header_frame.pack(anchor="w", pady=10)
        tk.Label(header_frame, text="Nitte Meenakshi Institute of Technology", font=self.header_font, fg="white", bg="#2d3748").pack(anchor="w")
        tk.Label(header_frame, text="Bengaluru-560064", font=self.subheader_font, fg="white", bg="#2d3748").pack(anchor="w")

        tk.Label(left_frame, text="Welcome to NMIT", font=self.header_font, fg="white", bg="#2d3748", pady=20).pack(anchor="w")
        tk.Label(left_frame, text="""Nitte Meenakshi Institute of Technology is an autonomous engineering college in Bangalore, Karnataka,\nIndia affiliated to the Visvesvaraya Technological University, Belagavi.""", wraplength=600, font=self.subheader_font, fg="white",
                 bg="#2d3748", pady=20, anchor="w", justify="left").pack(anchor="w")

        notice_board_frame = tk.Frame(left_frame, bg="white", padx=20, pady=20, relief="raised")
        notice_board_frame.pack(anchor="w", pady=20, fill="x")
        tk.Label(notice_board_frame, text="Notice Board", font=self.header_font, fg="black", bg="white").pack(anchor="w")
        tk.Label(notice_board_frame, text="Welcome to the preview of the new mobile friendly parent portal", wraplength=600,
                 font=self.notice_font, fg="black", bg="white").pack(anchor="w", pady=10)

        # Right section content
        login_frame = tk.Frame(right_frame, bg="#2c5282", padx=20, pady=20, relief="raised")
        login_frame.pack(anchor="e", pady=20, fill="x")
        tk.Label(login_frame, text="Login to Your Account", font=self.header_font, fg="white", bg="#2c5282").pack(anchor="w")

        tk.Label(login_frame, text="Username", font=self.subheader_font, fg="white", bg="#2c5282").pack(anchor="w", pady=10)
        self.username_entry = tk.Entry(login_frame, bg="white", fg="black", font=self.subheader_font)
        self.username_entry.pack(anchor="w", fill="x")

        tk.Label(login_frame, text="Password", font=self.subheader_font, fg="white", bg="#2c5282").pack(anchor="w", pady=10)
        self.password_entry = tk.Entry(login_frame, bg="white", fg="black", font=self.subheader_font, show="*")
        self.password_entry.pack(anchor="w", fill="x")

        login_button = tk.Button(login_frame, text="LOGIN", font=self.header_font, bg="#dd6b20", fg="white", command=self.teacher_page)
        login_button.pack(anchor="w", pady=20, fill="x")

        # Back button
        back_button = tk.Button(right_frame, text="Back", font=self.header_font, bg="#dd6b20", fg="white", command=self.create_choose_screen)
        back_button.pack(anchor="se", pady=10)

        # Configure grid weights for responsiveness
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_columnconfigure(1, weight=1)


    def teacher_page(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        conn = get_db_connection()
        if conn:
            cursor = conn.cursor()
            name_query = "SELECT Name FROM teachers WHERE Username=%s"
            subject_query = "SELECT Course_name FROM courses c, teachers t WHERE t.teacherID=c.teacherID AND Username=%s"
            code_query = "SELECT Course_code FROM courses c, teachers t WHERE t.teacherID=c.teacherID AND Username=%s"
            query = "SELECT * FROM teachers WHERE Username=%s AND Password=%s"
            cursor.execute(query, (username, password))
            result = cursor.fetchone()
            cursor.execute(name_query, (username,))
            name = cursor.fetchone()
            name = name[0] if name else None
            cursor.execute(subject_query, (username,))
            subject = cursor.fetchone()
            cursor.execute(code_query, (username,))
            code = cursor.fetchone()
    
            if result:
                self.main_teacher_page(name, subject, code)
            else:
                messagebox.showerror("Login", "Incorrect username or password")

            cursor.close()
            conn.close()
        else:
            messagebox.showerror("Login", "Database connection failed")

    
    def main_student_page(self, name: str, username: str):
        courses = [
            {"code": "22MAT41A", "name": "APPLIED DISCRETE MATHEMATICAL STRUCTURES AND GRAPH THEORY"},
            {"code": "22CS42", "name": "SOFTWARE ENGINEERING AND PROJECT MANAGEMENT"},
            {"code": "22CS43", "name": "DESIGN AND ANALYSIS OF ALGORITHMS"},
            {"code": "22CSG44", "name": "DATABASE MANAGEMENT SYSTEM"},
            {"code": "22CSB48", "name": "BIOLOGY FOR ENGINEERS"},
            {"code": "22EVS411", "name": "ENVIRONMENTAL STUDIES"},
        ]

        # Clear the current screen
        for widget in self.root.winfo_children():
            widget.destroy()

        # Create the header frame
        header_frame = tk.Frame(self.root, bg="#333333")
        header_frame.pack(fill="x")

        # Configure the grid layout for the header frame
        header_frame.grid_columnconfigure(0, weight=1)
        header_frame.grid_columnconfigure(1, weight=1)
        header_frame.grid_columnconfigure(2, weight=1)

        # Add the institution's logo
        logo = Image.open("nitte_logo.png")  # Path to the logo image
        logo = logo.resize((50, 50))
        logo_image = ImageTk.PhotoImage(logo)
        logo_label = tk.Label(header_frame, image=logo_image, bg="#333333")
        logo_label.image = logo_image
        logo_label.grid(row=0, column=0, padx=10, pady=10, rowspan=2, sticky='nw')

        # Add the institution's name in the center
        institution_name = tk.Label(header_frame, text="Nitte Meenakshi Institute of Technology\nBengaluru-560064", fg="white", bg="#333333", font=("Helvetica", 16))
        institution_name.grid(row=0, column=1, padx=10, pady=10, sticky='n')

        # Add the student's profile picture and details
        profile_frame = tk.Frame(header_frame, bg="#333333")
        profile_frame.grid(row=0, column=2, padx=10, sticky='ne')

        student_details = tk.Label(profile_frame, text=f"{name}\n{username}\nB.E-CS, SEM 04", fg="white", bg="#333333", font=("Helvetica", 12))
        student_details.pack(side="left", padx=10)

        # Add the navigation menu with LOGOUT button
        nav_frame = tk.Frame(header_frame, bg="#333333")
        nav_frame.grid(row=1, column=2, padx=10, sticky='ne')

        # Display the student's name
        student_name = name  # Replace with actual logged-in student's name
        tk.Label(self.root, text=f"Welcome, {student_name}", font=self.header_font).pack(pady=10)

        # Create the table
        table_frame = tk.Frame(self.root)
        table_frame.pack(fill="both", expand=True, padx=50, pady=70)  # Add padding to the table frame

        # Create the table headers
        headers = ["COURSE CODE", "COURSE NAME", "ATTENDANCE", "CIE"]
        for col, header in enumerate(headers):
            tk.Label(table_frame, text=header, font=self.subheader_font, borderwidth=2, relief="solid", width=20).grid(row=0, column=col, sticky="nsew", padx=1, pady=1)

        # Populate the table with courses
        for row, course in enumerate(courses, start=1):
            tk.Label(table_frame, text=course["code"], borderwidth=2, relief="solid", width=20, font=('Helvetica', 12)).grid(row=row, column=0, sticky="nsew", padx=1, pady=1)
            tk.Label(table_frame, text=course["name"], borderwidth=2, relief="solid", width=60, font=('Helvetica', 12)).grid(row=row, column=1, sticky="nsew", padx=1, pady=1)

            attendance_button = tk.Button(table_frame, text="ATTENDANCE", bg="green", fg="white", width=10,
                                          command=lambda course_code=course["code"]: self.attendance(name, username, course_code))
            attendance_button.grid(row=row, column=2, sticky="nsew", padx=1, pady=1)

            cie_frame = tk.Frame(table_frame, width=10)
            cie_frame.grid(row=row, column=3, sticky="nsew", padx=1, pady=1)
            cie_button = tk.Button(cie_frame, text="CIE", bg="#03A9F4", fg="white", width=10, command=lambda course=course: self.CIE(name, username, course))

            cie_button.pack(side="left", expand=True, fill="x")

        # Configure the grid to ensure equal column widths
        table_frame.grid_columnconfigure(0, weight=1)
        table_frame.grid_columnconfigure(1, weight=2)
        table_frame.grid_columnconfigure(2, weight=1)
        table_frame.grid_columnconfigure(3, weight=1)

        # Add the bottom frame
        bottom_frame = tk.Frame(self.root, bg="#333333")
        bottom_frame.pack(side="bottom", fill="x")

        # Add the logout button to the table frame below the table
        logout_button = tk.Button(table_frame, text="LOGOUT", bg="red", fg="white", font=("Helvetica", 12),
                                  command=self.create_choose_screen)
        logout_button.grid(row=len(courses) + 1, column=3, sticky="e", padx=10, pady=10)

        # Add the copyright and powered by text
        copyright_label = tk.Label(bottom_frame, text="Copyright © Powered By: EduTrack", fg="white", bg="#333333", font=("Helvetica", 14))
        copyright_label.pack(side="left", padx=10, pady=5)

        # Add the terms of service and privacy policy text
        terms_label = tk.Label(bottom_frame, text="Terms of Service | Privacy Policy", fg="white", bg="#333333", font=("Helvetica", 14))
        terms_label.pack(side="right", padx=10, pady=5)


    def CIE(self, name: str, username: str, subject: dict):
        # Clear the root window
        for widget in self.root.winfo_children():
            widget.destroy()

        # Create top header frame
        top_frame = tk.Frame(self.root, bg='gray', height=100)
        top_frame.pack(fill='x')

        # Configure grid layout
        top_frame.grid_columnconfigure(0, weight=1)
        top_frame.grid_columnconfigure(1, weight=1)
        top_frame.grid_columnconfigure(2, weight=1)

        # Logo
        logo_image = Image.open("nitte_logo.png")  # Replace with actual path to the logo image
        logo_image = logo_image.resize((60, 60))
        logo_photo = ImageTk.PhotoImage(logo_image)
        logo_label = tk.Label(top_frame, image=logo_photo, bg='gray')
        logo_label.image = logo_photo  # Keep a reference to avoid garbage collection
        logo_label.grid(row=0, column=0, padx=10, sticky='nw')  # Moved logo to top left corner

        # Title
        title_label = tk.Label(top_frame, text="Nitte Meenakshi Institute of Technology\nBengaluru-560064", font=self.header_font, bg='gray')
        title_label.grid(row=0, column=1, padx=20, sticky='n')

        # Navigation buttons
        home_button = tk.Button(top_frame, text="HOME", font=self.subheader_font, command=lambda: self.main_student_page(name, username))
        home_button.grid(row=0, column=2, padx=20, sticky='ne')

        # Main content frame
        content_frame = tk.Frame(self.root)
        content_frame.pack(fill='both', expand=True, pady=20)

        internal_assessment = tk.Label(content_frame, text="Internal Assessment", font=self.subheader_font)
        internal_assessment.pack(pady=10)

        final_ia_marks = 0  # Initialize the final IA marks variable

        final_marks_label_text = f"FINAL CIE MARKS OBTAINED: {final_ia_marks}"  # Set initial text for final marks
        final_marks = tk.Label(content_frame, text=final_marks_label_text, bg="green", fg="white", font=self.notice_font)
        final_marks.pack(pady=5)

        subject_title = tk.Label(content_frame, text=f"{subject['name']} ({subject['code']})", font=self.subheader_font)
        subject_title.pack(pady=10)

        # Create a frame for the plot
        plot_frame = tk.Frame(content_frame)
        plot_frame.pack(pady=10)

        # Create the plot
        fig, ax = plt.subplots(figsize=(13, 3))  # Adjusted the figure size to make it shorter
        canvas = FigureCanvasTkAgg(fig, master=plot_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Create the marks table
        marks_frame = ttk.Frame(content_frame)
        marks_frame.pack(pady=10)

        columns = ('component', 'marks_obtained', 'max_marks')
        tree = ttk.Treeview(marks_frame, columns=columns, show='headings', height=6)  # Reduced height

        tree.heading('component', text='Component')
        tree.heading('marks_obtained', text='Marks Obtained')
        tree.heading('max_marks', text='Max Marks')

        tree.pack()

        conn = get_db_connection()
        cursor = conn.cursor()

        # Fetch the marks from the database
        query = '''
        SELECT AssessmentType, MarksObtained
        FROM marks
        WHERE USN = %s AND Course_code = %s
        '''
        cursor.execute(query, (username, subject['code']))
        result = cursor.fetchall()

        # Close the database connection
        conn.close()

        # Prepare the data for the Treeview and plot
        data = [
            ['MSE1', 0, 12],
            ['MSE2', 0, 12],
            ['MSE3', 0, 6],
            ['LA1', 0, 10],
            ['LA2', 0, 10],
            ['FINAL IA', 0, 50],
        ]

        # Map the results to the data
        for row in result:
            assessment_type, marks_obtained = row
            for data_row in data:
                if data_row[0] == assessment_type:
                    data_row[1] = marks_obtained
                    if assessment_type in ['MSE1', 'MSE2', 'MSE3', 'LA1', 'LA2']:
                        final_ia_marks += marks_obtained

        # Update the final IA marks
        for data_row in data:
            if data_row[0] == 'FINAL IA':
                data_row[1] = final_ia_marks

        # Update the final marks label text with the calculated IA marks
        final_marks.config(text=f"FINAL CIE MARKS OBTAINED: {final_ia_marks}")

        # Insert the data into the Treeview
        for row in data:
            tree.insert('', tk.END, values=row)

        # Update the plot data
        components = [row[0] for row in data]
        obtained_marks = [row[1] for row in data]
        max_marks = [row[2] for row in data]

        ax.clear()  # Clear the previous plot
        bars1 = ax.bar(components, max_marks, label='Max Marks', color='#FFA07A')
        bars2 = ax.bar(components, obtained_marks, label='Marks Obtained', color='#87CEEB')
        ax.set_ylabel('Marks')
        ax.legend()

        # Add marks on top of each bar
        for bar, mark in zip(bars2, obtained_marks):
            ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height(), str(mark), ha='center', va='bottom')

        canvas.draw()  # Redraw the canvas

        # Add the bottom frame
        bottom_frame = tk.Frame(self.root, bg="#333333")
        bottom_frame.pack(side="bottom", fill="x")

        # Add the copyright and powered by text
        copyright_label = tk.Label(bottom_frame, text="Copyright © Powered By: EduTrack", fg="white", bg="#333333", font=("Helvetica", 14))
        copyright_label.pack(side="left", padx=10, pady=5)

        # Add the terms of service and privacy policy text
        terms_label = tk.Label(bottom_frame, text="Terms of Service | Privacy Policy", fg="white", bg="#333333", font=("Helvetica", 14))
        terms_label.pack(side="right", padx=10, pady=5)


    def attendance(self, name: str, username: str, course_code: str):
        # Clear the root window
        for widget in self.root.winfo_children():
            widget.destroy()

        # Create top header frame
        top_frame = tk.Frame(self.root, bg='gray', height=100)
        top_frame.pack(fill='x')

        # Configure grid layout
        top_frame.grid_columnconfigure(0, weight=1)
        top_frame.grid_columnconfigure(1, weight=1)
        top_frame.grid_columnconfigure(2, weight=1)

        # Logo
        logo_image = Image.open("nitte_logo.png")  # Replace with actual path to the logo image
        logo_image = logo_image.resize((60, 60))
        logo_photo = ImageTk.PhotoImage(logo_image)
        logo_label = tk.Label(top_frame, image=logo_photo, bg='gray')
        logo_label.image = logo_photo  # Keep a reference to avoid garbage collection
        logo_label.grid(row=0, column=0, padx=10, sticky='nw')  # Moved logo to top left corner

        # Title
        title_label = tk.Label(top_frame, text="Nitte Meenakshi Institute of Technology\nBengaluru-560064", font=self.header_font, bg='gray')
        title_label.grid(row=0, column=1, padx=20, sticky='n')

        # Navigation buttons
        home_button = tk.Button(top_frame, text="HOME", font=self.subheader_font, command=lambda: self.main_student_page(name, username))
        home_button.grid(row=0, column=2, padx=20, sticky='ne')

        # Create content frame
        content_frame = tk.Frame(self.root)
        content_frame.pack(fill='both', expand=True, pady=20)

        # Fetch the attendance data from the database
        conn = get_db_connection()
        cursor = conn.cursor()

        # Query to fetch attendance data
        query = '''
        SELECT Date, Status
        FROM attendence
        WHERE USN = %s AND Course_code = %s
        ORDER BY Date
        '''
        cursor.execute(query, (username, course_code))
        attendance_records = cursor.fetchall()

        conn.close()

        # Calculate attendance statistics
        total_classes = len(attendance_records)
        present_classes = sum(1 for record in attendance_records if record[1] == 'Present')
        absent_classes = total_classes - present_classes
        attendance_percent = (present_classes / total_classes) * 100 if total_classes > 0 else 0
    
        # Attendance Status
        attendance_status_frame = tk.Frame(content_frame)
        attendance_status_frame.pack(pady=10)

        attendance_status_label = tk.Label(attendance_status_frame, text="Attendance Status", font=self.subheader_font)
        attendance_status_label.pack(pady=5)

        status_label_text = f"Present: {present_classes}   Absent: {absent_classes}   Attendance: {attendance_percent:.2f}%"
        status_label = tk.Label(attendance_status_frame, text=status_label_text, font=self.notice_font, bg="green", fg="white")
        status_label.pack(pady=5)

        # Attendance list
        attendance_list_frame = tk.Frame(content_frame)
        attendance_list_frame.pack(pady=10)

        # Present table
        present_label = tk.Label(attendance_list_frame, text=f"Present Classes: {present_classes}", bg="green", fg="white", font=self.subheader_font)
        present_label.grid(row=0, column=0, padx=10, pady=5, sticky='nw')


        present_tree = ttk.Treeview(attendance_list_frame, columns=("SL NO", "DATE", "STATUS"), show='headings')
        present_tree.heading("SL NO", text="SL NO")
        present_tree.heading("DATE", text="DATE")
        present_tree.heading("STATUS", text="STATUS")

        present_tree.grid(row=1, column=0, padx=10, pady=5, sticky='nw')

        # Absent table
        absent_label = tk.Label(attendance_list_frame, text=f"Absent Classes: {absent_classes}", bg="red", fg="white", font=self.subheader_font)
        absent_label.grid(row=0, column=1, padx=10, pady=5, sticky='ne')

        absent_tree = ttk.Treeview(attendance_list_frame, columns=("SL NO", "DATE", "STATUS"), show='headings')
        absent_tree.heading("SL NO", text="SL NO")
        absent_tree.heading("DATE", text="DATE")
        absent_tree.heading("STATUS", text="STATUS")

        absent_tree.grid(row=1, column=1, padx=10, pady=5, sticky='ne')

        # Insert data into the attendance lists
        present_sl_no = 1
        absent_sl_no = 1
        
        for record in attendance_records:
            date, status = record
            if status == 'Present':
                present_tree.insert('', tk.END, values=(present_sl_no, date, status))
                present_sl_no += 1
            else:
                absent_tree.insert('', tk.END, values=(absent_sl_no, date, status))
                absent_sl_no += 1

        # Add the bottom frame
        bottom_frame = tk.Frame(self.root, bg="#333333")
        bottom_frame.pack(side="bottom", fill="x")

        # Add the copyright and powered by text
        copyright_label = tk.Label(bottom_frame, text="Copyright © Powered By: EduTrack", fg="white", bg="#333333", font=("Helvetica", 14))
        copyright_label.pack(side="left", padx=10, pady=5)

        # Add the terms of service and privacy policy text
        terms_label = tk.Label(bottom_frame, text="Terms of Service | Privacy Policy", fg="white", bg="#333333", font=("Helvetica", 14))
        terms_label.pack(side="right", padx=10, pady=5)


    def main_teacher_page(self, name: str, subject: str, code: str):
        # Clear the current screen
        for widget in self.root.winfo_children():
            widget.destroy()

        # Create the header frame
        header_frame = tk.Frame(self.root, bg="#333333")
        header_frame.pack(fill="x")

        # Add the institution's logo and name
        logo = Image.open("nitte_logo.png")  # Path to the logo image
        logo = logo.resize((75, 75))
        logo_image = ImageTk.PhotoImage(logo)
        logo_label = tk.Label(header_frame, image=logo_image, bg="#333333")
        logo_label.image = logo_image
        logo_label.pack(side="left", padx=10, pady=10)

        # Add the teacher's profile picture and details on the right
        profile_frame = tk.Frame(header_frame, bg="#333333")
        profile_frame.pack(side="right", padx=10)

        teacher_details = tk.Label(profile_frame, text=f"{name}\n", fg="white", bg="#333333", font=("Helvetica", 12))
        teacher_details.pack(side="left", padx=10)

        # Center the institution name and align it with the teacher's name
        institution_frame = tk.Frame(header_frame, bg="#333333")
        institution_frame.pack(side="top", pady=10, expand=True)
        
        institution_name = tk.Label(institution_frame, text="Nitte Meenakshi Institute of Technology\nBengaluru-560064", fg="white", bg="#333333", font=("Helvetica", 16))
        institution_name.pack()

        # Display the teacher's name
        teacher_name = name  # Replace with actual logged-in teacher's name
        tk.Label(self.root, text=f"Welcome, {teacher_name}", font=self.header_font).pack(pady=(1, 1))

        # Create the main frame for subject buttons
        subject_frame = tk.Frame(self.root, bg="#f0f0f0", padx=5, pady=5)
        subject_frame.pack(fill="both", expand=True, padx=10, pady=10)

        # Move the subject name, attendance, and marks buttons closer to the welcome message
        middle_frame = tk.Frame(subject_frame, bg="#f0f0f0")
        middle_frame.pack(pady=0, expand=True)  # Adjust 'pady' to move buttons up

        # Add the subject name
        subject_label = tk.Label(middle_frame, text=subject, font=self.header_font, anchor="w")
        subject_label.pack(fill="x", pady=(0, 50))  # Adjust 'pady' to move subject label up

        # Add the buttons for "Attendance" and "Marks"
        attendance_button = tk.Button(middle_frame, text="Attendance", bg="blue", fg="white", font=("Helvetica", 20), command=lambda: self.mark_attendance(name, subject, code))
        attendance_button.pack(fill="x", pady=(0, 50))  # Adjust 'pady' to move attendance button up

        marks_button = tk.Button(middle_frame, text="Marks", bg="blue", fg="white", font=("Helvetica", 20), command=lambda: self.choose_student_marks(name, subject, code))
        marks_button.pack(fill="x", pady=(0, 50))  # Adjust 'pady' to move marks button up

        # Add a frame for the logout button to position it correctly
        logout_frame = tk.Frame(middle_frame, bg="#f0f0f0")
        logout_frame.pack(fill="x")

        logout_button = tk.Button(logout_frame, text="Logout", bg="red", fg="white", font=("Helvetica", 20), command=self.create_choose_screen)
        logout_button.pack(anchor="e", padx=10, pady=10)

        # Add the bottom frame
        bottom_frame = tk.Frame(self.root, bg="#333333")
        bottom_frame.pack(side="bottom", fill="x")

        # Add the copyright and powered by text
        copyright_label = tk.Label(bottom_frame, text="Copyright © Powered By: EduTrack", fg="white", bg="#333333", font=("Helvetica", 14))
        copyright_label.pack(side="left", padx=10, pady=5)

        # Add the terms of service and privacy policy text
        terms_label = tk.Label(bottom_frame, text="Terms of Service | Privacy Policy", fg="white", bg="#333333", font=("Helvetica", 14))
        terms_label.pack(side="right", padx=10, pady=5)

    
    def choose_student_marks(self, name: str, subject: str, code: str):
        self.clear_screen()

        # Add header
        header_frame = tk.Frame(self.root, bg="#003366")
        header_frame.pack(fill="x")

        # Place the logo in the top left corner
        img = Image.open("nitte_logo.png")  # Replace with the path to the student's image
        img = img.resize((75, 75))
        photo = ImageTk.PhotoImage(img)
        tk.Label(header_frame, image=photo, bg="#003366").grid(row=0, column=0, rowspan=2, padx=10, pady=10, sticky="w")

        # Add the labels in the center without spacing
        center_label_frame = tk.Frame(header_frame, bg="#003366")
        center_label_frame.grid(row=0, column=1, columnspan=2, padx=5, pady=10, sticky="ew")
        
        tk.Label(center_label_frame, text="Nitte Meenakshi Institute of Technology", font=self.header_font, fg="white", bg="#003366").pack()
        tk.Label(center_label_frame, text="Bengaluru-560064", font=self.subheader_font, fg="white", bg="#003366").pack()

        # Add HOME button in the top right corner
        tk.Button(header_frame, text="HOME", font=self.subheader_font, command=lambda: self.main_teacher_page(name, subject, code)).grid(row=0, column=3, rowspan=2, padx=10, pady=10, sticky="e")

        # Make sure the header frame's columns expand appropriately
        header_frame.grid_columnconfigure(1, weight=1)

        # Add student's details section
        details_frame = tk.Frame(self.root, bg="#e6e6e6", pady=20)
        details_frame.pack(fill="x")

        # Add form to update marks
        form_frame = tk.Frame(self.root, pady=80)
        form_frame.pack()

        tk.Label(form_frame, text="Enter USN:", font=self.subheader_font).pack(pady=5)
        self.usn_entry = tk.Entry(form_frame, font=self.subheader_font)
        self.usn_entry.pack(pady=5)

        tk.Label(form_frame, text="Enter Assessment Type (MSE1, MSE2, MSE3, LA1, LA2):", font=self.subheader_font).pack(pady=5)
        self.assessment_type_entry = tk.Entry(form_frame, font=self.subheader_font)
        self.assessment_type_entry.pack(pady=5)

        tk.Label(form_frame, text="Enter Marks Obtained:", font=self.subheader_font).pack(pady=5)
        self.marks_entry = tk.Entry(form_frame, font=self.subheader_font)
        self.marks_entry.pack(pady=5)

        tk.Button(form_frame, text="Enter Marks", font=self.subheader_font, bg='#003366', fg='white', command=lambda: self.enter_marks(code)).pack(pady=20)
        tk.Button(form_frame, text="Update Marks", font=self.subheader_font, bg='#003366', fg='white', command=lambda: self.update_marks(code)).pack(pady=20)
        tk.Button(form_frame, text="Clear", font=self.subheader_font, bg='#003366', fg='white', command=self.clear_inputs).pack(pady=10)

        # Keep the reference to the image
        self.photo = photo

        # Add the bottom frame
        bottom_frame = tk.Frame(self.root, bg="#333333")
        bottom_frame.pack(side="bottom", fill="x")

        # Add the copyright and powered by text
        copyright_label = tk.Label(bottom_frame, text="Copyright © Powered By: EduTrack", fg="white", bg="#333333", font=("Helvetica", 14))
        copyright_label.pack(side="left", padx=10, pady=5)

        # Add the terms of service and privacy policy text
        terms_label = tk.Label(bottom_frame, text="Terms of Service | Privacy Policy", fg="white", bg="#333333", font=("Helvetica", 14))
        terms_label.pack(side="right", padx=10, pady=5)


    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def clearo_inputs(self):
        self.usn_entry.delete(0, tk.END)
        self.assessment_type_entry.delete(0, tk.END)
        self.marks_entry.delete(0, tk.END)
        

    def enter_marks(self, code: str):
        usn = self.usn_entry.get().strip()
        course_code = code[0]
        assessment_type = self.assessment_type_entry.get().strip().upper()
        marks_obtained = self.marks_entry.get().strip()

        if not usn or not course_code or not assessment_type or not marks_obtained:
            messagebox.showerror("Input Error", "All fields are required")
            return

        if assessment_type not in ['MSE1', 'MSE2', 'MSE3', 'LA1', 'LA2']:
            messagebox.showerror("Input Error", "Invalid assessment type")
            return

        try:
            marks_obtained = int(marks_obtained)
        except ValueError:
            messagebox.showerror("Input Error", "Marks obtained must be an integer")
            return

        # Validate the marks based on the assessment type
        if assessment_type in ['MSE1', 'MSE2', 'MSE3'] and (marks_obtained < 0 or marks_obtained > 30):
            messagebox.showerror("Input Error", f"Marks for {assessment_type} should be between 0 and 30")
            return
        elif assessment_type in ['LA1', 'LA2'] and (marks_obtained < 0 or marks_obtained > 10):
            messagebox.showerror("Input Error", f"Marks for {assessment_type} should be between 0 and 10")
            return

        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            # Check if the USN is present in the student table
            cursor.execute("SELECT 1 FROM student WHERE USN = %s", (usn,))
            if cursor.fetchone() is None:
                messagebox.showerror("Input Error", "USN not found in the student table")
                return

            # Check if the marks already exist for the given USN, course code, and assessment type
            cursor.execute("""
                SELECT 1 FROM marks
                WHERE USN = %s AND Course_code = %s AND AssessmentType = %s
            """, (usn, course_code, assessment_type))
            if cursor.fetchone():
                messagebox.showerror("Input Error", "Marks for this assessment type already exist")
                return

            # Calculate the converted marks based on the assessment type
            if assessment_type in ['MSE1', 'MSE2']:
                converted_marks = marks_obtained * 0.4  # 40% of the marks
            elif assessment_type == 'MSE3':
                converted_marks = marks_obtained * 0.2  # 20% of the marks
            elif assessment_type in ['LA1', 'LA2']:
                converted_marks = marks_obtained  # No conversion needed, out of 10

            # Insert the marks in the database
            insert_query = """
                INSERT INTO marks (USN, Course_code, AssessmentType, MarksObtained)
                VALUES (%s, %s, %s, %s)
            """
            
            cursor.execute(insert_query, (usn, course_code, assessment_type, converted_marks))
            
            conn.commit()
            messagebox.showinfo("Success", "Marks entered successfully")
        
        except mysql.connector.Error as err:
            messagebox.showerror("Database Error", f"Error: {err}")
        
        finally:
            cursor.close()
            conn.close()


    def update_marks(self, code: str):
        usn = self.usn_entry.get().strip()
        course_code = code[0]
        assessment_type = self.assessment_type_entry.get().strip().upper()
        marks_obtained = self.marks_entry.get().strip()

        if not usn or not course_code or not assessment_type or not marks_obtained:
            messagebox.showerror("Input Error", "All fields are required")
            return

        if assessment_type not in ['MSE1', 'MSE2', 'MSE3', 'LA1', 'LA2']:
            messagebox.showerror("Input Error", "Invalid assessment type")
            return

        try:
            marks_obtained = int(marks_obtained)
        except ValueError:
            messagebox.showerror("Input Error", "Marks obtained must be an integer")
            return

        # Validate the marks based on the assessment type
        if assessment_type in ['MSE1', 'MSE2', 'MSE3'] and (marks_obtained < 0 or marks_obtained > 30):
            messagebox.showerror("Input Error", f"Marks for {assessment_type} should be between 0 and 30")
            return
        elif assessment_type in ['LA1', 'LA2'] and (marks_obtained < 0 or marks_obtained > 10):
            messagebox.showerror("Input Error", f"Marks for {assessment_type} should be between 0 and 10")
            return

        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            # Check if the USN is present in the student table
            cursor.execute("SELECT 1 FROM student WHERE USN = %s", (usn,))
            if cursor.fetchone() is None:
                messagebox.showerror("Input Error", "USN not found in the student table")
                return

            # Check if the marks exist for the given USN, course code, and assessment type
            cursor.execute("""
                SELECT 1 FROM marks
                WHERE USN = %s AND Course_code = %s AND AssessmentType = %s
            """, (usn, course_code, assessment_type))
            if cursor.fetchone() is None:
                messagebox.showerror("Input Error", "Marks for this assessment type do not exist. Use 'Enter Marks' to add new marks.")
                return

            # Calculate the converted marks based on the assessment type
            if assessment_type in ['MSE1', 'MSE2']:
                converted_marks = marks_obtained * 0.4  # 40% of the marks
            elif assessment_type == 'MSE3':
                converted_marks = marks_obtained * 0.2  # 20% of the marks
            elif assessment_type in ['LA1', 'LA2']:
                converted_marks = marks_obtained  # No conversion needed, out of 10

            # Update the marks in the database
            update_query = """
                UPDATE marks
                SET MarksObtained = %s
                WHERE USN = %s AND Course_code = %s AND AssessmentType = %s
            """
            
            cursor.execute(update_query, (converted_marks, usn, course_code, assessment_type))
            
            conn.commit()

            # Check if the update was successful
            if cursor.rowcount == 0:
                messagebox.showerror("Update Error", "Failed to update marks. Please check the USN, Course Code, and Assessment Type.")
                return

            messagebox.showinfo("Success", "Marks updated successfully")
        
        except mysql.connector.Error as err:
            messagebox.showerror("Database Error", f"Error: {err}")
        
        finally:
            cursor.close()
            conn.close()
            

    def mark_attendance(self, name: str, subject: str, code: str):
        self.clear_screen()

        # Add header
        header_frame = tk.Frame(self.root, bg="#003366")
        header_frame.pack(fill="x")

        # Place the logo in the top left corner
        img = Image.open("nitte_logo.png")  # Replace with the path to the student's image
        img = img.resize((75, 75))
        photo = ImageTk.PhotoImage(img)
        tk.Label(header_frame, image=photo, bg="#003366").grid(row=0, column=0, rowspan=2, padx=10, pady=10, sticky="w")

        # Add the labels in the center without spacing
        center_label_frame = tk.Frame(header_frame, bg="#003366")
        center_label_frame.grid(row=0, column=1, columnspan=2, padx=5, pady=10, sticky="ew")
        
        tk.Label(center_label_frame, text="Nitte Meenakshi Institute of Technology", font=self.header_font, fg="white", bg="#003366").pack()
        tk.Label(center_label_frame, text="Bengaluru-560064", font=self.subheader_font, fg="white", bg="#003366").pack()

        # Add HOME button in the top right corner
        tk.Button(header_frame, text="HOME", font=self.subheader_font, command=lambda: self.main_teacher_page(name, subject, code)).grid(row=0, column=3, rowspan=2, padx=10, pady=10, sticky="e")

        # Make sure the header frame's columns expand appropriately
        header_frame.grid_columnconfigure(1, weight=1)

        # Keep the reference to the image
        self.photo = photo

        def submit_attendance():
            usn = usn_entry.get().strip()
            date = date_entry.get()
            status = status_var.get()
            course_code = code[0]

            if not usn or not date or not status or not course_code:
                messagebox.showerror("Input Error", "All fields are required")
                return

            try:
                conn = get_db_connection()
                cursor = conn.cursor()

                # Check if the USN is present in the student table
                cursor.execute("SELECT 1 FROM student WHERE USN = %s", (usn,))
                if cursor.fetchone() is None:
                    messagebox.showerror("Input Error", "USN not found in the student table")
                    return

                # Check if an attendance record already exists for the given USN, Course_code, and Date
                cursor.execute("""
                    SELECT 1 FROM attendence
                    WHERE USN = %s AND Course_code = %s AND Date = %s
                """, (usn, course_code, date))
                
                if cursor.fetchone() is not None:
                    messagebox.showerror("Input Error", "Attendance record for this USN, Course_code, and Date already exists")
                    return

                # Insert the attendance record if it doesn't already exist
                insert_query = """
                    INSERT INTO attendence (USN, Course_code, Date, Status)
                    VALUES (%s, %s, %s, %s)
                """

                cursor.execute(insert_query, (usn, course_code, date, status))
                
                conn.commit()
                messagebox.showinfo("Success", "Attendance Marked Successfully")

            except mysql.connector.Error as err:
                messagebox.showerror("Database Error", f"Error: {err}")

            finally:
                cursor.close()
                conn.close()


        def update_attendance():
            usn = usn_entry.get().strip()
            date = date_entry.get()
            status = status_var.get()
            course_code = code[0]

            if not usn or not date or not status or not course_code:
                messagebox.showerror("Input Error", "All fields are required")
                return

            try:
                conn = get_db_connection()
                cursor = conn.cursor()

                # Check if the USN is present in the student table
                cursor.execute("SELECT 1 FROM student WHERE USN = %s", (usn,))
                if cursor.fetchone() is None:
                    messagebox.showerror("Input Error", "USN not found in the student table")
                    return

                update_query = """
                    UPDATE attendence SET Status=%s WHERE USN=%s AND Course_code=%s AND Date=%s
                """

                cursor.execute(update_query, (status, usn, course_code, date))
                
                conn.commit()
                messagebox.showinfo("Success", "Attendance Updated Successfully")

            except mysql.connector.Error as err:
                messagebox.showerror("Database Error", f"Error: {err}")

            finally:
                cursor.close()
                conn.close()
                        
        # Creating a frame to hold the form elements
        form_frame = tk.Frame(self.root)
        form_frame.pack(padx=20, pady=120)

        # USN entry
        tk.Label(form_frame, text="USN:", font=("Helvetica", 20)).grid(row=0, column=0, padx=10, pady=10, sticky="e")
        usn_entry = tk.Entry(form_frame, width=50, font=('Helvetica', 12))  # Adjust the width as needed
        usn_entry.grid(row=0, column=1, padx=10, pady=10)

        # Date entry
        tk.Label(form_frame, text="Date:", font=("Helvetica", 20)).grid(row=1, column=0, padx=10, pady=10, sticky="e")
        date_entry = DateEntry(form_frame, width=45, background='darkblue', font=('Helvetica', 12), foreground='white', borderwidth=2, date_pattern='dd/mm/yyyy')
        date_entry.grid(row=1, column=1, padx=10, pady=10)

        # Status radio buttons
        tk.Label(form_frame, text="Status:", font=("Helvetica", 20)).grid(row=2, column=0, padx=10, pady=10, sticky="e")
        status_var = tk.StringVar()
        status_present = tk.Radiobutton(form_frame, text="Present", font=('Helvetica', 12), variable=status_var, value="Present")
        status_present.grid(row=2, column=1, padx=10, pady=10, sticky="w")
        status_absent = tk.Radiobutton(form_frame, text="Absent", font=('Helvetica', 12), variable=status_var, value="Absent")
        status_absent.grid(row=2, column=1, padx=10, pady=10, sticky="e")

        # Create a frame to hold the buttons
        button_frame = tk.Frame(form_frame)
        button_frame.grid(row=3, columnspan=2, pady=10)

        # Submit button
        submit_button = tk.Button(button_frame, text="Submit", width=25, height=2, font=("Helvetica", 14), bg='#003366', fg='white', command=submit_attendance)  # Adjust width and height
        submit_button.pack(side="left", padx=0, pady=0)

        # Update attendance button
        update_button = tk.Button(button_frame, text="Update", width=25, height=2, font=("Helvetica", 14), bg='#003366', fg='white',  command=update_attendance)  # Adjust width and height
        update_button.pack(side="right", padx=0, pady=0)

        # Add the bottom frame
        bottom_frame = tk.Frame(self.root, bg="#333333")
        bottom_frame.pack(side="bottom", fill="x")

        # Add the copyright and powered by text
        copyright_label = tk.Label(bottom_frame, text="Copyright © Powered By: EduTrack", fg="white", bg="#333333", font=("Helvetica", 14))
        copyright_label.pack(side="left", padx=10, pady=5)

        # Add the terms of service and privacy policy text
        terms_label = tk.Label(bottom_frame, text="Terms of Service | Privacy Policy", fg="white", bg="#333333", font=("Helvetica", 14))
        terms_label.pack(side="right", padx=10, pady=5)
        
    def exit_fullscreen(self, event=None):
        self.root.attributes('-fullscreen', False)
        self.root.geometry('800x600')  # Optional: Set a default window size
