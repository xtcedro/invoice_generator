import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from src.services.invoice_generator import generate_invoice  # Adjust import based on your project structure


class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        
        # Window Configuration
        self.title("Invoice Generator")
        self.geometry("600x400")
        self.configure(padx=20, pady=20)
        
        # Customer Details Section
        self.customer_frame = ttk.LabelFrame(self, text="Customer Details")
        self.customer_frame.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

        ttk.Label(self.customer_frame, text="Name:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.customer_name = ttk.Entry(self.customer_frame, width=40)
        self.customer_name.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(self.customer_frame, text="Email:").grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.customer_email = ttk.Entry(self.customer_frame, width=40)
        self.customer_email.grid(row=1, column=1, padx=5, pady=5)

        # Service Details Section
        self.service_frame = ttk.LabelFrame(self, text="Service Details")
        self.service_frame.grid(row=1, column=0, padx=10, pady=10, sticky="ew")

        ttk.Label(self.service_frame, text="Service Description:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.service_description = ttk.Entry(self.service_frame, width=40)
        self.service_description.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(self.service_frame, text="Amount:").grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.service_amount = ttk.Entry(self.service_frame, width=20)
        self.service_amount.grid(row=1, column=1, padx=5, pady=5)

        # Buttons Section
        self.button_frame = ttk.Frame(self)
        self.button_frame.grid(row=2, column=0, padx=10, pady=10, sticky="ew")

        self.generate_button = ttk.Button(self.button_frame, text="Generate Invoice", command=self.generate_invoice)
        self.generate_button.grid(row=0, column=0, padx=5, pady=5)

        self.clear_button = ttk.Button(self.button_frame, text="Clear", command=self.clear_fields)
        self.clear_button.grid(row=0, column=1, padx=5, pady=5)

    def generate_invoice(self):
        """Callback for the 'Generate Invoice' button."""
        # Collect input data
        customer_name = self.customer_name.get().strip()
        customer_email = self.customer_email.get().strip()
        service_description = self.service_description.get().strip()
        service_amount = self.service_amount.get().strip()

        # Input validation
        if not customer_name or not customer_email or not service_description or not service_amount:
            messagebox.showerror("Error", "All fields are required.")
            return
        
        try:
            service_amount = float(service_amount)  # Ensure amount is a valid number
        except ValueError:
            messagebox.showerror("Error", "Amount must be a valid number.")
            return
        
        # Call the invoice generator function
        try:
            generate_invoice(
                customer_name=customer_name,
                customer_email=customer_email,
                service_description=service_description,
                service_amount=service_amount
            )
            messagebox.showinfo("Success", "Invoice generated successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to generate invoice: {e}")

    def clear_fields(self):
        """Clear all input fields."""
        self.customer_name.delete(0, tk.END)
        self.customer_email.delete(0, tk.END)
        self.service_description.delete(0, tk.END)
        self.service_amount.delete(0, tk.END)


if __name__ == "__main__":
    app = MainWindow()
    app.mainloop()
