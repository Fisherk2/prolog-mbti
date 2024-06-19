"""
Tecnologico Nacional de México.
Instituto Tecnológico de León.
Materia: Programación Lógica y Funcional.
Alumnos:
Gómez Gaona Jessica Janet
Zúñiga Gómez José Alberto

Programa de exposición (Personalidades MBTI).

"""
from Controlador import ViewModel
from Modelo import BD
from Vista import ScreenCLI


def main() -> None:
    controlador = ViewModel(modelo=BD(nombre_fichero="bd"), vista=ScreenCLI())
    controlador.init()


if __name__ == '__main__':
    main()
