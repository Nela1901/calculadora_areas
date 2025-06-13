"""
Contiene funciones para calcular el área de figuras geométricas básicas.
"""


class CalculadoraAreas:
    """
    Clase con métodos estáticos para calcular áreas.
    """

    @staticmethod
    def area_circulo(radio: float) -> float:
        """
        Calcula el área de un círculo.

        :param radio: Radio del círculo
        :return: Área calculada
        """
        return 3.1416 * radio**2

    @staticmethod
    def area_triangulo(base: float, altura: float) -> float:
        """
        Calcula el área de un triángulo.

        :param base: Base del triángulo
        :param altura: Altura del triángulo
        :return: Área calculada
        """
        return (base * altura) / 2

    @staticmethod
    def area_rectangulo(base: float, altura: float) -> float:
        """
        Calcula el área de un rectángulo.

        :param base: Base del rectángulo
        :param altura: Altura del rectángulo
        :return: Área calculada
        """
        return base * altura

    @staticmethod
    def area_cuadrado(lado: float) -> float:
        """
        Calcula el área de un cuadrado.

        :param lado: Longitud del lado
        :return: Área calculada
        """
        return lado**2
