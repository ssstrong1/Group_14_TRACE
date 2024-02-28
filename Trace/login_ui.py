import customtkinter as ctk
from tkinter import *
import tkinter as tk
from PIL import ImageTk, Image
import sqlite3
import bcrypt
from tkinter import messagebox

import ui

import ctypes

user = ctypes.windll.user32
screensize = user.GetSystemMetrics(0), user.GetSystemMetrics(1)

font1 = ('Helvetica', 25, 'bold')
font2 = ('Arial', 17, 'bold')

user_connection = sqlite3.connect('data.db')
user_cursor = user_connection.cursor()

user_cursor.execute('''CREATE TABLE IF NOT EXISTS users ( 
    username TEXT NOT NULL, 
    password TEXT NOT NULL)''')


def login_account(self):
    l = LoginInterface()
    username = l.username_input_field_l.get()
    password = l.password_input_field_l.get()
    if username != '' and password != '':
        user_cursor.execute('SELECT password FROM users WHERE username=?', [username])
        result = user_cursor.fetchone()
        if result:
            if bcrypt.checkpw(password.encode('utf-8'), result[0]):
                self.x = messagebox.showinfo('Success', 'Logged in successfully.')
                self.app1.destroy()
                import ui
            else:
                messagebox.showerror('Error', 'Invalid password.')
        else:
            messagebox.showerror('Error', 'Invalid username.')
    else:
        messagebox.showerror('Error', 'Please enter a username and password.')


