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

        # Add a simple frame using CustomTkinter
        self.main_frame = ctk.CTkFrame(self.root)
        self.main_frame.pack(fill="both", expand=True, padx=10, pady=10)

        # Add a sample label
        self.label = ctk.CTkLabel(self.main_frame, text="Welcome to the Invoice Generator!", font=self.settings.gui_font)
        self.label.pack(pady=20)

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

# For testing purposes
if __name__ == "__main__":
    root = tk.Tk()
    app = MainWindow(root)
    root.mainloop()
