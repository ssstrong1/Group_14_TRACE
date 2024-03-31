import customtkinter as ctk
from tkinter import *
import tkinter as tk
from PIL import ImageTk, Image
import bcrypt
from tkinter import messagebox
import create_tables_1
import user_login_info



import ctypes

user_person = ctypes.windll.user32
screensize = user_person.GetSystemMetrics(0), user_person.GetSystemMetrics(1)


font1 = ('Helvetica', 25, 'bold')
font2 = ('Arial', 17, 'bold')


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

        ctk.set_appearance_mode("Dark")

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
                                                   width=200, height=1, show='*')

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
                                                   width=200, height=1, show='*')

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
        """
        Signs up a new user account.

        This method retrieves the username and password from input fields. If both fields are non-empty:
        1. It checks if the username already exists in the database.
        2. If the username is unique, it encodes the password, hashes it, and inserts the user into the 'users' table.
        3. A success message is displayed if the account is created; otherwise, an error message is shown.

        Returns:
            None
        """
        username = self.username_input_field_s.get()
        password = self.password_input_field_s.get()
        if username != '' and password != '':
            create_tables_1.user_cursor.execute('SELECT username FROM users WHERE username=?', [username])
            if create_tables_1.user_cursor.fetchone() is not None:
                messagebox.showerror('Error', 'Username already exists.')
            else:
                user_encoded_password = password.encode('utf-8')
                user_hashed_password = bcrypt.hashpw(user_encoded_password, bcrypt.gensalt())
                create_tables_1.user_cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', [username, user_hashed_password])
                create_tables_1.user_connection.commit()
                messagebox.showinfo('Success', 'Account has been created.')
        else:
            messagebox.showerror('Error', 'Please enter a username and password.')

    def login_account(self):
        """
        Validates user login credentials and performs necessary actions.

        This method retrieves the username and password entered by the user from input fields.
        It then checks if both fields are non-empty. If so, it queries the database to find the
        hashed password associated with the provided username. If a matching record is found,
        it verifies the password using bcrypt. If the password is correct, the user is considered
        logged in, and the appropriate UI transitions are made. Otherwise, error messages are
        displayed for invalid credentials.

        Returns:
            None
        """
        username = self.username_input_field_l.get()
        password = self.password_input_field_l.get()
        if username != '' and password != '':
            create_tables_1.user_cursor.execute('SELECT password FROM users WHERE username=?', [username])
            result = create_tables_1.user_cursor.fetchone()
            if result:
                if bcrypt.checkpw(password.encode('utf-8'), result[0]):
                    self.x = messagebox.showinfo('Success', 'Logged in successfully.')
                    self.app1.withdraw()
                    user_login_info.username = username
                    user_login_info.password = password
                    self.start_form_ui()
                else:
                    messagebox.showerror('Error', 'Invalid password.')
            else:
                messagebox.showerror('Error', 'Invalid username.')
        else:
            messagebox.showerror('Error', 'Please enter a username and password.')

    def sign_up(self):
        """
        Displays the sign-up interface by adjusting the placement of various widgets.

        This method hides the login-related widgets (such as login title, username input field, password input field,
        login button, and signup button) and displays the sign-up title, user icon label, password icon label,
        username line, password line, username input field (small), password input field (small), signup button (small),
        and login button (small) at specific coordinates on the screen.

        Returns:
            None
        """
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
        """
       Handles the login functionality for the user interface.

       This method performs the following actions:
       1. Hides the sign-up related widgets (title, input fields, and buttons).
       2. Places the login title widget at coordinates (x=85, y=50).
       3. Positions the username input field at coordinates (x=80, y=135).
       4. Positions the password input field at coordinates (x=80, y=200).
       5. Places the login button at coordinates (x=30, y=300).
       6. Places the signup button at coordinates (x=170, y=300).

       Returns:
           None
       """
        placements = [self.sign_up_title, self.username_input_field_s,
                      self.password_input_field_s, self.signup_btn_s, self.login_btn_s]

        for i in placements:
            i.place_forget()

        self.login_title.place(x=85, y=50)

        self.username_input_field_l.place(x=80, y=135)

        self.password_input_field_l.place(x=80, y=200)

        self.login_btn_l.place(x=30, y=300)

        self.signup_btn_l.place(x=170, y=300)

    # Open New Window
    def start_form_ui(self):
        import ui
        """
        Opens a new window for the user interface.

        This function initializes a new user interface window using the `ui.UserInterface()` class.
        It is responsible for creating and displaying the graphical elements of the form.

        Returns:
            None
        """
        ui.UserInterface()