class LoginInterface:
    """
    A graphical user interface for the login/sign up TRACE application.
    """

    def __init__(self):
        self.x = ''
        self.app1 = ctk.CTk()
        self.app1.geometry("700x500")
        self.app1.title("TRACE")
        self.app1.resizable(False, False)

        ctk.set_appearance_mode("")

        ###############################

        # Start Of Input Fields

        ###############################

        self.frame_space = ctk.CTkCanvas(self.app1, width=700, height=500)
        self.frame_space.place(x=-2, y=-2)

        self.general = ctk.CTkFrame(self.frame_space, width=320, height=360, corner_radius=0, border_width=3)
        self.general.place(relx=0.3, rely=0.5, anchor='center')

        self.sign_up_title = ctk.CTkLabel(self.general, font=('Times New Roman', 50, 'bold'),
                                          text='Sign Up', text_color='light blue', bg_color='#2b2b2b')

        self.login_title = ctk.CTkLabel(self.general, font=('Times New Roman', 50, 'bold'),
                                        text='Login', text_color='light blue', bg_color='#2b2b2b')

        self.username_line = ctk.CTkLabel(self.general, text="                      ",
                                          font=('Times New Roman', 40, 'underline'))

        self.password_line = ctk.CTkLabel(self.general, text="                      ",
                                          font=('Times New Roman', 40, 'underline'))

        self.username_input_field_s = ctk.CTkEntry(self.general, font=font2, text_color='#fff', fg_color='transparent',
                                                   border_width=0,
                                                   placeholder_text='Username',
                                                   placeholder_text_color='#a3a3a3',
                                                   width=200, height=1)

        self.password_input_field_s = ctk.CTkEntry(self.general, font=font2, text_color='#fff', fg_color='transparent',
                                                   border_width=0,
                                                   placeholder_text='Password',
                                                   placeholder_text_color='#a3a3a3',
                                                   width=200, height=1)

        self.signup_btn_s = ctk.CTkButton(self.general, command=self.sign_up_account, font=font2, text='Sign up',
                                          fg_color='#004780',
                                          hover_color='#003763', bg_color='#2b2b2b', cursor='hand2',
                                          corner_radius=5, width=120)

        self.login_btn_s = ctk.CTkButton(self.general, command=self.login, font=font2, text='Login',
                                         fg_color='#004780',
                                         hover_color='#003763', bg_color='#2b2b2b', cursor='hand2',
                                         corner_radius=5, width=120)

        self.username_input_field_l = ctk.CTkEntry(self.general, font=font2, text_color='#fff', fg_color='transparent',
                                                   border_width=0,
                                                   placeholder_text='Username',
                                                   placeholder_text_color='#a3a3a3',
                                                   width=200, height=1)

        self.password_input_field_l = ctk.CTkEntry(self.general, font=font2, text_color='#fff', fg_color='transparent',
                                                   border_width=0,
                                                   placeholder_text='Password',
                                                   placeholder_text_color='#a3a3a3',
                                                   width=200, height=1)

        self.signup_btn_l = ctk.CTkButton(self.general, command=self.sign_up, font=font2, text='Sign up',
                                          fg_color='#004780',
                                          hover_color='#003763', bg_color='#2b2b2b', cursor='hand2',
                                          corner_radius=5,
                                          width=120)

        self.login_btn_l = ctk.CTkButton(self.general, command=self.login_account, font=font2, text='Login',
                                         fg_color='#004780',
                                         hover_color='#003763', bg_color='#2b2b2b', cursor='hand2',
                                         corner_radius=5, width=120)

        ###############################

        # End Of Input Fields

        ###############################

        self.d_2_img = ImageTk.PhotoImage(Image.open("images/pattern_back.png").resize((1300, 700)))
        self.frame_space.create_image(-10, 0, anchor=tk.NW, image=self.d_2_img)

        self.user_icon = ctk.CTkImage(light_image=Image.open('images/user_icon.png'),
                                      size=(20, 20))
        self.user_icon_label = ctk.CTkLabel(self.general, text="", image=self.user_icon)

        self.pass_icon = ctk.CTkImage(light_image=Image.open('images/lock_icon.png'),
                                      size=(20, 20))
        self.pass_icon_label = ctk.CTkLabel(self.general, text="", image=self.pass_icon)

        LoginInterface.sign_up(self)

        self.app1.mainloop()

    def sign_up_account(self):
        username = self.username_input_field_s.get()
        password = self.password_input_field_s.get()
        if username != '' and password != '':
            user_cursor.execute('SELECT username FROM users WHERE username=?', [username])
            if user_cursor.fetchone() is not None:
                messagebox.showerror('Error', 'Username already exists.')
            else:
                user_encoded_password = password.encode('utf-8')
                user_hashed_password = bcrypt.hashpw(user_encoded_password, bcrypt.gensalt())
                user_cursor.execute('INSERT INTO users VALUES (?, ?)', [username, user_hashed_password])
                user_connection.commit()
                messagebox.showinfo('Success', 'Account has been created.')
        else:
            messagebox.showerror('Error', 'Please enter a username and password.')

    def login_account(self):
        username = self.username_input_field_l.get()
        password = self.password_input_field_l.get()
        if username != '' and password != '':
            user_cursor.execute('SELECT password FROM users WHERE username=?', [username])
            result = user_cursor.fetchone()
            if result:
                if bcrypt.checkpw(password.encode('utf-8'), result[0]):
                    self.x = messagebox.showinfo('Success', 'Logged in successfully.')
                    self.app1.destroy()
                    ui.UserInterface()
                else:
                    messagebox.showerror('Error', 'Invalid password.')
            else:
                messagebox.showerror('Error', 'Invalid username.')
        else:
            messagebox.showerror('Error', 'Please enter a username and password.')

    def sign_up(self):
        placements = [self.login_title, self.username_input_field_l,
                      self.password_input_field_l, self.login_btn_l, self.signup_btn_l]

        for i in placements:
            i.place_forget()

        self.sign_up_title.place(x=65, y=50)

        self.user_icon_label.place(x=55, y=130)

        self.pass_icon_label.place(x=55, y=195)

        self.username_line.place(x=50, y=120)

        self.password_line.place(x=50, y=185)

        self.username_input_field_s.place(x=80, y=135)

        self.password_input_field_s.place(x=80, y=200)

        self.signup_btn_s.place(x=30, y=300)

        self.login_btn_s.place(x=170, y=300)

    def login(self):
        placements = [self.sign_up_title, self.username_input_field_s,
                      self.password_input_field_s, self.signup_btn_s, self.login_btn_s]

        for i in placements:
            i.place_forget()

        self.login_title.place(x=85, y=50)

        self.username_input_field_l.place(x=80, y=135)

        self.password_input_field_l.place(x=80, y=200)

        self.login_btn_l.place(x=30, y=300)

        self.signup_btn_l.place(x=170, y=300)
