"""
Ventana principal conectada a la lógica de cálculo de áreas.

Este módulo define la clase `Dialogo`, que gestiona la interfaz gráfica y
conecta los eventos del menú con los métodos para calcular áreas geométricas.
"""

from PyQt6.QtWidgets import QMainWindow, QInputDialog, QMessageBox
from .ventana_areas import Ui_CalculadoraAreas
from calculo_de_areas.src.logica.CalculadoraAreas import CalculadoraAreas


class Dialogo(QMainWindow):
    """
    Clase principal que conecta la interfaz con los cálculos de área.
    """

    def __init__(self):
        """
        Inicializa la interfaz y conecta los botones del menú con sus respectivas funciones.
        """
        super().__init__()
        self.ui = Ui_CalculadoraAreas()
        self.ui.setupUi(self)

        # Conectar acciones del menú a métodos
        self.ui.actionArea_del_circulo.triggered.connect(self.calcular_area_circulo)
        self.ui.actionArea_del_triangulo.triggered.connect(self.calcular_area_triangulo)
        self.ui.actionArea_del_rectangulo.triggered.connect(self.calcular_area_rectangulo)
        self.ui.actionArea_del_cuadrado.triggered.connect(self.calcular_area_cuadrado)

    def calcular_area_circulo(self):
        """
        Solicita el radio del círculo, calcula el área y muestra el resultado.
        """
        radio, ok = QInputDialog.getDouble(self, "Área del Círculo", "Ingrese el radio:")
        if ok:
            area = CalculadoraAreas.area_circulo(radio)
            QMessageBox.information(self, "Resultado", f"Área del círculo: {area:.2f}")

    def calcular_area_triangulo(self):
        """
        Solicita la base y la altura del triángulo, calcula el área y muestra el resultado.
        """
        base, ok1 = QInputDialog.getDouble(self, "Área del Triángulo", "Ingrese la base:")
        if ok1:
            altura, ok2 = QInputDialog.getDouble(self, "Área del Triángulo", "Ingrese la altura:")
            if ok2:
                area = CalculadoraAreas.area_triangulo(base, altura)
                QMessageBox.information(self, "Resultado", f"Área del triángulo: {area:.2f}")

    def calcular_area_rectangulo(self):
        """
        Solicita la base y la altura del rectángulo, calcula el área y muestra el resultado.
        """
        base, ok1 = QInputDialog.getDouble(self, "Área del Rectángulo", "Ingrese la base:")
        if ok1:
            altura, ok2 = QInputDialog.getDouble(self, "Área del Rectángulo", "Ingrese la altura:")
            if ok2:
                area = CalculadoraAreas.area_rectangulo(base, altura)
                QMessageBox.information(self, "Resultado", f"Área del rectángulo: {area:.2f}")

    def calcular_area_cuadrado(self):
        """
        Solicita el lado del cuadrado, calcula el área y muestra el resultado.
        """
        lado, ok = QInputDialog.getDouble(self, "Área del Cuadrado", "Ingrese el lado:")
        if ok:
            area = CalculadoraAreas.area_cuadrado(lado)
            QMessageBox.information(self, "Resultado", f"Área del cuadrado: {area:.2f}")
