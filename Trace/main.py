import customtkinter as ctk
from tkinter import *
import tkinter as tk
from tkinter import ttk
import re
from tkinter import filedialog
from PIL import ImageTk, Image


import ctypes
user = ctypes.windll.user32
screensize = user.GetSystemMetrics(0), user.GetSystemMetrics(1)


class Trace:
    def __init__(self):
        self.app = ctk.CTk()
        self.app.geometry("1500x1200")
        self.app.title("TRACE")
        self.app.resizable(False, False)

        canvas = tk.Canvas(self.app, width=1500, height=1200)
        canvas.place(relx=.5, rely=.5, anchor="center")

        if screensize == (1920, 1080):
            ctk.set_widget_scaling(.75)
            ctk.set_window_scaling(.75)
            d_2_img = ImageTk.PhotoImage(Image.open("pattern_back.png").resize((1500, 1200)))
            canvas.create_image(0, 0, anchor=tk.NW, image=d_2_img)
            cosmos = canvas.create_text(635, 150, anchor="nw", fill="yellow")
            canvas.itemconfig(cosmos, text="TRACE", width=780)
            canvas.itemconfig(cosmos, font=("Arial", 50))
            aqua = canvas.create_text(670, 755, anchor="nw", fill="yellow")
            canvas.itemconfig(aqua, text="Results", width=780)
            canvas.itemconfig(aqua, font=("Arial", 35))
        else:
            d_2_img = ImageTk.PhotoImage(Image.open("pattern_back.png").resize((1500, 1200)))
            canvas.create_image(2, 2, anchor=tk.NW, image=d_2_img)
            cosmos = canvas.create_text(635, 5, anchor="nw", fill="yellow")
            canvas.itemconfig(cosmos, text="TRACE", width=780)
            canvas.itemconfig(cosmos, font=("Arial", 50))
            aqua = canvas.create_text(670, 825, anchor="nw", fill="yellow")
            canvas.itemconfig(aqua, text="Results", width=780)
            canvas.itemconfig(aqua, font=("Arial", 35))
            ctk.set_widget_scaling(1)
            ctk.set_window_scaling(1)

        ctk.set_appearance_mode("")

        # Menu bar
        menubar = Menu(self.app)
        self.app.config(menu=menubar)

        # File menu
        file_menu = Menu(menubar, tearoff=0)
        file_menu.add_command(label="New", command=self.new_session)
        file_menu.add_command(label="Save as", command=self.save_as)
        file_menu.add_command(label="Browse", command=self.browse)
        file_menu.add_separator()
        menubar.add_cascade(label="File", menu=file_menu)

        # Edit menu
        edit_menu = Menu(menubar, tearoff=0)
        edit_menu.add_command(label="1040")
        edit_menu.add_command(label="1099")
        edit_menu.add_command(label="W-2")
        menubar.add_cascade(label="Form", menu=edit_menu)

        # Help menu
        help_menu = Menu(menubar, tearoff=0)
        help_menu.add_command(label="About")
        menubar.add_cascade(label="Settings", menu=help_menu)

        ###############################

        # W-2 Form Section

        # Start Of Input Fields

        w_2_img = ctk.CTkImage(light_image=Image.open('w_2_form.png'), size=(1300, 700))
        w_2_label_for_img = ctk.CTkLabel(self.app, text="", image=w_2_img)

        # Employee Social Security Number

        essn_entry = ctk.CTkEntry(master=self.app, placeholder_text="ESSN", width=256, height=25, text_color="#000000",
                                  bg_color="white", fg_color="transparent")

        # Employer ID Number

        ein_entry = ctk.CTkEntry(master=self.app, placeholder_text="EIN", width=370, text_color="#000000",
                                 bg_color="white", fg_color="transparent")

        # Wages, Tips, Other Compensation

        wages_tips_c = ctk.CTkEntry(master=self.app, placeholder_text="wages", width=235, height=25,
                                    text_color="#000000",
                                    bg_color="white", fg_color="transparent")

        # Social Security Wages

        social_wages = ctk.CTkEntry(master=self.app, placeholder_text="social wages", width=235, height=25,
                                    text_color="#000000",
                                    bg_color="white", fg_color="transparent")

        # Medicare Wages

        medicare_wages = ctk.CTkEntry(master=self.app, placeholder_text="medicare", width=235, height=25,
                                      text_color="#000000",
                                      bg_color="white", fg_color="transparent")

        # Social Security Tips

        social_security_tips = ctk.CTkEntry(master=self.app, placeholder_text="SS Tips", width=235, height=25,
                                            text_color="#000000",
                                            bg_color="white", fg_color="transparent")

        # 9 box

        nine_box = ctk.CTkEntry(master=self.app, placeholder_text="Nine", width=235, height=25,
                                text_color="#000000",
                                bg_color="#c0c0c0", fg_color="white")

        #  Non-Qualified Plans

        non_qualified_plans = ctk.CTkEntry(master=self.app, placeholder_text="plans", width=235, height=25,
                                           text_color="#000000",
                                           bg_color="white", fg_color="transparent")

        #  Federal Income Tax Withheld

        fed_income_tax_withheld = ctk.CTkEntry(master=self.app, placeholder_text="fed", width=235, height=25,
                                               text_color="#000000",
                                               bg_color="white", fg_color="transparent")

        #  Social Security Tax Withheld

        social_security_tax_withheld = ctk.CTkEntry(master=self.app, placeholder_text="SS Tax", width=235, height=25,
                                                    text_color="#000000",
                                                    bg_color="white", fg_color="transparent")

        #  Medicare Tax Withheld

        medicare_tax_withheld = ctk.CTkEntry(master=self.app, placeholder_text="medicare withheld", width=235, height=25,
                                             text_color="#000000",
                                             bg_color="white", fg_color="transparent")

        #  Allocated Tips

        allocated_tips = ctk.CTkEntry(master=self.app, placeholder_text="A Tips", width=235, height=25,
                                      text_color="#000000",
                                      bg_color="white", fg_color="transparent")

        #  Dependent Care Benefits

        dependent_care_benefits = ctk.CTkEntry(master=self.app, placeholder_text="DCB", width=235, height=25,
                                               text_color="#000000",
                                               bg_color="white", fg_color="transparent")

        # Employer Name, Address, ZIP

        employer_name = ctk.CTkEntry(master=self.app, placeholder_text="Name", width=250, text_color="#000000",
                                     bg_color="white", fg_color="transparent")
        employer_address = ctk.CTkEntry(master=self.app, placeholder_text="Address", width=250, text_color="#000000",
                                        bg_color="white", fg_color="transparent")
        employer_zip = ctk.CTkEntry(master=self.app, placeholder_text="ZIP Code", width=250, text_color="#000000",
                                    bg_color="white", fg_color="transparent")

        # Control Number

        cn_entry = ctk.CTkEntry(master=self.app, placeholder_text="CN", width=510, text_color="#000000",
                                bg_color="white", fg_color="transparent")

        # Employee Name And Initial

        employee_name_i = ctk.CTkEntry(master=self.app, placeholder_text="Name and Initial", width=230,
                                       text_color="#000000", bg_color="white", fg_color="transparent")

        # Employee Last Name

        employee_last_name = ctk.CTkEntry(master=self.app, placeholder_text="Last", width=230,
                                          text_color="#000000", bg_color="white", fg_color="transparent")

        # Employee Suffix

        employee_suffix = ctk.CTkEntry(master=self.app, placeholder_text="Suff.", width=40,
                                       text_color="#000000", bg_color="white", fg_color="transparent")

        # Employee Address

        employee_address = ctk.CTkEntry(master=self.app, placeholder_text="Address", width=230, height=25,
                                        text_color="#000000", bg_color="white", fg_color="transparent")

        # Employee ZIP

        employee_zip = ctk.CTkEntry(master=self.app, placeholder_text="ZIP", width=100, height=25,
                                    text_color="#000000", bg_color="white", fg_color="transparent")

        # Cover And Replacer For Year On Form

        blocker = ctk.CTkImage(light_image=Image.open('blocker.png'), size=(150, 85))
        blocker_img = ctk.CTkLabel(self.app, text="", image=blocker)
        twenty_four = ctk.CTkImage(light_image=Image.open('2024.png'), size=(100, 30))
        twenty_four_img = ctk.CTkLabel(self.app, text="", image=twenty_four)

        # Positioning of Input Fields

        # W-2

        w_2_label_for_img.place(relx=0.5, rely=0.5, anchor="s")
        w_2_label_for_img.pack(pady=88)

        # Employee SSN

        essn_entry.place(relx=.46, rely=0.123, anchor="e")

        # EIN

        ein_entry.place(relx=.535, rely=0.160, anchor="e")

        # Wages TC

        wages_tips_c.place(relx=.719, rely=0.162, anchor="e")

        # SS Wages

        social_wages.place(relx=.719, rely=0.2, anchor="e")

        # M Wages and T

        medicare_wages.place(relx=.719, rely=0.238, anchor="e")

        # SS Tips

        social_security_tips.place(relx=.719, rely=0.277, anchor="e")

        # Nine

        nine_box.place(relx=.719, rely=0.315, anchor="e")

        # NQP

        non_qualified_plans.place(relx=.719, rely=0.354, anchor="e")

        # FED Income

        fed_income_tax_withheld.place(relx=.902, rely=0.162, anchor="e")

        # SST Withheld

        social_security_tax_withheld.place(relx=.902, rely=0.2, anchor="e")

        # M Withheld

        medicare_tax_withheld.place(relx=.902, rely=0.238, anchor="e")

        # A Tips

        allocated_tips.place(relx=.902, rely=0.277, anchor="e")

        # DC Benefits

        dependent_care_benefits.place(relx=.902, rely=0.315, anchor="e")

        # Employer NAZ

        employer_name.place(relx=.285, rely=0.21, anchor="e")
        employer_address.place(relx=.285, rely=0.24, anchor="e")
        employer_zip.place(relx=.285, rely=0.27, anchor="e")

        # CN

        cn_entry.place(relx=.535, rely=0.314, anchor="e")

        # Employee NI

        employee_name_i.place(relx=.270, rely=0.36, anchor="e")

        # Employee LN

        employee_last_name.place(relx=.46, rely=0.36, anchor="e")

        # Employee S

        employee_suffix.place(relx=.535, rely=0.36, anchor="e")

        # Employee A

        employee_address.place(relx=.433, rely=0.489, anchor="e")

        # Employee Z

        employee_zip.place(relx=.535, rely=0.489, anchor="e")

        # Blocker

        blocker_img.place(relx=0.525, rely=0.655, anchor="s")
        twenty_four_img.place(relx=0.525, rely=0.607, anchor="s")

        # End Of Input Fields

        ###############################

        # Results Section

        results_textbox = ctk.CTkTextbox(master=self.app, scrollbar_button_color="#FFCC70", width=500, corner_radius=16,
                                         border_color="#FFCC70")

        # Results Positioning

        results_textbox.pack(pady=20)

        # Results Section

        results_textbox1 = 0

        # Buttons

        Button(self.app, text="Calculate").place(relx=.5, rely=0.965, anchor="center")
        Button(self.app, text="Save Session").place(relx=.4, rely=0.965, anchor="center")
        Button(self.app, text="Load Session").place(relx=.6, rely=0.965, anchor="center")

        self.app.mainloop()

    # New Session

    def new_session(self):
        pass

    # Browse

    def browse(self):
        file = filedialog.askopenfile(mode='r', defaultextension=".txt")
        if file is None:
            return
        contents = file.read()
        income = re.sub(r"[^0-9.]", "", contents.split("\n")[0])
        deductions = re.sub(r"[^0-9.]", "", contents.split("\n")[1])
        tax_year = re.sub(r"[^0-9.]", "", contents.split("\n")[2])
        # Assign values to self.income_entry, self.deductions_entry, self.tax_year_entry (create these widgets first)
        file.close()

    # Save As

    def save_as(self):
        # Open file explorer
        filename = filedialog.asksaveasfilename(initialdir="/", title="Save As",
                                                filetypes=(("Text Files", "*.txt"), ("All Files", "*.*")))


Trace()
