# import os

# tiempo = input("En cuantas horas deseas apagar?")
# tiempo = float(tiempo)


# # tiempo en segundos después del cual se apagará la computadora
# tiempo = 60 * 60 * tiempo
# tiempo = int(tiempo)


# # ejecutar el comando de apagado
# os.system(f"shutdown /s /t {tiempo}")
# print("Apagado en ", tiempo, "segundos") 

import os
import sys
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Crear widgets
        self.horas_label = QLabel("Horas:")
        self.horas_spinbox = QSpinBox()
        self.horas_spinbox.setRange(0, 23)

        self.minutos_label = QLabel("Minutos:")
        self.minutos_spinbox = QSpinBox()
        self.minutos_spinbox.setRange(0, 59)

        self.autoapagar_button = QPushButton("Autoapagar")
        self.autoapagar_button.setStyleSheet("background-color: #4CAF50; color: white; border-radius: 5px;")
        self.autoapagar_button.clicked.connect(self.autoapagar)

        self.cancelar_button = QPushButton("Cancelar")
        self.cancelar_button.setStyleSheet("background-color: #f44336; color: white; border-radius: 5px;")
        self.cancelar_button.clicked.connect(self.cancelar)

        # Crear layout
        layout = QVBoxLayout()
        layout.addWidget(self.horas_label)
        layout.addWidget(self.horas_spinbox)
        layout.addWidget(self.minutos_label)
        layout.addWidget(self.minutos_spinbox)

        buttons_layout = QHBoxLayout()
        buttons_layout.addWidget(self.autoapagar_button)
        buttons_layout.addWidget(self.cancelar_button)

        layout.addLayout(buttons_layout)

        # Crear widget central
        widget = QWidget()
        widget.setLayout(layout)

        # Establecer widget central
        self.setCentralWidget(widget)

    def autoapagar(self):
        horas = self.horas_spinbox.value()
        minutos = self.minutos_spinbox.value()

        # Crear comando para autoapagar Windows
        comando = f"shutdown /s /t {horas*3600 + minutos*60}"

        # Ejecutar comando
        import os
        os.system(comando)

    def cancelar(self):
        # Crear comando para cancelar el autoapagado de Windows
        comando = "shutdown /a"

        # Ejecutar comando
        os.system(comando)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


