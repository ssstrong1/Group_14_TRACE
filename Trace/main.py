import re
from tkinter import filedialog
import ui


class Trace:

    """
    Class for handling tax-related operations.
    """

    def new_session(self):

        """
        Creates a new session for tax calculations.
        """

        pass

    # Browse

    def browse(self):

        """
        Opens a file explorer to select a text file containing tax information.
        Parses the file and extracts income, deductions, and tax year.
        Assigns data to self.income_entry, self.deductions_entry, and self.tax_year_entry.
        """

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

        """
        Opens a file explorer to save the tax-related data to a text file.
        """

        # Open file explorer
        filename = filedialog.asksaveasfilename(initialdir="/", title="Save As",
                                                filetypes=(("Text Files", "*.txt"), ("All Files", "*.*")))


Trace()

