from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QFormLayout, QRadioButton, QComboBox, QGroupBox, QFrame
import sys

class RegistrationUI(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
    
    def init_ui(self):
        identity_group = QGroupBox("Identitas (vertical box layout)")
        identity_layout = QVBoxLayout()
        identity_layout.addWidget(QLabel("Nama : Putra Heryan Gagah Perkasa"))
        identity_layout.addWidget(QLabel("Nim : F1D022087"))
        identity_layout.addWidget(QLabel("Kelas : C"))
        identity_group.setLayout(identity_layout)

        nav_layout = QHBoxLayout()
        nav_layout.addWidget(QPushButton("Home"))
        nav_layout.addWidget(QPushButton("About"))
        nav_layout.addWidget(QPushButton("Contact"))
        nav_frame = QFrame()
        nav_frame.setLayout(nav_layout)

        form_group = QGroupBox("User Registration (form layout)")
        form_layout = QFormLayout()
        self.full_name = QLineEdit()
        self.email = QLineEdit()
        self.phone = QLineEdit()
        
        gender_layout = QHBoxLayout()
        self.male_radio = QRadioButton("Male")
        self.female_radio = QRadioButton("Female")
        gender_layout.addWidget(self.male_radio)
        gender_layout.addWidget(self.female_radio)
        
        self.country_combo = QComboBox()
        self.country_combo.addItems(["Select Country", "Canada", "America", "Indonesia", "Malaysia"])
        
        form_layout.addRow("Full Name:", self.full_name)
        form_layout.addRow("Email:", self.email)
        form_layout.addRow("Phone:", self.phone)
        form_layout.addRow("Gender:", gender_layout)
        form_layout.addRow("Country:", self.country_combo)
        form_group.setLayout(form_layout)

        action_layout = QHBoxLayout()
        action_layout.addWidget(QPushButton("Submit"))
        action_layout.addWidget(QPushButton("Cancel"))
        action_frame = QFrame()
        action_frame.setLayout(action_layout)

        main_layout = QVBoxLayout()
        main_layout.addWidget(identity_group)
        main_layout.addWidget(nav_frame)
        main_layout.addWidget(form_group)
        main_layout.addWidget(action_frame)
        
        self.setLayout(main_layout)
        self.setWindowTitle("User Registration Form")
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = RegistrationUI()
    window.show()
    sys.exit(app.exec())
