# /src/gui/main_window.py

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

        button = ctk.CTkButton(parent, text="Create New Invoice", command=self.new_invoice)
        button.pack(pady=10)

    def create_invoice_history_tab(self, parent):
        """Creates the content for the 'Invoice History' tab."""
        label = ctk.CTkLabel(parent, text="Invoice History", font=self.settings.gui_font)
        label.pack(pady=10)

        button = ctk.CTkButton(parent, text="View History", command=self.view_history)
        button.pack(pady=10)

    def new_invoice(self):
        """Placeholder function for creating a new invoice."""
        print("New Invoice button clicked!")

    def view_history(self):
        """Placeholder function for viewing invoice history."""
        print("View History button clicked!")


# For testing purposes
if __name__ == "__main__":
    root = ctk.CTk()
    app = MainWindow(root)
    root.mainloop()