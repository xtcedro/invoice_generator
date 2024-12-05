import tkinter as tk
from tkinter import Menu, ttk
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

        # Add tabs to the main window
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
        """Creates tabs for the main application."""
        tab_control = ttk.Notebook(self.root)

        # Generate Invoice Tab
        generate_invoice_tab = ctk.CTkFrame(tab_control)
        tab_control.add(generate_invoice_tab, text="Generate Invoice")
        self.create_generate_invoice_tab(generate_invoice_tab)

        # Invoice History Tab
        invoice_history_tab = ctk.CTkFrame(tab_control)
        tab_control.add(invoice_history_tab, text="Invoice History")
        self.create_invoice_history_tab(invoice_history_tab)

        # Placeholder for the third tab
        third_tab = ctk.CTkFrame(tab_control)
        tab_control.add(third_tab, text="Placeholder Tab")
        self.create_placeholder_tab(third_tab)

        tab_control.pack(expand=True, fill="both")

    def create_generate_invoice_tab(self, parent):
        """Creates the content for the 'Generate Invoice' tab."""
        label = ctk.CTkLabel(parent, text="Generate Invoice", font=self.settings.gui_font)
        label.pack(pady=10)

    def create_invoice_history_tab(self, parent):
        """Creates the content for the 'Invoice History' tab."""
        label = ctk.CTkLabel(parent, text="Invoice History", font=self.settings.gui_font)
        label.pack(pady=10)

    def create_placeholder_tab(self, parent):
        """Creates the content for the placeholder tab."""
        label = ctk.CTkLabel(parent, text="Placeholder Tab Content", font=self.settings.gui_font)
        label.pack(pady=10)


# For testing purposes
if __name__ == "__main__":
    root = tk.Tk()
    app = MainWindow(root)
    root.mainloop()
