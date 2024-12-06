class Settings:
    """Class to hold application settings."""

    def __init__(self):
        self.app_name = "Invoice Generator"
        self.default_width = 800
        self.default_height = 600
        self.theme = "dark"  # Options: "dark", "light"
        self.menu_font = ("Arial", 22)
        self.gui_font = ("Arial", 20)

    def get_window_size(self):
        """Returns the default window dimensions."""
        return f"{self.default_width}x{self.default_height}"