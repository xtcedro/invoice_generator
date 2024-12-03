import tkinter as tk
from tkinter import ttk, messagebox


class InvoiceGeneratorApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Invoice Generator")
        self.geometry("400x400")
        
        self.create_menu_bar()
        self.create_widgets()
    
    def create_menu_bar(self):
        """Creates a menu bar with basic options."""
        menu_bar = tk.Menu(self)
        
        # File menu
        file_menu = tk.Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="New", command=self.new_invoice)
        file_menu.add_command(label="Save", command=self.save_invoice)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.quit)
        menu_bar.add_cascade(label="File", menu=file_menu)
        
        # Help menu
        help_menu = tk.Menu(menu_bar, tearoff=0)
        help_menu.add_command(label="About", command=self.show_about)
        menu_bar.add_cascade(label="Help", menu=help_menu)
        
        self.config(menu=menu_bar)
    
    def create_widgets(self):
        """Creates the main widgets for user input."""
        # Customer Name
        self.name_label = ttk.Label(self, text="Customer Name:")
        self.name_label.pack(pady=(10, 0))
        self.name_entry = ttk.Entry(self)
        self.name_entry.pack(fill="x", padx=20, pady=(0, 10))
        
        # Customer Number
        self.number_label = ttk.Label(self, text="Customer Number:")
        self.number_label.pack()
        self.number_entry = ttk.Entry(self)
        self.number_entry.pack(fill="x", padx=20, pady=(0, 10))
        
        # Service or Sale
        self.service_label = ttk.Label(self, text="Service or Sale:")
        self.service_label.pack()
        self.service_entry = ttk.Entry(self)
        self.service_entry.pack(fill="x", padx=20, pady=(0, 10))
        
        # Amount Charged
        self.amount_label = ttk.Label(self, text="Amount Charged ($):")
        self.amount_label.pack()
        self.amount_entry = ttk.Entry(self)
        self.amount_entry.pack(fill="x", padx=20, pady=(0, 10))
        
        # Submit Button
        self.submit_button = ttk.Button(self, text="Submit", command=self.submit_form)
        self.submit_button.pack(pady=(10, 0))
    
    def submit_form(self):
        """Handles form submission."""
        name = self.name_entry.get()
        number = self.number_entry.get()
        service = self.service_entry.get()
        amount = self.amount_entry.get()
        
        if not (name and number and service and amount):
            messagebox.showerror("Error", "All fields are required.")
            return
        
        try:
            amount = float(amount)
        except ValueError:
            messagebox.showerror("Error", "Amount must be a valid number.")
            return
        
        # Simulate saving the data or generating an invoice
        messagebox.showinfo("Success", "Invoice generated successfully!")
    
    def new_invoice(self):
        """Clears all input fields to create a new invoice."""
        self.name_entry.delete(0, tk.END)
        self.number_entry.delete(0, tk.END)
        self.service_entry.delete(0, tk.END)
        self.amount_entry.delete(0, tk.END)
        messagebox.showinfo("New Invoice", "Ready to create a new invoice.")
    
    def save_invoice(self):
        """Simulates saving the invoice data."""
        messagebox.showinfo("Save Invoice", "Invoice saved successfully!")
    
    def show_about(self):
        """Displays information about the application."""
        messagebox.showinfo("About", "Invoice Generator v1.0\nDeveloped by Pedro Dominguez")


if __name__ == "__main__":
    app = InvoiceGeneratorApp()
    app.mainloop()
