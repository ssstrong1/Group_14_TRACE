import customtkinter as ctk
from tkinter import *
import tkinter as tk
from PIL import ImageTk, Image

import ctypes

from main import Trace

t = Trace()

user = ctypes.windll.user32
screensize = user.GetSystemMetrics(0), user.GetSystemMetrics(1)


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

        self.app = ctk.CTk()
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
            cosmos = canvas.create_text(635, 150, anchor="nw", fill="yellow")
            canvas.itemconfig(cosmos, text="TRACE", width=780)
            canvas.itemconfig(cosmos, font=("Arial", 50))
            aqua = canvas.create_text(670, 755, anchor="nw", fill="yellow")
            canvas.itemconfig(aqua, text="Results", width=780)
            canvas.itemconfig(aqua, font=("Arial", 35))
        else:
            d_2_img = ImageTk.PhotoImage(Image.open("images/pattern_back.png").resize((1500, 1200)))
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
        file_menu.add_command(label="New", command=t.new_session)
        file_menu.add_command(label="Save as", command=t.save_as)
        file_menu.add_command(label="Browse", command=t.browse)
        file_menu.add_separator()
        menubar.add_cascade(label="File", menu=file_menu)

        # Edit menu
        edit_menu = Menu(menubar, tearoff=0)
        edit_menu.add_command(label="W-2", command=self.positions)
        edit_menu.add_command(label="1099", command=self.remove)
        edit_menu.add_command(label="1040")
        menubar.add_cascade(label="Form", menu=edit_menu)

        # Help menu
        help_menu = Menu(menubar, tearoff=0)
        help_menu.add_command(label="About")
        menubar.add_cascade(label="Settings", menu=help_menu)

        ###############################

        # Start Of Input Fields

        # Other Form Image

        self.ten_ninety_nine_img = ctk.CTkImage(light_image=Image.open('images/background3.png'), size=(1300, 700))
        self.ten_ninety_nine_label_for_img = ctk.CTkLabel(self.app, text="", image=self.ten_ninety_nine_img)

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

        # 9 box

        self.nine_box = ctk.CTkEntry(master=self.app, placeholder_text="Nine", width=235, height=35,
                                     text_color="#000000",
                                     bg_color="#c0c0c0", fg_color="white")

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
                                               height=25, text_color="#000000", bg_color="white",
                                               fg_color="transparent")

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

        #  Statutory Employee

        self.statutory_emp = ctk.CTkCheckBox(master=self.app, width=0, text="", checkbox_height=22, height=0,
                                             bg_color="white")

        #  Retirement Plan

        self.retirement_p = ctk.CTkCheckBox(master=self.app, width=0, text="", checkbox_height=22, height=0,
                                            bg_color="white")

        #  Third Party Sick Pay

        self.third_party_sp = ctk.CTkCheckBox(master=self.app, width=0, text="", checkbox_height=22, height=0,
                                              bg_color="white")

        #  Other

        self.other_field = ctk.CTkEntry(master=self.app, placeholder_text="other", width=269, height=90,
                                        text_color="#000000",
                                        bg_color="white", fg_color="transparent")

        # Employer Name, Address, ZIP

        self.employer_name = ctk.CTkEntry(master=self.app, placeholder_text="Name", width=250, text_color="#000000",
                                          bg_color="white", fg_color="transparent")
        self.employer_address = ctk.CTkEntry(master=self.app, placeholder_text="Address", width=250,
                                             text_color="#000000",
                                             bg_color="white", fg_color="transparent")
        self.employer_zip = ctk.CTkEntry(master=self.app, placeholder_text="ZIP Code", width=250, text_color="#000000",
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

        # Employee Address

        self.employee_address = ctk.CTkEntry(master=self.app, placeholder_text="Address", width=230, height=20,
                                             text_color="#000000", bg_color="white", fg_color="transparent")

        # Employee ZIP

        self.employee_zip = ctk.CTkEntry(master=self.app, placeholder_text="ZIP", width=100, height=20,
                                         text_color="#000000", bg_color="white", fg_color="transparent")

        # Cover And Replacer For Year On Form

        self.blocker = ctk.CTkImage(light_image=Image.open('images/blocker.png'), size=(150, 85))
        self.blocker_img = ctk.CTkLabel(self.app, text="", image=self.blocker)
        self.twenty_four = ctk.CTkImage(light_image=Image.open('images/2024.png'), size=(100, 30))
        self.twenty_four_img = ctk.CTkLabel(self.app, text="", image=self.twenty_four)



        # End Of W-2 Input Fields

        # Start 1099 Input Fields

        # Payer name, street address, city/town, state/province, country, zip/postal, phone no.

        self.ten_ninety_nine_payer_name = ctk.CTkEntry(master=self.app, placeholder_text="Name", width=250,
                                                       text_color="#000000", bg_color="white", fg_color="transparent")
        self.ten_ninety_nine_payer_address = ctk.CTkEntry(master=self.app, placeholder_text="Address", width=250,
                                                          text_color="#000000", bg_color="white",
                                                          fg_color="transparent")
        self.ten_ninety_nine_payer_city = ctk.CTkEntry(master=self.app, placeholder_text="City or Town", width=250,
                                                       text_color="#000000", bg_color="white", fg_color="transparent")
        self.ten_ninety_nine_payer_state = ctk.CTkEntry(master=self.app, placeholder_text="State or Province",
                                                        width=250, text_color="#000000", bg_color="white",
                                                        fg_color="transparent")
        self.ten_ninety_nine_payer_country = ctk.CTkEntry(master=self.app, placeholder_text="Country", width=250,
                                                          text_color="#000000", bg_color="white",
                                                          fg_color="transparent")
        self.ten_ninety_nine_payer_ZIP = ctk.CTkEntry(master=self.app, placeholder_text="ZIP or Postal Code", width=250,
                                                      text_color="#000000", bg_color="white", fg_color="transparent")
        self.ten_ninety_nine_payer_phone = ctk.CTkEntry(master=self.app, placeholder_text="Phone #", width=250,
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

        self.ten_ninety_nine_recipient_city = ctk.CTkEntry(master=self.app, placeholder_text="City or Town", width=250,
                                                           text_color="#000000", bg_color="white",
                                                           fg_color="transparent")
        self.ten_ninety_nine_recipient_state = ctk.CTkEntry(master=self.app, placeholder_text="State or Province",
                                                            width=250, text_color="#000000", bg_color="white",
                                                            fg_color="transparent")
        self.ten_ninety_nine_recipient_country = ctk.CTkEntry(master=self.app, placeholder_text="Country", width=250,
                                                              text_color="#000000", bg_color="white",
                                                              fg_color="transparent")
        self.ten_ninety_nine_recipient_ZIP = ctk.CTkEntry(master=self.app, placeholder_text="ZIP or Postal Code",
                                                          width=250, text_color="#000000", bg_color="white",
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
        # FACTA Filing Requirement [checkbox]
        self.ten_ninety_nine_facta_filing = ctk.CTkCheckBox(master=self.app, width=0, text="", checkbox_height=22,
                                                            height=0, bg_color="white")
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

        UserInterface.positions(self)

        # End Input Fields
        ###############################

        # Results Section

        results_textbox = ctk.CTkTextbox(master=self.app, scrollbar_button_color="#FFCC70", width=500, corner_radius=16,
                                         border_color="#FFCC70")

        # Results Positioning

        results_textbox.place(relx=.5, rely=0.85, anchor="center")

        # Buttons

        Button(self.app, text="Calculate").place(relx=.5, rely=0.965, anchor="center")
        Button(self.app, text="Save Session").place(relx=.4, rely=0.965, anchor="center")
        Button(self.app, text="Load Session").place(relx=.6, rely=0.965, anchor="center")

        self.app.mainloop()

    def positions(self):
        # Positioning of Input Fields

        placements = [self.ten_ninety_nine_label_for_img, self.ten_ninety_nine_payer_name, self.ten_ninety_nine_payer_address,
                      self.ten_ninety_nine_payer_city, self.ten_ninety_nine_payer_state, self.ten_ninety_nine_payer_country,
                      self.ten_ninety_nine_payer_ZIP, self.ten_ninety_nine_payer_phone, self.ten_ninety_nine_payer_tin,
                      self.ten_ninety_nine_recipient_tin, self.ten_ninety_nine_recipient_name, self.ten_ninety_nine_recipient_address,
                      self.ten_ninety_nine_recipient_city, self.ten_ninety_nine_recipient_state, self.ten_ninety_nine_recipient_country,
                      self.ten_ninety_nine_recipient_ZIP, self.ten_ninety_nine_facta_filing, self.ten_ninety_nine_account_number,
                      self.ten_ninety_nine_ordinary_dividends, self.ten_ninety_nine_qualified_dividends, self.ten_ninety_nine_capital_gain,
                      self.ten_ninety_nine_1250_gain, self.ten_ninety_nine_1202_gain, self.ten_ninety_nine_collectibles_gain,
                      self.ten_ninety_nine_897_dividends, self.ten_ninety_nine_897_gain, self.ten_ninety_nine_nondividend,
                      self.ten_ninety_nine_federal_tax_withheld, self.ten_ninety_nine_199a, self.ten_ninety_nine_investment_expenses,
                      self.ten_ninety_nine_foreign_tax, self.ten_ninety_nine_foreign_tax_country, self.ten_ninety_nine_cash_liquidation,
                      self.ten_ninety_nine_noncash_liquidation, self.ten_ninety_nine_exempt_dividends, self.ten_ninety_nine_specified_bond_dividends,
                      self.ten_ninety_nine_state, self.ten_ninety_nine_state_id_number, self.ten_ninety_nine_state_tax_withheld]

        for i in placements:
            i.place_forget()
            i.pack_forget()

        # W-2

        self.w_2_label_for_img.place(relx=0.5, rely=0.5, anchor="s")
        self.w_2_label_for_img.pack(pady=88)

        # Employee SSN

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

        # Nine

        self.nine_box.place(relx=.719, rely=0.31, anchor="e")

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

        #  Stat Emp

        self.statutory_emp.place(relx=.691, rely=0.395, anchor="e")

        #  retire plan

        self.retirement_p.place(relx=.6365, rely=0.395, anchor="e")

        #  third party

        self.third_party_sp.place(relx=.583, rely=0.395, anchor="e")

        #  Other

        self.other_field.place(relx=.719, rely=0.462, anchor="e")

        # Employer NAZ

        self.employer_name.place(relx=.285, rely=0.21, anchor="e")
        self.employer_address.place(relx=.285, rely=0.24, anchor="e")
        self.employer_zip.place(relx=.285, rely=0.27, anchor="e")

        # CN

        self.cn_entry.place(relx=.535, rely=0.316, anchor="e")

        # Employee NI

        self.employee_name_i.place(relx=.3, rely=0.357, anchor="e")

        # Employee LN

        self.employee_last_name.place(relx=.505, rely=0.357, anchor="e")

        # Employee S

        self.employee_suffix.place(relx=.535, rely=0.357, anchor="e")

        # Employee A

        self.employee_address.place(relx=.433, rely=0.4915, anchor="e")

        # Employee Z

        self.employee_zip.place(relx=.535, rely=0.4915, anchor="e")

        # Blocker

        self.blocker_img.place(relx=0.525, rely=0.655, anchor="s")
        self.twenty_four_img.place(relx=0.525, rely=0.607, anchor="s")

    def remove(self):
        """
        Removes certain UI elements from the display.
        This method hides and forgets the placement of various UI widgets.
        The list of widgets to be removed is stored in the 'placements' list.
        """

        self.other_form()
        placements = [self.twenty_four_img, self.blocker_img, self.employee_zip,
                      self.employee_address, self.employee_suffix,
                      self.employee_last_name, self.employee_name_i,
                      self.cn_entry, self.employer_address, self.employer_zip,
                      self.employer_name, self.other_field, self.third_party_sp,
                      self.retirement_p, self.statutory_emp, self.locality_name,
                      self.state_field, self.employers_state_id, self.state_wage_tips,
                      self.state_income_tax, self.local_wage_tips, self.local_income_tax,
                      self.twelve_a, self.twelve_b, self.twelve_c, self.twelve_d,
                      self.dependent_care_benefits, self.allocated_tips, self.medicare_tax_withheld,
                      self.social_security_tax_withheld, self.fed_income_tax_withheld,
                      self.non_qualified_plans, self.nine_box, self.social_security_tips,
                      self.medicare_wages, self.social_wages, self.wages_tips_c, self.ein_entry,
                      self.essn_entry, self.w_2_label_for_img]

        for i in placements:
            i.place_forget()
            i.pack_forget()

    def other_form(self):
        """
        Places the 'ten_ninety_nine_label_for_img' widget at the center of the screen
        and sets vertical padding to 88 pixels.
        """
        self.ten_ninety_nine_label_for_img.place(relx=0.5, rely=0.5, anchor="s")
        self.ten_ninety_nine_label_for_img.pack(pady=88)

        self.ten_ninety_nine_payer_name.place(relx=.249, rely=0.156, anchor="e")
        self.ten_ninety_nine_payer_address.place(relx=.440, rely=0.156, anchor="e")
        self.ten_ninety_nine_payer_city.place(relx=.249, rely=0.181, anchor="e")
        self.ten_ninety_nine_payer_state.place(relx=.440, rely=0.181, anchor="e")
        self.ten_ninety_nine_payer_country.place(relx=.249, rely=0.204, anchor="e")
        self.ten_ninety_nine_payer_ZIP.place(relx=.440, rely=0.204, anchor="e")
        self.ten_ninety_nine_payer_phone.place(relx=.249, rely=0.228, anchor="e")

        self.ten_ninety_nine_payer_tin.place(relx=.249, rely=0.286, anchor="e")
        self.ten_ninety_nine_recipient_tin.place(relx=.440, rely=0.286, anchor="e")

        self.ten_ninety_nine_recipient_name.place(relx=.431, rely=0.357, anchor="e")

        self.ten_ninety_nine_recipient_address.place(relx=.431, rely=0.411, anchor="e")

        self.ten_ninety_nine_recipient_city.place(relx=.249, rely=0.456, anchor="e")
        self.ten_ninety_nine_recipient_state.place(relx=.440, rely=0.456, anchor="e")
        self.ten_ninety_nine_recipient_country.place(relx=0.249, rely=0.478, anchor="e")
        self.ten_ninety_nine_recipient_ZIP.place(relx=0.440, rely=0.478, anchor="e")

        self.ten_ninety_nine_facta_filing.place(relx=0.440, rely=0.531, anchor="e")

        self.ten_ninety_nine_account_number.place(relx=0.431, rely=0.571, anchor="e")

        self.ten_ninety_nine_ordinary_dividends.place(relx=0.611, rely=0.153, anchor="e")
        self.ten_ninety_nine_qualified_dividends.place(relx=0.611, rely=0.203, anchor="e")

        self.ten_ninety_nine_capital_gain.place(relx=0.611, rely=0.244, anchor="e")
        self.ten_ninety_nine_1250_gain.place(relx=0.768, rely=0.244, anchor="e")
        self.ten_ninety_nine_1202_gain.place(relx=0.611, rely=0.279, anchor="e")
        self.ten_ninety_nine_collectibles_gain.place(relx=0.768, rely=0.279, anchor="e")
        self.ten_ninety_nine_897_dividends.place(relx=0.611, rely=0.315, anchor="e")
        self.ten_ninety_nine_897_gain.place(relx=0.768, rely=0.315, anchor="e")

        self.ten_ninety_nine_nondividend.place(relx=0.611, rely=0.351, anchor="e")
        self.ten_ninety_nine_federal_tax_withheld.place(relx=0.768, rely=0.351, anchor="e")
        self.ten_ninety_nine_199a.place(relx=0.611, rely=0.388, anchor="e")
        self.ten_ninety_nine_investment_expenses.place(relx=0.768, rely=0.388, anchor="e")

        self.ten_ninety_nine_foreign_tax.place(relx=0.611, rely=0.440, anchor="e")
        self.ten_ninety_nine_foreign_tax_country.place(relx=0.768, rely=0.440, anchor="e")

        self.ten_ninety_nine_cash_liquidation.place(relx=0.611, rely=0.478, anchor="e")
        self.ten_ninety_nine_noncash_liquidation.place(relx=0.768, rely=0.478, anchor="e")

        self.ten_ninety_nine_exempt_dividends.place(relx=0.611, rely=0.527, anchor="e")
        self.ten_ninety_nine_specified_bond_dividends.place(relx=0.768, rely=0.527, anchor="e")

        self.ten_ninety_nine_state.place(relx=0.5, rely=0.565, anchor="e")
        self.ten_ninety_nine_state_id_number.place(relx=0.611, rely=0.565, anchor="e")
        self.ten_ninety_nine_state_tax_withheld.place(relx=0.768, rely=0.565, anchor="e")






UserInterface()
