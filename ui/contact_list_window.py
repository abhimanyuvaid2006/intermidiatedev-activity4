"""The module defines the ContactListWindow class."""



from PySide6.QtCore import Slot
from PySide6.QtWidgets import QMessageBox, QTableWidgetItem

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

        self._name_line_edit.textChanged.connect(self.__on_input_changed)
        self._phone_line_edit.textChanged.connect(self.__on_input_changed)

        self._add_button.clicked.connect(self.__on_add_button_clicked)

        self._contact_table.itemSelectionChanged.connect(
            self.__on_table_selection_changed)

        self._remove_button.clicked.connect(self.__on_remove_button_clicked)

    @Slot()
    def __on_input_changed(self) -> None:
        """Handles the changed events for the name and phone line edits."""

        phone = self._phone_line_edit.text()
        phone = phone.replace("(", "").replace(")", "").replace("-", "")
        phone = phone.replace(" ", "").replace("_", "")

        self._add_button.setEnabled(False)

        if self._name_line_edit.text().strip() != "" and len(phone) == 10:
            self._add_button.setEnabled(True)

    @Slot()
    def __on_add_button_clicked(self) -> None:
        """Handles the clicked event of the add button."""

        name = self._name_line_edit.text().strip()
        phone = self._phone_line_edit.text()

        row = self._contact_table.rowCount()
        self._contact_table.insertRow(row)

        name_item = QTableWidgetItem()
        name_item.setText(name)
        phone_item = QTableWidgetItem()
        phone_item.setText(phone)

        self._contact_table.setItem(row, 0, name_item)
        self._contact_table.setItem(row, 1, phone_item)

        self._name_line_edit.setText("")
        self._phone_line_edit.setText("")
        self._name_line_edit.setFocus()

    @Slot()
    def __on_table_selection_changed(self) -> None:
        """Handles the item selection changed event of the table."""

        self._remove_button.setEnabled(False)

        if len(self._contact_table.selectedItems()) != 0:
            self._remove_button.setEnabled(True)

    @Slot()
    def __on_remove_button_clicked(self) -> None:
        """Handles the clicked event of the remove button."""

        row = self._contact_table.selectedItems()[0].row()
        name = self._contact_table.item(row, 0).text()

        message_box = QMessageBox()
        message_box.setWindowTitle("Remove Contact")
        message_box.setText(f"Do you want to remove the contact {name}?")
        message_box.setIcon(QMessageBox.Icon.Question)
        message_box.setStandardButtons(QMessageBox.StandardButton.Yes |
                                       QMessageBox.StandardButton.No)
        message_box.setDefaultButton(QMessageBox.StandardButton.No)

        answer = message_box.exec()

        if answer == QMessageBox.StandardButton.Yes:
            self._contact_table.removeRow(row)