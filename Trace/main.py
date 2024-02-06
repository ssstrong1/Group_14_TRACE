import customtkinter as ctk
from tkinter import *
import tkinter as tk
from tkinter import ttk
import re
from tkinter import filedialog
from PIL import ImageTk, Image

class Trace:
    def __init__(self):
        self.app = ctk.CTk()
        self.app.geometry("1000x1200")
        self.app.title("TRACE")

        ctk.set_appearance_mode("dark")

        # Create a menu bar
        menubar = Menu(self.app)
        self.app.config(menu=menubar)

        # Create a file menu
        file_menu = Menu(menubar, tearoff=0)
        file_menu.add_command(label="New", command=self.new_session)
        file_menu.add_command(label="Save as", command=self.save_as)
        file_menu.add_command(label="Browse", command=self.browse)
        file_menu.add_separator()
        menubar.add_cascade(label="File", menu=file_menu)

        # Create an edit menu
        edit_menu = Menu(menubar, tearoff=0)
        edit_menu.add_command(label="1040")
        edit_menu.add_command(label="1099")
        edit_menu.add_command(label="W-2")
        menubar.add_cascade(label="Form", menu=edit_menu)

        # Create a help menu
        help_menu = Menu(menubar, tearoff=0)
        help_menu.add_command(label="About")
        menubar.add_cascade(label="Settings", menu=help_menu)

        trace_label = ctk.CTkLabel(master=self.app, text="Trace", font=("Arial", 50), text_color="#FFCC70")

        ###############################

        style = ttk.Style()
        style.configure("Transparent.TEntry", background="systemTransparent")

        w_2_img = ctk.CTkImage(light_image=Image.open('background.png'), size=(900, 700))

        w_2_label_for_img = ctk.CTkLabel(self.app, text="", image=w_2_img)

        ein_entry = ctk.CTkEntry(master=self.app, placeholder_text="EIN", width=250, text_color="#FFCC70",
                                 bg_color="white", fg_color="transparent")

        employer_name = ctk.CTkEntry(master=self.app, placeholder_text="Name", width=250, text_color="#FFCC70",
                                     bg_color="white", fg_color="transparent")
        employer_address = ctk.CTkEntry(master=self.app, placeholder_text="Address", width=250, text_color="#FFCC70",
                                        bg_color="white", fg_color="transparent")
        employer_zip = ctk.CTkEntry(master=self.app, placeholder_text="ZIP Code", width=250, text_color="#FFCC70",
                                    bg_color="white", fg_color="transparent")

        ###############################

        results_label = ctk.CTkLabel(master=self.app, text="Results", font=("Arial", 20), text_color="#FFCC70")

        results_textbox = ctk.CTkTextbox(master=self.app, scrollbar_button_color="#FFCC70", width=500, corner_radius=16,
                                         border_color="#FFCC70")
        trace_label.pack(pady=5)

        w_2_label_for_img.place(relx=0.5, rely=0.5, anchor="s")
        ein_entry.place(relx=.535, rely=0.161, anchor="e")
        employer_name.place(relx=.35, rely=0.21, anchor="e")
        employer_address.place(relx=.35, rely=0.24, anchor="e")
        employer_zip.place(relx=.35, rely=0.27, anchor="e")

        w_2_label_for_img.pack(pady=20)

        results_label.pack(pady=20)
        results_textbox.pack(pady=20)
        # Create buttons
        Button(self.app, text="Calculate").place(relx=.5, rely=0.965, anchor="center")
        Button(self.app, text="Save Session").place(relx=.4, rely=0.965, anchor="center")
        Button(self.app, text="Load Session").place(relx=.6, rely=0.965, anchor="center")

        self.app.mainloop()

    def new_session(self):
        # Clear input fields (create these widgets first)
        pass

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

    def save_as(self):
        # Open file explorer
        filename = filedialog.asksaveasfilename(initialdir="/", title="Save As",
                                                filetypes=(("Text Files", "*.txt"), ("All Files", "*.*")))


Trace()
