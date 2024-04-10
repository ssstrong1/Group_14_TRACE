import customtkinter as ctk
from tkinter import messagebox
import sys
import os
import fitz
from PyPDF2 import PdfReader
from tkinter import filedialog
from tkinter import *
import tkinter as tk
from PIL import ImageTk, Image
from fpdf import FPDF
import create_tables_1
import user_login_info
import datetime
import ctypes
from input_validation import FormValidatorW2
from input_validation import FormValidator1099DIV
from input_validation import FormValidator1040

from form_1040 import Form1040

user_form_1040 = Form1040()

w2_user_validation = FormValidatorW2()
ten_99_validation = FormValidator1099DIV()
ten_40_validation = FormValidator1040()

y = create_tables_1

user = ctypes.windll.user32
screensize = user.GetSystemMetrics(0), user.GetSystemMetrics(1)

print(user_login_info.username)


class UserInterface:
    """
    A graphical user interface for the TRACE application.
    """

    def __init__(self):

        """

        __init__(self): Part 1

        Initializes the user interface window.
        All styles are as follows:
        Window Sizing
        Canvas Sizing

        __init__(self): Part 2

        A Canvas is created with the specified dimensions: width = 1500 and height = 1200.
        The canvas is intended for drawing graphics, shapes, and images.
        canvas.place(relx=.5, rely=.5, anchor="center") line centers the canvas within
        its parent

        __init__(self): Part 3

        Checks if the screensize is equal to (1920, 1080).
        If true, it performs the following actions:
        Sets widget scaling and window scaling using ctk.set_widget_scaling(.7465) and ctk.set_window_scaling(.7465).
        Loads an image from “pattern_back.png” and resizes it to 1500x1200 pixels.
        Creates an image on the canvas at top-left corner (anchor NW) using the resized image.

        __init__(self): Part 4

        Adds two text elements:
        “TRACE” at coordinates (635, 150) with a font size of 50.
        “Results” at coordinates (670, 755) with a font size of 35.
        If the screensize condition is not met:
        it loads the same image and places it at (2, 2) on the canvas.
        Adjusts the text positions for “TRACE” and “Results”.
        Resets widget and window scaling to 1.

        __init__(self): Part 5

        Most if not all variables are attributes. This will allow for usability throughout the whole class.

        ctk.set_appearance_mode("") is used to set the appearance mode for a custom GUI application.

        The menubar is created using the Menu widget.
        It is associated with the main application window (self.app) using self.app.config(menu=menubar).

        A submenu called file_menu is created within the menubar.
        It includes three commands: “New,” “Save as,” and “Browse.”
        These commands are associated with specific functions (t.new_session, t.save_as, and t.browse).
        A separator line is added after the commands using file_menu.add_separator().

        The entire file_menu is added as a cascade under the “File” label in the menubar.
        Similar to the file menu, an edit_menu is created within the menubar.
        It contains three commands labeled “1040,” “1099,” and “W-2.”
        These commands are connected to their respective functions.

        The edit_menu is added as a cascade under the “Form” label in the menubar.
        A help_menu is created within the menubar.
        It has a single command labeled “About.”
        The help_menu is added as a cascade under the “Settings” label in the menubar.

        Image Display:
        w_2_img: An instance of a custom image widget (ctk.CTkImage) that displays the W-2 form image
        loaded from the file 'w_2_form.png'.
        w_2_label_for_img: A label widget that shows the image (w_2_img) within the GUI.

        Input Fields:

        essn_entry: An entry field (text input) for the Employee Social Security Number (ESSN). It has a placeholder
        text, specified width and height, and transparent styling.

        ein_entry: An entry field for the Employer ID Number (EIN), with similar properties.
        wages_tips_c: An entry field for Wages, Tips, and Other Compensation.
        social_wages: An entry field for Social Security Wages.
        medicare_wages: An entry field for Medicare Wages.

        social_security_tips: An entry field for Social Security Tips.
        nine_box: An entry field labeled as “Nine.”

        Non-Qualified Plans:
        An entry widget named non_qualified_plans is created. It has the following properties:
        Placeholder text: “plans”
        Width: 269 pixels
        Height: 25 pixels
        Text color: Black (#000000)
        Background color: White
        Foreground color (transparent)

        Federal Income Tax Withheld:
        An entry widget named fed_income_tax_withheld is created with similar properties:
        Placeholder text: “fed”
        Width: 269 pixels
        Height: 25 pixels
        Text color: Black
        Background color: White
        Foreground color (transparent)

        Social Security Tax Withheld:
        An entry widget named social_security_tax_withheld is created:
        Placeholder text: “SS Tax”
        Width: 269 pixels
        Height: 25 pixels
        Text color: Black
        Background color: White
        Foreground color (transparent)

        Medicare Tax Withheld:
        An entry widget named medicare_tax_withheld is created:
        Placeholder text: “medicare withheld”
        Width: 269 pixels
        Height: 25 pixels
        Text color: Black
        Background color: White
        Foreground color (transparent)

        Allocated Tips:
        An entry widget named allocated_tips is created:
        Placeholder text: “A Tips”
        Width: 269 pixels
        Height: 25 pixels
        Text color: Black
        Background color: White
        Foreground color (transparent)

        Dependent Care Benefits:
        An entry widget named dependent_care_benefits is created:
        Placeholder text: “DCB”
        Width: 269 pixels
        Height: 25 pixels
        Text color: Black
        Background color: White
        Foreground color (transparent)

        12-A:
        An entry widget named twelve_a is created:
        Placeholder text: “12a”
        Width: 190 pixels
        Height: 25 pixels
        Text color: Black

        twelve_b:
        CTkEntry.
        The widget is placed within the self.app container.
        It has the following properties:
        Placeholder text: “12b”
        Width: 190 pixels
        Height: 25 pixels
        Text color: Black (#000000)
        Background color: White
        Foreground color (text transparency): Transparent

        twelve_c:
        CTkEntry.
        Placeholder text: “12c”
        Width: 190 pixels
        Height: 25 pixels
        Text color: Black
        Background color: White
        Foreground color: Transparent

        twelve_d:
        CTkEntry.
        Placeholder text: “12d”
        Width: 190 pixels
        Height: 25 pixels
        Text color: Black
        Background color: White
        Foreground color: Transparent

        local_income_tax:
        CTkEntry.
        Placeholder text: “12d”
        Width: 174 pixels
        Height: 25 pixels
        Text color: Black
        Background color: White
        Foreground color: Transparent

        state_income_tax:
        CTkEntry.
        Placeholder text: “12d”
        Width: 174 pixels
        Height: 25 pixels
        Text color: Black
        Background color: White
        Foreground color: Transparent

        state_wage_tips:
        CTkEntry.
        Placeholder text: “12d”
        Width: 190 pixels
        Height: 25 pixels
        Text color: Black
        Background color: White
        Foreground color: Transparent

        employers_state_id:
        CTkEntry.
        Placeholder text: “12d”
        Width: 287 pixels
        Height: 25 pixels
        Text color: Black
        Background color: White
        Foreground color: Transparent

        state_field:
        CTkEntry.
        Placeholder text: “12d”
        Width: 60 pixels
        Height: 25 pixels
        Text color: Black

        Locality Name:
        locality_name is an instance of a custom widget called CTkEntry.
        It’s a text input field with the placeholder text “locality”.
        The widget has a width of 109 pixels and a height of 25 pixels.
        The text color is set to black (#000000), and the background color is white.
        The foreground color (text transparency) is set to transparent.

        Local Wages, Tips, ETC.:
        local_wage_tips is an instance of CTkEntry.
        It’s a text input field with the placeholder text “local wages”.
        This widget has a wider width (190 pixels) and the same height (25 pixels).
        Similar to locality_name, it has black text color and a white background.

        Statutory Employee:
        statutory_emp is an instance of CTkCheckBox.
        It’s a checkbox widget with a height of 22 pixels.
        The checkbox itself does not display any text (empty string).
        The background color is white.

        Retirement Plan:
        retirement_p is an instance of CTkCheckBox.
        checkbox with the height (22 pixels).

        Third Party Sick Pay:
        third_party_sp is an instance of CTkCheckBox.
        checkbox with the height (22 pixels).

        Other:
        other_field is an instance of CTkEntry.
        It’s a larger text input field with a width of 269 pixels and a height of 90 pixels.
        The placeholder text is “other”.
        Text color is black, and the background color is white.

        Employer Name, Address, ZIP:
        employer_name, employer_address, and employer_zip are all CTkEntry instances.
        Each represents an input field for the employer’s name, address, and ZIP code.
        They have different placeholder texts (“Name”, “Address”, and “ZIP Code”).
        All three widgets have a width of 250 pixels and black text color.

        Control Number Entry (cn_entry):
        A text input field for entering a control number (CN).
        It has a placeholder text “CN” and a width of 653 pixels.
        The text color is black (#000000), and the background color is white.
        The foreground color (text transparency) is set to transparent.

        Employee Name and Initial Entry (employee_name_i):
        Text input field for entering the employee’s name and initials.
        It has a placeholder text “Name and Initial” and a width of 300 pixels.
        Similar styling with black text color and white background.

        Employee Last Name Entry (employee_last_name):
        A text input field specifically for the employee’s last name.
        Placeholder text is “Last,” and the width is 305 pixels.

        Employee Suffix Entry (employee_suffix):
        A smaller input field for any suffix (e.g., Jr., Sr.) related to the employee’s name.
        Placeholder text is “Suff.” and width is 43 pixels.

        Employee Address Entry (employee_address):
        A larger input field for entering the employee’s address.
        Placeholder text is “Address,” and it has a width of 230 pixels and a height of 20 pixels.

        Employee ZIP Code Entry (employee_zip):
        A compact input field for the employee’s ZIP code.
        Placeholder text is “ZIP,” and it has a width of 100 pixels and a height of 20 pixels.

        Cover and Replacer Images:
        blocker_img: Displays an image loaded from “blocker.png” with a size of 150x85 pixels.
        twenty_four_img: Displays an image loaded from “2024.png” with a size of 100x30 pixels.

        W-2 Label Placement:
        A label for the “W-2” section is positioned at the center of the screen
        (relative x-coordinate = 0.5, relative y-coordinate = 0.5) with an anchor point at the south ("s").
        The label is then packed with a vertical padding of 88 units.

        Employee SSN Entry Field:
        An entry field for the employee’s Social Security Number (SSN) is placed at a relative
        x-coordinate of 0.46 and a relative y-coordinate of 0.123, anchored to the east ("e").

        EIN Entry Field:
        An entry field for the Employer Identification Number (EIN) is placed at a relative
        x-coordinate of 0.535 and a relative y-coordinate of 0.162, anchored to the east.

        Wages Tips C Entry Field:
        An entry field for wages and tips (presumably related to tax reporting) is placed at a relative
        x-coordinate of 0.719 and a relative y-coordinate of 0.162, anchored to the east.

        Social Security Wages Entry Field:
        An entry field for Social Security wages is placed at a relative
        x-coordinate of 0.719 and a relative y-coordinate of 0.2, anchored to the east.

        Medicare Wages and Tips Entry Field:
        An entry field for Medicare wages and tips is placed at a relative
        x-coordinate of 0.719 and a relative y-coordinate of 0.238, anchored to the east.

        Social Security Tips Entry Field:
        An entry field for Social Security tips is placed at a relative
        x-coordinate of 0.719 and a relative y-coordinate of 0.277, anchored to the east.

        Nine Box Entry Field:
        An entry field is placed at a relative
        x-coordinate of 0.719 and a relative y-coordinate of 0.31, anchored to the east.

        Non-Qualified Plans Entry Field:
        An entry field for non-qualified plans is placed at a relative
        x-coordinate of 0.719 and a relative y-coordinate of 0.354, anchored to the east.

        Federal Income Tax Withheld Entry Field:
        An entry field for federal income tax withheld is placed at a relative
        x-coordinate of 0.902 and a relative y-coordinate of 0.162, anchored to the east.

        Social Security Tax Withheld Entry Field:
        An entry field for Social Security tax withheld is placed at a relative
        x-coordinate of 0.902 and a relative y-coordinate of 0.2, anchored to the east.

        Medicare Tax Withheld Entry Field:
        An entry field for Medicare tax withheld is placed at a relative
        x-coordinate of 0.902 and a relative y-coordinate of 0.238, anchored to the east.

        Allocated Tips Entry Field:
        An entry field for allocated tips is placed at a relative
        x-coordinate of 0.902 and a relative y-coordinate of 0.277, anchored to the east.

        Dependent Care Benefits Entry Field:
        An entry field for dependent care benefits is placed at a relative
        x-coordinate of 0.902 and a relative y-coordinate of 0.315, anchored to the east.

        12-A Entry Field:
        An entry field labeled “12-A” is placed at a relative
        x-coordinate of 0.902 and a relative y-coordinate of 0.355, anchored to the east.

        12-B Entry Field:
        An entry field labeled “12-B” is placed at a relative
        x-coordinate of 0.902 and a relative y-coordinate of 0.393, anchored to the east.

        12-C Entry Field:
        An entry field labeled “12-C” is placed at a relative
        x-coordinate of 0.902 and a relative y-coordinate of 0.432, anchored to the east.

        12-D Entry Field:
        An entry field labeled “12-D” is placed at a relative
        x-coordinate of 0.902 and a relative y-coordinate of 0.47, anchored to the east.

        Local Income Tax Entry Field:
        An entry field for local income tax is placed at a relative
        x-coordinate of 0.8265 and a relative y-coordinate of 0.528, anchored to the east.

        Local Wages Tips Entry Field:
        An entry field for local wages and tips is placed at a relative

        The place() method in Tkinter is used for explicitly setting the position and size of a widget within a parent
        container. It allows you to specify the coordinates (x, y) or use relative positioning based on anchor points.

        Several widgets (such as buttons, labels, and text entry fields) are being placed within a GUI
        window using the place() method.

        state_income_tax.place(relx=.5795, rely=0.528, anchor="e"): This places a widget
        at a specific relative position within the parent container. The relx
        and rely parameters determine the relative position, and anchor="e" specifies that the widget should be anchored
        to the east (right) side of its allocated space.

        Other widgets like state wages, employer’s state ID, locality name, etc. are used. Each widget is
        positioned using relative coordinates and an anchor point.
        The blocker_img and twenty_four_img widgets are placed with specific anchor points
        ("s" for south) and relative positions.

        A results_textbox widget is created with specific properties
        (scrollbar button color, width, corner radius, etc.)
        using the CTkTextbox class.

        The comments in the code provide context for each widget, indicating what information or functionality they
        represent (e.g., state income tax, employer’s state ID).

        The ####################### section separates the input fields from the results section.

        Three buttons are being created using the Button widget.
        Each button has a specific label (text) associated with it: “Calculate,” “Save Session,” and “Load Session.”

        The .place() method is used to position the buttons within the GUI window.
        The relx and rely parameters determine the relative position of the button within the window.

        relx=.5 means the button’s horizontal position is centered (50% from the left edge).
        rely=0.965 means the button’s vertical position is near the bottom (96.5% from the top edge).
        The anchor="center" parameter ensures that the button is centered horizontally.

        “Calculate” Button:
        Positioned at the center horizontally (50% from the left edge) and near the bottom (96.5% from the top edge).
        “Save Session” Button:
        Positioned slightly to the left (40% from the left edge) and near the bottom (96.5% from the top edge).
        “Load Session” Button:
        Positioned slightly to the right (60% from the left edge) and near the bottom (96.5% from the top edge).

        """

        self.app = ctk.CTkToplevel()
        self.app.geometry("1500x1200")
        self.app.title("TRACE")
        self.app.resizable(False, False)

        canvas = tk.Canvas(self.app, width=1500, height=1200)
        canvas.place(relx=.5, rely=.5, anchor="center")

        if screensize == (1920, 1080):
            ctk.set_widget_scaling(.7465)
            ctk.set_window_scaling(.7465)
            d_2_img = ImageTk.PhotoImage(Image.open("images/pattern_back.png").resize((1500, 1200)))
            canvas.create_image(0, 0, anchor=tk.NW, image=d_2_img)
            cosmos = canvas.create_text(635, 150, anchor="nw", fill="light blue")
            canvas.itemconfig(cosmos, text="TRACE", width=780)
            canvas.itemconfig(cosmos, font=("Arial", 50))
            aqua = canvas.create_text(670, 755, anchor="nw", fill="light blue")
            canvas.itemconfig(aqua, text="Results", width=780)
            canvas.itemconfig(aqua, font=("Arial", 35))
        else:
            d_2_img = ImageTk.PhotoImage(Image.open("images/pattern_back.png").resize((1500, 1200)))
            canvas.create_image(2, 2, anchor=tk.NW, image=d_2_img)
            cosmos = canvas.create_text(635, 5, anchor="nw", fill="light blue")
            canvas.itemconfig(cosmos, text="TRACE", width=780)
            canvas.itemconfig(cosmos, font=("Arial", 50))
            aqua = canvas.create_text(670, 825, anchor="nw", fill="light blue")
            canvas.itemconfig(aqua, text="Results", width=780)
            canvas.itemconfig(aqua, font=("Arial", 35))
            ctk.set_widget_scaling(1)
            ctk.set_window_scaling(1)

        ctk.set_appearance_mode("")

        # Menu bar
        menubar = Menu(self.app)
        self.app.config(menu=menubar)

        # File menu
        self.file_menu = Menu(menubar, tearoff=0)
        self.file_menu.add_command(label="New", command=self.new_session)
        self.file_menu.add_command(label="Save W-2 As", command=self.save_form_w2_as)
        self.file_menu.add_command(label="Save 1099 As", command=self.save_form_1099_as)
        self.file_menu.add_command(label="Save 1040 As", command=self.save_form_1040_as)
        self.file_menu.add_command(label="Browse W-2", command=self.browse_form_w2)
        self.file_menu.add_command(label="Browse 1099", command=self.browse_form_1099)
        self.file_menu.add_command(label="Browse 1040", command=self.browse_form_1040)
        self.file_menu.add_separator()
        menubar.add_cascade(label="File", menu=self.file_menu)

        # Edit menu
        edit_menu = Menu(menubar, tearoff=0)
        edit_menu.add_command(label="W-2", command=self.setup_w_2)
        edit_menu.add_command(label="1099", command=self.setup_1099)
        edit_menu.add_command(label="1040", command=self.setup_1040)
        menubar.add_cascade(label="Form", menu=edit_menu)

        # Help menu
        help_menu = Menu(menubar, tearoff=0)
        help_menu.add_command(label="About", command=self.view_about)
        help_menu.add_command(label="Quit", command=self.quit)
        menubar.add_cascade(label="Settings", menu=help_menu)

        self.new_decision = "w2"

        self.cursor = y.user_cursor
        self.user_connect = y.user_connection

        self.current_time_date = datetime.datetime.today().strftime('%I:%M %p')
        self.elapsed_time = 0
        self.submit_changer = 0

        self.checkbox_checker = False

        self.filing_status = ""

        self.born_1959 = 0

        self.calculate_changer = "w2"

        self.auto_save_runner = True

        self.old_new = 00.00
        self.old_new_w2_withheld = 00.00

        self.loaded = ""

        ###############################

        # Start Of Input Fields

        self.ten_ninety_nine_img = ctk.CTkImage(light_image=Image.open('images/1099_new.png'), size=(1300, 700))
        self.ten_ninety_nine_label_for_img = ctk.CTkLabel(self.app, text="", image=self.ten_ninety_nine_img)

        # Start 1099 Input Fields

        # Payer name, street address, city/town, state/province, country, zip/postal, phone no.

        self.ten_ninety_nine_payer_info = ctk.CTkEntry(master=self.app, placeholder_text="Payer Name, Address, Phone",
                                                       width=525, height=125,
                                                       text_color="#000000", bg_color="white", fg_color="transparent")

        # Payer TIN

        self.ten_ninety_nine_payer_tin = ctk.CTkEntry(master=self.app, placeholder_text="Payer TIN", width=250,
                                                      text_color="#000000", bg_color="white", fg_color="transparent")

        # Recipient TIN

        self.ten_ninety_nine_recipient_tin = ctk.CTkEntry(master=self.app, placeholder_text="Recipient TIN", width=250,
                                                          text_color="#000000", bg_color="white",
                                                          fg_color="transparent")

        # Recipient Name

        self.ten_ninety_nine_recipient_name = ctk.CTkEntry(master=self.app, placeholder_text="Name", width=500,
                                                           text_color="#000000", bg_color="white",
                                                           fg_color="transparent")

        # Recipient Street Address

        self.ten_ninety_nine_recipient_address = ctk.CTkEntry(master=self.app, placeholder_text="Address", width=500,
                                                              text_color="#000000",
                                                              bg_color="white", fg_color="transparent")

        # Recipient Location Info

        self.ten_ninety_nine_recipient_city_etc = ctk.CTkEntry(master=self.app,
                                                               placeholder_text="City, State, Country, ZIP", width=525,
                                                               height=45, text_color="#000000", bg_color="white",
                                                               fg_color="transparent")

        # Total Ordinary Dividends

        self.ten_ninety_nine_ordinary_dividends = ctk.CTkEntry(master=self.app, placeholder_text="Ordinary Dividends",
                                                               width=200, text_color="#000000", bg_color="white",
                                                               fg_color="transparent")
        # Qualified Dividends
        self.ten_ninety_nine_qualified_dividends = ctk.CTkEntry(master=self.app, placeholder_text="Qualified Dividends",
                                                                width=200, text_color="#000000", bg_color="white",
                                                                fg_color="transparent")
        # Total Capital Gain
        self.ten_ninety_nine_capital_gain = ctk.CTkEntry(master=self.app, placeholder_text="Total Capital Gain",
                                                         width=200, text_color="#000000", bg_color="white",
                                                         fg_color="transparent")
        # Unrecap. Section 1250 Gain
        self.ten_ninety_nine_1250_gain = ctk.CTkEntry(master=self.app, placeholder_text="Section 1250 Gain", width=200,
                                                      text_color="#000000", bg_color="white", fg_color="transparent")
        # Section 1202 Gain
        self.ten_ninety_nine_1202_gain = ctk.CTkEntry(master=self.app, placeholder_text="Section 1202 Gain", width=200,
                                                      text_color="#000000", bg_color="white", fg_color="transparent")
        # Collectibles gain
        self.ten_ninety_nine_collectibles_gain = ctk.CTkEntry(master=self.app, placeholder_text="Collections Gain",
                                                              width=200, text_color="#000000", bg_color="white",
                                                              fg_color="transparent")
        # Section 897 Ordinary Dividends
        self.ten_ninety_nine_897_dividends = ctk.CTkEntry(master=self.app, placeholder_text="897 Ordinary Dividends",
                                                          width=200, text_color="#000000", bg_color="white",
                                                          fg_color="transparent")
        # Section 897 Capital Gain
        self.ten_ninety_nine_897_gain = ctk.CTkEntry(master=self.app, placeholder_text="897 Gains", width=200,
                                                     text_color="#000000", bg_color="white", fg_color="transparent")
        # Nondividend Distributions
        self.ten_ninety_nine_nondividend = ctk.CTkEntry(master=self.app, placeholder_text="Nondividend Distributions",
                                                        width=200, text_color="#000000", bg_color="white",
                                                        fg_color="transparent")
        # Federal Income Tax Withheld
        self.ten_ninety_nine_federal_tax_withheld = ctk.CTkEntry(master=self.app,
                                                                 placeholder_text="Federal Tax Withheld", width=200,
                                                                 text_color="#000000", bg_color="white",
                                                                 fg_color="transparent")
        # Section 199A Dividends
        self.ten_ninety_nine_199a = ctk.CTkEntry(master=self.app, placeholder_text="199A Dividends", width=200,
                                                 text_color="#000000", bg_color="white", fg_color="transparent")
        # Investment Expenses
        self.ten_ninety_nine_investment_expenses = ctk.CTkEntry(master=self.app, placeholder_text="Investment Expenses",
                                                                width=200, text_color="#000000", bg_color="white",
                                                                fg_color="transparent")
        # Foreign Tax Paid
        self.ten_ninety_nine_foreign_tax = ctk.CTkEntry(master=self.app, placeholder_text="Foreign Tax", width=200,
                                                        text_color="#000000", bg_color="white", fg_color="transparent")
        # Foreign Country or U.S. Possession
        self.ten_ninety_nine_foreign_tax_country = ctk.CTkEntry(master=self.app, placeholder_text="Country", width=200,
                                                                text_color="#000000", bg_color="white",
                                                                fg_color="transparent")

        # Cash Liquidation Distributions
        self.ten_ninety_nine_cash_liquidation = ctk.CTkEntry(master=self.app, placeholder_text="Cash Liquidation",
                                                             width=200, text_color="#000000", bg_color="white",
                                                             fg_color="transparent")
        # Noncash Liquidation Distributions
        self.ten_ninety_nine_noncash_liquidation = ctk.CTkEntry(master=self.app, placeholder_text="Noncash Liquidation",
                                                                width=200, text_color="#000000", bg_color="white",
                                                                fg_color="transparent")

        # Exempt-Interest Dividends
        self.ten_ninety_nine_exempt_dividends = ctk.CTkEntry(master=self.app, placeholder_text="Interest-Exempt",
                                                             width=200, text_color="#000000", bg_color="white",
                                                             fg_color="transparent")
        # Specified Private Activity Bond Interest Dividends
        self.ten_ninety_nine_specified_bond_dividends = ctk.CTkEntry(master=self.app,
                                                                     placeholder_text="Specified Bond Dividends",
                                                                     width=200, text_color="#000000", bg_color="white",
                                                                     fg_color="transparent")
        # Account Number
        self.ten_ninety_nine_account_number = ctk.CTkEntry(master=self.app, placeholder_text="Account Number",
                                                           width=500, text_color="#000000", bg_color="white",
                                                           fg_color="transparent")
        # State
        self.ten_ninety_nine_state = ctk.CTkEntry(master=self.app, placeholder_text="ST", width=50,
                                                  text_color="#000000", bg_color="white", fg_color="transparent")
        # State Identification Number
        self.ten_ninety_nine_state_id_number = ctk.CTkEntry(master=self.app, placeholder_text="State ID", width=130,
                                                            text_color="#000000", bg_color="white",
                                                            fg_color="transparent")
        # State Tax Withheld
        self.ten_ninety_nine_state_tax_withheld = ctk.CTkEntry(master=self.app, placeholder_text="State Tax", width=200,
                                                               text_color="#000000", bg_color="white",
                                                               fg_color="transparent")

        # End 1099 Input Fields

        # W-2 Form Section

        self.w_2_img = ctk.CTkImage(light_image=Image.open('images/w_2_form.png'), size=(1300, 700))
        self.w_2_label_for_img = ctk.CTkLabel(self.app, text="", image=self.w_2_img)

        # Employee Social Security Number

        self.essn_entry = ctk.CTkEntry(master=self.app, placeholder_text="ESSN", width=283, height=25,
                                       text_color="#000000",
                                       bg_color="white", fg_color="transparent")

        # Employer ID Number

        self.ein_entry = ctk.CTkEntry(master=self.app, placeholder_text="EIN", width=653, height=25,
                                      text_color="#000000",
                                      bg_color="white", fg_color="transparent")

        # Wages, Tips, Other Compensation

        self.wages_tips_c = ctk.CTkEntry(master=self.app, placeholder_text="wages", width=269, height=25,
                                         text_color="#000000",
                                         bg_color="white", fg_color="transparent")

        # Social Security Wages

        self.social_wages = ctk.CTkEntry(master=self.app, placeholder_text="social wages", width=269, height=25,
                                         text_color="#000000",
                                         bg_color="white", fg_color="transparent")

        # Medicare Wages

        self.medicare_wages = ctk.CTkEntry(master=self.app, placeholder_text="medicare", width=269, height=25,
                                           text_color="#000000",
                                           bg_color="white", fg_color="transparent")

        # Social Security Tips

        self.social_security_tips = ctk.CTkEntry(master=self.app, placeholder_text="SS Tips", width=269, height=25,
                                                 text_color="#000000",
                                                 bg_color="white", fg_color="transparent")

        #  Non-Qualified Plans

        self.non_qualified_plans = ctk.CTkEntry(master=self.app, placeholder_text="plans", width=269, height=25,
                                                text_color="#000000",
                                                bg_color="white", fg_color="transparent")

        #  Federal Income Tax Withheld

        self.fed_income_tax_withheld = ctk.CTkEntry(master=self.app, placeholder_text="fed", width=269, height=25,
                                                    text_color="#000000",
                                                    bg_color="white", fg_color="transparent")

        #  Social Security Tax Withheld

        self.social_security_tax_withheld = ctk.CTkEntry(master=self.app, placeholder_text="SS Tax", width=269,
                                                         height=25,
                                                         text_color="#000000",
                                                         bg_color="white", fg_color="transparent")

        #  Medicare Tax Withheld

        self.medicare_tax_withheld = ctk.CTkEntry(master=self.app, placeholder_text="medicare withheld", width=269,
                                                  height=25,
                                                  text_color="#000000",
                                                  bg_color="white", fg_color="transparent")

        #  Allocated Tips

        self.allocated_tips = ctk.CTkEntry(master=self.app, placeholder_text="A Tips", width=269, height=25,
                                           text_color="#000000",
                                           bg_color="white", fg_color="transparent")

        #  Dependent Care Benefits

        self.dependent_care_benefits = ctk.CTkEntry(master=self.app, placeholder_text="DCB", width=269, height=25,
                                                    text_color="#000000",
                                                    bg_color="white", fg_color="transparent")

        #  12-A

        self.twelve_a = ctk.CTkEntry(master=self.app, placeholder_text="12a", width=190, height=25,
                                     text_color="#000000",
                                     bg_color="white", fg_color="transparent")

        #  12-B

        self.twelve_b = ctk.CTkEntry(master=self.app, placeholder_text="12b", width=190, height=25,
                                     text_color="#000000",
                                     bg_color="white", fg_color="transparent")

        #  12-C

        self.twelve_c = ctk.CTkEntry(master=self.app, placeholder_text="12c", width=190, height=25,
                                     text_color="#000000",
                                     bg_color="white", fg_color="transparent")

        #  12-D

        self.twelve_d = ctk.CTkEntry(master=self.app, placeholder_text="12d", width=190, height=25,
                                     text_color="#000000",
                                     bg_color="white", fg_color="transparent")

        #  Local Income Tax

        self.local_income_tax = ctk.CTkEntry(master=self.app, placeholder_text="local income", width=174, height=25,
                                             text_color="#000000",
                                             bg_color="white", fg_color="transparent")

        #  State Income Tax

        self.state_income_tax = ctk.CTkEntry(master=self.app, placeholder_text="state income", width=174, height=25,
                                             text_color="#000000",
                                             bg_color="white", fg_color="transparent")

        #  State Wages, Tips, ETC.

        self.state_wage_tips = ctk.CTkEntry(master=self.app, placeholder_text="state wages", width=190, height=25,
                                            text_color="#000000",
                                            bg_color="white", fg_color="transparent")

        #  Employer's State ID

        self.employers_state_id = ctk.CTkEntry(master=self.app, placeholder_text="employer's state", width=287,
                                               height=25,
                                               text_color="#000000",
                                               bg_color="white", fg_color="transparent")

        #  State

        self.state_field = ctk.CTkEntry(master=self.app, placeholder_text="state", width=60, height=25,
                                        text_color="#000000",
                                        bg_color="white", fg_color="transparent")

        #  Locality Name

        self.locality_name = ctk.CTkEntry(master=self.app, placeholder_text="locality", width=109, height=25,
                                          text_color="#000000",
                                          bg_color="white", fg_color="transparent")

        #  Local Wages, Tips, ETC.

        self.local_wage_tips = ctk.CTkEntry(master=self.app, placeholder_text="local wages", width=190, height=25,
                                            text_color="#000000",
                                            bg_color="white", fg_color="transparent")

        #  Other

        self.other_field = ctk.CTkEntry(master=self.app, placeholder_text="other", width=269, height=90,
                                        text_color="#000000",
                                        bg_color="white", fg_color="transparent")

        # Employer Name, Address, ZIP

        self.employer_name_etc = ctk.CTkEntry(master=self.app, placeholder_text="Name, Address, ZIP", height=115,
                                              width=653, text_color="#000000",
                                              bg_color="white", fg_color="transparent")

        # Control Number

        self.cn_entry = ctk.CTkEntry(master=self.app, placeholder_text="CN", width=653, height=25, text_color="#000000",
                                     bg_color="white", fg_color="transparent")

        # Employee Name And Initial

        self.employee_name_i = ctk.CTkEntry(master=self.app, placeholder_text="Name and Initial", width=300,
                                            text_color="#000000", bg_color="white", fg_color="transparent")

        # Employee Last Name

        self.employee_last_name = ctk.CTkEntry(master=self.app, placeholder_text="Last", width=305,
                                               text_color="#000000", bg_color="white", fg_color="transparent")

        # Employee Suffix

        self.employee_suffix = ctk.CTkEntry(master=self.app, placeholder_text="Suff.", width=43,
                                            text_color="#000000", bg_color="white", fg_color="transparent")

        # Employee Address and Zip

        self.employee_address_etc = ctk.CTkEntry(master=self.app, placeholder_text="Address and ZIP", width=387,
                                                 height=20,
                                                 text_color="#000000", bg_color="white", fg_color="transparent")

        # Cover And Replacer For Year On Form

        self.blocker = ctk.CTkImage(light_image=Image.open('images/blocker.png'), size=(150, 85))
        self.blocker_img = ctk.CTkLabel(self.app, text="", image=self.blocker)
        self.twenty_four = ctk.CTkImage(light_image=Image.open('images/2024.png'), size=(100, 30))
        self.twenty_four_img = ctk.CTkLabel(self.app, text="", image=self.twenty_four)

        # End Of W-2 Input Fields

        # Start 1040 Input Fields

        self.ten_forty_scrolling_frame = ctk.CTkScrollableFrame(self.app, width=1000, height=690)

        self.ten_forty_img_1 = ctk.CTkImage(light_image=Image.open('images/1040_new_pg1.jpg'), size=(1000, 2000))
        self.ten_forty_img_2 = ctk.CTkImage(light_image=Image.open('images/1040_new_pg2.jpg'), size=(1000, 1655))
        self.ten_forty_label_for_pg_1 = ctk.CTkLabel(self.ten_forty_scrolling_frame, text="",
                                                     image=self.ten_forty_img_1)
        self.ten_forty_label_for_pg_2 = ctk.CTkLabel(self.ten_forty_scrolling_frame, text="",
                                                     image=self.ten_forty_img_2)

        self.ten_forty_first_name = ctk.CTkEntry(master=self.ten_forty_scrolling_frame,
                                                 placeholder_text="First and Initial",
                                                 width=310, height=40, text_color="#000000", bg_color="white",
                                                 fg_color="transparent")
        self.ten_forty_last_name = ctk.CTkEntry(master=self.ten_forty_scrolling_frame, placeholder_text="Last",
                                                width=335, height=40, text_color="#000000", bg_color="white",
                                                fg_color="transparent")
        self.ten_forty_spouse_first = ctk.CTkEntry(master=self.ten_forty_scrolling_frame,
                                                   placeholder_text="First and Initial",
                                                   width=310, height=40, text_color="#000000", bg_color="white",
                                                   fg_color="transparent")
        self.ten_forty_spouse_last = ctk.CTkEntry(master=self.ten_forty_scrolling_frame, placeholder_text="Last",
                                                  width=335, height=40, text_color="#000000", bg_color="white",
                                                  fg_color="transparent")
        self.ten_forty_home_address = ctk.CTkEntry(master=self.ten_forty_scrolling_frame, placeholder_text="Address",
                                                   width=650, height=40, text_color="#000000", bg_color="white",
                                                   fg_color="transparent")
        self.ten_forty_apt_no = ctk.CTkEntry(master=self.ten_forty_scrolling_frame, placeholder_text="No.", width=60,
                                             height=40, text_color="#000000", bg_color="white", fg_color="transparent")
        self.ten_forty_city = ctk.CTkEntry(master=self.ten_forty_scrolling_frame,
                                           placeholder_text="City, Town, or Post Office",
                                           width=420, height=40, text_color="#000000", bg_color="white",
                                           fg_color="transparent")
        self.ten_forty_state = ctk.CTkEntry(master=self.ten_forty_scrolling_frame, placeholder_text="State", width=75,
                                            height=40, text_color="#000000", bg_color="white", fg_color="transparent")
        self.ten_forty_zip = ctk.CTkEntry(master=self.ten_forty_scrolling_frame, placeholder_text="ZIP", width=75,
                                          height=40, text_color="#000000", bg_color="white", fg_color="transparent")
        self.ten_forty_foreign_country = ctk.CTkEntry(master=self.ten_forty_scrolling_frame,
                                                      placeholder_text="Foreign Country",
                                                      width=320, height=40, text_color="#000000", bg_color="white",
                                                      fg_color="transparent")
        self.ten_forty_foreign_province = ctk.CTkEntry(master=self.ten_forty_scrolling_frame,
                                                       placeholder_text="Foreign Province",
                                                       width=200, height=40, text_color="#000000", bg_color="white",
                                                       fg_color="transparent")
        self.ten_forty_foreign_post_code = ctk.CTkEntry(master=self.ten_forty_scrolling_frame,
                                                        placeholder_text="Post", width=75,
                                                        height=40, text_color="#000000", bg_color="white",
                                                        fg_color="transparent")

        self.ten_forty_presidential_you = ctk.CTkCheckBox(master=self.ten_forty_scrolling_frame, width=0, text="",
                                                          checkbox_height=25, height=0, bg_color="white")
        self.ten_forty_presidential_spouse = ctk.CTkCheckBox(master=self.ten_forty_scrolling_frame, width=0, text="",
                                                             checkbox_height=25, height=0, bg_color="white")

        self.ten_forty_filing_single = ctk.CTkCheckBox(master=self.ten_forty_scrolling_frame, width=0, text="",
                                                       checkbox_height=22, height=0, bg_color="white")
        self.ten_forty_filing_jointly = ctk.CTkCheckBox(master=self.ten_forty_scrolling_frame, width=0, text="",
                                                        checkbox_height=22, height=0, bg_color="white")
        self.ten_forty_filing_separately = ctk.CTkCheckBox(master=self.ten_forty_scrolling_frame, width=0, text="",
                                                           checkbox_height=22, height=0, bg_color="white")
        self.ten_forty_filing_hoh = ctk.CTkCheckBox(master=self.ten_forty_scrolling_frame, width=0, text="",
                                                    checkbox_height=22, height=0, bg_color="white")
        self.ten_forty_filing_qss = ctk.CTkCheckBox(master=self.ten_forty_scrolling_frame, width=0, text="",
                                                    checkbox_height=22, height=0, bg_color="white")
        self.ten_forty_digital_assets_yes = ctk.CTkCheckBox(master=self.ten_forty_scrolling_frame, width=0, text="",
                                                            checkbox_height=22, height=0, bg_color="white")
        self.ten_forty_digital_assets_no = ctk.CTkCheckBox(master=self.ten_forty_scrolling_frame, width=0, text="",
                                                           checkbox_height=22, height=0, bg_color="white")
        self.ten_forty_are_dependent = ctk.CTkCheckBox(master=self.ten_forty_scrolling_frame, width=0, text="",
                                                       checkbox_height=22, height=0, bg_color="white")
        self.ten_forty_spouse_dependent = ctk.CTkCheckBox(master=self.ten_forty_scrolling_frame, width=0, text="",
                                                          checkbox_height=22, height=0, bg_color="white")
        self.ten_forty_spouse_separate = ctk.CTkCheckBox(master=self.ten_forty_scrolling_frame, width=0, text="",
                                                         checkbox_height=22, height=0, bg_color="white")
        self.ten_forty_self_1959 = ctk.CTkCheckBox(master=self.ten_forty_scrolling_frame, width=0, text="",
                                                   checkbox_height=22, height=0, bg_color="white")
        self.ten_forty_self_blind = ctk.CTkCheckBox(master=self.ten_forty_scrolling_frame, width=0, text="",
                                                    checkbox_height=22, height=0, bg_color="white")
        self.ten_forty_spouse_1959 = ctk.CTkCheckBox(master=self.ten_forty_scrolling_frame, width=0, text="",
                                                     checkbox_height=22, height=0, bg_color="white")
        self.ten_forty_spouse_blind = ctk.CTkCheckBox(master=self.ten_forty_scrolling_frame, width=0, text="",
                                                      checkbox_height=22, height=0, bg_color="white")
        self.ten_forty_many_dependents = ctk.CTkCheckBox(master=self.ten_forty_scrolling_frame, width=0, text="",
                                                         checkbox_height=22, height=0, bg_color="white")
        self.ten_forty_dependent_first_1 = ctk.CTkEntry(master=self.ten_forty_scrolling_frame,
                                                        placeholder_text="First and Last",
                                                        width=300, height=32,
                                                        text_color="#000000", bg_color="white", fg_color="transparent")

        self.ten_forty_dependent_first_2 = ctk.CTkEntry(master=self.ten_forty_scrolling_frame,
                                                        placeholder_text="First and Last",
                                                        width=300, height=32,
                                                        text_color="#000000", bg_color="white", fg_color="transparent")

        self.ten_forty_dependent_first_3 = ctk.CTkEntry(master=self.ten_forty_scrolling_frame,
                                                        placeholder_text="First and Last",
                                                        width=300, height=32,
                                                        text_color="#000000", bg_color="white", fg_color="transparent")

        self.ten_forty_dependent_first_4 = ctk.CTkEntry(master=self.ten_forty_scrolling_frame,
                                                        placeholder_text="First and Last",
                                                        width=300, height=32,
                                                        text_color="#000000", bg_color="white", fg_color="transparent")

        self.ten_forty_dependent_1_child_credit = ctk.CTkCheckBox(master=self.ten_forty_scrolling_frame, width=0,
                                                                  text="",
                                                                  checkbox_height=22, height=0, bg_color="white")
        self.ten_forty_dependent_1_other_credit = ctk.CTkCheckBox(master=self.ten_forty_scrolling_frame, width=0,
                                                                  text="", checkbox_height=22, height=0,
                                                                  bg_color="white")
        self.ten_forty_dependent_2_child_credit = ctk.CTkCheckBox(master=self.ten_forty_scrolling_frame, width=0,
                                                                  text="", checkbox_height=22, height=0,
                                                                  bg_color="white")
        self.ten_forty_dependent_2_other_credit = ctk.CTkCheckBox(master=self.ten_forty_scrolling_frame, width=0,
                                                                  text="", checkbox_height=22, height=0,
                                                                  bg_color="white")
        self.ten_forty_dependent_3_child_credit = ctk.CTkCheckBox(master=self.ten_forty_scrolling_frame, width=0,
                                                                  text="", checkbox_height=22, height=0,
                                                                  bg_color="white")
        self.ten_forty_dependent_3_other_credit = ctk.CTkCheckBox(master=self.ten_forty_scrolling_frame, width=0,
                                                                  text="", checkbox_height=22, height=0,
                                                                  bg_color="white")
        self.ten_forty_dependent_4_child_credit = ctk.CTkCheckBox(master=self.ten_forty_scrolling_frame, width=0,
                                                                  text="", checkbox_height=22, height=0,
                                                                  bg_color="white")
        self.ten_forty_dependent_4_other_credit = ctk.CTkCheckBox(master=self.ten_forty_scrolling_frame, width=0,
                                                                  text="", checkbox_height=22, height=0,
                                                                  bg_color="white")
        self.ten_forty_total_w2s = ctk.CTkEntry(master=self.ten_forty_scrolling_frame, placeholder_text="W-2 Total",
                                                width=125,
                                                height=32, text_color="#000000", bg_color="white",
                                                fg_color="transparent")
        self.ten_forty_household_wages = ctk.CTkEntry(master=self.ten_forty_scrolling_frame,
                                                      placeholder_text="Household Wage",
                                                      width=125, height=32, text_color="#000000", bg_color="white",
                                                      fg_color="transparent")
        self.ten_forty_tip_income = ctk.CTkEntry(master=self.ten_forty_scrolling_frame, placeholder_text="Tips",
                                                 width=125, height=32, text_color="#000000", bg_color="white",
                                                 fg_color="transparent")
        self.ten_forty_medicaid_waiver = ctk.CTkEntry(master=self.ten_forty_scrolling_frame,
                                                      placeholder_text="Medicaid Payments",
                                                      width=125, height=32, text_color="#000000", bg_color="white",
                                                      fg_color="transparent")
        self.ten_forty_dependent_benefits = ctk.CTkEntry(master=self.ten_forty_scrolling_frame,
                                                         placeholder_text="Dependent Payments",
                                                         width=125, height=32, text_color="#000000", bg_color="white",
                                                         fg_color="transparent")
        self.ten_forty_adoption_benefits = ctk.CTkEntry(master=self.ten_forty_scrolling_frame,
                                                        placeholder_text="Adoption Benefits",
                                                        width=125, height=32, text_color="#000000", bg_color="white",
                                                        fg_color="transparent")
        self.ten_forty_8919_wages = ctk.CTkEntry(master=self.ten_forty_scrolling_frame, placeholder_text="8919 Wages",
                                                 width=125, height=32, text_color="#000000", bg_color="white",
                                                 fg_color="transparent")
        self.ten_forty_other_income = ctk.CTkEntry(master=self.ten_forty_scrolling_frame,
                                                   placeholder_text="Other Income",
                                                   width=125, height=32, text_color="#000000", bg_color="white",
                                                   fg_color="transparent")
        self.ten_forty_combat_pay = ctk.CTkEntry(master=self.ten_forty_scrolling_frame, placeholder_text="Combat Pay",
                                                 width=125, height=32, text_color="#000000", bg_color="white",
                                                 fg_color="transparent")
        self.ten_forty_1_ah_sum = ctk.CTkEntry(master=self.ten_forty_scrolling_frame, placeholder_text="Total",
                                               width=125,
                                               height=32, text_color="#000000", bg_color="white",
                                               fg_color="transparent")
        self.ten_forty_tax_exempt_interest = ctk.CTkEntry(master=self.ten_forty_scrolling_frame,
                                                          placeholder_text="Exempt Interest",
                                                          width=125, height=32, text_color="#000000", bg_color="white",
                                                          fg_color="transparent")
        self.ten_forty_taxable_interest = ctk.CTkEntry(master=self.ten_forty_scrolling_frame,
                                                       placeholder_text="Taxable Interest",
                                                       width=125, height=32, text_color="#000000", bg_color="white",
                                                       fg_color="transparent")
        self.ten_forty_qualified_dividends = ctk.CTkEntry(master=self.ten_forty_scrolling_frame,
                                                          placeholder_text="Qualified Dividends",
                                                          width=125, height=32, text_color="#000000", bg_color="white",
                                                          fg_color="transparent")
        self.ten_forty_ordinary_dividends = ctk.CTkEntry(master=self.ten_forty_scrolling_frame,
                                                         placeholder_text="Ordinary Dividends",
                                                         width=125, height=32, text_color="#000000", bg_color="white",
                                                         fg_color="transparent")
        self.ten_forty_ira_distributions = ctk.CTkEntry(master=self.ten_forty_scrolling_frame,
                                                        placeholder_text="IRA Distributions",
                                                        width=125, height=32, text_color="#000000", bg_color="white",
                                                        fg_color="transparent")
        self.ten_forty_taxable_ira = ctk.CTkEntry(master=self.ten_forty_scrolling_frame,
                                                  placeholder_text="Taxable Amount",
                                                  width=125, height=32, text_color="#000000", bg_color="white",
                                                  fg_color="transparent")
        self.ten_forty_pensions_annuities = ctk.CTkEntry(master=self.ten_forty_scrolling_frame,
                                                         placeholder_text="Pensions",
                                                         width=125, height=32, text_color="#000000", bg_color="white",
                                                         fg_color="transparent")
        self.ten_forty_taxable_pensions = ctk.CTkEntry(master=self.ten_forty_scrolling_frame,
                                                       placeholder_text="Taxable Amount",
                                                       width=125, height=32, text_color="#000000", bg_color="white",
                                                       fg_color="transparent")
        self.ten_forty_social_security = ctk.CTkEntry(master=self.ten_forty_scrolling_frame,
                                                      placeholder_text="Social Security",
                                                      width=125, height=32, text_color="#000000", bg_color="white",
                                                      fg_color="transparent")
        self.ten_forty_social_taxable = ctk.CTkEntry(master=self.ten_forty_scrolling_frame,
                                                     placeholder_text="Taxable Amount",
                                                     width=125, height=32, text_color="#000000", bg_color="white",
                                                     fg_color="transparent")

        self.ten_forty_lump_sum_method = ctk.CTkCheckBox(master=self.ten_forty_scrolling_frame, width=0,
                                                         text="", checkbox_height=22, height=0, bg_color="white")
        self.ten_forty_schedule_d = ctk.CTkCheckBox(master=self.ten_forty_scrolling_frame, width=0,
                                                    text="", checkbox_height=25, height=0, bg_color="white")

        self.ten_forty_capital_gain = ctk.CTkEntry(master=self.ten_forty_scrolling_frame,
                                                   placeholder_text="Capital Gain",
                                                   width=125, height=32, text_color="#000000", bg_color="white",
                                                   fg_color="transparent")
        self.ten_forty_schedule_1 = ctk.CTkEntry(master=self.ten_forty_scrolling_frame,
                                                 placeholder_text="Schedule 1 Income",
                                                 width=125, height=32, text_color="#000000", bg_color="white",
                                                 fg_color="transparent")
        self.ten_forty_total_income = ctk.CTkEntry(master=self.ten_forty_scrolling_frame,
                                                   placeholder_text="Total Income",
                                                   width=125, height=32, text_color="#000000", bg_color="white",
                                                   fg_color="transparent")
        self.ten_forty_income_adjustments = ctk.CTkEntry(master=self.ten_forty_scrolling_frame,
                                                         placeholder_text="Adjustments",
                                                         width=125, height=32, text_color="#000000", bg_color="white",
                                                         fg_color="transparent")
        self.ten_forty_adjusted_income = ctk.CTkEntry(master=self.ten_forty_scrolling_frame,
                                                      placeholder_text="Adjusted Income",
                                                      width=125, height=32, text_color="#000000", bg_color="white",
                                                      fg_color="transparent")
        self.ten_forty_deductions = ctk.CTkEntry(master=self.ten_forty_scrolling_frame, placeholder_text="Deductions",
                                                 width=125, height=32, text_color="#000000", bg_color="white",
                                                 fg_color="transparent")
        self.ten_forty_business_deductions = ctk.CTkEntry(master=self.ten_forty_scrolling_frame,
                                                          placeholder_text="Business Deductions",
                                                          width=125, height=32, text_color="#000000", bg_color="white",
                                                          fg_color="transparent")
        self.ten_forty_total_deductions = ctk.CTkEntry(master=self.ten_forty_scrolling_frame,
                                                       placeholder_text="Total Deductions",
                                                       width=125, height=32, text_color="#000000", bg_color="white",
                                                       fg_color="transparent")
        self.ten_forty_taxable_income = ctk.CTkEntry(master=self.ten_forty_scrolling_frame,
                                                     placeholder_text="Taxable Income",
                                                     width=125, height=32, text_color="#000000", bg_color="white",
                                                     fg_color="transparent")

        self.ten_forty_8814 = ctk.CTkCheckBox(master=self.ten_forty_scrolling_frame, width=0, text="",
                                              checkbox_height=22, height=0, bg_color="white")
        self.ten_forty_4972 = ctk.CTkCheckBox(master=self.ten_forty_scrolling_frame, width=0, text="",
                                              checkbox_height=22, height=0, bg_color="white")
        self.ten_forty_other_form_check = ctk.CTkCheckBox(master=self.ten_forty_scrolling_frame, width=0, text="",
                                                          checkbox_height=22, height=0, bg_color="white")

        self.ten_forty_8888 = ctk.CTkCheckBox(master=self.ten_forty_scrolling_frame, width=0, text="",
                                              checkbox_height=25, height=0, bg_color="white")
        self.ten_forty_route_checking = ctk.CTkCheckBox(master=self.ten_forty_scrolling_frame, width=0, text="",
                                                        checkbox_height=25, height=0, bg_color="white")
        self.ten_forty_route_savings = ctk.CTkCheckBox(master=self.ten_forty_scrolling_frame, width=0, text="",
                                                       checkbox_height=25, height=0, bg_color="white")
        self.ten_forty_third_party_yes = ctk.CTkCheckBox(master=self.ten_forty_scrolling_frame, width=0, text="",
                                                         checkbox_height=25, height=0, bg_color="white")
        self.ten_forty_third_party_no = ctk.CTkCheckBox(master=self.ten_forty_scrolling_frame, width=0, text="",
                                                        checkbox_height=25, height=0, bg_color="white")
        self.ten_forty_self_employed = ctk.CTkCheckBox(master=self.ten_forty_scrolling_frame, width=0, text="",
                                                       checkbox_height=25, height=0, bg_color="white")

        self.ten_forty_other_form_no = ctk.CTkEntry(master=self.ten_forty_scrolling_frame, placeholder_text="Form No.",
                                                    width=75, height=32, text_color="#000000", bg_color="white",
                                                    fg_color="transparent")
        self.ten_forty_other_form_total = ctk.CTkEntry(master=self.ten_forty_scrolling_frame, placeholder_text="Tax",
                                                       width=125, height=32, text_color="#000000", bg_color="white",
                                                       fg_color="transparent")
        self.ten_forty_schedule_2 = ctk.CTkEntry(master=self.ten_forty_scrolling_frame, placeholder_text="Schedule 2",
                                                 width=125, height=32, text_color="#000000", bg_color="white",
                                                 fg_color="transparent")
        self.ten_forty_add_16_17 = ctk.CTkEntry(master=self.ten_forty_scrolling_frame, placeholder_text="Total",
                                                width=125,
                                                height=32, text_color="#000000", bg_color="white",
                                                fg_color="transparent")
        self.ten_forty_child_credit = ctk.CTkEntry(master=self.ten_forty_scrolling_frame,
                                                   placeholder_text="Child Credits",
                                                   width=125, height=32, text_color="#000000", bg_color="white",
                                                   fg_color="transparent")
        self.ten_forty_schedule_3 = ctk.CTkEntry(master=self.ten_forty_scrolling_frame, placeholder_text="Schedule 3",
                                                 width=125, height=32, text_color="#000000", bg_color="white",
                                                 fg_color="transparent")
        self.ten_forty_add_19_20 = ctk.CTkEntry(master=self.ten_forty_scrolling_frame, placeholder_text="Total",
                                                width=125, height=32, text_color="#000000", bg_color="white",
                                                fg_color="transparent")
        self.ten_forty_sub_21_18 = ctk.CTkEntry(master=self.ten_forty_scrolling_frame, placeholder_text="22",
                                                width=125, height=32, text_color="#000000", bg_color="white",
                                                fg_color="transparent")
        self.ten_forty_other_taxes = ctk.CTkEntry(master=self.ten_forty_scrolling_frame, placeholder_text="Other Taxes",
                                                  width=125, height=32, text_color="#000000", bg_color="white",
                                                  fg_color="transparent")
        self.ten_forty_total_tax = ctk.CTkEntry(master=self.ten_forty_scrolling_frame, placeholder_text="Total Tax",
                                                width=125, height=32, text_color="#000000", bg_color="white",
                                                fg_color="transparent")

        self.ten_forty_withheld_w2 = ctk.CTkEntry(master=self.ten_forty_scrolling_frame, placeholder_text="W-2 Tax",
                                                  width=125, height=32, text_color="#000000", bg_color="white",
                                                  fg_color="transparent")
        self.ten_forty_withheld_1099 = ctk.CTkEntry(master=self.ten_forty_scrolling_frame, placeholder_text="1099 Tax",
                                                    width=125, height=32, text_color="#000000", bg_color="white",
                                                    fg_color="transparent")
        self.ten_forty_withheld_other = ctk.CTkEntry(master=self.ten_forty_scrolling_frame, placeholder_text="Other",
                                                     width=125, height=32, text_color="#000000", bg_color="white",
                                                     fg_color="transparent")
        self.ten_forty_withheld_total = ctk.CTkEntry(master=self.ten_forty_scrolling_frame, placeholder_text="Total",
                                                     width=125, height=32, text_color="#000000", bg_color="white",
                                                     fg_color="transparent")
        self.ten_forty_previous_year = ctk.CTkEntry(master=self.ten_forty_scrolling_frame,
                                                    placeholder_text="Applied Return",
                                                    width=125, height=32, text_color="#000000", bg_color="white",
                                                    fg_color="transparent")
        self.ten_forty_eic = ctk.CTkEntry(master=self.ten_forty_scrolling_frame, placeholder_text="EIC", width=125,
                                          height=32, text_color="#000000", bg_color="white", fg_color="transparent")
        self.ten_forty_8812_child_credit = ctk.CTkEntry(master=self.ten_forty_scrolling_frame,
                                                        placeholder_text="Child Credits",
                                                        width=125, height=32, text_color="#000000", bg_color="white",
                                                        fg_color="transparent")
        self.ten_forty_8863_opportunity_credit = ctk.CTkEntry(master=self.ten_forty_scrolling_frame,
                                                              placeholder_text="Opportunity Credit",
                                                              width=125, height=32, text_color="#000000",
                                                              bg_color="white",
                                                              fg_color="transparent")
        self.ten_forty_schedule_3_line_15 = ctk.CTkEntry(master=self.ten_forty_scrolling_frame,
                                                         placeholder_text="Schedule 3",
                                                         width=125, height=32, text_color="#000000", bg_color="white",
                                                         fg_color="transparent")
        self.ten_forty_other_payments = ctk.CTkEntry(master=self.ten_forty_scrolling_frame,
                                                     placeholder_text="Total Other",
                                                     width=125, height=32, text_color="#000000", bg_color="white",
                                                     fg_color="transparent")
        self.ten_forty_total_payments = ctk.CTkEntry(master=self.ten_forty_scrolling_frame,
                                                     placeholder_text="Total Payments",
                                                     width=125, height=32, text_color="#000000", bg_color="white",
                                                     fg_color="transparent")

        self.ten_forty_overpaid = ctk.CTkEntry(master=self.ten_forty_scrolling_frame, placeholder_text="Total",
                                               width=125, height=32, text_color="#000000", bg_color="white",
                                               fg_color="transparent")
        self.ten_forty_owed = ctk.CTkEntry(master=self.ten_forty_scrolling_frame, placeholder_text="Total Owed",
                                           width=125, height=32, text_color="#000000", bg_color="white",
                                           fg_color="transparent")
        self.ten_forty_penalty = ctk.CTkEntry(master=self.ten_forty_scrolling_frame, placeholder_text="Penalty",
                                              width=125, height=32, text_color="#000000", bg_color="white",
                                              fg_color="transparent")

        self.user_id = ctk.CTkEntry(master=self.app, placeholder_text="Username",
                                    width=125, height=32, text_color="white", bg_color="black",
                                    fg_color="transparent")

        self.user_password = ctk.CTkEntry(master=self.app, placeholder_text="Password",
                                          width=125, height=32, text_color="white", bg_color="black",
                                          fg_color="transparent")

        self.submit_and_erase = Button(self.app, text="Submit To 1040", width=35, height=5,
                                       command=self.submit_and_clear)

        self.export_results_as_pdf = Button(self.app, text="Export Results As PDF", width=35, height=5,
                                            command=self.export_results)

        self.export_results_as_pdf.place(relx=.2, rely=0.85, anchor="center")

        self.w2_increasing_number_for_forms = IntVar()
        self.w2_increasing_number_for_forms.set(self.w2_increasing_number_for_forms.get() + 1)

        self.ten_99_increasing_number_for_forms = IntVar()
        self.ten_99_increasing_number_for_forms.set(self.ten_99_increasing_number_for_forms.get() + 1)

        self.w2_form_counter = ctk.CTkLabel(self.app, textvariable=self.w2_increasing_number_for_forms, width=40)

        self.ten_99_form_counter = ctk.CTkLabel(self.app, textvariable=self.ten_99_increasing_number_for_forms,
                                                width=40)

        self.form_counter_hashtag = ctk.CTkLabel(self.app, text="#", width=5)

        # End Input Fields

        self.ten_ninety_nine_placements = [self.ten_ninety_nine_label_for_img, self.ten_ninety_nine_payer_info,
                                           self.ten_ninety_nine_payer_tin,
                                           self.ten_ninety_nine_recipient_tin, self.ten_ninety_nine_recipient_name,
                                           self.ten_ninety_nine_recipient_address,
                                           self.ten_ninety_nine_recipient_city_etc,
                                           self.ten_ninety_nine_account_number,
                                           self.ten_ninety_nine_ordinary_dividends,
                                           self.ten_ninety_nine_qualified_dividends,
                                           self.ten_ninety_nine_capital_gain,
                                           self.ten_ninety_nine_1250_gain, self.ten_ninety_nine_1202_gain,
                                           self.ten_ninety_nine_collectibles_gain,
                                           self.ten_ninety_nine_897_dividends, self.ten_ninety_nine_897_gain,
                                           self.ten_ninety_nine_nondividend,
                                           self.ten_ninety_nine_federal_tax_withheld, self.ten_ninety_nine_199a,
                                           self.ten_ninety_nine_investment_expenses,
                                           self.ten_ninety_nine_foreign_tax, self.ten_ninety_nine_foreign_tax_country,
                                           self.ten_ninety_nine_cash_liquidation,
                                           self.ten_ninety_nine_noncash_liquidation,
                                           self.ten_ninety_nine_exempt_dividends,
                                           self.ten_ninety_nine_specified_bond_dividends,
                                           self.ten_ninety_nine_state, self.ten_ninety_nine_state_id_number,
                                           self.ten_ninety_nine_state_tax_withheld]

        self.w_2_placements = [self.twenty_four_img, self.blocker_img, self.essn_entry, self.ein_entry,
                               self.employer_name_etc, self.cn_entry, self.employee_name_i, self.employee_last_name,
                               self.employee_suffix, self.employee_address_etc,
                               self.state_field, self.employers_state_id, self.state_wage_tips, self.state_income_tax,
                               self.local_wage_tips, self.local_income_tax, self.locality_name, self.wages_tips_c,
                               self.social_wages, self.medicare_wages, self.social_security_tips,
                               self.non_qualified_plans, self.other_field, self.fed_income_tax_withheld,
                               self.social_security_tax_withheld, self.medicare_tax_withheld, self.allocated_tips,
                               self.dependent_care_benefits, self.twelve_a, self.twelve_b, self.twelve_c, self.twelve_d,
                               self.w_2_label_for_img]

        self.ten_forty_placements = [self.ten_forty_label_for_pg_1, self.ten_forty_label_for_pg_2,
                                     self.ten_forty_scrolling_frame,
                                     self.ten_forty_first_name, self.ten_forty_last_name,
                                     self.ten_forty_spouse_first, self.ten_forty_spouse_last,
                                     self.ten_forty_home_address, self.ten_forty_apt_no, self.ten_forty_city,
                                     self.ten_forty_state, self.ten_forty_zip, self.ten_forty_foreign_country,
                                     self.ten_forty_foreign_province, self.ten_forty_foreign_post_code,

                                     self.ten_forty_dependent_first_1, self.ten_forty_dependent_first_2,
                                     self.ten_forty_dependent_first_3,
                                     self.ten_forty_dependent_first_4,

                                     self.ten_forty_total_w2s, self.ten_forty_household_wages,
                                     self.ten_forty_tip_income,
                                     self.ten_forty_medicaid_waiver, self.ten_forty_dependent_benefits,
                                     self.ten_forty_adoption_benefits, self.ten_forty_8919_wages,
                                     self.ten_forty_other_income,
                                     self.ten_forty_combat_pay, self.ten_forty_1_ah_sum,
                                     self.ten_forty_tax_exempt_interest,

                                     self.ten_forty_taxable_interest, self.ten_forty_qualified_dividends,
                                     self.ten_forty_ordinary_dividends, self.ten_forty_ira_distributions,
                                     self.ten_forty_taxable_ira,
                                     self.ten_forty_pensions_annuities, self.ten_forty_taxable_pensions,
                                     self.ten_forty_social_security, self.ten_forty_social_taxable,
                                     self.ten_forty_capital_gain,
                                     self.ten_forty_schedule_1, self.ten_forty_total_income,
                                     self.ten_forty_income_adjustments, self.ten_forty_adjusted_income,
                                     self.ten_forty_deductions, self.ten_forty_business_deductions,
                                     self.ten_forty_total_deductions,
                                     self.ten_forty_taxable_income,
                                     self.ten_forty_other_form_no,
                                     self.ten_forty_other_form_total, self.ten_forty_schedule_2,
                                     self.ten_forty_add_16_17,
                                     self.ten_forty_child_credit, self.ten_forty_schedule_3, self.ten_forty_add_19_20,
                                     self.ten_forty_sub_21_18, self.ten_forty_other_taxes, self.ten_forty_total_tax,
                                     self.ten_forty_withheld_w2, self.ten_forty_withheld_1099,
                                     self.ten_forty_withheld_other,
                                     self.ten_forty_withheld_total, self.ten_forty_previous_year, self.ten_forty_eic,
                                     self.ten_forty_8812_child_credit, self.ten_forty_8863_opportunity_credit,
                                     self.ten_forty_schedule_3_line_15, self.ten_forty_other_payments,
                                     self.ten_forty_total_payments,
                                     self.ten_forty_overpaid, self.ten_forty_owed, self.ten_forty_penalty]

        self.ten_forty_checkboxes_placements = [
            self.ten_forty_presidential_you, self.ten_forty_presidential_spouse,
            self.ten_forty_filing_single, self.ten_forty_filing_jointly,
            self.ten_forty_filing_separately,
            self.ten_forty_filing_hoh, self.ten_forty_filing_qss,
            self.ten_forty_digital_assets_yes,
            self.ten_forty_digital_assets_no, self.ten_forty_are_dependent,
            self.ten_forty_spouse_dependent,
            self.ten_forty_spouse_separate, self.ten_forty_self_1959,
            self.ten_forty_self_blind,
            self.ten_forty_spouse_1959, self.ten_forty_spouse_blind,
            self.ten_forty_many_dependents,
            self.ten_forty_dependent_1_child_credit, self.ten_forty_dependent_1_other_credit,
            self.ten_forty_dependent_2_child_credit, self.ten_forty_dependent_2_other_credit,
            self.ten_forty_dependent_3_child_credit, self.ten_forty_dependent_3_other_credit,
            self.ten_forty_dependent_4_child_credit, self.ten_forty_dependent_4_other_credit,
            self.ten_forty_schedule_d,
            self.ten_forty_lump_sum_method,
            self.ten_forty_8814,
            self.ten_forty_4972,
            self.ten_forty_other_form_check,
            self.ten_forty_8888,
            self.ten_forty_route_checking,
            self.ten_forty_route_savings,
            self.ten_forty_third_party_yes,
            self.ten_forty_third_party_no,
            self.ten_forty_self_employed]

        UserInterface.setup_w_2(self)
        ###############################

        # Results Section

        self.results_textbox = ctk.CTkTextbox(master=self.app, scrollbar_button_color="#FFCC70", width=500,
                                              corner_radius=16,
                                              border_color="#FFCC70")

        # Results Positioning

        self.results_textbox.place(relx=.5, rely=0.85, anchor="center")
        self.results_textbox.configure(state="disabled")

        # Buttons

        Button(self.app, text="Calculate", command=self.send_info_calculate).place(relx=.5, rely=0.965, anchor="center")
        Button(self.app, text="Auto/Save Session", command=self.main_save).place(relx=.4, rely=0.965, anchor="center")
        Button(self.app, text="Load Session", command=self.load_session).place(relx=.6, rely=0.965, anchor="center")

        self.user_id.place(relx=0.4, rely=0.746, anchor="center")

        self.user_password.place(relx=0.6, rely=0.746, anchor="center")

        self.app.protocol("WM_DELETE_WINDOW", self.exit_program)

        self.w_2_fields_save_load = self.w_2_placements.copy()
        self.w_2_fields_save_load.pop(self.w_2_placements.index(self.w_2_label_for_img))
        self.w_2_fields_save_load.pop(self.w_2_placements.index(self.blocker_img))
        self.w_2_fields_save_load.pop(self.w_2_placements.index(self.twenty_four_img))

        self.ten_ninety_nine_fields_save_load = self.ten_ninety_nine_placements.copy()
        self.ten_ninety_nine_fields_save_load.pop(
            self.ten_ninety_nine_placements.index(self.ten_ninety_nine_label_for_img))

        self.ten_forty_fields_save_load = self.ten_forty_placements.copy()
        # Creating a list of indexes to remove

        indexes_to_remove = [
            self.ten_forty_placements.index(self.ten_forty_scrolling_frame),
            self.ten_forty_placements.index(self.ten_forty_label_for_pg_2),
            self.ten_forty_placements.index(self.ten_forty_label_for_pg_1)
        ]

        # Removing the elements at the specified indexes from self.ten_forty_fields_save_load
        for index in sorted(indexes_to_remove, reverse=True):
            self.ten_forty_fields_save_load.pop(index)

        # Combining all three lists into one list
        self.all_fields = self.w_2_fields_save_load + self.ten_ninety_nine_fields_save_load + \
                          self.ten_forty_fields_save_load + [
                              self.user_id]

        self.other_all_fields = self.ten_forty_checkboxes_placements + [self.user_password]

        self.app.mainloop()

    def export_results(self):
        # Opening the file explorer
        filename = filedialog.asksaveasfilename(initialdir="/", title="Save As",
                                                filetypes=(("PDF Files", "*.pdf"),))
        if filename:
            output_pdf_file = os.path.splitext(filename)[0] + ".pdf"
            pdf = FPDF()
            pdf.add_page()
            pdf.set_xy(0, 0)
            pdf.set_font('arial', 'B', 13)

            # Assuming self.results_textbox contains the text with new lines
            x = self.results_textbox.get("1.0", "end")
            x = "Results:\n\n" + x
            pdf.multi_cell(0, 5, txt=x, align='L')  # Use multi_cell to handle new lines

            pdf.output(output_pdf_file)

    def submit_and_clear(self):
        """
        Submits the current session and clears any relevant data.

        This method is responsible for submitting the current session to the 1040 form.
        It first initializes a new session
        using the `new_session()` method.
        After successful submission, a message box displays a success notification with
        the message 'Submitted To 1040'.

        Args:
            self: An instance of the class containing this method.

        Returns:
            None
        """

        if self.submit_changer == 0:
            if messagebox.askyesno("Alert", "Upon clicking yes, boxes 1 and 2 will be sent to the 1040 form. All other fields will be cleared and autosave will be disabled until saving or loading the session again."):
                if self.fed_income_tax_withheld.get() == "" or self.wages_tips_c.get() == "":
                    messagebox.showerror("Error", "Please Enter Your Information For Box 1 And 2 To Submit It To 1040")

                else:
                    self.w2_increasing_number_for_forms.set(self.w2_increasing_number_for_forms.get() + 1)

                    dict_w2 = {"WAGES_TIPS_OTHER_COMP": float(self.wages_tips_c.get()),
                               "FEDERAL_INCOME_TAX_WITHHELD": float(self.fed_income_tax_withheld.get()),
                               "SOCIAL_SECURITY_WAGES": 0000, "SOCIAL_SECURITY_TAX_WITHHELD": 0000,
                               "MEDICARE_WAGES_AND_TIPS": 0000, "MEDICARE_TAX_WITHHELD": 0000,
                               "DEPENDANT_CARE_BENEFITS": 0000,
                               "STATES":
                                   [{"STATE": "STATE01", "STATE_INCOME": 0000, "STATE_TAX_WITHHELD": 0000},
                                    {"STATE": "STATE02", "STATE_INCOME": 0000, "STATE_TAX_WITHHELD": 0000}]}

                    if str(self.ten_forty_total_w2s.get()) == "":
                        self.old_new = 00.00
                        self.old_new_w2_withheld = 00.00
                        user_form_1040.income_w2 = 00.00
                    else:
                        if self.loaded == "yes":
                            if str(self.ten_forty_total_w2s.get()) == "":
                                self.old_new = 00.00
                                self.old_new_w2_withheld = 00.00
                                user_form_1040.income_w2 = 00.00
                            else:
                                self.old_new = float(self.wages_tips_c.get())
                                self.old_new_w2_withheld = float(self.fed_income_tax_withheld.get())

                    user_form_1040.add_w2(dict_w2, self.old_new, self.old_new_w2_withheld)


                    self.ten_forty_total_w2s.configure(state="normal")
                    self.ten_forty_total_w2s.delete(0, ctk.END)
                    self.ten_forty_total_w2s.insert("end", f"{user_form_1040.income_w2:.2f}")

                    self.ten_forty_withheld_w2.configure(state="normal")
                    self.ten_forty_withheld_w2.delete(0, ctk.END)
                    self.ten_forty_withheld_w2.insert("end", f"{user_form_1040.tax_withheld_w2:.2f}")


                    self.new_session()

                    messagebox.showinfo('Success', 'Submitted To 1040')
        else:
            if messagebox.askyesno("Alert", "Upon clicking yes, box 4 will be sent to the 1040 form. All other fields will be cleared and autosave will be disabled until saving or loading the session again."):
                if self.ten_ninety_nine_federal_tax_withheld.get() == "":
                    messagebox.showerror("Error", "Please Enter Your Information For Box 1 And 2 To Submit It To 1040")

                else:
                    self.ten_99_increasing_number_for_forms.set(self.ten_99_increasing_number_for_forms.get() + 1)

                    dict_1099_div = {"ORDINARY_DIVIDENDS": 0000,
                                     "QUALIFIED_DIVIDENDS": 0000,
                                     "CAPITAL_GAIN_DISTR": 0000, "UNRECAP_SEC_1250_GAIN": 0000,
                                     "SECTION_1202_GAIN": 0000, "COLLECTIBLES_GAIN": 0000,
                                     "SECTION_897_ORDINARY_DIVIDENDS": 0000, "SECTION_897_CAPITAL_GAIN": 0000,
                                     "NONDIVIDEND_DISTRIBUTIONS": 0000, "INCOME_TAX_WITHHELD": 0000,
                                     "SECTION_1999A_DIVIDENDS": 0000, "INVESTMENT_EXPENSES": 0000,
                                     "FOREIGN_TAX_PAID": 0000, "FOREIGN_COUNTRY_OR_US_POSSESSION": "Country",
                                     "CASH_LIQUIDATION_DISTRIBUTIONS": 0000, "NONCASH_LIQUIDATION_DISTRIBUTIONS": 0000,
                                     "EXEMPT_INTEREST_DIVIDENDS": 0000, "PRIVATE_ACTIVITY_BOND_INTEREST_DIVIDENDS": 0000,
                                     "FED_TAX_WITHHELD": float(self.ten_ninety_nine_federal_tax_withheld.get())}

                    user_form_1040.add_ten_99(dict_1099_div)

                    self.ten_forty_withheld_1099.configure(state="normal")
                    self.ten_forty_withheld_1099.delete(0, ctk.END)
                    self.ten_forty_withheld_1099.insert("end", f"{user_form_1040.tax_withheld_1099:.2f}")

                    self.new_session()

                    messagebox.showinfo('Success', 'Submitted To 1040')

    def setup_w_2(self):
        """
        Removes certain UI elements from the display.
        This method hides and forgets the placement of various UI widgets.
        The list of widgets to be removed is stored in the 'placements' list.
        """
        # Positioning of Input Fields

        self.new_decision = "w2"

        self.submit_changer = 0

        self.calculate_changer = "w2"

        for i in self.ten_ninety_nine_placements:
            i.place_forget()
            i.pack_forget()

        for i in self.ten_forty_placements:
            i.place_forget()
            i.pack_forget()

        for i in self.ten_forty_checkboxes_placements:
            i.place_forget()
            i.pack_forget()

        self.ten_99_form_counter.place_forget()

        # W-2

        self.w_2_label_for_img.place(relx=0.5, rely=0.5, anchor="s")
        self.w_2_label_for_img.pack(pady=88)

        # Employee SSN

        self.submit_and_erase.place(relx=.8, rely=0.85, anchor="center")

        self.form_counter_hashtag.place(relx=0.073, rely=0.09, anchor="center")

        self.w2_form_counter.place(relx=0.08, rely=0.09, anchor="center")

        self.essn_entry.place(relx=.46, rely=0.123, anchor="e")

        # EIN

        self.ein_entry.place(relx=.535, rely=0.162, anchor="e")

        # Wages TC

        self.wages_tips_c.place(relx=.719, rely=0.162, anchor="e")

        # SS Wages

        self.social_wages.place(relx=.719, rely=0.2, anchor="e")

        # M Wages and T

        self.medicare_wages.place(relx=.719, rely=0.238, anchor="e")

        # SS Tips

        self.social_security_tips.place(relx=.719, rely=0.277, anchor="e")

        # NQP

        self.non_qualified_plans.place(relx=.719, rely=0.354, anchor="e")

        # FED Income

        self.fed_income_tax_withheld.place(relx=.902, rely=0.162, anchor="e")

        # SST Withheld

        self.social_security_tax_withheld.place(relx=.902, rely=0.2, anchor="e")

        # M Withheld

        self.medicare_tax_withheld.place(relx=.902, rely=0.238, anchor="e")

        # A Tips

        self.allocated_tips.place(relx=.902, rely=0.277, anchor="e")

        # DC Benefits

        self.dependent_care_benefits.place(relx=.902, rely=0.315, anchor="e")

        #  12-A

        self.twelve_a.place(relx=.902, rely=0.355, anchor="e")

        #  12-B

        self.twelve_b.place(relx=.902, rely=0.393, anchor="e")

        #  12-C

        self.twelve_c.place(relx=.902, rely=0.432, anchor="e")

        #  12-D

        self.twelve_d.place(relx=.902, rely=0.47, anchor="e")

        #  Local Income Tax

        self.local_income_tax.place(relx=.8265, rely=0.528, anchor="e")

        #  Local Wages

        self.local_wage_tips.place(relx=.7085, rely=0.528, anchor="e")

        #  State Income Tax

        self.state_income_tax.place(relx=.5795, rely=0.528, anchor="e")

        #  State Wages

        self.state_wage_tips.place(relx=.461, rely=0.528, anchor="e")

        #  Employer's State ID

        self.employers_state_id.place(relx=.3325, rely=0.528, anchor="e")

        #  State Field

        self.state_field.place(relx=.1385, rely=0.528, anchor="e")

        #  Locality Name

        self.locality_name.place(relx=.902, rely=0.528, anchor="e")

        #  Other

        self.other_field.place(relx=.719, rely=0.462, anchor="e")

        # Employer NAZ

        self.employer_name_etc.place(relx=.535, rely=0.24, anchor="e")

        # CN

        self.cn_entry.place(relx=.535, rely=0.316, anchor="e")

        # Employee NI

        self.employee_name_i.place(relx=.3, rely=0.357, anchor="e")

        # Employee LN

        self.employee_last_name.place(relx=.505, rely=0.357, anchor="e")

        # Employee S

        self.employee_suffix.place(relx=.535, rely=0.357, anchor="e")

        # Employee A

        self.employee_address_etc.place(relx=.535, rely=0.4915, anchor="e")

        # Blocker

        self.blocker_img.place(relx=0.525, rely=0.655, anchor="s")
        self.twenty_four_img.place(relx=0.525, rely=0.607, anchor="s")

    def setup_1099(self):
        """
        Removes certain UI elements from the display.
        This method hides and forgets the placement of various UI widgets.
        The list of widgets to be removed is stored in the 'placements' list.
        """

        self.place_1099_form()

        self.new_decision = "1099"

        self.calculate_changer = "1099"

        self.submit_changer = 1

        for i in self.w_2_placements:
            i.place_forget()
            i.pack_forget()

        for i in self.ten_forty_placements:
            i.place_forget()
            i.pack_forget()

        for i in self.ten_forty_checkboxes_placements:
            i.place_forget()
            i.pack_forget()

        self.w2_form_counter.place_forget()

    def place_1099_form(self):
        """
        Places the 'ten_ninety_nine_label_for_img' widget at the center of the screen
        and sets vertical padding to 88 pixels.
        """
        self.ten_ninety_nine_label_for_img.place(relx=0.5, rely=0.5, anchor="s")
        self.ten_ninety_nine_label_for_img.pack(pady=88)

        self.submit_and_erase.place(relx=.8, rely=0.85, anchor="center")

        self.form_counter_hashtag.place(relx=0.073, rely=0.09, anchor="center")

        self.ten_99_form_counter.place(relx=0.08, rely=0.09, anchor="center")

        self.ten_ninety_nine_payer_info.place(relx=.480, rely=0.205, anchor="e")

        self.ten_ninety_nine_payer_tin.place(relx=.294, rely=0.286, anchor="e")
        self.ten_ninety_nine_recipient_tin.place(relx=.475, rely=0.286, anchor="e")

        self.ten_ninety_nine_recipient_name.place(relx=.466, rely=0.357, anchor="e")

        self.ten_ninety_nine_recipient_address.place(relx=.466, rely=0.411, anchor="e")

        self.ten_ninety_nine_recipient_city_etc.place(relx=.478, rely=0.471, anchor="e")

        self.ten_ninety_nine_account_number.place(relx=0.475, rely=0.571, anchor="e")

        self.ten_ninety_nine_ordinary_dividends.place(relx=0.629, rely=0.156, anchor="e")
        self.ten_ninety_nine_qualified_dividends.place(relx=0.629, rely=0.209, anchor="e")

        self.ten_ninety_nine_capital_gain.place(relx=0.629, rely=0.247, anchor="e")
        self.ten_ninety_nine_1250_gain.place(relx=0.776, rely=0.247, anchor="e")
        self.ten_ninety_nine_1202_gain.place(relx=0.629, rely=0.282, anchor="e")
        self.ten_ninety_nine_collectibles_gain.place(relx=0.776, rely=0.282, anchor="e")
        self.ten_ninety_nine_897_dividends.place(relx=0.629, rely=0.317, anchor="e")
        self.ten_ninety_nine_897_gain.place(relx=0.776, rely=0.317, anchor="e")

        self.ten_ninety_nine_nondividend.place(relx=0.629, rely=0.354, anchor="e")
        self.ten_ninety_nine_federal_tax_withheld.place(relx=0.776, rely=0.354, anchor="e")
        self.ten_ninety_nine_199a.place(relx=0.629, rely=0.391, anchor="e")
        self.ten_ninety_nine_investment_expenses.place(relx=0.776, rely=0.391, anchor="e")

        self.ten_ninety_nine_foreign_tax.place(relx=0.629, rely=0.443, anchor="e")
        self.ten_ninety_nine_foreign_tax_country.place(relx=0.776, rely=0.443, anchor="e")

        self.ten_ninety_nine_cash_liquidation.place(relx=0.629, rely=0.481, anchor="e")
        self.ten_ninety_nine_noncash_liquidation.place(relx=0.776, rely=0.481, anchor="e")

        self.ten_ninety_nine_exempt_dividends.place(relx=0.629, rely=0.530, anchor="e")
        self.ten_ninety_nine_specified_bond_dividends.place(relx=0.776, rely=0.530, anchor="e")

        self.ten_ninety_nine_state.place(relx=0.531, rely=0.568, anchor="e")
        self.ten_ninety_nine_state_id_number.place(relx=0.629, rely=0.568, anchor="e")
        self.ten_ninety_nine_state_tax_withheld.place(relx=0.776, rely=0.568, anchor="e")

    def setup_1040(self):
        """
        Removes certain UI elements from the display.
        This method hides and forgets the placement of various UI widgets.
        The list of widgets to be removed is stored in the 'placements' list.
        """

        self.new_decision = "1040"

        self.calculate_changer = "1040"

        for i in self.ten_ninety_nine_placements:
            i.place_forget()
            i.pack_forget()

        for i in self.w_2_placements:
            i.place_forget()
            i.pack_forget()

        self.submit_and_erase.place_forget()
        self.form_counter_hashtag.place_forget()
        self.w2_form_counter.place_forget()
        self.ten_99_form_counter.place_forget()

        self.ten_forty_scrolling_frame.place(relx=0.5, rely=0.365, anchor="center")

        self.ten_forty_label_for_pg_1.place(relx=0.5, rely=0.5, anchor="s")
        self.ten_forty_label_for_pg_1.pack(pady=5)
        self.ten_forty_label_for_pg_2.place(relx=0.5, rely=0.5, anchor="s")
        self.ten_forty_label_for_pg_2.pack(pady=5)

        self.ten_forty_first_name.place(relx=0.335, rely=0.058, anchor="e")
        self.ten_forty_last_name.place(relx=0.744, rely=0.058, anchor="e")
        self.ten_forty_spouse_first.place(relx=0.335, rely=0.077, anchor="e")
        self.ten_forty_spouse_last.place(relx=0.744, rely=0.077, anchor="e")
        self.ten_forty_home_address.place(relx=0.695, rely=0.096, anchor="e")
        self.ten_forty_apt_no.place(relx=0.788, rely=0.096, anchor="e")
        self.ten_forty_city.place(relx=0.472, rely=0.114, anchor="e")
        self.ten_forty_state.place(relx=0.661, rely=0.114, anchor="e")
        self.ten_forty_zip.place(relx=0.788, rely=0.114, anchor="e")
        self.ten_forty_foreign_country.place(relx=0.385, rely=0.133, anchor="e")
        self.ten_forty_foreign_province.place(relx=0.661, rely=0.133, anchor="e")
        self.ten_forty_foreign_post_code.place(relx=0.788, rely=0.133, anchor="e")

        self.ten_forty_presidential_you.place(relx=0.878, rely=0.133, anchor="e")
        self.ten_forty_presidential_spouse.place(relx=0.943, rely=0.133, anchor="e")

        self.ten_forty_filing_single.place(relx=0.164, rely=0.144, anchor="e")
        self.ten_forty_filing_jointly.place(relx=0.164, rely=0.153, anchor="e")
        self.ten_forty_filing_separately.place(relx=0.164, rely=0.162, anchor="e")
        self.ten_forty_filing_hoh.place(relx=0.613, rely=0.144, anchor="e")
        self.ten_forty_filing_qss.place(relx=0.613, rely=0.162, anchor="e")

        self.ten_forty_digital_assets_yes.place(relx=0.877, rely=0.204, anchor="e")
        self.ten_forty_digital_assets_no.place(relx=0.942, rely=0.204, anchor="e")

        self.ten_forty_are_dependent.place(relx=0.309, rely=0.214, anchor="e")
        self.ten_forty_spouse_dependent.place(relx=0.482, rely=0.214, anchor="e")
        self.ten_forty_spouse_separate.place(relx=0.151, rely=0.224, anchor="e")

        self.ten_forty_self_1959.place(relx=0.189, rely=0.237, anchor="e")
        self.ten_forty_self_blind.place(relx=0.448, rely=0.237, anchor="e")
        self.ten_forty_spouse_1959.place(relx=0.624, rely=0.237, anchor="e")
        self.ten_forty_spouse_blind.place(relx=0.881, rely=0.237, anchor="e")

        self.ten_forty_dependent_first_1.place(relx=0.43, rely=0.265, anchor="e")

        self.ten_forty_dependent_first_2.place(relx=0.43, rely=0.274, anchor="e")

        self.ten_forty_dependent_first_3.place(relx=0.43, rely=0.2835, anchor="e")

        self.ten_forty_dependent_first_4.place(relx=0.43, rely=0.2925, anchor="e")

        self.ten_forty_many_dependents.place(relx=0.130, rely=0.293, anchor="e")
        self.ten_forty_dependent_1_child_credit.place(relx=0.788, rely=0.265, anchor="e")
        self.ten_forty_dependent_1_other_credit.place(relx=0.940, rely=0.265, anchor="e")
        self.ten_forty_dependent_2_child_credit.place(relx=0.788, rely=0.273, anchor="e")
        self.ten_forty_dependent_2_other_credit.place(relx=0.940, rely=0.273, anchor="e")
        self.ten_forty_dependent_3_child_credit.place(relx=0.788, rely=0.283, anchor="e")
        self.ten_forty_dependent_3_other_credit.place(relx=0.940, rely=0.283, anchor="e")
        self.ten_forty_dependent_4_child_credit.place(relx=0.788, rely=0.293, anchor="e")
        self.ten_forty_dependent_4_other_credit.place(relx=0.940, rely=0.293, anchor="e")

        self.ten_forty_total_w2s.place(relx=0.987, rely=0.302, anchor="e")
        self.ten_forty_household_wages.place(relx=0.987, rely=0.3115, anchor="e")
        self.ten_forty_tip_income.place(relx=0.987, rely=0.321, anchor="e")
        self.ten_forty_medicaid_waiver.place(relx=0.987, rely=0.3295, anchor="e")
        self.ten_forty_dependent_benefits.place(relx=0.987, rely=0.3395, anchor="e")
        self.ten_forty_adoption_benefits.place(relx=0.987, rely=0.3485, anchor="e")
        self.ten_forty_8919_wages.place(relx=0.987, rely=0.358, anchor="e")
        self.ten_forty_other_income.place(relx=0.987, rely=0.3675, anchor="e")
        self.ten_forty_combat_pay.place(relx=0.822, rely=0.377, anchor="e")
        self.ten_forty_1_ah_sum.place(relx=0.987, rely=0.386, anchor="e")
        self.ten_forty_tax_exempt_interest.place(relx=0.539, rely=0.3955, anchor="e")
        self.ten_forty_taxable_interest.place(relx=0.987, rely=0.3955, anchor="e")
        self.ten_forty_qualified_dividends.place(relx=0.539, rely=0.404, anchor="e")
        self.ten_forty_ordinary_dividends.place(relx=0.987, rely=0.404, anchor="e")
        self.ten_forty_ira_distributions.place(relx=0.539, rely=0.4135, anchor="e")
        self.ten_forty_taxable_ira.place(relx=0.987, rely=0.4135, anchor="e")
        self.ten_forty_pensions_annuities.place(relx=0.539, rely=0.423, anchor="e")
        self.ten_forty_taxable_pensions.place(relx=0.987, rely=0.423, anchor="e")
        self.ten_forty_social_security.place(relx=0.539, rely=0.4325, anchor="e")
        self.ten_forty_social_taxable.place(relx=0.987, rely=0.4325, anchor="e")

        self.ten_forty_schedule_d.place(relx=0.82, rely=0.4512, anchor="e")
        self.ten_forty_lump_sum_method.place(relx=0.822, rely=0.442, anchor="e")

        self.ten_forty_capital_gain.place(relx=0.987, rely=0.4505, anchor="e")
        self.ten_forty_schedule_1.place(relx=0.987, rely=0.459, anchor="e")
        self.ten_forty_total_income.place(relx=0.987, rely=0.4685, anchor="e")
        self.ten_forty_income_adjustments.place(relx=0.987, rely=0.478, anchor="e")
        self.ten_forty_adjusted_income.place(relx=0.987, rely=0.488, anchor="e")
        self.ten_forty_deductions.place(relx=0.987, rely=0.498, anchor="e")
        self.ten_forty_business_deductions.place(relx=0.987, rely=0.5075, anchor="e")
        self.ten_forty_total_deductions.place(relx=0.987, rely=0.517, anchor="e")
        self.ten_forty_taxable_income.place(relx=0.987, rely=0.5265, anchor="e")

        self.ten_forty_8814.place(relx=0.5115, rely=0.565, anchor="e")
        self.ten_forty_4972.place(relx=0.602, rely=0.565, anchor="e")
        self.ten_forty_other_form_check.place(relx=0.692, rely=0.565, anchor="e")

        self.ten_forty_8888.place(relx=0.815, rely=0.7813, anchor="e")
        self.ten_forty_route_checking.place(relx=0.652, rely=0.791, anchor="e")
        self.ten_forty_route_savings.place(relx=0.755, rely=0.791, anchor="e")
        self.ten_forty_third_party_yes.place(relx=0.71, rely=0.8547, anchor="e")
        self.ten_forty_third_party_no.place(relx=0.89, rely=0.8547, anchor="e")
        self.ten_forty_self_employed.place(relx=0.8912, rely=0.9633, anchor="e")

        self.ten_forty_other_form_no.place(relx=0.765, rely=0.565, anchor="e")
        self.ten_forty_other_form_total.place(relx=0.987, rely=0.565, anchor="e")
        self.ten_forty_schedule_2.place(relx=0.987, rely=0.5745, anchor="e")
        self.ten_forty_add_16_17.place(relx=0.987, rely=0.584, anchor="e")
        self.ten_forty_child_credit.place(relx=0.987, rely=0.5935, anchor="e")
        self.ten_forty_schedule_3.place(relx=0.987, rely=0.603, anchor="e")
        self.ten_forty_add_19_20.place(relx=0.987, rely=0.6125, anchor="e")
        self.ten_forty_sub_21_18.place(relx=0.987, rely=0.622, anchor="e")
        self.ten_forty_other_taxes.place(relx=0.987, rely=0.6315, anchor="e")
        self.ten_forty_total_tax.place(relx=0.987, rely=0.641, anchor="e")

        self.ten_forty_withheld_w2.place(relx=0.811, rely=0.660, anchor="e")
        self.ten_forty_withheld_1099.place(relx=0.811, rely=0.6695, anchor="e")
        self.ten_forty_withheld_other.place(relx=0.811, rely=0.679, anchor="e")
        self.ten_forty_withheld_total.place(relx=0.987, rely=0.6885, anchor="e")
        self.ten_forty_previous_year.place(relx=0.987, rely=0.698, anchor="e")
        self.ten_forty_eic.place(relx=0.811, rely=0.706, anchor="e")
        self.ten_forty_8812_child_credit.place(relx=0.811, rely=0.715, anchor="e")
        self.ten_forty_8863_opportunity_credit.place(relx=0.811, rely=0.725, anchor="e")
        self.ten_forty_schedule_3_line_15.place(relx=0.811, rely=0.744, anchor="e")
        self.ten_forty_other_payments.place(relx=0.987, rely=0.754, anchor="e")
        self.ten_forty_total_payments.place(relx=0.987, rely=0.763, anchor="e")

        self.ten_forty_overpaid.place(relx=0.987, rely=0.773, anchor="e")
        self.ten_forty_owed.place(relx=0.987, rely=0.829, anchor="e")
        self.ten_forty_penalty.place(relx=0.811, rely=0.838, anchor="e")

    def new_session(self):
        """
        Creates a new session for tax calculations.
        """

        if messagebox.askyesno("Warning", "Upon clicking yes, all fields will be cleared and autosave will be disabled until saving or loading the session again."):

            self.auto_save_runner = False

            w_2_fields = [self.employee_address_etc, self.employee_suffix,
                          self.employee_last_name, self.employee_name_i,
                          self.cn_entry,
                          self.employer_name_etc, self.other_field, self.locality_name,
                          self.state_field, self.employers_state_id, self.state_wage_tips,
                          self.state_income_tax, self.local_wage_tips, self.local_income_tax,
                          self.twelve_a, self.twelve_b, self.twelve_c, self.twelve_d,
                          self.dependent_care_benefits, self.allocated_tips, self.medicare_tax_withheld,
                          self.social_security_tax_withheld, self.fed_income_tax_withheld,
                          self.non_qualified_plans, self.social_security_tips,
                          self.medicare_wages, self.social_wages, self.wages_tips_c, self.ein_entry,
                          self.essn_entry]

            ten_ninety_nine_fields = [self.ten_ninety_nine_payer_info,
                                      self.ten_ninety_nine_payer_tin,
                                      self.ten_ninety_nine_recipient_tin, self.ten_ninety_nine_recipient_name,
                                      self.ten_ninety_nine_recipient_address,
                                      self.ten_ninety_nine_recipient_city_etc,
                                      self.ten_ninety_nine_account_number,
                                      self.ten_ninety_nine_ordinary_dividends,
                                      self.ten_ninety_nine_qualified_dividends,
                                      self.ten_ninety_nine_capital_gain,
                                      self.ten_ninety_nine_1250_gain, self.ten_ninety_nine_1202_gain,
                                      self.ten_ninety_nine_collectibles_gain,
                                      self.ten_ninety_nine_897_dividends, self.ten_ninety_nine_897_gain,
                                      self.ten_ninety_nine_nondividend,
                                      self.ten_ninety_nine_federal_tax_withheld, self.ten_ninety_nine_199a,
                                      self.ten_ninety_nine_investment_expenses,
                                      self.ten_ninety_nine_foreign_tax, self.ten_ninety_nine_foreign_tax_country,
                                      self.ten_ninety_nine_cash_liquidation,
                                      self.ten_ninety_nine_noncash_liquidation,
                                      self.ten_ninety_nine_exempt_dividends,
                                      self.ten_ninety_nine_specified_bond_dividends,
                                      self.ten_ninety_nine_state, self.ten_ninety_nine_state_id_number,
                                      self.ten_ninety_nine_state_tax_withheld]

            ten_forty_fields = [self.ten_forty_first_name, self.ten_forty_last_name,
                                self.ten_forty_spouse_first, self.ten_forty_spouse_last,
                                self.ten_forty_home_address, self.ten_forty_apt_no, self.ten_forty_city,
                                self.ten_forty_state, self.ten_forty_zip, self.ten_forty_foreign_country,
                                self.ten_forty_foreign_province, self.ten_forty_foreign_post_code,
                                self.ten_forty_dependent_first_1, self.ten_forty_dependent_first_2,
                                self.ten_forty_dependent_first_3,
                                self.ten_forty_dependent_first_4,
                                self.ten_forty_total_w2s, self.ten_forty_household_wages,
                                self.ten_forty_tip_income,
                                self.ten_forty_medicaid_waiver, self.ten_forty_dependent_benefits,
                                self.ten_forty_adoption_benefits, self.ten_forty_8919_wages,
                                self.ten_forty_other_income,
                                self.ten_forty_combat_pay, self.ten_forty_1_ah_sum,
                                self.ten_forty_tax_exempt_interest,
                                self.ten_forty_taxable_interest, self.ten_forty_qualified_dividends,
                                self.ten_forty_ordinary_dividends, self.ten_forty_ira_distributions,
                                self.ten_forty_taxable_ira,
                                self.ten_forty_pensions_annuities, self.ten_forty_taxable_pensions,
                                self.ten_forty_social_security, self.ten_forty_social_taxable,
                                self.ten_forty_capital_gain,
                                self.ten_forty_schedule_1, self.ten_forty_schedule_1, self.ten_forty_total_income,
                                self.ten_forty_income_adjustments, self.ten_forty_adjusted_income,
                                self.ten_forty_deductions, self.ten_forty_business_deductions,
                                self.ten_forty_total_deductions,
                                self.ten_forty_taxable_income,
                                self.ten_forty_other_form_no,
                                self.ten_forty_other_form_total, self.ten_forty_schedule_2,
                                self.ten_forty_add_16_17,
                                self.ten_forty_child_credit, self.ten_forty_schedule_3, self.ten_forty_add_19_20,
                                self.ten_forty_sub_21_18, self.ten_forty_other_taxes, self.ten_forty_total_tax,
                                self.ten_forty_withheld_w2, self.ten_forty_withheld_1099,
                                self.ten_forty_withheld_other,
                                self.ten_forty_withheld_total, self.ten_forty_previous_year, self.ten_forty_eic,
                                self.ten_forty_8812_child_credit, self.ten_forty_8863_opportunity_credit,
                                self.ten_forty_schedule_3_line_15, self.ten_forty_other_payments,
                                self.ten_forty_total_payments,
                                self.ten_forty_overpaid, self.ten_forty_owed, self.ten_forty_penalty]

            ten_forty_checkboxes = [self.ten_forty_presidential_you, self.ten_forty_presidential_spouse,
                                    self.ten_forty_filing_single, self.ten_forty_filing_jointly,
                                    self.ten_forty_filing_separately,
                                    self.ten_forty_filing_hoh, self.ten_forty_filing_qss,
                                    self.ten_forty_digital_assets_yes,
                                    self.ten_forty_digital_assets_no, self.ten_forty_are_dependent,
                                    self.ten_forty_spouse_dependent,
                                    self.ten_forty_spouse_separate, self.ten_forty_self_1959,
                                    self.ten_forty_self_blind,
                                    self.ten_forty_spouse_1959, self.ten_forty_spouse_blind,
                                    self.ten_forty_many_dependents,
                                    self.ten_forty_dependent_1_child_credit, self.ten_forty_dependent_1_other_credit,
                                    self.ten_forty_dependent_2_child_credit, self.ten_forty_dependent_2_other_credit,
                                    self.ten_forty_dependent_3_child_credit, self.ten_forty_dependent_3_other_credit,
                                    self.ten_forty_dependent_4_child_credit, self.ten_forty_dependent_4_other_credit,
                                    self.ten_forty_lump_sum_method, self.ten_forty_schedule_d,
                                    self.ten_forty_8814, self.ten_forty_4972,
                                    self.ten_forty_other_form_check, self.ten_forty_8888,
                                    self.ten_forty_route_checking,
                                    self.ten_forty_route_savings,
                                    self.ten_forty_third_party_yes,
                                    self.ten_forty_third_party_no,
                                    self.ten_forty_self_employed]

            if self.new_decision == "w2":
                for i in w_2_fields:
                    i.delete(0, ctk.END)
            elif self.new_decision == "1099":
                for j in ten_ninety_nine_fields:
                    j.delete(0, ctk.END)
            elif self.new_decision == "1040":
                for h in ten_forty_fields:
                    h.delete(0, ctk.END)
                for k in ten_forty_checkboxes:
                    k.deselect()

    def quit(self):
        """
        Displays a confirmation dialog asking the user if they want to quit.
        If the user confirms, the program exits.

        Returns:
            None
        """
        if messagebox.askyesno("Exit", "Are you sure you want to quit?"):
            sys.exit()

    def exit_program(self):
        """
        Displays a confirmation dialog asking the user if they want to quit.
        If the user confirms, the program exits.

        Returns:
            None
        """
        if messagebox.askyesno("Exit", "Are you sure you want to quit? "
                                       "If you have unsaved progress that "
                                       "you would like to save please click the save "
                                       "session button or one of the formats from the file menu."):
            sys.exit()

    ###################################################################################################################
    # W-2 #
    # Save-as W2 #
    def save_form_w2_as(self):
        """
        Opens a file explorer to save the tax-related data to a pdf file.

        Updates the form fields in a given PDF document with values from a dictionary.

        Returns:
            None
        """

        # Opening the file explorer
        filename = filedialog.asksaveasfilename(initialdir="/", title="Save As",
                                                filetypes=(("PDF Files", "*.pdf"),))
        if filename:

            def update_widget_values_w2(input_pdf, output_pdf):
                # Opening the input PDF
                pdf = fitz.open(input_pdf)
                save_as_w2_field_values_mixing = {
                    'topmostSubform[0].Copy1[0].f2_01[0]': str(self.essn_entry.get()),
                    'topmostSubform[0].Copy1[0].Col_Left[0].f2_02[0]': str(self.ein_entry.get()),
                    'topmostSubform[0].Copy1[0].Col_Left[0].f2_03[0]': str(self.employer_name_etc.get()),
                    'topmostSubform[0].Copy1[0].Col_Left[0].f2_04[0]': str(self.cn_entry.get()),
                    'topmostSubform[0].Copy1[0].Col_Left[0].f2_05[0]': str(self.employee_name_i.get()),
                    'topmostSubform[0].Copy1[0].Col_Left[0].f2_06[0]': str(self.employee_last_name.get()),
                    'topmostSubform[0].Copy1[0].Col_Left[0].f2_07[0]': str(self.employee_suffix.get()),
                    'topmostSubform[0].Copy1[0].Col_Left[0].f2_08[0]': str(self.employee_address_etc.get()),
                    'topmostSubform[0].Copy1[0].Col_Right[0].f2_09[0]': str(self.wages_tips_c.get()),
                    'topmostSubform[0].Copy1[0].Col_Right[0].f2_10[0]': str(self.fed_income_tax_withheld.get()),
                    'topmostSubform[0].Copy1[0].Col_Right[0].f2_11[0]': str(self.social_wages.get()),
                    'topmostSubform[0].Copy1[0].Col_Right[0].f2_12[0]': str(self.social_security_tax_withheld.get()),
                    'topmostSubform[0].Copy1[0].Col_Right[0].f2_13[0]': str(self.medicare_wages.get()),
                    'topmostSubform[0].Copy1[0].Col_Right[0].f2_14[0]': str(self.medicare_tax_withheld.get()),
                    'topmostSubform[0].Copy1[0].Col_Right[0].f2_15[0]': str(self.social_security_tips.get()),
                    'topmostSubform[0].Copy1[0].Col_Right[0].f2_16[0]': str(self.allocated_tips.get()),
                    'topmostSubform[0].Copy1[0].Col_Right[0].f2_18[0]': str(self.dependent_care_benefits.get()),
                    'topmostSubform[0].Copy1[0].Col_Right[0].f2_19[0]': str(self.non_qualified_plans.get()),
                    'topmostSubform[0].Copy1[0].Col_Right[0].Box12_ReadOrder[0].f2_21[0]': str(self.twelve_a.get()),
                    'topmostSubform[0].Copy1[0].Col_Right[0].Box12_ReadOrder[0].f2_23[0]': str(self.twelve_b.get()),
                    'topmostSubform[0].Copy1[0].Col_Right[0].Box12_ReadOrder[0].f2_25[0]': str(self.twelve_c.get()),
                    'topmostSubform[0].Copy1[0].Col_Right[0].Box12_ReadOrder[0].f2_27[0]': str(self.twelve_d.get()),
                    'topmostSubform[0].Copy1[0].Col_Right[0].f2_28[0]': str(self.other_field.get()),
                    'topmostSubform[0].Copy1[0].Boxes15_ReadOrder[0].f2_29[0]': str(self.state_field.get()),
                    'topmostSubform[0].Copy1[0].Boxes15_ReadOrder[0].f2_30[0]': str(self.employers_state_id.get()),
                    'topmostSubform[0].Copy1[0].Box16_ReadOrder[0].f2_33[0]': str(self.state_wage_tips.get()),
                    'topmostSubform[0].Copy1[0].Box17_ReadOrder[0].f2_35[0]': str(self.state_income_tax.get()),
                    'topmostSubform[0].Copy1[0].Box18_ReadOrder[0].f2_37[0]': str(self.local_wage_tips.get()),
                    'topmostSubform[0].Copy1[0].Box19_ReadOrder[0].f2_39[0]': str(self.local_income_tax.get()),
                    'topmostSubform[0].Copy1[0].f2_41[0]': str(self.locality_name.get())
                }

                save_as_w2_field_values_mixing_2 = {
                    'topmostSubform[0].CopyB[0].f2_01[0]': str(self.essn_entry.get()),
                    'topmostSubform[0].CopyB[0].Col_Left[0].f2_02[0]': str(self.ein_entry.get()),
                    'topmostSubform[0].CopyB[0].Col_Left[0].f2_03[0]': str(self.employer_name_etc.get()),
                    'topmostSubform[0].CopyB[0].Col_Left[0].f2_04[0]': str(self.cn_entry.get()),
                    'topmostSubform[0].CopyB[0].Col_Left[0].f2_05[0]': str(self.employee_name_i.get()),
                    'topmostSubform[0].CopyB[0].Col_Left[0].f2_06[0]': str(self.employee_last_name.get()),
                    'topmostSubform[0].CopyB[0].Col_Left[0].f2_07[0]': str(self.employee_suffix.get()),
                    'topmostSubform[0].CopyB[0].Col_Left[0].f2_08[0]': str(self.employee_address_etc.get()),
                    'topmostSubform[0].CopyB[0].Col_Right[0].f2_09[0]': str(self.wages_tips_c.get()),
                    'topmostSubform[0].CopyB[0].Col_Right[0].f2_10[0]': str(self.fed_income_tax_withheld.get()),
                    'topmostSubform[0].CopyB[0].Col_Right[0].f2_11[0]': str(self.social_wages.get()),
                    'topmostSubform[0].CopyB[0].Col_Right[0].f2_12[0]': str(self.social_security_tax_withheld.get()),
                    'topmostSubform[0].CopyB[0].Col_Right[0].f2_13[0]': str(self.medicare_wages.get()),
                    'topmostSubform[0].CopyB[0].Col_Right[0].f2_14[0]': str(self.medicare_tax_withheld.get()),
                    'topmostSubform[0].CopyB[0].Col_Right[0].f2_15[0]': str(self.social_security_tips.get()),
                    'topmostSubform[0].CopyB[0].Col_Right[0].f2_16[0]': str(self.allocated_tips.get()),
                    'topmostSubform[0].CopyB[0].Col_Right[0].f2_18[0]': str(self.dependent_care_benefits.get()),
                    'topmostSubform[0].CopyB[0].Col_Right[0].f2_19[0]': str(self.non_qualified_plans.get()),
                    'topmostSubform[0].CopyB[0].Col_Right[0].Box12_ReadOrder[0].f2_21[0]': str(self.twelve_a.get()),
                    'topmostSubform[0].CopyB[0].Col_Right[0].Box12_ReadOrder[0].f2_23[0]': str(self.twelve_b.get()),
                    'topmostSubform[0].CopyB[0].Col_Right[0].Box12_ReadOrder[0].f2_25[0]': str(self.twelve_c.get()),
                    'topmostSubform[0].CopyB[0].Col_Right[0].Box12_ReadOrder[0].f2_27[0]': str(self.twelve_d.get()),
                    'topmostSubform[0].CopyB[0].Col_Right[0].f2_28[0]': str(self.other_field.get()),
                    'topmostSubform[0].CopyB[0].Boxes15_ReadOrder[0].f2_29[0]': str(self.state_field.get()),
                    'topmostSubform[0].CopyB[0].Boxes15_ReadOrder[0].f2_30[0]': str(self.employers_state_id.get()),
                    'topmostSubform[0].CopyB[0].Box16_ReadOrder[0].f2_33[0]': str(self.state_wage_tips.get()),
                    'topmostSubform[0].CopyB[0].Box17_ReadOrder[0].f2_35[0]': str(self.state_income_tax.get()),
                    'topmostSubform[0].CopyB[0].Box18_ReadOrder[0].f2_37[0]': str(self.local_wage_tips.get()),
                    'topmostSubform[0].CopyB[0].Box19_ReadOrder[0].f2_39[0]': str(self.local_income_tax.get()),
                    'topmostSubform[0].CopyB[0].f2_41[0]': str(self.locality_name.get())
                }

                save_as_w2_field_values_mixing_3 = {
                    'topmostSubform[0].CopyC[0].f2_01[0]': str(self.essn_entry.get()),
                    'topmostSubform[0].CopyC[0].Col_Left[0].f2_02[0]': str(self.ein_entry.get()),
                    'topmostSubform[0].CopyC[0].Col_Left[0].f2_03[0]': str(self.employer_name_etc.get()),
                    'topmostSubform[0].CopyC[0].Col_Left[0].f2_04[0]': str(self.cn_entry.get()),
                    'topmostSubform[0].CopyC[0].Col_Left[0].f2_05[0]': str(self.employee_name_i.get()),
                    'topmostSubform[0].CopyC[0].Col_Left[0].f2_06[0]': str(self.employee_last_name.get()),
                    'topmostSubform[0].CopyC[0].Col_Left[0].f2_07[0]': str(self.employee_suffix.get()),
                    'topmostSubform[0].CopyC[0].Col_Left[0].f2_08[0]': str(self.employee_address_etc.get()),
                    'topmostSubform[0].CopyC[0].Col_Right[0].f2_09[0]': str(self.wages_tips_c.get()),
                    'topmostSubform[0].CopyC[0].Col_Right[0].f2_10[0]': str(self.fed_income_tax_withheld.get()),
                    'topmostSubform[0].CopyC[0].Col_Right[0].f2_11[0]': str(self.social_wages.get()),
                    'topmostSubform[0].CopyC[0].Col_Right[0].f2_12[0]': str(self.social_security_tax_withheld.get()),
                    'topmostSubform[0].CopyC[0].Col_Right[0].f2_13[0]': str(self.medicare_wages.get()),
                    'topmostSubform[0].CopyC[0].Col_Right[0].f2_14[0]': str(self.medicare_tax_withheld.get()),
                    'topmostSubform[0].CopyC[0].Col_Right[0].f2_15[0]': str(self.social_security_tips.get()),
                    'topmostSubform[0].CopyC[0].Col_Right[0].f2_16[0]': str(self.allocated_tips.get()),
                    'topmostSubform[0].CopyC[0].Col_Right[0].f2_18[0]': str(self.dependent_care_benefits.get()),
                    'topmostSubform[0].CopyC[0].Col_Right[0].f2_19[0]': str(self.non_qualified_plans.get()),
                    'topmostSubform[0].CopyC[0].Col_Right[0].Box12_ReadOrder[0].f2_21[0]': str(self.twelve_a.get()),
                    'topmostSubform[0].CopyC[0].Col_Right[0].Box12_ReadOrder[0].f2_23[0]': str(self.twelve_b.get()),
                    'topmostSubform[0].CopyC[0].Col_Right[0].Box12_ReadOrder[0].f2_25[0]': str(self.twelve_c.get()),
                    'topmostSubform[0].CopyC[0].Col_Right[0].Box12_ReadOrder[0].f2_27[0]': str(self.twelve_d.get()),
                    'topmostSubform[0].CopyC[0].Col_Right[0].f2_28[0]': str(self.other_field.get()),
                    'topmostSubform[0].CopyC[0].Boxes15_ReadOrder[0].f2_29[0]': str(self.state_field.get()),
                    'topmostSubform[0].CopyC[0].Boxes15_ReadOrder[0].f2_30[0]': str(self.employers_state_id.get()),
                    'topmostSubform[0].CopyC[0].Box16_ReadOrder[0].f2_33[0]': str(self.state_wage_tips.get()),
                    'topmostSubform[0].CopyC[0].Box17_ReadOrder[0].f2_35[0]': str(self.state_income_tax.get()),
                    'topmostSubform[0].CopyC[0].Box18_ReadOrder[0].f2_37[0]': str(self.local_wage_tips.get()),
                    'topmostSubform[0].CopyC[0].Box19_ReadOrder[0].f2_39[0]': str(self.local_income_tax.get()),
                    'topmostSubform[0].CopyC[0].f2_41[0]': str(self.locality_name.get())
                }

                save_as_w2_field_values_mixing_4 = {
                    'topmostSubform[0].Copy2[0].f2_01[0]': str(self.essn_entry.get()),
                    'topmostSubform[0].Copy2[0].Col_Left[0].f2_02[0]': str(self.ein_entry.get()),
                    'topmostSubform[0].Copy2[0].Col_Left[0].f2_03[0]': str(self.employer_name_etc.get()),
                    'topmostSubform[0].Copy2[0].Col_Left[0].f2_04[0]': str(self.cn_entry.get()),
                    'topmostSubform[0].Copy2[0].Col_Left[0].f2_05[0]': str(self.employee_name_i.get()),
                    'topmostSubform[0].Copy2[0].Col_Left[0].f2_06[0]': str(self.employee_last_name.get()),
                    'topmostSubform[0].Copy2[0].Col_Left[0].f2_07[0]': str(self.employee_suffix.get()),
                    'topmostSubform[0].Copy2[0].Col_Left[0].f2_08[0]': str(self.employee_address_etc.get()),
                    'topmostSubform[0].Copy2[0].Col_Right[0].f2_09[0]': str(self.wages_tips_c.get()),
                    'topmostSubform[0].Copy2[0].Col_Right[0].f2_10[0]': str(self.fed_income_tax_withheld.get()),
                    'topmostSubform[0].Copy2[0].Col_Right[0].f2_11[0]': str(self.social_wages.get()),
                    'topmostSubform[0].Copy2[0].Col_Right[0].f2_12[0]': str(self.social_security_tax_withheld.get()),
                    'topmostSubform[0].Copy2[0].Col_Right[0].f2_13[0]': str(self.medicare_wages.get()),
                    'topmostSubform[0].Copy2[0].Col_Right[0].f2_14[0]': str(self.medicare_tax_withheld.get()),
                    'topmostSubform[0].Copy2[0].Col_Right[0].f2_15[0]': str(self.social_security_tips.get()),
                    'topmostSubform[0].Copy2[0].Col_Right[0].f2_16[0]': str(self.allocated_tips.get()),
                    'topmostSubform[0].Copy2[0].Col_Right[0].f2_18[0]': str(self.dependent_care_benefits.get()),
                    'topmostSubform[0].Copy2[0].Col_Right[0].f2_19[0]': str(self.non_qualified_plans.get()),
                    'topmostSubform[0].Copy2[0].Col_Right[0].Box12_ReadOrder[0].f2_21[0]': str(self.twelve_a.get()),
                    'topmostSubform[0].Copy2[0].Col_Right[0].Box12_ReadOrder[0].f2_23[0]': str(self.twelve_b.get()),
                    'topmostSubform[0].Copy2[0].Col_Right[0].Box12_ReadOrder[0].f2_25[0]': str(self.twelve_c.get()),
                    'topmostSubform[0].Copy2[0].Col_Right[0].Box12_ReadOrder[0].f2_27[0]': str(self.twelve_d.get()),
                    'topmostSubform[0].Copy2[0].Col_Right[0].f2_28[0]': str(self.other_field.get()),
                    'topmostSubform[0].Copy2[0].Boxes15_ReadOrder[0].f2_29[0]': str(self.state_field.get()),
                    'topmostSubform[0].Copy2[0].Boxes15_ReadOrder[0].f2_30[0]': str(self.employers_state_id.get()),
                    'topmostSubform[0].Copy2[0].Box16_ReadOrder[0].f2_33[0]': str(self.state_wage_tips.get()),
                    'topmostSubform[0].Copy2[0].Box17_ReadOrder[0].f2_35[0]': str(self.state_income_tax.get()),
                    'topmostSubform[0].Copy2[0].Box18_ReadOrder[0].f2_37[0]': str(self.local_wage_tips.get()),
                    'topmostSubform[0].Copy2[0].Box19_ReadOrder[0].f2_39[0]': str(self.local_income_tax.get()),
                    'topmostSubform[0].Copy2[0].f2_41[0]': str(self.locality_name.get())
                }

                save_as_w2_field_values_mixing_5 = {
                    'topmostSubform[0].CopyD[0].f2_01[0]': str(self.essn_entry.get()),
                    'topmostSubform[0].CopyD[0].Col_Left[0].f2_02[0]': str(self.ein_entry.get()),
                    'topmostSubform[0].CopyD[0].Col_Left[0].f2_03[0]': str(self.employer_name_etc.get()),
                    'topmostSubform[0].CopyD[0].Col_Left[0].f2_04[0]': str(self.cn_entry.get()),
                    'topmostSubform[0].CopyD[0].Col_Left[0].f2_05[0]': str(self.employee_name_i.get()),
                    'topmostSubform[0].CopyD[0].Col_Left[0].f2_06[0]': str(self.employee_last_name.get()),
                    'topmostSubform[0].CopyD[0].Col_Left[0].f2_07[0]': str(self.employee_suffix.get()),
                    'topmostSubform[0].CopyD[0].Col_Left[0].f2_08[0]': str(self.employee_address_etc.get()),
                    'topmostSubform[0].CopyD[0].Col_Right[0].f2_09[0]': str(self.wages_tips_c.get()),
                    'topmostSubform[0].CopyD[0].Col_Right[0].f2_10[0]': str(self.fed_income_tax_withheld.get()),
                    'topmostSubform[0].CopyD[0].Col_Right[0].f2_11[0]': str(self.social_wages.get()),
                    'topmostSubform[0].CopyD[0].Col_Right[0].f2_12[0]': str(self.social_security_tax_withheld.get()),
                    'topmostSubform[0].CopyD[0].Col_Right[0].f2_13[0]': str(self.medicare_wages.get()),
                    'topmostSubform[0].CopyD[0].Col_Right[0].f2_14[0]': str(self.medicare_tax_withheld.get()),
                    'topmostSubform[0].CopyD[0].Col_Right[0].f2_15[0]': str(self.social_security_tips.get()),
                    'topmostSubform[0].CopyD[0].Col_Right[0].f2_16[0]': str(self.allocated_tips.get()),
                    'topmostSubform[0].CopyD[0].Col_Right[0].f2_18[0]': str(self.dependent_care_benefits.get()),
                    'topmostSubform[0].CopyD[0].Col_Right[0].f2_19[0]': str(self.non_qualified_plans.get()),
                    'topmostSubform[0].CopyD[0].Col_Right[0].Box12_ReadOrder[0].f2_21[0]': str(self.twelve_a.get()),
                    'topmostSubform[0].CopyD[0].Col_Right[0].Box12_ReadOrder[0].f2_23[0]': str(self.twelve_b.get()),
                    'topmostSubform[0].CopyD[0].Col_Right[0].Box12_ReadOrder[0].f2_25[0]': str(self.twelve_c.get()),
                    'topmostSubform[0].CopyD[0].Col_Right[0].Box12_ReadOrder[0].f2_27[0]': str(self.twelve_d.get()),
                    'topmostSubform[0].CopyD[0].Col_Right[0].f2_28[0]': str(self.other_field.get()),
                    'topmostSubform[0].CopyD[0].Boxes15_ReadOrder[0].f2_29[0]': str(self.state_field.get()),
                    'topmostSubform[0].CopyD[0].Boxes15_ReadOrder[0].f2_30[0]': str(self.employers_state_id.get()),
                    'topmostSubform[0].CopyD[0].Box16_ReadOrder[0].f2_33[0]': str(self.state_wage_tips.get()),
                    'topmostSubform[0].CopyD[0].Box17_ReadOrder[0].f2_35[0]': str(self.state_income_tax.get()),
                    'topmostSubform[0].CopyD[0].Box18_ReadOrder[0].f2_37[0]': str(self.local_wage_tips.get()),
                    'topmostSubform[0].CopyD[0].Box19_ReadOrder[0].f2_39[0]': str(self.local_income_tax.get()),
                    'topmostSubform[0].CopyD[0].f2_41[0]': str(self.locality_name.get())
                }

                # Iteration for each page
                for each_page in pdf:
                    widgets = each_page.widgets()
                    for content in widgets:
                        for field_name, value in {**save_as_w2_field_values_mixing,
                                                  **save_as_w2_field_values_mixing_2,
                                                  **save_as_w2_field_values_mixing_3,
                                                  **save_as_w2_field_values_mixing_4,
                                                  **save_as_w2_field_values_mixing_5}.items():
                            if content.field_name == field_name:
                                if value == "":
                                    content.field_value = " "
                                else:
                                    content.field_value = value
                                content.update()

                # Saving the modified PDF
                pdf.save(output_pdf)
                pdf.close()

            # Input and output PDF filenames
            input_pdf_file = "default_w2.pdf"
            output_pdf_file = os.path.splitext(filename)[0] + ".pdf"

            # Updating of widget values and saving the modified PDF
            update_widget_values_w2(input_pdf_file, output_pdf_file)
            print(f"Modified PDF saved as {output_pdf_file}")

    # Browse W2

    def browse_form_w2(self):
        """
           Opens a file explorer to select a pdf file containing tax information.
           Assigns data accordingly.
        """
        filename = filedialog.askopenfilename(initialdir="/", title="Open", filetypes=(("PDF Files", "*.pdf"),))
        if filename:
            self.update_input_fields_w2(filename)

    def update_input_fields_w2(self, input_pdf):
        """
            Updates entry widgets with field values extracted from a PDF.

            Details:
                - The code iterates through each page in the PDF.
                - For each page, it retrieves the widgets (form fields).
                - It then checks if the field name matches any of the specified entry widgets.
                - If a match is found and the field value is not empty, it updates the corresponding entry widget:
                    - Clears the existing text in the widget.
                    - Inserts the extracted value into the widget.
        """
        # Opening the input PDF
        pdf = fitz.open(input_pdf)
        browse_w2_field_values_mixing = {
            'topmostSubform[0].Copy1[0].f2_01[0]': self.essn_entry,
            'topmostSubform[0].Copy1[0].Col_Left[0].f2_02[0]': self.ein_entry,
            'topmostSubform[0].Copy1[0].Col_Left[0].f2_03[0]': self.employer_name_etc,
            'topmostSubform[0].Copy1[0].Col_Left[0].f2_04[0]': self.cn_entry,
            'topmostSubform[0].Copy1[0].Col_Left[0].f2_05[0]': self.employee_name_i,
            'topmostSubform[0].Copy1[0].Col_Left[0].f2_06[0]': self.employee_last_name,
            'topmostSubform[0].Copy1[0].Col_Left[0].f2_07[0]': self.employee_suffix,
            'topmostSubform[0].Copy1[0].Col_Left[0].f2_08[0]': self.employee_address_etc,
            'topmostSubform[0].Copy1[0].Col_Right[0].f2_09[0]': self.wages_tips_c,
            'topmostSubform[0].Copy1[0].Col_Right[0].f2_10[0]': self.fed_income_tax_withheld,
            'topmostSubform[0].Copy1[0].Col_Right[0].f2_11[0]': self.social_wages,
            'topmostSubform[0].Copy1[0].Col_Right[0].f2_12[0]': self.social_security_tax_withheld,
            'topmostSubform[0].Copy1[0].Col_Right[0].f2_13[0]': self.medicare_wages,
            'topmostSubform[0].Copy1[0].Col_Right[0].f2_14[0]': self.medicare_tax_withheld,
            'topmostSubform[0].Copy1[0].Col_Right[0].f2_15[0]': self.social_security_tips,
            'topmostSubform[0].Copy1[0].Col_Right[0].f2_16[0]': self.allocated_tips,
            'topmostSubform[0].Copy1[0].Col_Right[0].f2_18[0]': self.dependent_care_benefits,
            'topmostSubform[0].Copy1[0].Col_Right[0].f2_19[0]': self.non_qualified_plans,
            'topmostSubform[0].Copy1[0].Col_Right[0].Box12_ReadOrder[0].f2_21[0]': self.twelve_a,
            'topmostSubform[0].Copy1[0].Col_Right[0].Box12_ReadOrder[0].f2_23[0]': self.twelve_b,
            'topmostSubform[0].Copy1[0].Col_Right[0].Box12_ReadOrder[0].f2_25[0]': self.twelve_c,
            'topmostSubform[0].Copy1[0].Col_Right[0].Box12_ReadOrder[0].f2_27[0]': self.twelve_d,
            'topmostSubform[0].Copy1[0].Col_Right[0].f2_28[0]': self.other_field,
            'topmostSubform[0].Copy1[0].Boxes15_ReadOrder[0].f2_29[0]': self.state_field,
            'topmostSubform[0].Copy1[0].Boxes15_ReadOrder[0].f2_30[0]': self.employers_state_id,
            'topmostSubform[0].Copy1[0].Box16_ReadOrder[0].f2_33[0]': self.state_wage_tips,
            'topmostSubform[0].Copy1[0].Box17_ReadOrder[0].f2_35[0]': self.state_income_tax,
            'topmostSubform[0].Copy1[0].Box18_ReadOrder[0].f2_37[0]': self.local_wage_tips,
            'topmostSubform[0].Copy1[0].Box19_ReadOrder[0].f2_39[0]': self.local_income_tax,
            'topmostSubform[0].Copy1[0].f2_41[0]': self.locality_name
        }

        browse_w2_field_values_mixing_2 = {
            'topmostSubform[0].CopyB[0].f2_01[0]': self.essn_entry,
            'topmostSubform[0].CopyB[0].Col_Left[0].f2_02[0]': self.ein_entry,
            'topmostSubform[0].CopyB[0].Col_Left[0].f2_03[0]': self.employer_name_etc,
            'topmostSubform[0].CopyB[0].Col_Left[0].f2_04[0]': self.cn_entry,
            'topmostSubform[0].CopyB[0].Col_Left[0].f2_05[0]': self.employee_name_i,
            'topmostSubform[0].CopyB[0].Col_Left[0].f2_06[0]': self.employee_last_name,
            'topmostSubform[0].CopyB[0].Col_Left[0].f2_07[0]': self.employee_suffix,
            'topmostSubform[0].CopyB[0].Col_Left[0].f2_08[0]': self.employee_address_etc,
            'topmostSubform[0].CopyB[0].Col_Right[0].f2_09[0]': self.wages_tips_c,
            'topmostSubform[0].CopyB[0].Col_Right[0].f2_10[0]': self.fed_income_tax_withheld,
            'topmostSubform[0].CopyB[0].Col_Right[0].f2_11[0]': self.social_wages,
            'topmostSubform[0].CopyB[0].Col_Right[0].f2_12[0]': self.social_security_tax_withheld,
            'topmostSubform[0].CopyB[0].Col_Right[0].f2_13[0]': self.medicare_wages,
            'topmostSubform[0].CopyB[0].Col_Right[0].f2_14[0]': self.medicare_tax_withheld,
            'topmostSubform[0].CopyB[0].Col_Right[0].f2_15[0]': self.social_security_tips,
            'topmostSubform[0].CopyB[0].Col_Right[0].f2_16[0]': self.allocated_tips,
            'topmostSubform[0].CopyB[0].Col_Right[0].f2_18[0]': self.dependent_care_benefits,
            'topmostSubform[0].CopyB[0].Col_Right[0].f2_19[0]': self.non_qualified_plans,
            'topmostSubform[0].CopyB[0].Col_Right[0].Box12_ReadOrder[0].f2_21[0]': self.twelve_a,
            'topmostSubform[0].CopyB[0].Col_Right[0].Box12_ReadOrder[0].f2_23[0]': self.twelve_b,
            'topmostSubform[0].CopyB[0].Col_Right[0].Box12_ReadOrder[0].f2_25[0]': self.twelve_c,
            'topmostSubform[0].CopyB[0].Col_Right[0].Box12_ReadOrder[0].f2_27[0]': self.twelve_d,
            'topmostSubform[0].CopyB[0].Col_Right[0].f2_28[0]': self.other_field,
            'topmostSubform[0].CopyB[0].Boxes15_ReadOrder[0].f2_29[0]': self.state_field,
            'topmostSubform[0].CopyB[0].Boxes15_ReadOrder[0].f2_30[0]': self.employers_state_id,
            'topmostSubform[0].CopyB[0].Box16_ReadOrder[0].f2_33[0]': self.state_wage_tips,
            'topmostSubform[0].CopyB[0].Box17_ReadOrder[0].f2_35[0]': self.state_income_tax,
            'topmostSubform[0].CopyB[0].Box18_ReadOrder[0].f2_37[0]': self.local_wage_tips,
            'topmostSubform[0].CopyB[0].Box19_ReadOrder[0].f2_39[0]': self.local_income_tax,
            'topmostSubform[0].CopyB[0].f2_41[0]': self.locality_name
        }

        browse_w2_field_values_mixing_3 = {
            'topmostSubform[0].CopyC[0].f2_01[0]': self.essn_entry,
            'topmostSubform[0].CopyC[0].Col_Left[0].f2_02[0]': self.ein_entry,
            'topmostSubform[0].CopyC[0].Col_Left[0].f2_03[0]': self.employer_name_etc,
            'topmostSubform[0].CopyC[0].Col_Left[0].f2_04[0]': self.cn_entry,
            'topmostSubform[0].CopyC[0].Col_Left[0].f2_05[0]': self.employee_name_i,
            'topmostSubform[0].CopyC[0].Col_Left[0].f2_06[0]': self.employee_last_name,
            'topmostSubform[0].CopyC[0].Col_Left[0].f2_07[0]': self.employee_suffix,
            'topmostSubform[0].CopyC[0].Col_Left[0].f2_08[0]': self.employee_address_etc,
            'topmostSubform[0].CopyC[0].Col_Right[0].f2_09[0]': self.wages_tips_c,
            'topmostSubform[0].CopyC[0].Col_Right[0].f2_10[0]': self.fed_income_tax_withheld,
            'topmostSubform[0].CopyC[0].Col_Right[0].f2_11[0]': self.social_wages,
            'topmostSubform[0].CopyC[0].Col_Right[0].f2_12[0]': self.social_security_tax_withheld,
            'topmostSubform[0].CopyC[0].Col_Right[0].f2_13[0]': self.medicare_wages,
            'topmostSubform[0].CopyC[0].Col_Right[0].f2_14[0]': self.medicare_tax_withheld,
            'topmostSubform[0].CopyC[0].Col_Right[0].f2_15[0]': self.social_security_tips,
            'topmostSubform[0].CopyC[0].Col_Right[0].f2_16[0]': self.allocated_tips,
            'topmostSubform[0].CopyC[0].Col_Right[0].f2_18[0]': self.dependent_care_benefits,
            'topmostSubform[0].CopyC[0].Col_Right[0].f2_19[0]': self.non_qualified_plans,
            'topmostSubform[0].CopyC[0].Col_Right[0].Box12_ReadOrder[0].f2_21[0]': self.twelve_a,
            'topmostSubform[0].CopyC[0].Col_Right[0].Box12_ReadOrder[0].f2_23[0]': self.twelve_b,
            'topmostSubform[0].CopyC[0].Col_Right[0].Box12_ReadOrder[0].f2_25[0]': self.twelve_c,
            'topmostSubform[0].CopyC[0].Col_Right[0].Box12_ReadOrder[0].f2_27[0]': self.twelve_d,
            'topmostSubform[0].CopyC[0].Col_Right[0].f2_28[0]': self.other_field,
            'topmostSubform[0].CopyC[0].Boxes15_ReadOrder[0].f2_29[0]': self.state_field,
            'topmostSubform[0].CopyC[0].Boxes15_ReadOrder[0].f2_30[0]': self.employers_state_id,
            'topmostSubform[0].CopyC[0].Box16_ReadOrder[0].f2_33[0]': self.state_wage_tips,
            'topmostSubform[0].CopyC[0].Box17_ReadOrder[0].f2_35[0]': self.state_income_tax,
            'topmostSubform[0].CopyC[0].Box18_ReadOrder[0].f2_37[0]': self.local_wage_tips,
            'topmostSubform[0].CopyC[0].Box19_ReadOrder[0].f2_39[0]': self.local_income_tax,
            'topmostSubform[0].CopyC[0].f2_41[0]': self.locality_name
        }

        browse_w2_field_values_mixing_4 = {
            'topmostSubform[0].Copy2[0].f2_01[0]': self.essn_entry,
            'topmostSubform[0].Copy2[0].Col_Left[0].f2_02[0]': self.ein_entry,
            'topmostSubform[0].Copy2[0].Col_Left[0].f2_03[0]': self.employer_name_etc,
            'topmostSubform[0].Copy2[0].Col_Left[0].f2_04[0]': self.cn_entry,
            'topmostSubform[0].Copy2[0].Col_Left[0].f2_05[0]': self.employee_name_i,
            'topmostSubform[0].Copy2[0].Col_Left[0].f2_06[0]': self.employee_last_name,
            'topmostSubform[0].Copy2[0].Col_Left[0].f2_07[0]': self.employee_suffix,
            'topmostSubform[0].Copy2[0].Col_Left[0].f2_08[0]': self.employee_address_etc,
            'topmostSubform[0].Copy2[0].Col_Right[0].f2_09[0]': self.wages_tips_c,
            'topmostSubform[0].Copy2[0].Col_Right[0].f2_10[0]': self.fed_income_tax_withheld,
            'topmostSubform[0].Copy2[0].Col_Right[0].f2_11[0]': self.social_wages,
            'topmostSubform[0].Copy2[0].Col_Right[0].f2_12[0]': self.social_security_tax_withheld,
            'topmostSubform[0].Copy2[0].Col_Right[0].f2_13[0]': self.medicare_wages,
            'topmostSubform[0].Copy2[0].Col_Right[0].f2_14[0]': self.medicare_tax_withheld,
            'topmostSubform[0].Copy2[0].Col_Right[0].f2_15[0]': self.social_security_tips,
            'topmostSubform[0].Copy2[0].Col_Right[0].f2_16[0]': self.allocated_tips,
            'topmostSubform[0].Copy2[0].Col_Right[0].f2_18[0]': self.dependent_care_benefits,
            'topmostSubform[0].Copy2[0].Col_Right[0].f2_19[0]': self.non_qualified_plans,
            'topmostSubform[0].Copy2[0].Col_Right[0].Box12_ReadOrder[0].f2_21[0]': self.twelve_a,
            'topmostSubform[0].Copy2[0].Col_Right[0].Box12_ReadOrder[0].f2_23[0]': self.twelve_b,
            'topmostSubform[0].Copy2[0].Col_Right[0].Box12_ReadOrder[0].f2_25[0]': self.twelve_c,
            'topmostSubform[0].Copy2[0].Col_Right[0].Box12_ReadOrder[0].f2_27[0]': self.twelve_d,
            'topmostSubform[0].Copy2[0].Col_Right[0].f2_28[0]': self.other_field,
            'topmostSubform[0].Copy2[0].Boxes15_ReadOrder[0].f2_29[0]': self.state_field,
            'topmostSubform[0].Copy2[0].Boxes15_ReadOrder[0].f2_30[0]': self.employers_state_id,
            'topmostSubform[0].Copy2[0].Box16_ReadOrder[0].f2_33[0]': self.state_wage_tips,
            'topmostSubform[0].Copy2[0].Box17_ReadOrder[0].f2_35[0]': self.state_income_tax,
            'topmostSubform[0].Copy2[0].Box18_ReadOrder[0].f2_37[0]': self.local_wage_tips,
            'topmostSubform[0].Copy2[0].Box19_ReadOrder[0].f2_39[0]': self.local_income_tax,
            'topmostSubform[0].Copy2[0].f2_41[0]': self.locality_name
        }

        browse_w2_field_values_mixing_5 = {
            'topmostSubform[0].CopyD[0].f2_01[0]': self.essn_entry,
            'topmostSubform[0].CopyD[0].Col_Left[0].f2_02[0]': self.ein_entry,
            'topmostSubform[0].CopyD[0].Col_Left[0].f2_03[0]': self.employer_name_etc,
            'topmostSubform[0].CopyD[0].Col_Left[0].f2_04[0]': self.cn_entry,
            'topmostSubform[0].CopyD[0].Col_Left[0].f2_05[0]': self.employee_name_i,
            'topmostSubform[0].CopyD[0].Col_Left[0].f2_06[0]': self.employee_last_name,
            'topmostSubform[0].CopyD[0].Col_Left[0].f2_07[0]': self.employee_suffix,
            'topmostSubform[0].CopyD[0].Col_Left[0].f2_08[0]': self.employee_address_etc,
            'topmostSubform[0].CopyD[0].Col_Right[0].f2_09[0]': self.wages_tips_c,
            'topmostSubform[0].CopyD[0].Col_Right[0].f2_10[0]': self.fed_income_tax_withheld,
            'topmostSubform[0].CopyD[0].Col_Right[0].f2_11[0]': self.social_wages,
            'topmostSubform[0].CopyD[0].Col_Right[0].f2_12[0]': self.social_security_tax_withheld,
            'topmostSubform[0].CopyD[0].Col_Right[0].f2_13[0]': self.medicare_wages,
            'topmostSubform[0].CopyD[0].Col_Right[0].f2_14[0]': self.medicare_tax_withheld,
            'topmostSubform[0].CopyD[0].Col_Right[0].f2_15[0]': self.social_security_tips,
            'topmostSubform[0].CopyD[0].Col_Right[0].f2_16[0]': self.allocated_tips,
            'topmostSubform[0].CopyD[0].Col_Right[0].f2_18[0]': self.dependent_care_benefits,
            'topmostSubform[0].CopyD[0].Col_Right[0].f2_19[0]': self.non_qualified_plans,
            'topmostSubform[0].CopyD[0].Col_Right[0].Box12_ReadOrder[0].f2_21[0]': self.twelve_a,
            'topmostSubform[0].CopyD[0].Col_Right[0].Box12_ReadOrder[0].f2_23[0]': self.twelve_b,
            'topmostSubform[0].CopyD[0].Col_Right[0].Box12_ReadOrder[0].f2_25[0]': self.twelve_c,
            'topmostSubform[0].CopyD[0].Col_Right[0].Box12_ReadOrder[0].f2_27[0]': self.twelve_d,
            'topmostSubform[0].CopyD[0].Col_Right[0].f2_28[0]': self.other_field,
            'topmostSubform[0].CopyD[0].Boxes15_ReadOrder[0].f2_29[0]': self.state_field,
            'topmostSubform[0].CopyD[0].Boxes15_ReadOrder[0].f2_30[0]': self.employers_state_id,
            'topmostSubform[0].CopyD[0].Box16_ReadOrder[0].f2_33[0]': self.state_wage_tips,
            'topmostSubform[0].CopyD[0].Box17_ReadOrder[0].f2_35[0]': self.state_income_tax,
            'topmostSubform[0].CopyD[0].Box18_ReadOrder[0].f2_37[0]': self.local_wage_tips,
            'topmostSubform[0].CopyD[0].Box19_ReadOrder[0].f2_39[0]': self.local_income_tax,
            'topmostSubform[0].CopyD[0].f2_41[0]': self.locality_name
        }

        for each_page in pdf:
            widgets = each_page.widgets()
            for content in widgets:
                for field_name, entry_widget in {**browse_w2_field_values_mixing, **browse_w2_field_values_mixing_2,
                                                 **browse_w2_field_values_mixing_3,
                                                 **browse_w2_field_values_mixing_4,
                                                 **browse_w2_field_values_mixing_5}.items():
                    if content.field_name == field_name:

                        value = content.field_value.strip()
                        if value != "":
                            entry_widget.delete(0, tk.END)  # Clear text
                            entry_widget.insert(0, value)  # Set value

        pdf.close()

    ###################################################################################################################

    ###################################################################################################################
    # 1099 #
    # Save-as 1099 #
    def save_form_1099_as(self):
        """
        Opens a file explorer to save the tax-related data to a pdf file.

        Updates the form fields in a given PDF document with values from a dictionary.

        Returns:
            None
        """

        # Opening the file explorer
        filename = filedialog.asksaveasfilename(initialdir="/", title="Save As",
                                                filetypes=(("PDF Files", "*.pdf"),))
        if filename:

            def update_widget_values_1099(input_pdf, output_pdf):
                """
                    Updates entry widgets with field values extracted from a PDF.

                    Details:
                        - The code iterates through each page in the PDF.
                        - For each page, it retrieves the widgets (form fields).
                        - It then checks if the field name matches any of the specified entry widgets.
                        - If a match is found and the field value is not empty,
                        it updates the corresponding entry widget
                """
                # Opening the input PDF
                pdf = fitz.open(input_pdf)
                save_as_1099_field_values_mixing = {
                    'topmostSubform[0].Copy1[0].LeftCol[0].f2_2[0]': str(self.ten_ninety_nine_payer_info.get()),
                    'topmostSubform[0].Copy1[0].LeftCol[0].f2_3[0]': str(self.ten_ninety_nine_payer_tin.get()),
                    'topmostSubform[0].Copy1[0].LeftCol[0].f2_4[0]': str(self.ten_ninety_nine_recipient_tin.get()),
                    'topmostSubform[0].Copy1[0].LeftCol[0].f2_5[0]': str(self.ten_ninety_nine_recipient_name.get()),
                    'topmostSubform[0].Copy1[0].LeftCol[0].f2_6[0]': str(self.ten_ninety_nine_recipient_address.get()),
                    'topmostSubform[0].Copy1[0].LeftCol[0].f2_7[0]': str(self.ten_ninety_nine_recipient_city_etc.get()),
                    'topmostSubform[0].Copy1[0].LeftCol[0].f2_8[0]': str(self.ten_ninety_nine_account_number.get()),
                    'topmostSubform[0].Copy1[0].RghtCol[0].f2_9[0]': str(self.ten_ninety_nine_ordinary_dividends.get()),
                    'topmostSubform[0].Copy1[0].RghtCol[0].f2_10[0]': str(
                        self.ten_ninety_nine_qualified_dividends.get()),
                    'topmostSubform[0].Copy1[0].RghtCol[0].Box2a_ReadOrder[0].f2_11[0]':
                        str(self.ten_ninety_nine_capital_gain.get()),
                    'topmostSubform[0].Copy1[0].RghtCol[0].Box2c_ReadOrder[0].f2_13[0]':
                        str(self.ten_ninety_nine_1202_gain.get()),
                    'topmostSubform[0].Copy1[0].RghtCol[0].Box2e_ReadOrder[0].f2_15[0]':
                        str(self.ten_ninety_nine_897_dividends.get()),
                    'topmostSubform[0].Copy1[0].RghtCol[0].Box3_ReadOrder[0].f2_17[0]':
                        str(self.ten_ninety_nine_nondividend.get()),
                    'topmostSubform[0].Copy1[0].RghtCol[0].Box5_ReadOrder[0].f2_19[0]':
                        str(self.ten_ninety_nine_199a.get()),
                    'topmostSubform[0].Copy1[0].RghtCol[0].Box7_ReadOrder[0].f2_21[0]':
                        str(self.ten_ninety_nine_foreign_tax.get()),
                    'topmostSubform[0].Copy1[0].RghtCol[0].Box9_ReadOrder[0].f2_23[0]':
                        str(self.ten_ninety_nine_cash_liquidation.get()),
                    'topmostSubform[0].Copy1[0].RghtCol[0].Box12_ReadOrder[0].f2_25[0]':
                        str(self.ten_ninety_nine_exempt_dividends.get()),
                    'topmostSubform[0].Copy1[0].RghtCol[0].Box14_ReadOrder[0].f2_27[0]': str(
                        self.ten_ninety_nine_state.get()),
                    'topmostSubform[0].Copy1[0].RghtCol[0].Box15_ReadOrder[0].f2_29[0]': str(
                        self.ten_ninety_nine_state_id_number.get()),
                    'topmostSubform[0].Copy1[0].RghtCol[0].f2_12[0]': str(self.ten_ninety_nine_1250_gain.get()),
                    'topmostSubform[0].Copy1[0].RghtCol[0].f2_14[0]': str(self.ten_ninety_nine_collectibles_gain.get()),
                    'topmostSubform[0].Copy1[0].RghtCol[0].f2_16[0]': str(self.ten_ninety_nine_897_gain.get()),
                    'topmostSubform[0].Copy1[0].RghtCol[0].f2_18[0]': str(
                        self.ten_ninety_nine_federal_tax_withheld.get()),
                    'topmostSubform[0].Copy1[0].RghtCol[0].f2_20[0]': str(
                        self.ten_ninety_nine_investment_expenses.get()),
                    'topmostSubform[0].Copy1[0].RghtCol[0].f2_22[0]': str(
                        self.ten_ninety_nine_foreign_tax_country.get()),
                    'topmostSubform[0].Copy1[0].RghtCol[0].f2_24[0]': str(
                        self.ten_ninety_nine_noncash_liquidation.get()),
                    'topmostSubform[0].Copy1[0].RghtCol[0].f2_26[0]': str(
                        self.ten_ninety_nine_specified_bond_dividends.get()),
                    'topmostSubform[0].Copy1[0].RghtCol[0].f2_31[0]': str(self.ten_ninety_nine_state_tax_withheld.get())
                }

                save_as_1099_field_values_mixing_2 = {
                    'topmostSubform[0].CopyB[0].LeftCol[0].f2_2[0]': str(self.ten_ninety_nine_payer_info.get()),
                    'topmostSubform[0].CopyB[0].LeftCol[0].f2_3[0]': str(self.ten_ninety_nine_payer_tin.get()),
                    'topmostSubform[0].CopyB[0].LeftCol[0].f2_4[0]': str(self.ten_ninety_nine_recipient_tin.get()),
                    'topmostSubform[0].CopyB[0].LeftCol[0].f2_5[0]': str(self.ten_ninety_nine_recipient_name.get()),
                    'topmostSubform[0].CopyB[0].LeftCol[0].f2_6[0]': str(self.ten_ninety_nine_recipient_address.get()),
                    'topmostSubform[0].CopyB[0].LeftCol[0].f2_7[0]': str(self.ten_ninety_nine_recipient_city_etc.get()),
                    'topmostSubform[0].CopyB[0].LeftCol[0].f2_8[0]': str(self.ten_ninety_nine_account_number.get()),
                    'topmostSubform[0].CopyB[0].RghtCol[0].f2_9[0]': str(self.ten_ninety_nine_ordinary_dividends.get()),
                    'topmostSubform[0].CopyB[0].RghtCol[0].f2_10[0]': str(
                        self.ten_ninety_nine_qualified_dividends.get()),
                    'topmostSubform[0].CopyB[0].RghtCol[0].Box2a_ReadOrder[0].f2_11[0]':
                        str(self.ten_ninety_nine_capital_gain.get()),
                    'topmostSubform[0].CopyB[0].RghtCol[0].Box2c_ReadOrder[0].f2_13[0]':
                        str(self.ten_ninety_nine_1202_gain.get()),
                    'topmostSubform[0].CopyB[0].RghtCol[0].Box2e_ReadOrder[0].f2_15[0]':
                        str(self.ten_ninety_nine_897_dividends.get()),
                    'topmostSubform[0].CopyB[0].RghtCol[0].Box3_ReadOrder[0].f2_17[0]':
                        str(self.ten_ninety_nine_nondividend.get()),
                    'topmostSubform[0].CopyB[0].RghtCol[0].Box5_ReadOrder[0].f2_19[0]':
                        str(self.ten_ninety_nine_199a.get()),
                    'topmostSubform[0].CopyB[0].RghtCol[0].Box7_ReadOrder[0].f2_21[0]':
                        str(self.ten_ninety_nine_foreign_tax.get()),
                    'topmostSubform[0].CopyB[0].RghtCol[0].Box9_ReadOrder[0].f2_23[0]':
                        str(self.ten_ninety_nine_cash_liquidation.get()),
                    'topmostSubform[0].CopyB[0].RghtCol[0].Box12_ReadOrder[0].f2_25[0]':
                        str(self.ten_ninety_nine_exempt_dividends.get()),
                    'topmostSubform[0].CopyB[0].RghtCol[0].Box14_ReadOrder[0].f2_27[0]': str(
                        self.ten_ninety_nine_state.get()),
                    'topmostSubform[0].CopyB[0].RghtCol[0].Box15_ReadOrder[0].f2_29[0]': str(
                        self.ten_ninety_nine_state_id_number.get()),
                    'topmostSubform[0].CopyB[0].RghtCol[0].f2_12[0]': str(self.ten_ninety_nine_1250_gain.get()),
                    'topmostSubform[0].CopyB[0].RghtCol[0].f2_14[0]': str(self.ten_ninety_nine_collectibles_gain.get()),
                    'topmostSubform[0].CopyB[0].RghtCol[0].f2_16[0]': str(self.ten_ninety_nine_897_gain.get()),
                    'topmostSubform[0].CopyB[0].RghtCol[0].f2_18[0]': str(
                        self.ten_ninety_nine_federal_tax_withheld.get()),
                    'topmostSubform[0].CopyB[0].RghtCol[0].f2_20[0]': str(
                        self.ten_ninety_nine_investment_expenses.get()),
                    'topmostSubform[0].CopyB[0].RghtCol[0].f2_22[0]': str(
                        self.ten_ninety_nine_foreign_tax_country.get()),
                    'topmostSubform[0].CopyB[0].RghtCol[0].f2_24[0]': str(
                        self.ten_ninety_nine_noncash_liquidation.get()),
                    'topmostSubform[0].CopyB[0].RghtCol[0].f2_26[0]': str(
                        self.ten_ninety_nine_specified_bond_dividends.get()),
                    'topmostSubform[0].CopyB[0].RghtCol[0].f2_31[0]': str(self.ten_ninety_nine_state_tax_withheld.get())
                }

                save_as_1099_field_values_mixing_3 = {
                    'topmostSubform[0].Copy2[0].LeftCol[0].f2_2[0]': str(self.ten_ninety_nine_payer_info.get()),
                    'topmostSubform[0].Copy2[0].LeftCol[0].f2_3[0]': str(self.ten_ninety_nine_payer_tin.get()),
                    'topmostSubform[0].Copy2[0].LeftCol[0].f2_4[0]': str(self.ten_ninety_nine_recipient_tin.get()),
                    'topmostSubform[0].Copy2[0].LeftCol[0].f2_5[0]': str(self.ten_ninety_nine_recipient_name.get()),
                    'topmostSubform[0].Copy2[0].LeftCol[0].f2_6[0]': str(self.ten_ninety_nine_recipient_address.get()),
                    'topmostSubform[0].Copy2[0].LeftCol[0].f2_7[0]': str(self.ten_ninety_nine_recipient_city_etc.get()),
                    'topmostSubform[0].Copy2[0].LeftCol[0].f2_8[0]': str(self.ten_ninety_nine_account_number.get()),
                    'topmostSubform[0].Copy2[0].RghtCol[0].f2_9[0]': str(self.ten_ninety_nine_ordinary_dividends.get()),
                    'topmostSubform[0].Copy2[0].RghtCol[0].f2_10[0]': str(
                        self.ten_ninety_nine_qualified_dividends.get()),
                    'topmostSubform[0].Copy2[0].RghtCol[0].Box2a_ReadOrder[0].f2_11[0]':
                        str(self.ten_ninety_nine_capital_gain.get()),
                    'topmostSubform[0].Copy2[0].RghtCol[0].Box2c_ReadOrder[0].f2_13[0]':
                        str(self.ten_ninety_nine_1202_gain.get()),
                    'topmostSubform[0].Copy2[0].RghtCol[0].Box2e_ReadOrder[0].f2_15[0]':
                        str(self.ten_ninety_nine_897_dividends.get()),
                    'topmostSubform[0].Copy2[0].RghtCol[0].Box3_ReadOrder[0].f2_17[0]':
                        str(self.ten_ninety_nine_nondividend.get()),
                    'topmostSubform[0].Copy2[0].RghtCol[0].Box5_ReadOrder[0].f2_19[0]':
                        str(self.ten_ninety_nine_199a.get()),
                    'topmostSubform[0].Copy2[0].RghtCol[0].Box7_ReadOrder[0].f2_21[0]':
                        str(self.ten_ninety_nine_foreign_tax.get()),
                    'topmostSubform[0].Copy2[0].RghtCol[0].Box9_ReadOrder[0].f2_23[0]':
                        str(self.ten_ninety_nine_cash_liquidation.get()),
                    'topmostSubform[0].Copy2[0].RghtCol[0].Box12_ReadOrder[0].f2_25[0]':
                        str(self.ten_ninety_nine_exempt_dividends.get()),
                    'topmostSubform[0].Copy2[0].RghtCol[0].Box14_ReadOrder[0].f2_27[0]': str(
                        self.ten_ninety_nine_state.get()),
                    'topmostSubform[0].Copy2[0].RghtCol[0].Box15_ReadOrder[0].f2_29[0]': str(
                        self.ten_ninety_nine_state_id_number.get()),
                    'topmostSubform[0].Copy2[0].RghtCol[0].f2_12[0]': str(self.ten_ninety_nine_1250_gain.get()),
                    'topmostSubform[0].Copy2[0].RghtCol[0].f2_14[0]': str(self.ten_ninety_nine_collectibles_gain.get()),
                    'topmostSubform[0].Copy2[0].RghtCol[0].f2_16[0]': str(self.ten_ninety_nine_897_gain.get()),
                    'topmostSubform[0].Copy2[0].RghtCol[0].f2_18[0]': str(
                        self.ten_ninety_nine_federal_tax_withheld.get()),
                    'topmostSubform[0].Copy2[0].RghtCol[0].f2_20[0]': str(
                        self.ten_ninety_nine_investment_expenses.get()),
                    'topmostSubform[0].Copy2[0].RghtCol[0].f2_22[0]': str(
                        self.ten_ninety_nine_foreign_tax_country.get()),
                    'topmostSubform[0].Copy2[0].RghtCol[0].f2_24[0]': str(
                        self.ten_ninety_nine_noncash_liquidation.get()),
                    'topmostSubform[0].Copy2[0].RghtCol[0].f2_26[0]': str(
                        self.ten_ninety_nine_specified_bond_dividends.get()),
                    'topmostSubform[0].Copy2[0].RghtCol[0].f2_31[0]': str(self.ten_ninety_nine_state_tax_withheld.get())
                }

                # Iteration for each page
                for each_page in pdf:
                    widgets = each_page.widgets()
                    for content in widgets:
                        for field_name, value in {**save_as_1099_field_values_mixing,
                                                  **save_as_1099_field_values_mixing_2,
                                                  **save_as_1099_field_values_mixing_3}.items():
                            if content.field_name == field_name:
                                if value == "":
                                    content.field_value = " "
                                else:
                                    content.field_value = value
                                content.update()

                # Saving the modified PDF
                pdf.save(output_pdf)
                pdf.close()

            # Input and output PDF filenames
            input_pdf_file = "default_1099.pdf"
            output_pdf_file = os.path.splitext(filename)[0] + ".pdf"

            # Updating of widget values and saving the modified PDF
            update_widget_values_1099(input_pdf_file, output_pdf_file)
            print(f"Modified PDF saved as {output_pdf_file}")

    # Browse 1099

    def browse_form_1099(self):
        """
           Opens a file explorer to select a pdf file containing tax information.
           Assigns data accordingly.
        """
        filename = filedialog.askopenfilename(initialdir="/", title="Open", filetypes=(("PDF Files", "*.pdf"),))
        if filename:
            self.update_input_fields_1099(filename)

    def update_input_fields_1099(self, input_pdf):
        """
            Updates entry widgets with field values extracted from a PDF.

            Details:
                - The code iterates through each page in the PDF.
                - For each page, it retrieves the widgets (form fields).
                - It then checks if the field name matches any of the specified entry widgets.
                - If a match is found and the field value is not empty, it updates the corresponding entry widget
        """
        # Opening the input PDF
        pdf = fitz.open(input_pdf)
        browse_1099_field_values_mixing = {
            'topmostSubform[0].Copy1[0].LeftCol[0].f2_2[0]': self.ten_ninety_nine_payer_info,
            'topmostSubform[0].Copy1[0].LeftCol[0].f2_3[0]': self.ten_ninety_nine_payer_tin,
            'topmostSubform[0].Copy1[0].LeftCol[0].f2_4[0]': self.ten_ninety_nine_recipient_tin,
            'topmostSubform[0].Copy1[0].LeftCol[0].f2_5[0]': self.ten_ninety_nine_recipient_name,
            'topmostSubform[0].Copy1[0].LeftCol[0].f2_6[0]': self.ten_ninety_nine_recipient_address,
            'topmostSubform[0].Copy1[0].LeftCol[0].f2_7[0]': self.ten_ninety_nine_recipient_city_etc,
            'topmostSubform[0].Copy1[0].LeftCol[0].f2_8[0]': self.ten_ninety_nine_account_number,
            'topmostSubform[0].Copy1[0].RghtCol[0].f2_9[0]': self.ten_ninety_nine_ordinary_dividends,
            'topmostSubform[0].Copy1[0].RghtCol[0].f2_10[0]': self.ten_ninety_nine_qualified_dividends,
            'topmostSubform[0].Copy1[0].RghtCol[0].f2_11[0]': self.ten_ninety_nine_capital_gain,
            'topmostSubform[0].Copy1[0].RghtCol[0].f2_13[0]': self.ten_ninety_nine_1202_gain,
            'topmostSubform[0].Copy1[0].RghtCol[0].f2_15[0]': self.ten_ninety_nine_897_dividends,
            'topmostSubform[0].Copy1[0].RghtCol[0].f2_17[0]': self.ten_ninety_nine_nondividend,
            'topmostSubform[0].Copy1[0].RghtCol[0].f2_19[0]': self.ten_ninety_nine_199a,
            'topmostSubform[0].Copy1[0].RghtCol[0].f2_21[0]': self.ten_ninety_nine_foreign_tax,
            'topmostSubform[0].Copy1[0].RghtCol[0].f2_23[0]': self.ten_ninety_nine_cash_liquidation,
            'topmostSubform[0].Copy1[0].RghtCol[0].f2_25[0]': self.ten_ninety_nine_exempt_dividends,
            'topmostSubform[0].Copy1[0].RghtCol[0].Box14_ReadOrder[0].f2_27[0]': self.ten_ninety_nine_state,
            'topmostSubform[0].Copy1[0].RghtCol[0].Box15_ReadOrder[0].f2_29[0]': self.ten_ninety_nine_state_id_number,
            'topmostSubform[0].Copy1[0].RghtCol[0].f2_12[0]': self.ten_ninety_nine_1250_gain,
            'topmostSubform[0].Copy1[0].RghtCol[0].f2_14[0]': self.ten_ninety_nine_collectibles_gain,
            'topmostSubform[0].Copy1[0].RghtCol[0].f2_16[0]': self.ten_ninety_nine_897_gain,
            'topmostSubform[0].Copy1[0].RghtCol[0].f2_18[0]': self.ten_ninety_nine_federal_tax_withheld,
            'topmostSubform[0].Copy1[0].RghtCol[0].f2_20[0]': self.ten_ninety_nine_investment_expenses,
            'topmostSubform[0].Copy1[0].RghtCol[0].f2_22[0]': self.ten_ninety_nine_foreign_tax_country,
            'topmostSubform[0].Copy1[0].RghtCol[0].f2_24[0]': self.ten_ninety_nine_noncash_liquidation,
            'topmostSubform[0].Copy1[0].RghtCol[0].f2_26[0]': self.ten_ninety_nine_specified_bond_dividends,
            'topmostSubform[0].Copy1[0].RghtCol[0].f2_31[0]': self.ten_ninety_nine_state_tax_withheld
        }

        browse_1099_field_values_mixing_2 = {
            'topmostSubform[0].CopyB[0].LeftCol[0].f2_2[0]': self.ten_ninety_nine_payer_info,
            'topmostSubform[0].CopyB[0].LeftCol[0].f2_3[0]': self.ten_ninety_nine_payer_tin,
            'topmostSubform[0].CopyB[0].LeftCol[0].f2_4[0]': self.ten_ninety_nine_recipient_tin,
            'topmostSubform[0].CopyB[0].LeftCol[0].f2_5[0]': self.ten_ninety_nine_recipient_name,
            'topmostSubform[0].CopyB[0].LeftCol[0].f2_6[0]': self.ten_ninety_nine_recipient_address,
            'topmostSubform[0].CopyB[0].LeftCol[0].f2_7[0]': self.ten_ninety_nine_recipient_city_etc,
            'topmostSubform[0].CopyB[0].LeftCol[0].f2_8[0]': self.ten_ninety_nine_account_number,
            'topmostSubform[0].CopyB[0].RghtCol[0].f2_9[0]': self.ten_ninety_nine_ordinary_dividends,
            'topmostSubform[0].CopyB[0].RghtCol[0].f2_10[0]': self.ten_ninety_nine_qualified_dividends,
            'topmostSubform[0].CopyB[0].RghtCol[0].f2_11[0]': self.ten_ninety_nine_capital_gain,
            'topmostSubform[0].CopyB[0].RghtCol[0].f2_13[0]': self.ten_ninety_nine_1202_gain,
            'topmostSubform[0].CopyB[0].RghtCol[0].f2_15[0]': self.ten_ninety_nine_897_dividends,
            'topmostSubform[0].CopyB[0].RghtCol[0].f2_17[0]': self.ten_ninety_nine_nondividend,
            'topmostSubform[0].CopyB[0].RghtCol[0].f2_19[0]': self.ten_ninety_nine_199a,
            'topmostSubform[0].CopyB[0].RghtCol[0].f2_21[0]': self.ten_ninety_nine_foreign_tax,
            'topmostSubform[0].CopyB[0].RghtCol[0].f2_23[0]': self.ten_ninety_nine_cash_liquidation,
            'topmostSubform[0].CopyB[0].RghtCol[0].f2_25[0]': self.ten_ninety_nine_exempt_dividends,
            'topmostSubform[0].CopyB[0].RghtCol[0].Box14_ReadOrder[0].f2_27[0]': self.ten_ninety_nine_state,
            'topmostSubform[0].CopyB[0].RghtCol[0].Box15_ReadOrder[0].f2_29[0]': self.ten_ninety_nine_state_id_number,
            'topmostSubform[0].CopyB[0].RghtCol[0].f2_12[0]': self.ten_ninety_nine_1250_gain,
            'topmostSubform[0].CopyB[0].RghtCol[0].f2_14[0]': self.ten_ninety_nine_collectibles_gain,
            'topmostSubform[0].CopyB[0].RghtCol[0].f2_16[0]': self.ten_ninety_nine_897_gain,
            'topmostSubform[0].CopyB[0].RghtCol[0].f2_18[0]': self.ten_ninety_nine_federal_tax_withheld,
            'topmostSubform[0].CopyB[0].RghtCol[0].f2_20[0]': self.ten_ninety_nine_investment_expenses,
            'topmostSubform[0].CopyB[0].RghtCol[0].f2_22[0]': self.ten_ninety_nine_foreign_tax_country,
            'topmostSubform[0].CopyB[0].RghtCol[0].f2_24[0]': self.ten_ninety_nine_noncash_liquidation,
            'topmostSubform[0].CopyB[0].RghtCol[0].f2_26[0]': self.ten_ninety_nine_specified_bond_dividends,
            'topmostSubform[0].CopyB[0].RghtCol[0].f2_31[0]': self.ten_ninety_nine_state_tax_withheld
        }

        browse_1099_field_values_mixing_3 = {
            'topmostSubform[0].Copy2[0].LeftCol[0].f2_2[0]': self.ten_ninety_nine_payer_info,
            'topmostSubform[0].Copy2[0].LeftCol[0].f2_3[0]': self.ten_ninety_nine_payer_tin,
            'topmostSubform[0].Copy2[0].LeftCol[0].f2_4[0]': self.ten_ninety_nine_recipient_tin,
            'topmostSubform[0].Copy2[0].LeftCol[0].f2_5[0]': self.ten_ninety_nine_recipient_name,
            'topmostSubform[0].Copy2[0].LeftCol[0].f2_6[0]': self.ten_ninety_nine_recipient_address,
            'topmostSubform[0].Copy2[0].LeftCol[0].f2_7[0]': self.ten_ninety_nine_recipient_city_etc,
            'topmostSubform[0].Copy2[0].LeftCol[0].f2_8[0]': self.ten_ninety_nine_account_number,
            'topmostSubform[0].Copy2[0].RghtCol[0].f2_9[0]': self.ten_ninety_nine_ordinary_dividends,
            'topmostSubform[0].Copy2[0].RghtCol[0].f2_10[0]': self.ten_ninety_nine_qualified_dividends,
            'topmostSubform[0].Copy2[0].RghtCol[0].f2_11[0]': self.ten_ninety_nine_capital_gain,
            'topmostSubform[0].Copy2[0].RghtCol[0].f2_13[0]': self.ten_ninety_nine_1202_gain,
            'topmostSubform[0].Copy2[0].RghtCol[0].f2_15[0]': self.ten_ninety_nine_897_dividends,
            'topmostSubform[0].Copy2[0].RghtCol[0].f2_17[0]': self.ten_ninety_nine_nondividend,
            'topmostSubform[0].Copy2[0].RghtCol[0].f2_19[0]': self.ten_ninety_nine_199a,
            'topmostSubform[0].Copy2[0].RghtCol[0].f2_21[0]': self.ten_ninety_nine_foreign_tax,
            'topmostSubform[0].Copy2[0].RghtCol[0].f2_23[0]': self.ten_ninety_nine_cash_liquidation,
            'topmostSubform[0].Copy2[0].RghtCol[0].f2_25[0]': self.ten_ninety_nine_exempt_dividends,
            'topmostSubform[0].Copy2[0].RghtCol[0].Box14_ReadOrder[0].f2_27[0]': self.ten_ninety_nine_state,
            'topmostSubform[0].Copy2[0].RghtCol[0].Box15_ReadOrder[0].f2_29[0]': self.ten_ninety_nine_state_id_number,
            'topmostSubform[0].Copy2[0].RghtCol[0].f2_12[0]': self.ten_ninety_nine_1250_gain,
            'topmostSubform[0].Copy2[0].RghtCol[0].f2_14[0]': self.ten_ninety_nine_collectibles_gain,
            'topmostSubform[0].Copy2[0].RghtCol[0].f2_16[0]': self.ten_ninety_nine_897_gain,
            'topmostSubform[0].Copy2[0].RghtCol[0].f2_18[0]': self.ten_ninety_nine_federal_tax_withheld,
            'topmostSubform[0].Copy2[0].RghtCol[0].f2_20[0]': self.ten_ninety_nine_investment_expenses,
            'topmostSubform[0].Copy2[0].RghtCol[0].f2_22[0]': self.ten_ninety_nine_foreign_tax_country,
            'topmostSubform[0].Copy2[0].RghtCol[0].f2_24[0]': self.ten_ninety_nine_noncash_liquidation,
            'topmostSubform[0].Copy2[0].RghtCol[0].f2_26[0]': self.ten_ninety_nine_specified_bond_dividends,
            'topmostSubform[0].Copy2[0].RghtCol[0].f2_31[0]': self.ten_ninety_nine_state_tax_withheld
        }

        for each_page in pdf:
            widgets = each_page.widgets()
            for content in widgets:
                for field_name, entry_widget in {**browse_1099_field_values_mixing, **browse_1099_field_values_mixing_2,
                                                 **browse_1099_field_values_mixing_3}.items():
                    if content.field_name == field_name:

                        value = content.field_value.strip()
                        if value != "":
                            entry_widget.delete(0, tk.END)  # Clear text
                            entry_widget.insert(0, value)  # Set value

        pdf.close()

    ###################################################################################################################

    ###################################################################################################################

    ###################################################################################################################
    # 1040 #
    # Save-as 1040 #
    def save_form_1040_as(self):
        """
        Opens a file explorer to save the tax-related data to a pdf file.
        """

        # Opening the file explorer
        filename = filedialog.asksaveasfilename(initialdir="/", title="Save As",
                                                filetypes=(("PDF Files", "*.pdf"),))
        if filename:

            def update_widget_values_1040(input_pdf, output_pdf):
                """
                    Updates entry widgets with field values extracted from a PDF.

                    Details:
                        - The code iterates through each page in the PDF.
                        - For each page, it retrieves the widgets (form fields).
                        - It then checks if the field name matches any of the specified entry widgets.
                        - If a match is found and the field value is not empty,
                        - it updates the corresponding entry widget
                """
                # Opening the input PDF
                pdf = fitz.open(input_pdf)
                save_as_1040_field_values_mixing = {
                    'topmostSubform[0].Page1[0].f1_04[0]': str(self.ten_forty_first_name.get()),
                    'topmostSubform[0].Page1[0].f1_05[0]': str(self.ten_forty_last_name.get()),
                    'topmostSubform[0].Page1[0].f1_07[0]': str(self.ten_forty_spouse_first.get()),
                    'topmostSubform[0].Page1[0].f1_08[0]': str(self.ten_forty_spouse_last.get()),
                    'topmostSubform[0].Page1[0].Address_ReadOrder[0].f1_10[0]': str(self.ten_forty_home_address.get()),
                    'topmostSubform[0].Page1[0].Address_ReadOrder[0].f1_11[0]': str(self.ten_forty_apt_no.get()),
                    'topmostSubform[0].Page1[0].Address_ReadOrder[0].f1_12[0]': str(self.ten_forty_city.get()),
                    'topmostSubform[0].Page1[0].Address_ReadOrder[0].f1_13[0]': str(self.ten_forty_state.get()),
                    'topmostSubform[0].Page1[0].Address_ReadOrder[0].f1_14[0]': str(self.ten_forty_zip.get()),
                    'topmostSubform[0].Page1[0].Address_ReadOrder[0].f1_15[0]': str(
                        self.ten_forty_foreign_country.get()),
                    'topmostSubform[0].Page1[0].Address_ReadOrder[0].f1_16[0]': str(
                        self.ten_forty_foreign_province.get()),
                    'topmostSubform[0].Page1[0].Address_ReadOrder[0].f1_17[0]': str(
                        self.ten_forty_foreign_post_code.get()),
                    'topmostSubform[0].Page1[0].Table_Dependents[0].Row1[0].f1_19[0]': str(
                        self.ten_forty_dependent_first_1.get()),
                    'topmostSubform[0].Page1[0].Table_Dependents[0].Row2[0].f1_22[0]': str(
                        self.ten_forty_dependent_first_2.get()),
                    'topmostSubform[0].Page1[0].Table_Dependents[0].Row3[0].f1_25[0]': str(
                        self.ten_forty_dependent_first_3.get()),
                    'topmostSubform[0].Page1[0].Table_Dependents[0].Row4[0].f1_28[0]': str(
                        self.ten_forty_dependent_first_4.get()),
                    'topmostSubform[0].Page1[0].f1_31[0]': str(self.ten_forty_total_w2s.get()),
                    'topmostSubform[0].Page1[0].f1_32[0]': str(self.ten_forty_household_wages.get()),
                    'topmostSubform[0].Page1[0].f1_33[0]': str(self.ten_forty_tip_income.get()),
                    'topmostSubform[0].Page1[0].f1_34[0]': str(self.ten_forty_medicaid_waiver.get()),
                    'topmostSubform[0].Page1[0].f1_35[0]': str(self.ten_forty_dependent_benefits.get()),
                    'topmostSubform[0].Page1[0].f1_36[0]': str(self.ten_forty_adoption_benefits.get()),
                    'topmostSubform[0].Page1[0].f1_37[0]': str(self.ten_forty_8919_wages.get()),
                    'topmostSubform[0].Page1[0].f1_38[0]': str(self.ten_forty_other_income.get()),
                    'topmostSubform[0].Page1[0].f1_39[0]': str(self.ten_forty_combat_pay.get()),
                    'topmostSubform[0].Page1[0].f1_40[0]': str(self.ten_forty_1_ah_sum.get()),
                    'topmostSubform[0].Page1[0].f1_41[0]': str(self.ten_forty_tax_exempt_interest.get()),
                    'topmostSubform[0].Page1[0].f1_42[0]': str(self.ten_forty_taxable_interest.get()),
                    'topmostSubform[0].Page1[0].f1_43[0]': str(self.ten_forty_qualified_dividends.get()),
                    'topmostSubform[0].Page1[0].f1_44[0]': str(self.ten_forty_ordinary_dividends.get()),
                    'topmostSubform[0].Page1[0].Line4a-11_ReadOrder[0].f1_45[0]': str(
                        self.ten_forty_ira_distributions.get()),
                    'topmostSubform[0].Page1[0].Line4a-11_ReadOrder[0].f1_46[0]': str(self.ten_forty_taxable_ira.get()),
                    'topmostSubform[0].Page1[0].Line4a-11_ReadOrder[0].f1_47[0]': str(
                        self.ten_forty_pensions_annuities.get()),
                    'topmostSubform[0].Page1[0].Line4a-11_ReadOrder[0].f1_48[0]': str(
                        self.ten_forty_taxable_pensions.get()),
                    'topmostSubform[0].Page1[0].Line4a-11_ReadOrder[0].f1_49[0]': str(
                        self.ten_forty_social_security.get()),
                    'topmostSubform[0].Page1[0].Line4a-11_ReadOrder[0].f1_50[0]': str(
                        self.ten_forty_social_taxable.get()),
                    'topmostSubform[0].Page1[0].Line4a-11_ReadOrder[0].f1_51[0]': str(
                        self.ten_forty_capital_gain.get()),
                    'topmostSubform[0].Page1[0].Line4a-11_ReadOrder[0].f1_52[0]': str(self.ten_forty_schedule_1.get()),
                    'topmostSubform[0].Page1[0].Line4a-11_ReadOrder[0].f1_53[0]': str(
                        self.ten_forty_total_income.get()),
                    'topmostSubform[0].Page1[0].Line4a-11_ReadOrder[0].f1_54[0]': str(
                        self.ten_forty_income_adjustments.get()),
                    'topmostSubform[0].Page1[0].Line4a-11_ReadOrder[0].f1_55[0]': str(
                        self.ten_forty_adjusted_income.get()),
                    'topmostSubform[0].Page1[0].f1_56[0]': str(self.ten_forty_deductions.get()),
                    'topmostSubform[0].Page1[0].f1_57[0]': str(self.ten_forty_business_deductions.get()),
                    'topmostSubform[0].Page1[0].f1_58[0]': str(self.ten_forty_total_deductions.get()),
                    'topmostSubform[0].Page1[0].f1_59[0]': str(self.ten_forty_taxable_income.get())
                }

                save_as_1040_field_values_mixing_2 = {
                    'topmostSubform[0].Page2[0].f2_01[0]': str(self.ten_forty_other_form_no.get()),
                    'topmostSubform[0].Page2[0].f2_02[0]': str(self.ten_forty_other_form_total.get()),
                    'topmostSubform[0].Page2[0].f2_03[0]': str(self.ten_forty_schedule_2.get()),
                    'topmostSubform[0].Page2[0].f2_04[0]': str(self.ten_forty_add_16_17.get()),
                    'topmostSubform[0].Page2[0].f2_05[0]': str(self.ten_forty_child_credit.get()),
                    'topmostSubform[0].Page2[0].f2_06[0]': str(self.ten_forty_schedule_3.get()),
                    'topmostSubform[0].Page2[0].f2_07[0]': str(self.ten_forty_add_19_20.get()),
                    'topmostSubform[0].Page2[0].f2_08[0]': str(self.ten_forty_sub_21_18.get()),
                    'topmostSubform[0].Page2[0].f2_09[0]': str(self.ten_forty_other_taxes.get()),
                    'topmostSubform[0].Page2[0].f2_10[0]': str(self.ten_forty_total_tax.get()),
                    'topmostSubform[0].Page2[0].f2_11[0]': str(self.ten_forty_withheld_w2.get()),
                    'topmostSubform[0].Page2[0].f2_12[0]': str(self.ten_forty_withheld_1099.get()),
                    'topmostSubform[0].Page2[0].f2_13[0]': str(self.ten_forty_withheld_other.get()),
                    'topmostSubform[0].Page2[0].f2_14[0]': str(self.ten_forty_withheld_total.get()),
                    'topmostSubform[0].Page2[0].f2_15[0]': str(self.ten_forty_previous_year.get()),
                    'topmostSubform[0].Page2[0].f2_16[0]': str(self.ten_forty_eic.get()),
                    'topmostSubform[0].Page2[0].f2_17[0]': str(self.ten_forty_8812_child_credit.get()),
                    'topmostSubform[0].Page2[0].f2_18[0]': str(self.ten_forty_8863_opportunity_credit.get()),
                    'topmostSubform[0].Page2[0].f2_20[0]': str(self.ten_forty_schedule_3_line_15.get()),
                    'topmostSubform[0].Page2[0].f2_21[0]': str(self.ten_forty_other_payments.get()),
                    'topmostSubform[0].Page2[0].f2_22[0]': str(self.ten_forty_total_payments.get()),
                    'topmostSubform[0].Page2[0].f2_23[0]': str(self.ten_forty_overpaid.get()),
                    'topmostSubform[0].Page2[0].f2_28[0]': str(self.ten_forty_owed.get()),
                    'topmostSubform[0].Page2[0].f2_29[0]': str(self.ten_forty_penalty.get())
                }

                ten_forty_checkboxes = {'topmostSubform[0].Page1[0].c1_1[0]': self.ten_forty_presidential_you,
                                        'topmostSubform[0].Page1[0].c1_2[0]': self.ten_forty_presidential_spouse,
                                        'topmostSubform[0].Page1[0].c1_3[0]': self.ten_forty_filing_single,
                                        'topmostSubform[0].Page1[0].c1_3[1]': self.ten_forty_filing_hoh,
                                        'topmostSubform[0].Page1[0].c1_3[2]': self.ten_forty_filing_jointly,
                                        'topmostSubform[0].Page1[0].c1_3[3]': self.ten_forty_filing_separately,
                                        'topmostSubform[0].Page1[0].c1_3[4]': self.ten_forty_filing_qss,
                                        'topmostSubform[0].Page1[0].c1_4[0]': self.ten_forty_digital_assets_yes,
                                        'topmostSubform[0].Page1[0].c1_4[1]': self.ten_forty_digital_assets_no,
                                        'topmostSubform[0].Page1[0].c1_5[0]': self.ten_forty_are_dependent,
                                        'topmostSubform[0].Page1[0].c1_6[0]': self.ten_forty_spouse_dependent,
                                        'topmostSubform[0].Page1[0].c1_7[0]': self.ten_forty_spouse_separate,
                                        'topmostSubform[0].Page1[0].c1_8[0]': self.ten_forty_self_1959,
                                        'topmostSubform[0].Page1[0].c1_9[0]': self.ten_forty_self_blind,
                                        'topmostSubform[0].Page1[0].c1_10[0]': self.ten_forty_spouse_1959,
                                        'topmostSubform[0].Page1[0].c1_11[0]': self.ten_forty_spouse_blind,
                                        'topmostSubform[0].Page1[0].c1_12[0]': self.ten_forty_many_dependents,
                                        'topmostSubform[0].Page1[0].Table_Dependents[0].Row1[0].c1_13[0]':
                                            self.ten_forty_dependent_1_child_credit,
                                        'topmostSubform[0].Page1[0].Table_Dependents[0].Row1[0].c1_14[0]':
                                            self.ten_forty_dependent_1_other_credit,
                                        'topmostSubform[0].Page1[0].Table_Dependents[0].Row2[0].c1_15[0]':
                                            self.ten_forty_dependent_2_child_credit,
                                        'topmostSubform[0].Page1[0].Table_Dependents[0].Row2[0].c1_16[0]':
                                            self.ten_forty_dependent_2_other_credit,
                                        'topmostSubform[0].Page1[0].Table_Dependents[0].Row3[0].c1_17[0]':
                                            self.ten_forty_dependent_3_child_credit,
                                        'topmostSubform[0].Page1[0].Table_Dependents[0].Row3[0].c1_18[0]':
                                            self.ten_forty_dependent_3_other_credit,
                                        'topmostSubform[0].Page1[0].Table_Dependents[0].Row4[0].c1_19[0]':
                                            self.ten_forty_dependent_4_child_credit,
                                        'topmostSubform[0].Page1[0].Table_Dependents[0].Row4[0].c1_20[0]':
                                            self.ten_forty_dependent_4_other_credit,
                                        'topmostSubform[0].Page1[0].Line4a-11_ReadOrder[0].c1_21[0]':
                                            self.ten_forty_lump_sum_method,
                                        'topmostSubform[0].Page1[0].Line4a-11_ReadOrder[0].c1_22[0]':
                                            self.ten_forty_schedule_d,
                                        'topmostSubform[0].Page2[0].c2_1[0]': self.ten_forty_8814,
                                        'topmostSubform[0].Page2[0].c2_2[0]': self.ten_forty_4972,
                                        'topmostSubform[0].Page2[0].c2_3[0]': self.ten_forty_other_form_check,
                                        'topmostSubform[0].Page2[0].c2_4[0]': self.ten_forty_8888,
                                        'topmostSubform[0].Page2[0].c2_5[0]': self.ten_forty_route_checking,
                                        'topmostSubform[0].Page2[0].c2_5[1]': self.ten_forty_route_savings,
                                        'topmostSubform[0].Page2[0].c2_6[0]': self.ten_forty_third_party_yes,
                                        'topmostSubform[0].Page2[0].c2_6[1]': self.ten_forty_third_party_no,
                                        'topmostSubform[0].Page2[0].c2_7[0]': self.ten_forty_self_employed}

                # Iteration for each page
                for each_page in pdf:
                    widgets = each_page.widgets()
                    for content in widgets:
                        for field_name, value in ten_forty_checkboxes.items():
                            if content.field_name == field_name:
                                if value == "":
                                    content.field_value = " "
                                if value.get() == 1:
                                    content.field_value = True
                                else:
                                    content.field_value = value
                                content.update()

                # Saving the modified PDF
                pdf.save(output_pdf)

                # Iteration for each page
                for each_page in pdf:
                    widgets = each_page.widgets()
                    for content in widgets:
                        for field_name, value in {**save_as_1040_field_values_mixing,
                                                  **save_as_1040_field_values_mixing_2}.items():
                            if content.field_name == field_name:
                                if value == "":
                                    content.field_value = " "
                                else:
                                    content.field_value = value
                                content.update()

                # Saving the modified PDF
                pdf.save(output_pdf)
                pdf.close()

            # Input and output PDF filenames
            input_pdf_file = "default_f1040.pdf"
            output_pdf_file = os.path.splitext(filename)[0] + ".pdf"

            # Updating of widget values and saving the modified PDF
            update_widget_values_1040(input_pdf_file, output_pdf_file)
            print(f"Modified PDF saved as {output_pdf_file}")

    # Browse 1040

    def browse_form_1040(self):
        """
           Opens a file explorer to select a pdf file containing tax information.
           Assigns data accordingly.
        """
        filename = filedialog.askopenfilename(initialdir="/", title="Open", filetypes=(("PDF Files", "*.pdf"),))
        if filename:
            self.update_input_fields_1040(filename)

    def update_input_fields_1040(self, input_pdf):
        """
            Updates entry widgets with field values extracted from a PDF.

            Details:
                - The code iterates through each page in the PDF.
                - For each page, it retrieves the widgets (form fields).
                - It then checks if the field name matches any of the specified entry widgets.
                - If a match is found and the field value is not empty, it updates the corresponding entry widget
        """
        # Opening the input PDF
        pdf = fitz.open(input_pdf)
        browse_1040_field_values_mixing = {
            'topmostSubform[0].Page1[0].f1_04[0]': self.ten_forty_first_name,
            'topmostSubform[0].Page1[0].f1_05[0]': self.ten_forty_last_name,
            'topmostSubform[0].Page1[0].f1_07[0]': self.ten_forty_spouse_first,
            'topmostSubform[0].Page1[0].f1_08[0]': self.ten_forty_spouse_last,
            'topmostSubform[0].Page1[0].Address_ReadOrder[0].f1_10[0]': self.ten_forty_home_address,
            'topmostSubform[0].Page1[0].Address_ReadOrder[0].f1_11[0]': self.ten_forty_apt_no,
            'topmostSubform[0].Page1[0].Address_ReadOrder[0].f1_12[0]': self.ten_forty_city,
            'topmostSubform[0].Page1[0].Address_ReadOrder[0].f1_13[0]': self.ten_forty_state,
            'topmostSubform[0].Page1[0].Address_ReadOrder[0].f1_14[0]': self.ten_forty_zip,
            'topmostSubform[0].Page1[0].Address_ReadOrder[0].f1_15[0]': self.ten_forty_foreign_country,
            'topmostSubform[0].Page1[0].Address_ReadOrder[0].f1_16[0]': self.ten_forty_foreign_province,
            'topmostSubform[0].Page1[0].Address_ReadOrder[0].f1_17[0]': self.ten_forty_foreign_post_code,
            'topmostSubform[0].Page1[0].Table_Dependents[0].Row1[0].f1_19[0]': self.ten_forty_dependent_first_1,
            'topmostSubform[0].Page1[0].Table_Dependents[0].Row2[0].f1_22[0]': self.ten_forty_dependent_first_2,
            'topmostSubform[0].Page1[0].Table_Dependents[0].Row3[0].f1_25[0]': self.ten_forty_dependent_first_3,
            'topmostSubform[0].Page1[0].Table_Dependents[0].Row4[0].f1_28[0]': self.ten_forty_dependent_first_4,
            'topmostSubform[0].Page1[0].f1_31[0]': self.ten_forty_total_w2s,
            'topmostSubform[0].Page1[0].f1_32[0]': self.ten_forty_household_wages,
            'topmostSubform[0].Page1[0].f1_33[0]': self.ten_forty_tip_income,
            'topmostSubform[0].Page1[0].f1_34[0]': self.ten_forty_medicaid_waiver,
            'topmostSubform[0].Page1[0].f1_35[0]': self.ten_forty_dependent_benefits,
            'topmostSubform[0].Page1[0].f1_36[0]': self.ten_forty_adoption_benefits,
            'topmostSubform[0].Page1[0].f1_37[0]': self.ten_forty_8919_wages,
            'topmostSubform[0].Page1[0].f1_38[0]': self.ten_forty_other_income,
            'topmostSubform[0].Page1[0].f1_39[0]': self.ten_forty_combat_pay,
            'topmostSubform[0].Page1[0].f1_40[0]': self.ten_forty_1_ah_sum,
            'topmostSubform[0].Page1[0].f1_41[0]': self.ten_forty_tax_exempt_interest,
            'topmostSubform[0].Page1[0].f1_42[0]': self.ten_forty_taxable_interest,
            'topmostSubform[0].Page1[0].f1_43[0]': self.ten_forty_qualified_dividends,
            'topmostSubform[0].Page1[0].f1_44[0]': self.ten_forty_ordinary_dividends,
            'topmostSubform[0].Page1[0].Line4a-11_ReadOrder[0].f1_45[0]': self.ten_forty_ira_distributions,
            'topmostSubform[0].Page1[0].Line4a-11_ReadOrder[0].f1_46[0]': self.ten_forty_taxable_ira,
            'topmostSubform[0].Page1[0].Line4a-11_ReadOrder[0].f1_47[0]': self.ten_forty_pensions_annuities,
            'topmostSubform[0].Page1[0].Line4a-11_ReadOrder[0].f1_48[0]': self.ten_forty_taxable_pensions,
            'topmostSubform[0].Page1[0].Line4a-11_ReadOrder[0].f1_49[0]': self.ten_forty_social_security,
            'topmostSubform[0].Page1[0].Line4a-11_ReadOrder[0].f1_50[0]': self.ten_forty_social_taxable,
            'topmostSubform[0].Page1[0].Line4a-11_ReadOrder[0].f1_51[0]': self.ten_forty_capital_gain,
            'topmostSubform[0].Page1[0].Line4a-11_ReadOrder[0].f1_52[0]': self.ten_forty_schedule_1,
            'topmostSubform[0].Page1[0].Line4a-11_ReadOrder[0].f1_53[0]': self.ten_forty_total_income,
            'topmostSubform[0].Page1[0].Line4a-11_ReadOrder[0].f1_54[0]': self.ten_forty_income_adjustments,
            'topmostSubform[0].Page1[0].Line4a-11_ReadOrder[0].f1_55[0]': self.ten_forty_adjusted_income,
            'topmostSubform[0].Page1[0].f1_56[0]': self.ten_forty_deductions,
            'topmostSubform[0].Page1[0].f1_57[0]': self.ten_forty_business_deductions,
            'topmostSubform[0].Page1[0].f1_58[0]': self.ten_forty_total_deductions,
            'topmostSubform[0].Page1[0].f1_59[0]': self.ten_forty_taxable_income
        }

        browse_1040_field_values_mixing_2 = {
            'topmostSubform[0].Page2[0].f2_01[0]': self.ten_forty_other_form_no,
            'topmostSubform[0].Page2[0].f2_02[0]': self.ten_forty_other_form_total,
            'topmostSubform[0].Page2[0].f2_03[0]': self.ten_forty_schedule_2,
            'topmostSubform[0].Page2[0].f2_04[0]': self.ten_forty_add_16_17,
            'topmostSubform[0].Page2[0].f2_05[0]': self.ten_forty_child_credit,
            'topmostSubform[0].Page2[0].f2_06[0]': self.ten_forty_schedule_3,
            'topmostSubform[0].Page2[0].f2_07[0]': self.ten_forty_add_19_20,
            'topmostSubform[0].Page2[0].f2_08[0]': self.ten_forty_sub_21_18,
            'topmostSubform[0].Page2[0].f2_09[0]': self.ten_forty_other_taxes,
            'topmostSubform[0].Page2[0].f2_10[0]': self.ten_forty_total_tax,
            'topmostSubform[0].Page2[0].f2_11[0]': self.ten_forty_withheld_w2,
            'topmostSubform[0].Page2[0].f2_12[0]': self.ten_forty_withheld_1099,
            'topmostSubform[0].Page2[0].f2_13[0]': self.ten_forty_withheld_other,
            'topmostSubform[0].Page2[0].f2_14[0]': self.ten_forty_withheld_total,
            'topmostSubform[0].Page2[0].f2_15[0]': self.ten_forty_previous_year,
            'topmostSubform[0].Page2[0].f2_16[0]': self.ten_forty_eic,
            'topmostSubform[0].Page2[0].f2_17[0]': self.ten_forty_8812_child_credit,
            'topmostSubform[0].Page2[0].f2_18[0]': self.ten_forty_8863_opportunity_credit,
            'topmostSubform[0].Page2[0].f2_20[0]': self.ten_forty_schedule_3_line_15,
            'topmostSubform[0].Page2[0].f2_21[0]': self.ten_forty_other_payments,
            'topmostSubform[0].Page2[0].f2_22[0]': self.ten_forty_total_payments,
            'topmostSubform[0].Page2[0].f2_23[0]': self.ten_forty_overpaid,
            'topmostSubform[0].Page2[0].f2_28[0]': self.ten_forty_owed,
            'topmostSubform[0].Page2[0].f2_29[0]': self.ten_forty_penalty
        }

        ten_forty_checkboxes = {'c1_1[0]': self.ten_forty_presidential_you,
                                'c1_2[0]': self.ten_forty_presidential_spouse, 'c1_3[0]': self.ten_forty_filing_single,
                                'c1_3[1]': self.ten_forty_filing_hoh,
                                'c1_3[2]': self.ten_forty_filing_jointly, 'c1_3[3]': self.ten_forty_filing_separately,
                                'c1_3[4]': self.ten_forty_filing_qss, 'c1_4[0]': self.ten_forty_digital_assets_yes,
                                'c1_4[1]': self.ten_forty_digital_assets_no, 'c1_5[0]': self.ten_forty_are_dependent,
                                'c1_6[0]': self.ten_forty_spouse_dependent, 'c1_7[0]': self.ten_forty_spouse_separate,
                                'c1_8[0]': self.ten_forty_self_1959, 'c1_9[0]': self.ten_forty_self_blind,
                                'c1_10[0]': self.ten_forty_spouse_1959, 'c1_11[0]': self.ten_forty_spouse_blind,
                                'Dependents_ReadOrder[0]': self.ten_forty_many_dependents,
                                'c1_13[0]': self.ten_forty_dependent_1_child_credit,
                                'c1_14[0]': self.ten_forty_dependent_1_other_credit,
                                'c1_15[0]': self.ten_forty_dependent_2_child_credit,
                                'c1_16[0]': self.ten_forty_dependent_2_other_credit,
                                'c1_17[0]': self.ten_forty_dependent_3_child_credit,
                                'c1_18[0]': self.ten_forty_dependent_3_other_credit,
                                'c1_19[0]': self.ten_forty_dependent_4_child_credit,
                                'c1_20[0]': self.ten_forty_dependent_4_other_credit,
                                'c1_21[0]': self.ten_forty_lump_sum_method, 'c1_22[0]': self.ten_forty_schedule_d,
                                'c2_1[0]': self.ten_forty_8814,
                                'c2_2[0]': self.ten_forty_4972, 'c2_3[0]': self.ten_forty_other_form_check,
                                'c2_4[0]': self.ten_forty_8888,
                                'c2_5[0]': self.ten_forty_route_checking,
                                'c2_5[1]': self.ten_forty_route_savings,
                                'c2_6[0]': self.ten_forty_third_party_yes,
                                'c2_6[1]': self.ten_forty_third_party_no,
                                'c2_7[0]': self.ten_forty_self_employed}

        def extract_checkbox_values(pdf):
            """
                Extracts checkbox values from a PDF form.

                Args:
                    pdf (str): Path to the input PDF file.

                Returns:
                    dict: A dictionary containing checkbox field names as keys and boolean values
                          indicating whether the checkbox is checked (True) or not (False).
            """
            pdf_reader = PdfReader(pdf)
            pdf_fields = pdf_reader.get_fields()

            # dictionary creation
            checkbox_values = {}

            # Extract checkbox values
            for field_name, field_value in pdf_fields.items():
                if field_value.get("/FT") == "/Btn":
                    # retrieving the field name
                    clean_field_name = field_name.lstrip("/")
                    # Checking if the checkbox is checked
                    is_checked = field_value.get("/V") == "/1"
                    is_checked2 = field_value.get("/V") == "/2"
                    is_checked3 = field_value.get("/V") == "/3"
                    is_checked4 = field_value.get("/V") == "/4"
                    is_checked5 = field_value.get("/V") == "/5"
                    checkbox_values[
                        clean_field_name] = is_checked or is_checked2 or is_checked3 or is_checked4 or is_checked5

            return checkbox_values

        checkbox_values = extract_checkbox_values(input_pdf)

        for checkbox_name, entry_widget in ten_forty_checkboxes.items():
            if checkbox_name in checkbox_values:
                if checkbox_values[checkbox_name]:
                    # select entry widget
                    entry_widget.select()

                else:
                    # deselect entry widget
                    entry_widget.deselect()

        for each_page in pdf:
            widgets = each_page.widgets()
            for content in widgets:
                for field_name, entry_widget in {**browse_1040_field_values_mixing,
                                                 **browse_1040_field_values_mixing_2}.items():
                    if content.field_name == field_name:

                        value = content.field_value.strip()
                        if value != "":
                            entry_widget.delete(0, tk.END)  # Clear text
                            entry_widget.insert(0, value)  # Set value
        pdf.close()

    ###################################################################################################################
    def save_session(self):

        self.cursor.execute('INSERT INTO jk (essn,'
                            'ein,'
                            'employer_name_etc,'
                            'control_number,'
                            'employee_first_i,'
                            'employee_last,'
                            'employee_suffix,'
                            'employee_address_z,'
                            'state,'
                            'employers_state_id,'
                            'state_wages_tips_etc,'
                            'state_income_tax,'
                            'local_wages_tips_etc,'
                            'local_income_tax,'
                            'locality_name,'
                            'wages_tips_other_compensation,'
                            'social_security_wages,'
                            'medicare_wages_tips,'
                            'social_security_tips,'
                            'non_qualified_plans,'
                            'other,'
                            'federal_income_tax_withheld,'
                            'social_security_tax_withheld,'
                            'medicare_tax_withheld,'
                            'allocated_tips,'
                            'dependent_care_benefits,'
                            'twelve_a,'
                            'twelve_b,'
                            'twelve_c,'
                            'twelve_d,'

                            'ten_ninety_nine_payers_name_etc,'
                            'ten_ninety_nine_payers_tin,'
                            'ten_ninety_nine_recipients_tin,'
                            'ten_ninety_nine_recipients_name,'
                            'ten_ninety_nine_street_address,'
                            'ten_ninety_nine_city_town_etc,'
                            'ten_ninety_nine_account_number,'
                            'ten_ninety_nine_total_ordinary_dividends,'
                            'ten_ninety_nine_qualified_dividends,'
                            'ten_ninety_nine_total_capital_gain_dist,'
                            'ten_ninety_nine_section_1202_gain,'
                            'ten_ninety_nine_section_897_ordinary_dividends,'
                            'ten_ninety_nine_non_dividend_distributions,'
                            'ten_ninety_nine_section_199A_dividends,'
                            'ten_ninety_nine_foreign_tax_paid,'
                            'ten_ninety_nine_cash_liquidation_distributions,'
                            'ten_ninety_nine_exempt_interest_dividends,'
                            'ten_ninety_nine_state,'
                            'ten_ninety_nine_state_identification_no,'
                            'ten_ninety_nine_un_recap_sec_1250_gain,'
                            'ten_ninety_nine_collectibles_28_percent_gain,'
                            'ten_ninety_nine_section_897_capital_gain,'
                            'ten_ninety_nine_federal_income_tax_withheld,'
                            'ten_ninety_nine_investment_expenses,'
                            'ten_ninety_nine_foreign_country_or_us_possession,'
                            'ten_ninety_nine_non_cash_liquidation_distributions,'
                            'ten_ninety_nine_specified_private_activity_bond_interest_dividends,'
                            'ten_ninety_nine_state_tax_withheld,'


                            'ten_forty_your_first_name_and_middle_initial,'
                            'ten_forty_your_last_name,'
                            'ten_forty_if_joint_return_spouses_first_name_and_middle_initial,'
                            'ten_forty_if_joint_last_name,'
                            'ten_forty_home_address_number_and_street,'
                            'ten_forty_apt_no,'
                            'ten_forty_city_town_or_post_office,'
                            'ten_forty_state,'
                            'ten_forty_zip_code,'
                            'ten_forty_foreign_country_name,'
                            'ten_forty_foreign_province_state_county,'
                            'ten_forty_foreign_postal_code,'

                            'ten_forty_dependents_first_name_1,'
                            'ten_forty_dependents_first_name_2,'
                            'ten_forty_dependents_first_name_3,'
                            'ten_forty_dependents_first_name_4,'

                            'ten_forty_total_amount_from_forms_w2_box_1,'
                            'ten_forty_household_employee_wages_not_reported_on_forms_w2,'
                            'ten_forty_tip_income_not_reported_on_line_1a,'
                            'ten_forty_medicaid_waiver_payments_not_reported_on_forms_w2,'
                            'ten_forty_taxable_dependent_care_benefits_from_form_2441_line_26,'
                            'ten_forty_employer_provided_adoption_benefits_from_form_8839_line_29,'
                            'ten_forty_wages_from_form_8919_line_6,'
                            'ten_forty_other_earned_income,'
                            'ten_forty_non_taxable_combat_pay_election,'
                            'ten_forty_add_lines_1a_through_1h,'
                            'ten_forty_tax_exempt_interest,'

                            'ten_forty_taxable_interest,'
                            'ten_forty_qualified_dividends,'
                            'ten_forty_ordinary_dividends,'
                            'ten_forty_ira_distributions,'
                            'ten_forty_taxable_amount_4b,'
                            'ten_forty_pensions_and_annuities,'
                            'ten_forty_taxable_amount_5b,'
                            'ten_forty_social_security_benefits,'
                            'ten_forty_taxable_amount_6b,'

                            'ten_forty_capital_gain_or_loss_attach_schedule_d_if_required,'
                            'ten_forty_additional_income_from_schedule_1_line_10,'
                            'ten_forty_add_lines_1z_2b_3b_4b_5b_6b_7_8_this_is_your_total_income,'
                            'ten_forty_adjustments_to_income_from_schedule_1_line_26,'
                            'ten_forty_subtract_line_10_from_line_9_this_is_your_adjusted_gross_income,'
                            'ten_forty_standard_deduction_or_itemized_deductions_from_schedule_a,'
                            'ten_forty_qualified_business_income_deduction_from_form_8995_or_form_8995_a,'
                            'ten_forty_add_lines_12_and_13,'
                            'ten_forty_subtract_line_14_from_line_11_if_zero_or_less_enter_'
                            '0_this_is_your_taxable_income,'

                            'ten_forty_form_no,'
                            'ten_forty_tax_check_if_any_from_forms,'
                            'ten_forty_amount_from_schedule_2_line_3,'
                            'ten_forty_add_lines_16_and_17,'
                            'ten_forty_child_tax_credit_or_credit_for_other_dependents_from_schedule_8812,'
                            'ten_forty_amount_from_schedule_3_line_8,'
                            'ten_forty_add_lines_19_and_20,'
                            'ten_forty_subtract_line_21_from_line_18_if_zero_or_less_enter_0,'
                            'ten_forty_other_taxes_including_self_employment_tax_from_schedule_2_line_21,'
                            'ten_forty_add_lines_22_and_23_this_is_your_total_tax,'
                            'ten_forty_forms_w2,'
                            'ten_forty_forms_1099,'
                            'ten_forty_other_forms,'
                            'ten_forty_add_lines_25a_through_25c,'
                            'ten_forty_2023_estimated_tax_payments_and_amount_applied_from_2022_return,'
                            'ten_forty_earned_income_credit,'
                            'ten_forty_additional_child_tax_credit_from_schedule_8812,'
                            'ten_forty_american_opportunity_credit_from_form_8863_line_8,'
                            'ten_forty_amount_from_schedule_3_line_15,'
                            'ten_forty_add_lines_27_28_29_31_these_are_your_total_other_payments_refundable_credits,'
                            'ten_forty_add_lines_25d_26_32_these_are_your_total_payments,'
                            'ten_forty_if_line_33_is_more_than_line_24_subtract_line_24_'
                            'from_line_33_this_is_the_amount_you_overpaid,'
                            'ten_forty_subtract_line_33_from_line_24_this_is_the_amount_you_owe,'
                            'ten_forty_estimated_tax_penalty,'

                            'user_id) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,'
                            ' ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,'
                            ' ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, '
                            '?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, '
                            '?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, '
                            '?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, '
                            '?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, '
                            '?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',
                            [field.get() for field in self.all_fields])

        self.cursor.execute("""UPDATE jk SET essn = ?,
                                    ein = ?,
                                    employer_name_etc = ?,
                                    control_number = ?,
                                    employee_first_i = ?,
                                    employee_last = ?,
                                    employee_suffix = ?,
                                    employee_address_z = ?,
                                    state = ?,
                                    employers_state_id = ?,
                                    state_wages_tips_etc = ?,
                                    state_income_tax = ?,
                                    local_wages_tips_etc = ?,
                                    local_income_tax = ?,
                                    locality_name = ?,
                                    wages_tips_other_compensation = ?,
                                    social_security_wages = ?,
                                    medicare_wages_tips = ?,
                                    social_security_tips = ?,
                                    non_qualified_plans = ?,
                                    other = ?,
                                    federal_income_tax_withheld = ?,
                                    social_security_tax_withheld = ?,
                                    medicare_tax_withheld = ?,
                                    allocated_tips = ?,
                                    dependent_care_benefits = ?,
                                    twelve_a = ?,
                                    twelve_b = ?,
                                    twelve_c = ?,
                                    twelve_d = ?,

                                    ten_ninety_nine_payers_name_etc = ?,
                                    ten_ninety_nine_payers_tin = ?,
                                    ten_ninety_nine_recipients_tin = ?,
                                    ten_ninety_nine_recipients_name = ?,
                                    ten_ninety_nine_street_address = ?,
                                    ten_ninety_nine_city_town_etc = ?,
                                    ten_ninety_nine_account_number = ?,
                                    ten_ninety_nine_total_ordinary_dividends = ?,
                                    ten_ninety_nine_qualified_dividends = ?,
                                    ten_ninety_nine_total_capital_gain_dist = ?,
                                    ten_ninety_nine_section_1202_gain = ?,
                                    ten_ninety_nine_section_897_ordinary_dividends = ?,
                                    ten_ninety_nine_non_dividend_distributions = ?,
                                    ten_ninety_nine_section_199A_dividends = ?,
                                    ten_ninety_nine_foreign_tax_paid = ?,
                                    ten_ninety_nine_cash_liquidation_distributions = ?,
                                    ten_ninety_nine_exempt_interest_dividends = ?,
                                    ten_ninety_nine_state = ?,
                                    ten_ninety_nine_state_identification_no = ?,
                                    ten_ninety_nine_un_recap_sec_1250_gain = ?,
                                    ten_ninety_nine_collectibles_28_percent_gain = ?,
                                    ten_ninety_nine_section_897_capital_gain = ?,
                                    ten_ninety_nine_federal_income_tax_withheld = ?,
                                    ten_ninety_nine_investment_expenses = ?,
                                    ten_ninety_nine_foreign_country_or_us_possession = ?,
                                    ten_ninety_nine_non_cash_liquidation_distributions = ?,
                                    ten_ninety_nine_specified_private_activity_bond_interest_dividends = ?,
                                    ten_ninety_nine_state_tax_withheld = ?,


                                    ten_forty_your_first_name_and_middle_initial = ?,
                                    ten_forty_your_last_name = ?,
                                    ten_forty_if_joint_return_spouses_first_name_and_middle_initial = ?,
                                    ten_forty_if_joint_last_name = ?,
                                    ten_forty_home_address_number_and_street = ?,
                                    ten_forty_apt_no = ?,
                                    ten_forty_city_town_or_post_office = ?,
                                    ten_forty_state = ?,
                                    ten_forty_zip_code = ?,
                                    ten_forty_foreign_country_name = ?,
                                    ten_forty_foreign_province_state_county = ?,
                                    ten_forty_foreign_postal_code = ?,

                                    ten_forty_dependents_first_name_1 = ?,
                                    ten_forty_dependents_first_name_2 = ?,
                                    ten_forty_dependents_first_name_3 = ?,
                                    ten_forty_dependents_first_name_4 = ?,

                                    ten_forty_total_amount_from_forms_w2_box_1 = ?,
                                    ten_forty_household_employee_wages_not_reported_on_forms_w2 = ?,
                                    ten_forty_tip_income_not_reported_on_line_1a = ?,
                                    ten_forty_medicaid_waiver_payments_not_reported_on_forms_w2 = ?,
                                    ten_forty_taxable_dependent_care_benefits_from_form_2441_line_26 = ?,
                                    ten_forty_employer_provided_adoption_benefits_from_form_8839_line_29 = ?,
                                    ten_forty_wages_from_form_8919_line_6 = ?,
                                    ten_forty_other_earned_income = ?,
                                    ten_forty_non_taxable_combat_pay_election = ?,
                                    ten_forty_add_lines_1a_through_1h = ?,
                                    ten_forty_tax_exempt_interest = ?,

                                    ten_forty_taxable_interest = ?,
                                    ten_forty_qualified_dividends = ?,
                                    ten_forty_ordinary_dividends = ?,
                                    ten_forty_ira_distributions = ?,
                                    ten_forty_taxable_amount_4b = ?,
                                    ten_forty_pensions_and_annuities = ?,
                                    ten_forty_taxable_amount_5b = ?,
                                    ten_forty_social_security_benefits = ?,
                                    ten_forty_taxable_amount_6b = ?,

                                    ten_forty_capital_gain_or_loss_attach_schedule_d_if_required = ?,
                                    ten_forty_additional_income_from_schedule_1_line_10 = ?,
                                    ten_forty_add_lines_1z_2b_3b_4b_5b_6b_7_8_this_is_your_total_income = ?,
                                    ten_forty_adjustments_to_income_from_schedule_1_line_26 = ?,
                                    ten_forty_subtract_line_10_from_line_9_this_is_your_adjusted_gross_income = ?,
                                    ten_forty_standard_deduction_or_itemized_deductions_from_schedule_a = ?,
                                    ten_forty_qualified_business_income_deduction_from_form_8995_or_form_8995_a = ?,
                                    ten_forty_add_lines_12_and_13 = ?,
                                    ten_forty_subtract_line_14_from_line_11_if_zero_or_less_enter_0_this_is_your_taxable_income = ?,

                                    ten_forty_form_no = ?,
                                    ten_forty_tax_check_if_any_from_forms = ?,
                                    ten_forty_amount_from_schedule_2_line_3 = ?,
                                    ten_forty_add_lines_16_and_17 = ?,
                                    ten_forty_child_tax_credit_or_credit_for_other_dependents_from_schedule_8812 = ?,
                                    ten_forty_amount_from_schedule_3_line_8 = ?,
                                    ten_forty_add_lines_19_and_20 = ?,
                                    ten_forty_subtract_line_21_from_line_18_if_zero_or_less_enter_0 = ?,
                                    ten_forty_other_taxes_including_self_employment_tax_from_schedule_2_line_21 = ?,
                                    ten_forty_add_lines_22_and_23_this_is_your_total_tax = ?,
                                    ten_forty_forms_w2 = ?,
                                    ten_forty_forms_1099 = ?,
                                    ten_forty_other_forms = ?,
                                    ten_forty_add_lines_25a_through_25c = ?,
                                    ten_forty_2023_estimated_tax_payments_and_amount_applied_from_2022_return = ?,
                                    ten_forty_earned_income_credit = ?,
                                    ten_forty_additional_child_tax_credit_from_schedule_8812 = ?,
                                    ten_forty_american_opportunity_credit_from_form_8863_line_8 = ?,
                                    ten_forty_amount_from_schedule_3_line_15 = ?,
                                    ten_forty_add_lines_27_28_29_31_these_are_your_total_other_payments_refundable_credits = ?,
                                    ten_forty_add_lines_25d_26_32_these_are_your_total_payments = ?,
                                    ten_forty_if_line_33_is_more_than_line_24_subtract_line_24_from_line_33_this_is_the_amount_you_overpaid = ?,
                                    ten_forty_subtract_line_33_from_line_24_this_is_the_amount_you_owe = ?,
                                    ten_forty_estimated_tax_penalty = ?

                                    WHERE user_id = ?""",
                            [field.get() for field in self.all_fields])
        self.cursor.execute('INSERT INTO checks (ten_forty_presidential_you,'
                            'ten_forty_presidential_spouse,'
                            'ten_forty_filing_single,'
                            'ten_forty_filing_jointly,'
                            'ten_forty_filing_separately,'
                            'ten_forty_filing_hoh,'
                            'ten_forty_filing_qss,'
                            'ten_forty_digital_assets_yes,'
                            'ten_forty_digital_assets_no,'
                            'ten_forty_are_dependent,'
                            'ten_forty_spouse_dependent,'
                            'ten_forty_spouse_separate,'
                            'ten_forty_self_1959,'
                            'ten_forty_self_blind,'
                            'ten_forty_spouse_1959,'
                            'ten_forty_spouse_blind,'
                            'ten_forty_many_dependents,'
                            'ten_forty_dependent_1_child_credit,'
                            'ten_forty_dependent_1_other_credit,'
                            'ten_forty_dependent_2_child_credit,'
                            'ten_forty_dependent_2_other_credit,'
                            'ten_forty_dependent_3_child_credit,'
                            'ten_forty_dependent_3_other_credit,'
                            'ten_forty_dependent_4_child_credit,'
                            'ten_forty_dependent_4_other_credit,'
                            'ten_forty_schedule_d,'
                            'ten_forty_lump_sum_method,'
                            'ten_forty_8814,'
                            'ten_forty_4972,'
                            'ten_forty_other_form_check,'
                            'ten_forty_8888,'
                            'ten_forty_route_checking,'
                            'ten_forty_route_savings,'
                            'ten_forty_third_party_yes,'
                            'ten_forty_third_party_no,'
                            'ten_forty_self_employed,'
                            'user_password) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,'
                            '?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)',
                            [other_field.get() for other_field in self.other_all_fields])
        self.cursor.execute("""UPDATE checks SET ten_forty_presidential_you = ?,
                                    ten_forty_presidential_spouse = ?,
                                    ten_forty_filing_single = ?,
                                    ten_forty_filing_jointly = ?,
                                    ten_forty_filing_separately = ?,
                                    ten_forty_filing_hoh = ?,
                                    ten_forty_filing_qss = ?,
                                    ten_forty_digital_assets_yes = ?,
                                    ten_forty_digital_assets_no = ?,
                                    ten_forty_are_dependent = ?,
                                    ten_forty_spouse_dependent = ?,
                                    ten_forty_spouse_separate = ?,
                                    ten_forty_self_1959 = ?,
                                    ten_forty_self_blind = ?,
                                    ten_forty_spouse_1959 = ?,
                                    ten_forty_spouse_blind = ?,
                                    ten_forty_many_dependents = ?,
                                    ten_forty_dependent_1_child_credit = ?,
                                    ten_forty_dependent_1_other_credit = ?,
                                    ten_forty_dependent_2_child_credit = ?,
                                    ten_forty_dependent_2_other_credit = ?,
                                    ten_forty_dependent_3_child_credit = ?,
                                    ten_forty_dependent_3_other_credit = ?,
                                    ten_forty_dependent_4_child_credit = ?,
                                    ten_forty_dependent_4_other_credit = ?,
                                    ten_forty_schedule_d = ?,
                                    ten_forty_lump_sum_method = ?,
                                    ten_forty_8814 = ?,
                                    ten_forty_4972 = ?,
                                    ten_forty_other_form_check = ?,
                                    ten_forty_8888 = ?,
                                    ten_forty_route_checking = ?,
                                    ten_forty_route_savings = ?,
                                    ten_forty_third_party_yes = ?,
                                    ten_forty_third_party_no = ?,
                                    ten_forty_self_employed = ?
                                    WHERE user_password = ?""",
                            [other_field.get() for other_field in self.other_all_fields])
        self.user_connect.commit()

    def load_session(self):
        if messagebox.askyesno("Alert", "Upon clicking yes, all fields will be loaded from a database and autosave will be enabled until clicking new or exiting the program. This process may take several minutes"):
            self.auto_save_runner = True

            if self.user_id.get() == "":
                messagebox.showerror('Error', 'Please Enter A Username')
            elif self.user_password.get() == "":
                messagebox.showerror('Error', 'Please Enter A Password')
            else:
                if self.user_id.get() != user_login_info.username:
                    messagebox.showerror('Error', 'Invalid Username. Please Enter Your Username.')
                elif self.user_password.get() != user_login_info.password:
                    messagebox.showerror('Error', 'Invalid Password. Please Enter Your Password.')
                else:
                    self.cursor.execute("SELECT * FROM jk WHERE user_id=?", [user_login_info.username])
                    all_data = self.cursor.fetchall()
                    for i, row in enumerate(all_data):
                        for j, field in enumerate(self.all_fields):
                            field.delete(0, "end")  # Clear the existing content
                            field.insert(0, row[j])  # Insert the value from the database
                    self.cursor.execute("SELECT * FROM checks WHERE user_password=?", [user_login_info.password])
                    all_data2 = self.cursor.fetchall()
                    for x, row2 in enumerate(all_data2):
                        for y, field2 in enumerate(self.other_all_fields):
                            if row2[y] == 1:
                                field2.select()
                            else:
                                try:
                                    field2.deselect()
                                except AttributeError:
                                    continue

                    print("Data loaded from the database.")
                    messagebox.showinfo('Success', 'Loaded Session')
                    self.loaded = "yes"
                    self.auto_save()

    def auto_save(self):
        if self.auto_save_runner:
            # Increment time by 1 second
            self.elapsed_time += 1

            # Check if allotted time has passed
            if self.elapsed_time >= 10:
                print("Auto-Saved Session")
                self.save_session()
                self.elapsed_time = 0  # Resetting counter for next autosave

            # Time next autosave after 1 second
            self.app.after(1000, self.auto_save)

    def main_save(self):
        if messagebox.askyesno("Alert", "Upon clicking yes, all fields will be saved to a database and autosave will be enabled until clicking new or exiting the program."):
            self.auto_save_runner = True
            if self.user_id.get() == "":
                messagebox.showerror('Error', 'Please Enter A Username.')
            elif self.user_password.get() == "":
                messagebox.showerror('Error', 'Please Enter A Password.')
            else:
                if self.user_id.get() != user_login_info.username:
                    messagebox.showerror('Error', 'Invalid Username. Please Enter Your Username.')
                elif self.user_password.get() != user_login_info.password:
                    messagebox.showerror('Error', 'Invalid Password. Please Enter Your Password.')
                else:
                    self.program_run = False
                    self.save_session()
                    messagebox.showinfo("Success", f"Saved Session. Time: {self.current_time_date}")
                    print("Data saved to database.")
                    self.auto_save()

    def send_info_calculate(self):

        if self.calculate_changer == "w2":

            w2_user_validation.validate_essn(self.essn_entry.get())
            w2_user_validation.validate_ein(self.ein_entry.get())
            w2_user_validation.validate_employer_name_etc(self.employer_name_etc.get())
            w2_user_validation.validate_cn(self.cn_entry.get())
            w2_user_validation.validate_employee_name_i(self.employee_name_i.get())
            w2_user_validation.validate_employee_last(self.employee_last_name.get())
            w2_user_validation.validate_employee_address_zip(self.employee_address_etc.get())
            w2_user_validation.validate_state(self.state_field.get())

            w2_user_validation.validate_wages_tips_other_comp(self.wages_tips_c.get())
            w2_user_validation.validate_federal_income_tax_withheld(self.fed_income_tax_withheld.get())
            w2_user_validation.validate_social_security_wages(self.social_wages.get())
            w2_user_validation.validate_social_security_tax(self.social_security_tax_withheld.get())
            w2_user_validation.validate_medicare_wages(self.medicare_wages.get())
            w2_user_validation.validate_medicare_tax(self.medicare_tax_withheld.get())
            w2_user_validation.validate_social_security_tips(self.social_security_tips.get())
            w2_user_validation.validate_allocated_tips(self.allocated_tips.get())
            w2_user_validation.validate_dependant_care_benefits(self.dependent_care_benefits.get())
            w2_user_validation.validate_nonqualified_plans(self.non_qualified_plans.get())
            w2_user_validation.validate_12a(self.twelve_a.get())
            w2_user_validation.validate_12b(self.twelve_b.get())
            w2_user_validation.validate_12c(self.twelve_c.get())
            w2_user_validation.validate_12d(self.twelve_d.get())
            w2_user_validation.validate_state_wages_tips(self.state_wage_tips.get())
            w2_user_validation.validate_state_income_tax(self.state_income_tax.get())
            w2_user_validation.validate_local_income(self.local_wage_tips.get())
            w2_user_validation.validate_local_income_tax(self.local_income_tax.get())

            w2_list = [self.employee_name_i.get(), self.employee_last_name.get(),
                       self.employee_address_etc.get(), self.wages_tips_c.get(),
                       self.fed_income_tax_withheld.get()]

            for w in w2_list:
                if w == "":
                    messagebox.showerror("Error", "Please enter all fields: Employee First Name And Initial, "
                                                  "Employee Last Name, "
                                                  "Employee Address And ZIP, "
                                                  "Wages, Tips, Other Compensation, "
                                                  "Federal Income Tax Withheld")
                    break
                else:
                    self.results_textbox.configure(state="normal")
                    self.results_textbox.delete("1.0", "end")
                    self.results_textbox.insert("end", "Form W-2 Information:")
                    self.results_textbox.insert("end", "\n\n")
                    self.results_textbox.insert("end", f"Employee First Name And Initial: {self.employee_name_i.get()}")
                    self.results_textbox.insert("end", "\n")
                    self.results_textbox.insert("end", f"Employee Last Name: {self.employee_last_name.get()}")
                    self.results_textbox.insert("end", "\n")
                    self.results_textbox.insert("end", f"Employee Address And ZIP: {self.employee_address_etc.get()}")
                    self.results_textbox.insert("end", "\n")
                    self.results_textbox.insert("end", f"Wages, Tips, Other Compensation: {float(self.wages_tips_c.get()):.2f}")
                    self.results_textbox.insert("end", "\n")
                    self.results_textbox.insert("end",
                                                f"Federal Income Tax Withheld: {float(self.fed_income_tax_withheld.get()):.2f}")
                    self.results_textbox.configure(state="disabled")
                    break
        elif self.calculate_changer == "1099":

            ten_99_validation.validate_payer_name_etc(self.ten_ninety_nine_payer_info.get())
            ten_99_validation.validate_payer_tin(self.ten_ninety_nine_payer_tin.get())
            ten_99_validation.validate_recipient_tin(self.ten_ninety_nine_recipient_tin.get())
            ten_99_validation.validate_recipient_name(self.ten_ninety_nine_recipient_name.get())
            ten_99_validation.validate_recipient_address(self.ten_ninety_nine_recipient_address.get())
            ten_99_validation.validate_recipient_city_etc(self.ten_ninety_nine_recipient_city_etc.get())
            ten_99_validation.validate_account_number(self.ten_ninety_nine_account_number.get())
            ten_99_validation.validate_state(self.ten_ninety_nine_state.get())
            ten_99_validation.validate_state_id(self.ten_ninety_nine_state_id_number.get())

            ten_99_validation.validate_ordinary_dividends(self.ten_ninety_nine_ordinary_dividends.get())
            ten_99_validation.validate_qualified_dividends(self.ten_ninety_nine_qualified_dividends.get())
            ten_99_validation.validate_capital_gain_distr(self.ten_ninety_nine_capital_gain.get())
            ten_99_validation.validate_unrecap_sec_1250_gain(self.ten_ninety_nine_1250_gain.get())
            ten_99_validation.validate_section_1202_gain(self.ten_ninety_nine_1202_gain.get())
            ten_99_validation.validate_collectibles_gain(self.ten_ninety_nine_collectibles_gain.get())
            ten_99_validation.validate_ordinary_dividends(self.ten_ninety_nine_ordinary_dividends.get())
            ten_99_validation.validate_section_897_capital_gain(self.ten_ninety_nine_897_gain.get())
            ten_99_validation.validate_nondividend_distributions(self.ten_ninety_nine_nondividend.get())
            ten_99_validation.validate_income_tax_withheld(self.ten_ninety_nine_federal_tax_withheld.get())
            ten_99_validation.validate_section_199a_dividends(self.ten_ninety_nine_199a.get())
            ten_99_validation.validate_investment_expenses(self.ten_ninety_nine_investment_expenses.get())
            ten_99_validation.validate_foreign_tax_paid(self.ten_ninety_nine_foreign_tax.get())
            ten_99_validation.validate_foreign_country_or_us_possession(self.ten_ninety_nine_foreign_tax_country.get())
            ten_99_validation.validate_cash_liquidation_distributions(self.ten_ninety_nine_cash_liquidation.get())
            ten_99_validation.validate_noncash_liquidation_distributions(self.ten_ninety_nine_noncash_liquidation.get())
            ten_99_validation.validate_exempt_interest_dividends(self.ten_ninety_nine_exempt_dividends.get())
            ten_99_validation.validate_private_activity_bond_interest_dividends(self.ten_ninety_nine_specified_bond_dividends.get())
            ten_99_validation.validate_other_states_tax(self.ten_ninety_nine_state_tax_withheld.get())

            ten_99_list = [self.ten_ninety_nine_payer_info.get(), self.ten_ninety_nine_payer_tin.get(),
                           self.ten_ninety_nine_recipient_name.get(), self.ten_ninety_nine_recipient_tin.get(),
                           self.ten_ninety_nine_federal_tax_withheld.get()]

            for w in ten_99_list:
                if w == "":
                    messagebox.showerror("Error", "Please enter all fields: Payer's Name ETC, "
                                                  "Payer's Tin, "
                                                  "Recipient's Name, "
                                                  "Recipient's Tin, "
                                                  "And Federal Income Tax Withheld ")
                    break
                else:
                    self.results_textbox.configure(state="normal")
                    self.results_textbox.delete("1.0", "end")
                    self.results_textbox.insert("end", "Form 1099 Information:")
                    self.results_textbox.insert("end", "\n\n")
                    self.results_textbox.insert("end", f"Payer's Name ETC: {self.ten_ninety_nine_payer_info.get()}")
                    self.results_textbox.insert("end", "\n")
                    self.results_textbox.insert("end", f"Payer's Tin: {self.ten_ninety_nine_payer_tin.get()}")
                    self.results_textbox.insert("end", "\n")
                    self.results_textbox.insert("end", f"Recipient's Name: {self.ten_ninety_nine_recipient_name.get()}")
                    self.results_textbox.insert("end", "\n")
                    self.results_textbox.insert("end", f"Recipient's Tin: {self.ten_ninety_nine_recipient_tin.get()}")
                    self.results_textbox.insert("end", "\n")
                    self.results_textbox.insert("end",
                                                f"Federal Income Tax Withheld: "
                                                f"{float(self.ten_ninety_nine_federal_tax_withheld.get()):.2f}")
                    self.results_textbox.configure(state="disabled")
                    break
            pass
        elif self.calculate_changer == "1040":

            ten_40_validation.validate_first_name_i(self.ten_forty_first_name.get())
            ten_40_validation.validate_last_name(self.ten_forty_last_name.get())
            ten_40_validation.validate_spouse_first_i(self.ten_forty_spouse_first.get())
            ten_40_validation.validate_spouse_last_name(self.ten_forty_spouse_last.get())
            ten_40_validation.validate_home_address(self.ten_forty_home_address.get())
            ten_40_validation.validate_apt_no(self.ten_forty_apt_no.get())
            ten_40_validation.validate_city_etc(self.ten_forty_city.get())
            ten_40_validation.validate_state(self.ten_forty_state.get())
            ten_40_validation.validate_zip_code(self.ten_forty_zip.get())
            ten_40_validation.validate_foreign_country_name(self.ten_forty_foreign_country.get())
            ten_40_validation.validate_foreign_province(self.ten_forty_foreign_province.get())
            ten_40_validation.validate_foreign_postal_code(self.ten_forty_foreign_post_code.get())

            if self.ten_forty_filing_single.get() == 1:
                self.filing_status = "Single"
                if self.ten_forty_filing_jointly.get() == 1:
                    self.filing_status = ""
                elif self.ten_forty_filing_separately.get() == 1:
                    self.filing_status = ""
                elif self.ten_forty_filing_hoh.get() == 1:
                    self.filing_status = ""
                elif self.ten_forty_filing_qss.get() == 1:
                    self.filing_status = ""
                ten_40_validation.validate_filing_status(self.filing_status)

            elif self.ten_forty_filing_jointly.get() == 1:
                self.filing_status = "Married Filing Jointly"
                if self.ten_forty_filing_single.get() == 1:
                    self.filing_status = ""
                elif self.ten_forty_filing_separately.get() == 1:
                    self.filing_status = ""
                elif self.ten_forty_filing_hoh.get() == 1:
                    self.filing_status = ""
                elif self.ten_forty_filing_qss.get() == 1:
                    self.filing_status = ""
                ten_40_validation.validate_filing_status(self.filing_status)

            elif self.ten_forty_filing_separately.get() == 1:
                self.filing_status = "Married Filing Separately"
                if self.ten_forty_filing_single.get() == 1:
                    self.filing_status = ""
                elif self.ten_forty_filing_jointly.get() == 1:
                    self.filing_status = ""
                elif self.ten_forty_filing_hoh.get() == 1:
                    self.filing_status = ""
                elif self.ten_forty_filing_qss.get() == 1:
                    self.filing_status = ""
                ten_40_validation.validate_filing_status(self.filing_status)

            elif self.ten_forty_filing_hoh.get() == 1:
                self.filing_status = "Head of Household"
                if self.ten_forty_filing_single.get() == 1:
                    self.filing_status = ""
                elif self.ten_forty_filing_jointly.get() == 1:
                    self.filing_status = ""
                elif self.ten_forty_filing_separately.get() == 1:
                    self.filing_status = ""
                elif self.ten_forty_filing_qss.get() == 1:
                    self.filing_status = ""
                user_form_1040.set_filing_status(self.filing_status)

            elif self.ten_forty_filing_qss.get() == 1:
                self.filing_status = "Qualifying Surviving Spouse"
                if self.ten_forty_filing_single.get() == 1:
                    self.filing_status = ""
                elif self.ten_forty_filing_jointly.get() == 1:
                    self.filing_status = ""
                elif self.ten_forty_filing_separately.get() == 1:
                    self.filing_status = ""
                elif self.ten_forty_filing_hoh.get() == 1:
                    self.filing_status = ""
                user_form_1040.set_filing_status(self.filing_status)
            else:
                self.filing_status = ""
                ten_40_validation.validate_filing_status(self.filing_status)


            if self.ten_forty_digital_assets_yes.get() == 1:
                self.checkbox_checker = True
                user_form_1040.set_has_digital_assets(self.checkbox_checker)
            if self.ten_forty_digital_assets_no.get() == 1:
                self.checkbox_checker = False
                user_form_1040.set_has_digital_assets(self.checkbox_checker)

            if self.ten_forty_are_dependent.get() == 1:
                self.checkbox_checker = True
                user_form_1040.set_is_dependent(self.checkbox_checker)

            if self.ten_forty_spouse_dependent.get() == 1:
                self.checkbox_checker = True
                user_form_1040.set_spouse_is_dependent(self.checkbox_checker)

            if self.ten_forty_spouse_separate.get() == 1:
                self.checkbox_checker = True
                user_form_1040.set_spouse_itemizes_separately(self.checkbox_checker)

            if self.ten_forty_self_1959.get() == 1:
                self.born_1959 = 66
                user_form_1040.set_user_age(self.born_1959)

            if self.ten_forty_self_blind.get() == 1:
                self.checkbox_checker = True
                user_form_1040.set_user_is_blind(self.checkbox_checker)

            if self.ten_forty_spouse_1959.get() == 1:
                self.born_1959 = 66
                user_form_1040.set_user_age(self.born_1959)

            if self.ten_forty_spouse_blind.get() == 1:
                self.checkbox_checker = True
                user_form_1040.set_spouse_is_blind(self.checkbox_checker)

            ten_40_validation.validate_dependets_first_last_1(self.ten_forty_dependent_first_1.get())
            ten_40_validation.validate_dependets_first_last_2(self.ten_forty_dependent_first_2.get())
            ten_40_validation.validate_dependets_first_last_3(self.ten_forty_dependent_first_3.get())
            ten_40_validation.validate_dependets_first_last_4(self.ten_forty_dependent_first_4.get())

            ten_40_validation.validate_income_w2(self.ten_forty_total_w2s.get())
            ten_40_validation.validate_household_employee_income(self.ten_forty_household_wages.get())
            ten_40_validation.validate_tip_income(self.ten_forty_tip_income.get())
            ten_40_validation.validate_medicaid_waiver_payments(self.ten_forty_medicaid_waiver.get())
            ten_40_validation.validate_dependent_care_benefits(self.ten_forty_dependent_benefits.get())
            ten_40_validation.validate_employer_adoption_benefits(self.ten_forty_adoption_benefits.get())
            ten_40_validation.validate_wages_form_8919(self.ten_forty_8919_wages.get())
            ten_40_validation.validate_other_income(self.ten_forty_other_income.get())
            ten_40_validation.validate_combat_pay(self.ten_forty_combat_pay.get())
            ten_40_validation.validate_tax_exempt_interest(self.ten_forty_tax_exempt_interest.get())
            ten_40_validation.validate_taxable_interest(self.ten_forty_taxable_interest.get())
            ten_40_validation.validate_qualified_dividends(self.ten_forty_qualified_dividends.get())
            ten_40_validation.validate_ordinary_dividends(self.ten_forty_ordinary_dividends.get())
            ten_40_validation.validate_ira_distributions(self.ten_forty_ira_distributions.get())
            ten_40_validation.validate_ira_taxable(self.ten_forty_taxable_ira.get())
            ten_40_validation.validate_pensions_annuities(self.ten_forty_pensions_annuities.get())
            ten_40_validation.validate_pensions_annuities_taxable(self.ten_forty_taxable_pensions.get())
            ten_40_validation.validate_social_security_benefits(self.ten_forty_social_security.get())
            ten_40_validation.validate_ss_benefits_taxable(self.ten_forty_social_taxable.get())
            ten_40_validation.validate_capital_gain_or_loss(self.ten_forty_capital_gain.get())
            ten_40_validation.validate_income_schedule_1(self.ten_forty_schedule_1.get())
            ten_40_validation.validate_adjustments(self.ten_forty_income_adjustments.get())
            ten_40_validation.validate_qualified_business_income_deduction(self.ten_forty_business_deductions.get())
            ten_40_validation.validate_form_no(self.ten_forty_other_form_no.get())
            ten_40_validation.validate_tax(self.ten_forty_other_form_total.get())
            ten_40_validation.validate_amount_schedule_2(self.ten_forty_schedule_2.get())
            ten_40_validation.validate_child_tax_credit(self.ten_forty_child_credit.get())
            ten_40_validation.validate_amount_schedule_3_line_8(self.ten_forty_schedule_3.get())
            ten_40_validation.validate_other_taxes(self.ten_forty_other_taxes.get())
            ten_40_validation.validate_tax_withheld_w2(self.ten_forty_withheld_w2.get())
            ten_40_validation.validate_tax_withheld_1099(self.ten_forty_withheld_1099.get())
            ten_40_validation.validate_tax_withheld_other(self.ten_forty_withheld_other.get())
            ten_40_validation.validate_estimate_tax_payments(self.ten_forty_previous_year.get())
            ten_40_validation.validate_earned_income_credit(self.ten_forty_eic.get())
            ten_40_validation.validate_additional_child_tax_credit(self.ten_forty_8812_child_credit.get())
            ten_40_validation.validate_american_opportunity_credit(self.ten_forty_8863_opportunity_credit.get())
            ten_40_validation.validate_amount_schedule_3_line_15(self.ten_forty_schedule_3_line_15.get())
            ten_40_validation.validate_penality(self.ten_forty_penalty.get())

            ten_40_list = self.ten_forty_placements.copy()
            # Creating a list of indexes to remove

            indexes_to_remove = [
                self.ten_forty_placements.index(self.ten_forty_penalty),
                self.ten_forty_placements.index(self.ten_forty_other_form_no),
                self.ten_forty_placements.index(self.ten_forty_dependent_first_4),
                self.ten_forty_placements.index(self.ten_forty_dependent_first_3),
                self.ten_forty_placements.index(self.ten_forty_dependent_first_2),
                self.ten_forty_placements.index(self.ten_forty_dependent_first_1),
                self.ten_forty_placements.index(self.ten_forty_foreign_post_code),
                self.ten_forty_placements.index(self.ten_forty_foreign_province),
                self.ten_forty_placements.index(self.ten_forty_foreign_country),
                self.ten_forty_placements.index(self.ten_forty_zip),
                self.ten_forty_placements.index(self.ten_forty_state),
                self.ten_forty_placements.index(self.ten_forty_city),
                self.ten_forty_placements.index(self.ten_forty_apt_no),
                self.ten_forty_placements.index(self.ten_forty_home_address),
                self.ten_forty_placements.index(self.ten_forty_spouse_last),
                self.ten_forty_placements.index(self.ten_forty_spouse_first),
                self.ten_forty_placements.index(self.ten_forty_last_name),
                self.ten_forty_placements.index(self.ten_forty_first_name),
                self.ten_forty_placements.index(self.ten_forty_scrolling_frame),
                self.ten_forty_placements.index(self.ten_forty_label_for_pg_2),
                self.ten_forty_placements.index(self.ten_forty_label_for_pg_1)
            ]

            # Removing the elements at the specified indexes from self.ten_forty_fields_save_load
            for index in sorted(indexes_to_remove, reverse=True):
                ten_40_list.pop(index)

            for w in ten_40_list:
                if w.get() == "":
                    messagebox.showerror("Error", "Please enter all fields 1a-Amount Owed")
                    break
                else:

                    user_form_1040.set_income_w2(float(self.ten_forty_total_w2s.get()))
                    user_form_1040.set_household_employee_wages(float(self.ten_forty_household_wages.get()))
                    user_form_1040.set_tip_income(float(self.ten_forty_tip_income.get()))
                    user_form_1040.set_medicaid_waiver_payments(float(self.ten_forty_medicaid_waiver.get()))
                    user_form_1040.set_dependent_care_benefits(float(self.ten_forty_dependent_benefits.get()))
                    user_form_1040.set_employer_adoption_benefits(float(self.ten_forty_adoption_benefits.get()))
                    user_form_1040.set_wages_form_8919(float(self.ten_forty_8919_wages.get()))
                    user_form_1040.set_other_income(float(self.ten_forty_other_income.get()))

                    user_form_1040.total_lines_1a_to_1h()

                    user_form_1040.set_taxable_interest(float(self.ten_forty_taxable_interest.get()))
                    user_form_1040.set_ordinary_dividends(float(self.ten_forty_ordinary_dividends.get()))
                    user_form_1040.set_ira_taxable(float(self.ten_forty_taxable_ira.get()))
                    user_form_1040.set_pensions_annuities_taxable(float(self.ten_forty_taxable_pensions.get()))
                    user_form_1040.set_ss_benefits_taxable(float(self.ten_forty_social_taxable.get()))
                    user_form_1040.set_capital_gain_or_loss(float(self.ten_forty_capital_gain.get()))
                    user_form_1040.set_income_schedule_1(float(self.ten_forty_schedule_1.get()))

                    user_form_1040.calc_total_income()

                    user_form_1040.set_adjustments(float(self.ten_forty_income_adjustments.get()))

                    user_form_1040.calc_adjusted_gross_income()

                    if self.ten_forty_filing_single.get() == 1:
                        self.filing_status = "Single"
                        user_form_1040.set_filing_status(self.filing_status)

                    if self.ten_forty_filing_jointly.get() == 1:
                        self.filing_status = "Married Filing Jointly"
                        user_form_1040.set_filing_status(self.filing_status)

                    if self.ten_forty_filing_separately.get() == 1:
                        self.filing_status = "Married Filing Separately"
                        user_form_1040.set_filing_status(self.filing_status)

                    if self.ten_forty_filing_hoh.get() == 1:
                        self.filing_status = "Head of Household"
                        user_form_1040.set_filing_status(self.filing_status)

                    if self.ten_forty_filing_qss.get() == 1:
                        self.filing_status = "Qualifying Surviving Spouse"
                        user_form_1040.set_filing_status(self.filing_status)

                    if self.ten_forty_digital_assets_yes.get() == 1:
                        self.checkbox_checker = True
                        user_form_1040.set_has_digital_assets(self.checkbox_checker)
                    if self.ten_forty_digital_assets_no.get() == 1:
                        self.checkbox_checker = False
                        user_form_1040.set_has_digital_assets(self.checkbox_checker)

                    if self.ten_forty_are_dependent.get() == 1:
                        self.checkbox_checker = True
                        user_form_1040.set_is_dependent(self.checkbox_checker)

                    if self.ten_forty_spouse_dependent.get() == 1:
                        self.checkbox_checker = True
                        user_form_1040.set_spouse_is_dependent(self.checkbox_checker)

                    if self.ten_forty_spouse_separate.get() == 1:
                        self.checkbox_checker = True
                        user_form_1040.set_spouse_itemizes_separately(self.checkbox_checker)

                    if self.ten_forty_self_1959.get() == 1:
                        self.born_1959 = 66
                        user_form_1040.set_user_age(self.born_1959)

                    if self.ten_forty_self_blind.get() == 1:
                        self.checkbox_checker = True
                        user_form_1040.set_user_is_blind(self.checkbox_checker)

                    if self.ten_forty_spouse_1959.get() == 1:
                        self.born_1959 = 66
                        user_form_1040.set_user_age(self.born_1959)

                    if self.ten_forty_spouse_blind.get() == 1:
                        self.checkbox_checker = True
                        user_form_1040.set_spouse_is_blind(self.checkbox_checker)

                    if self.ten_forty_lump_sum_method.get() == 1:
                        self.checkbox_checker = True
                        user_form_1040.set_use_lump_sum(self.checkbox_checker)

                    user_form_1040.calc_standard_deduction()

                    user_form_1040.set_qualified_business_income_deduction(
                        float(self.ten_forty_business_deductions.get()))

                    user_form_1040.calc_total_deductions()

                    user_form_1040.calc_taxable_income()

                    user_form_1040.set_tax(float(self.ten_forty_other_form_total.get()))
                    user_form_1040.set_amount_schedule_2(float(self.ten_forty_schedule_2.get()))

                    user_form_1040.calc_total_16_17()

                    user_form_1040.set_child_tax_credit(float(self.ten_forty_child_credit.get()))
                    user_form_1040.set_amount_schedule_3_line_8(float(self.ten_forty_schedule_3.get()))

                    user_form_1040.calc_total_19_20()

                    user_form_1040.calc_sub_21_18()

                    user_form_1040.set_other_taxes(float(self.ten_forty_other_taxes.get()))

                    user_form_1040.calc_total_tax()

                    user_form_1040.set_tax_withheld_w2(float(self.ten_forty_withheld_w2.get()))
                    user_form_1040.set_tax_withheld_1099(float(self.ten_forty_withheld_1099.get()))
                    user_form_1040.set_tax_withheld_other(float(self.ten_forty_withheld_other.get()))

                    user_form_1040.calc_total_withheld()

                    user_form_1040.set_estimate_tax_payments(float(self.ten_forty_previous_year.get()))
                    user_form_1040.set_earned_income_credit(float(self.ten_forty_eic.get()))
                    user_form_1040.set_additional_child_tax_credit(float(self.ten_forty_8812_child_credit.get()))
                    user_form_1040.set_american_opportunity_credit(float(self.ten_forty_8863_opportunity_credit.get()))
                    user_form_1040.set_amount_schedule_3_line_15(float(self.ten_forty_schedule_3_line_15.get()))

                    user_form_1040.calc_total_other_payments()

                    user_form_1040.calc_total_payments()

                    user_form_1040.calc_refund()

                    self.ten_forty_1_ah_sum.configure(state="normal")
                    self.ten_forty_1_ah_sum.delete(0, ctk.END)
                    self.ten_forty_1_ah_sum.insert("end", f"{user_form_1040.total_1a_to_1h:.2f}")

                    self.ten_forty_total_income.configure(state="normal")
                    self.ten_forty_total_income.delete(0, ctk.END)
                    self.ten_forty_total_income.insert("end", f"{user_form_1040.total_income:.2f}")

                    self.ten_forty_adjusted_income.configure(state="normal")
                    self.ten_forty_adjusted_income.delete(0, ctk.END)
                    self.ten_forty_adjusted_income.insert("end", f"{user_form_1040.adjusted_gross_income:.2f}")

                    self.ten_forty_add_16_17.configure(state="normal")
                    self.ten_forty_add_16_17.delete(0, ctk.END)
                    self.ten_forty_add_16_17.insert("end", f"{user_form_1040.total_16_17:.2f}")

                    self.ten_forty_add_19_20.configure(state="normal")
                    self.ten_forty_add_19_20.delete(0, ctk.END)
                    self.ten_forty_add_19_20.insert("end", f"{user_form_1040.total_19_20:.2f}")

                    self.ten_forty_sub_21_18.configure(state="normal")
                    self.ten_forty_sub_21_18.delete(0, ctk.END)
                    self.ten_forty_sub_21_18.insert("end", f"{user_form_1040.subtract_21_from_18:.2f}")

                    self.ten_forty_total_tax.configure(state="normal")
                    self.ten_forty_total_tax.delete(0, ctk.END)
                    self.ten_forty_total_tax.insert("end", f"{user_form_1040.total_tax:.2f}")

                    self.ten_forty_withheld_total.configure(state="normal")
                    self.ten_forty_withheld_total.delete(0, ctk.END)
                    self.ten_forty_withheld_total.insert("end", f"{user_form_1040.total_withheld:.2f}")

                    self.ten_forty_other_payments.configure(state="normal")
                    self.ten_forty_other_payments.delete(0, ctk.END)
                    self.ten_forty_other_payments.insert("end", f"{user_form_1040.total_other_payments:.2f}")

                    self.ten_forty_total_payments.configure(state="normal")
                    self.ten_forty_total_payments.delete(0, ctk.END)
                    self.ten_forty_total_payments.insert("end", f"{user_form_1040.total_payments:.2f}")

                    self.ten_forty_overpaid.configure(state="normal")
                    self.ten_forty_overpaid.delete(0, ctk.END)
                    self.ten_forty_overpaid.insert("end", f"{user_form_1040.overpaid:.2f}")

                    self.ten_forty_owed.configure(state="normal")
                    self.ten_forty_owed.delete(0, ctk.END)
                    self.ten_forty_owed.insert("end", f"{user_form_1040.amount_owed:.2f}")

                    self.ten_forty_deductions.configure(state="normal")
                    self.ten_forty_deductions.delete(0, ctk.END)
                    self.ten_forty_deductions.insert("end", f"{user_form_1040.standard_deduction:.2f}")

                    self.ten_forty_total_deductions.configure(state="normal")
                    self.ten_forty_total_deductions.delete(0, ctk.END)
                    self.ten_forty_total_deductions.insert("end", f"{user_form_1040.total_deductions:.2f}")

                    self.ten_forty_taxable_income.configure(state="normal")
                    self.ten_forty_taxable_income.delete(0, ctk.END)
                    self.ten_forty_taxable_income.insert("end", f"{user_form_1040.taxable_income:.2f}")

                    self.results_textbox.configure(state="normal")
                    self.results_textbox.delete("1.0", "end")
                    self.results_textbox.insert("end", "Form 1040 Information:")
                    self.results_textbox.insert("end", "\n\n")
                    self.results_textbox.insert("end", f"Amount Overpaid: ${user_form_1040.overpaid:.2f}")
                    self.results_textbox.insert("end", "\n")
                    self.results_textbox.insert("end", f"Amount Owed: ${user_form_1040.amount_owed:.2f}")
                    self.results_textbox.configure(state="disabled")
                    break

    def view_about(self):
        about_page = ctk.CTkToplevel()
        about_page.geometry("1000x1000")
        self.app.title("TRACE")
        self.app.resizable(False, False)

        about_canvas = tk.Canvas(about_page, width=1000, height=1000, bg="#222222")

        about_canvas.place(relx=.5, rely=.5, anchor="center")
        about_info = """ 
        The TRACE program is a form-based tax calculation software to help
        calculate your potential tax liability or refund.
        It provides fillable forms for the W2 1099. This information can be sent
        directly to an editable 1040 form, which is then used to calculate
        the potential return.
        This program was created using 2023 filing forms.
        """
        help_info = """
        To open a saved or downloaded PDF, click on the Browse button for the
        corresponding form under the File tab.
        To export your filled form as a PDF, click on the Export button for the form
        under the File tab.
        To send your numbers from your filled or imported W2 or 1099 form to your
        1040, click the Submit button.
        To switch which form you are filling out, select the corresponding form
        under the Form tab.
        In order to save or load your TRACE session, you must reenter your
        User ID and Password in the fields at the bottom of the screen before
        clicking the Save Session or Load Session buttons.
        After saving or loading your session at least once, autosave will
        be enabled and save your data as it is entered.
        """
        creator_info = """
        Programmed by Dylan Arone, Alexi McNabb, and Stephen Strong,
        with help from Sydney Southerland and guidance from Cindy Luttrell
        """
        about_canvas.create_text(500, 200, text="About", fill="white", font=("Arial", 40))
        about_canvas.create_text(490, 330, text=about_info, fill="white", font=("Arial", 16), justify="center")
        about_canvas.create_text(500, 450, text="Help", fill="white", font=("Arial", 40))
        about_canvas.create_text(490, 650, text=help_info, fill="white", font=("Arial", 16), justify="center")
        about_canvas.create_text(490, 850, text=creator_info, fill="white", justify="center")
