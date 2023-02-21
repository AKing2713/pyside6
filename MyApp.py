import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QVBoxLayout, QWidget

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        
        # Set the window title
        self.setWindowTitle("My App")

        # A simple label
        self.label = QLabel()

        # Set input box
        self.input = QLineEdit()
        # Connects to the label and changes the text based on what the user types
        self.input.textChanged.connect(self.label.setText)

        # Define a layout
        layout = QVBoxLayout()
        layout.addWidget(self.input)
        layout.addWidget(self.label)

        # Create a custom widget
        container = QWidget()
        container.setLayout(layout)

        # Set the central widget of the Window.
        self.setCentralWidget(container)

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()