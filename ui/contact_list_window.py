"""The module defines the ContactListWindow class."""

from ui.base.main_window import MainWindow

__author__ = "Abhimanyu"
__version__ = "1.0.0"

class ContactListWindow(MainWindow):
    """Represents a window for managing a list of contacts."""

    def __init__(self) -> None:
        """Initializes a new instance of the ContactListWindow class."""

        super().__init__()

        self.setWindowTitle("Contact Manager")
        self.__initialize_widgets()

    def __initialize_widgets(self) -> None:
        """Sets the widgets on the window to their initial state."""

        self._name_line_edit.setPlaceholderText("Contact Name")
        self._phone_line_edit.setInputMask("(000) 000-0000;_")

        self._add_button.setDefault(True)
        self._add_button.setEnabled(False)
        self._remove_button.setEnabled(False)