class ScreenCLI:
    """
    Clase que muestra de manera grafica en la consola las opciones que tiene el usuario.
    """

    def mostrarIntroduccion(self):
        print("""
                ==========================================================
                                  Bienvenido
            ==========================================================
            El Indicador de Tipos de Myers-Briggs (MBTI) es una herramienta
            que categoriza a las personas en 16 tipos de personalidad, 
            basándose en cómo perciben el mundo y toman decisiones.
                """)

    def mostrarMBTIs(self, map_MBTIs: dict):
        print("""
==========================================================
                Personalidades disponibles
==========================================================
                        """)
        for comando, mbti in map_MBTIs.items():
            print(str(comando) + ") " + mbti)

    def mostrarCompatibilidades(self, map_Compatiblidades: dict):
        print("""
==========================================================
                Compatibilidades disponibles
 ==========================================================
                        """)
        for comando, compatibilidad in map_Compatiblidades.items():
            print(str(comando) + ") " + compatibilidad)

    def mostrarPersonasRegistradas(self, lista_nombres: list):
        print("""
==========================================================
                Personas disponibles
==========================================================
                        """)
        for persona in lista_nombres:
            print(persona)

    def mostrarComandos(self):
        print("""
    A continuacion, ingresa la opcion numerica de lo que quieras
    consultar de la base de datos:

    1) ¿Que tipo de personalidad pertenece al MBTI en cuestion?.
    2) ¿Que tipo de MBTI pertenede a X persona de la lista disponible de la base de datos?.
    3) ¿Que caracteristicas pertenece al MBTI?.
    4) ¿Que tan compatible es tu MBTI con otro?.
    5) ¿Que tan compatible eres con una persona?.
    6) ¿Que personas pertenecen a tal MBTI?.
    7) ¿Que personas comparten tu mismo MBTI?.
    8) ¿Que MBTIs tienen una X compatibilidad contigo?.
    9) ¿Que personas tienen X compatibilidad con la tuya?.
    10) Lista todas la personas que se encuentran en la base de datos.
    11) Lista los tipos de compatibilidad de los MBTI.
    12) Salir
    """)

    def mostrarConsulta(self, resultado: str):
        print("------------------------------------------------------------------------")
        print("Resultado ====> ",resultado)
        print("------------------------------------------------------------------------")

# -----------------------------------------------PRUEBAS--------------------------------------#
if __name__ == '__main__':
    ...