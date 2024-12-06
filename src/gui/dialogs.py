import tkinter as tk
from tkinter import messagebox
import customtkinter as ctk


class Dialogs:
    """Class to handle various dialog boxes."""

    @staticmethod
    def show_info(title, message):
        """Displays an information dialog."""
        messagebox.showinfo(title, message)

    @staticmethod
    def show_warning(title, message):
        """Displays a warning dialog."""
        messagebox.showwarning(title, message)

    @staticmethod
    def show_error(title, message):
        """Displays an error dialog."""
        messagebox.showerror(title, message)

    @staticmethod
    def ask_question(title, message):
        """Displays a yes/no question dialog and returns the result."""
        return messagebox.askyesno(title, message)

    @staticmethod
    def custom_message(title, message, parent):
        """Displays a custom dialog box using CustomTkinter."""
        dialog = ctk.CTkToplevel(parent)
        dialog.title(title)
        dialog.geometry("300x150")
        dialog.resizable(False, False)

        # Message label
        label = ctk.CTkLabel(dialog, text=message, wraplength=280, font=("Arial", 12))
        label.pack(pady=20)

        # OK button
        button = ctk.CTkButton(dialog, text="OK", command=dialog.destroy)
        button.pack(pady=10)

        # Center the dialog
        dialog.transient(parent)
        dialog.grab_set()
        parent.wait_window(dialog)

    @staticmethod
    def about_dialog(parent):
        """Displays an About dialog box."""
        features = """
        Features:
        - Generate Invoice
        - Invoice History
        - Phone Number Validation
        - Service and Amount Input
        """
        about_message = f"""
        Invoice Generator v1.0
        Developed by Pedro Dominguez

        {features.strip()}
        """
        dialog = ctk.CTkToplevel(parent)
        dialog.title("About")
        dialog.geometry("400x300")
        dialog.resizable(False, False)

        # About label
        label = ctk.CTkLabel(dialog, text=about_message, wraplength=380, justify="left", font=("Arial", 12))
        label.pack(pady=20, padx=10)

        # OK button
        button = ctk.CTkButton(dialog, text="OK", command=dialog.destroy)
        button.pack(pady=10)

        # Center the dialog
        dialog.transient(parent)
        dialog.grab_set()
        parent.wait_window(dialog)
