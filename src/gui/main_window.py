import tkinter as tk
from tkinter import Menu
import customtkinter as ctk
from src.config.settings import Settings


class MainWindow:
    """Main application window."""

    def __init__(self, root):
        self.root = root
        self.settings = Settings()

        # Configure the root window
        self.root.title(self.settings.app_name)
        self.root.geometry(self.settings.get_window_size())
        self.root.resizable(True, True)

        # Apply the theme
        ctk.set_appearance_mode(self.settings.theme)

        # Create the menu bar
        self.create_menu_bar()

        # Create CustomTkinter tabs
        self.create_tabs()

    def create_menu_bar(self):
        """Creates the menu bar."""
        menu_bar = Menu(self.root)

        # File menu
        file_menu = Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="New Invoice")
        file_menu.add_command(label="Open Invoice")
        file_menu.add_command(label="Exit", command=self.root.quit)
        menu_bar.add_cascade(label="File", menu=file_menu)

        # Help menu
        help_menu = Menu(menu_bar, tearoff=0)
        help_menu.add_command(label="About")
        menu_bar.add_cascade(label="Help", menu=help_menu)

        self.root.config(menu=menu_bar)

    def create_tabs(self):
        """Creates tabs using CustomTkinter."""
        self.tab_view = ctk.CTkTabview(self.root, width=500, height=400)
        self.tab_view.pack(fill="both", expand=True, padx=10, pady=10)

        # Generate Invoice Tab
        generate_invoice_tab = self.tab_view.add("Generate Invoice")
        self.create_generate_invoice_tab(generate_invoice_tab)

        # Invoice History Tab
        invoice_history_tab = self.tab_view.add("Invoice History")
        self.create_invoice_history_tab(invoice_history_tab)

    def create_generate_invoice_tab(self, parent):
        """Creates the content for the 'Generate Invoice' tab."""
        label = ctk.CTkLabel(parent, text="Generate Invoice", font=self.settings.gui_font)
        label.pack(pady=10)

        # Customer Name
        self.customer_name_entry = ctk.CTkEntry(parent, placeholder_text="Customer Name")
        self.customer_name_entry.pack(pady=5)

        # Phone Number
        self.phone_number_entry = ctk.CTkEntry(parent, placeholder_text="Phone Number (10 digits)")
        self.phone_number_entry.pack(pady=5)
        self.phone_number_entry.bind("<KeyRelease>", self.validate_phone_number)

        # Email (optional)
        self.email_entry = ctk.CTkEntry(parent, placeholder_text="Email (optional)")
        self.email_entry.pack(pady=5)

        # Service Provided
        self.service_provided_entry = ctk.CTkEntry(parent, placeholder_text="Service Provided")
        self.service_provided_entry.pack(pady=5)

        # Amount Charged
        self.amount_charged_entry = ctk.CTkEntry(parent, placeholder_text="Amount Charged")
        self.amount_charged_entry.pack(pady=5)
        self.amount_charged_entry.bind("<KeyRelease>", self.validate_amount)

        # Submit Button
        button = ctk.CTkButton(parent, text="Submit Invoice", command=self.submit_invoice)
        button.pack(pady=10)

    def create_invoice_history_tab(self, parent):
        """Creates the content for the 'Invoice History' tab."""
        label = ctk.CTkLabel(parent, text="Invoice History", font=self.settings.gui_font)
        label.pack(pady=10)

    def validate_phone_number(self, event=None):
        """Ensures the phone number contains only digits and is up to 10 characters."""
        value = self.phone_number_entry.get()
        cleaned = ''.join(filter(str.isdigit, value))  # Keep only numeric characters

        if len(cleaned) > 10:
            cleaned = cleaned[:10]  # Limit to 10 digits

        # Update the field only if the value has changed
        if value != cleaned:
            self.phone_number_entry.delete(0, tk.END)
            self.phone_number_entry.insert(0, cleaned)

    def validate_amount(self, event=None):
        """Validates that the amount charged is numeric."""
        value = self.amount_charged_entry.get()
        if not value.replace(".", "", 1).isdigit() and value:
            self.amount_charged_entry.delete(len(value) - 1, tk.END)

    def submit_invoice(self):
        """Handles the submission of the invoice."""
        name = self.customer_name_entry.get()
        phone = self.phone_number_entry.get()
        email = self.email_entry.get()
        service = self.service_provided_entry.get()
        amount = self.amount_charged_entry.get()

        # Validate inputs
        if not name.strip():
            print("Error: Customer name is required.")
            return
        if len(phone) != 10 or not phone.isdigit():
            print("Error: Phone number must be exactly 10 digits.")
            return
        if email and "@" not in email:
            print("Error: Invalid email address.")
            return
        if not service.strip():
            print("Error: Service provided is required.")
            return
        if not amount or not amount.replace(".", "", 1).isdigit():
            print("Error: Amount charged must be numeric.")
            return

        # Submit logic
        print("Invoice submitted:")
        print(f"Name: {name}")
        print(f"Phone: {phone}")
        print(f"Email: {email or 'N/A'}")
        print(f"Service: {service}")
        print(f"Amount: ${amount}")


# For testing purposes
if __name__ == "__main__":
    root = ctk.CTk()
    app = MainWindow(root)
    root.mainloop()