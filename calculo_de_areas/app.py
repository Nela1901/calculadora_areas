"""
Módulo principal de ejecución de la aplicación Calculadora de Áreas.

Este script inicializa la aplicación PyQt6, carga la interfaz gráfica desde
la clase `Dialogo` (que conecta la lógica con la interfaz), y muestra la ventana principal.
"""

import sys
from PyQt6.QtWidgets import QApplication
from src.vista.GUI_ui import Dialogo


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = Dialogo()
    ventana.show()
    sys.exit(app.exec())
