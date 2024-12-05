# main.py

import tkinter as tk
from src.gui.main_window import MainWindow

def main():
    """Entry point for the application."""
    root = tk.Tk()
    app = MainWindow(root)
    root.mainloop()

if __name__ == "__main__":
    main()