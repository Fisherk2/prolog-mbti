from Modelo import BD
from Vista import ScreenCLI


class ViewModel:
    """
    Clase que manipula la interfaz grafica de nuestro programa.
    """

    def __init__(self, modelo: BD, vista: ScreenCLI):
        """
        Clase que manipula la interfaz grafica de nuestro programa.
        :param modelo: Modelo donde estara almacenado la informacion del programa.
        :param vista: Interfaz grafica que se estara manipulando.
        """
        self.dataBase: BD = modelo
        self.view: ScreenCLI = vista

    def deformatearNombre(self, cadena: str) -> str:
        """
        Funcion que transforma un nombre personal y lo transforma a un estilo snake_text
        :param cadena: Texto que se desea transformar.
        :return: Cadena con un estilo snake_text.
        """
        # Dividimos por espacios
        palabras = cadena.split(' ')

        # Regresamos a minusculas las palabras
        palabrasMinusculas = []
        for palabra in palabras:
            palabrasMinusculas.append(palabra.lower())

        # Se une las palabras en minusculas con un guion bajo
        nombreDeformateado = '_'.join(palabrasMinusculas)

        return nombreDeformateado

    def deFormatearTexto(self, cadena: str) -> str:
        """
        Funcion que transforma un nombre personal y lo transforma a un estilo snake_text
        :param cadena: Texto que se desea transformar.
        :return: Cadena con un estilo snake_text.
        """
        return cadena.replace(" ", "_").lower()
    def formatearNombre(self, cadena: str) -> str:
        """
        Funcion que transforma un texto en un nombre personal.
        :param cadena: Texto que se desea transformar-
        :return: Cadena de texto con un formato de nombre personal.
        """
        # Dividimos por guiones bajos
        palabras = cadena.split('_')

        # Capitalizamos la primera letra de cada palabra
        palabrasCapitalizadas = []
        for palabra in palabras:
            palabrasCapitalizadas.append(palabra.capitalize())

        # Se une las palabras capitalizadas con un espacio
        nombreReformateado = ' '.join(palabrasCapitalizadas)

        return nombreReformateado

    def formatearTexto(self, cadena: str) -> str:
        """
        Funcion que elimina guiones bajos y hace la primer letra mayuscula.
        :param cadena: Texto que se desea transformar
        :return: Cadena con guiones bajos eliminados que empiezan con mayuscula.
        """
        return cadena.replace("_", " ").capitalize()

    # ---------------------------------------Control de vistas----------------------------------------#
    def init(self):
        self.view.mostrarIntroduccion()
        self.listarComandos()

    def listarComandos(self):
        comando: int = 0
        while (comando != 12):
            self.view.mostrarComandos()
            # Mostrara prompts hasta que el usuario desee salir de la aplicacion.
            try:
                comando = int(input("¿Que deseas hacer? [1-12] ---> "))
                self.ejecutarComando(comando=comando)
            except(TypeError, Exception):
                print("Error, porfavor, intenta ingresar un comando de valor numerico [1-12]")

    def listarPersonalidades(self):
        textosFormateados: dict = {}
        for comando, mbti in self.dataBase.listarMBTIs().items():
            textosFormateados[comando] = self.formatearTexto(mbti)

        self.view.mostrarMBTIs(map_MBTIs=textosFormateados)

    def listarTiposCompatibles(self):
        textosFormateados: dict = {}
        for comando, compatibilidad in self.dataBase.listarTipoCompatibilidad().items():
            textosFormateados[comando] = self.formatearTexto(compatibilidad)

        self.view.mostrarCompatibilidades(map_Compatiblidades=textosFormateados)

    def listarPersonasRegistradas(self):
        textosFormateados: list[str] = []
        for persona in self.dataBase.listarPersonas():
            textosFormateados.append(self.formatearNombre(persona))

        self.view.mostrarPersonasRegistradas(lista_nombres=textosFormateados)

    def ejecutarComando(self, comando: int):
        # 1) ¿Que tipo de personalidad pertenece al MBTI en cuestion?.
        if (comando == 1):
            self.listarPersonalidades()
            try:
                prompt: int = int(input("Ingrese el MBTI [1-16] ---> "))
                mbti: str = self.dataBase.listarMBTIs()[prompt]  # Obtenemos el MBTI ingresado
                self.view.mostrarConsulta(self.formatearTexto(self.dataBase.quePersonalidadEs(mbti=mbti)))
            except(TypeError, Exception):
                print("Error, porfavor, intenta ingresar un comando de valor numerico correcto [1-16]")

        # 2) ¿Que tipo de MBTI pertenede a X persona de la lista disponible de la base de datos?.
        if (comando == 2):
            self.listarPersonasRegistradas()
            try:
                prompt: str = input("¿Cual es tu MBTI? Ingrese su nombre ---> ")
                self.view.mostrarConsulta(
                    self.formatearTexto(self.dataBase.queMBTIes(nombre=self.deformatearNombre(prompt))))
            except(TypeError, Exception):
                print("Error, porfavor, intenta ingresar un comando correcto (Verifica su nombre)")

        # 3) ¿Que caracteristicas pertenece al MBTI?.
        if (comando == 3):
            self.listarPersonalidades()
            try:
                prompt: int = int(input("Ingrese el MBTI [1-16] ---> "))
                mbti: str = self.dataBase.listarMBTIs()[prompt]  # Obtenemos el MBTI ingresado
                self.view.mostrarConsulta(self.formatearTexto(self.dataBase.acercaDe(mbti=mbti)))
            except(TypeError, Exception):
                print("Error, porfavor, intenta ingresar un comando de valor numerico correcto [1-16]")

        # 4) ¿Que tan compatible es tu MBTI con otro?.
        if (comando == 4):
            self.listarPersonalidades()
            try:
                prompt1: int = int(input("Ingrese su  MBTI [1-16] ---> "))
                mbti1: str = self.dataBase.listarMBTIs()[prompt1]  # Obtenemos el MBTI ingresado
                prompt2: int = int(input("Ingrese el otro  MBTI [1-16] ---> "))
                mbti2: str = self.dataBase.listarMBTIs()[prompt2]  # Obtenemos el MBTI ingresado
                self.view.mostrarConsulta(
                    self.formatearTexto(self.dataBase.queTanCompatibleEs(mbti_1=mbti1, mbti_2=mbti2)))
            except(TypeError, Exception):
                print("Error, porfavor, intenta ingresar un comando de valor numerico correcto [1-16]")

        # 5) ¿Que tan compatible eres con una persona?.
        if (comando == 5):
            self.listarPersonasRegistradas()
            try:
                prompt1: str = input("Ingrese su nombre ---> ")
                prompt2: str = input("Ingrese el otro nombre ---> ")
                self.view.mostrarConsulta(
                    self.formatearTexto(self.dataBase.queCompatibleEresCon(tu_nombre=self.deformatearNombre(prompt1),
                                                                           otro_nombre=self.deformatearNombre(
                                                                               prompt2))))
            except(TypeError, Exception):
                print("Error, porfavor, intenta ingresar un comando correcto (Verifica su nombre)")

        # 6) ¿Que personas pertenecen a tal MBTI?.
        if (comando == 6):
            self.listarPersonalidades()
            try:
                prompt: int = int(input("Ingrese el MBTI [1-16] ---> "))
                mbti: str = self.dataBase.listarMBTIs()[prompt]  # Obtenemos el MBTI ingresado

                resultado: str = "[ " + self.formatearTexto(mbti) + " ]\n"
                for nombre in self.dataBase.personasTipoMBTI(mbti=mbti):
                    resultado += self.formatearNombre(nombre) + "\n"

                self.view.mostrarConsulta(resultado)
            except(TypeError, Exception):
                print("Error, porfavor, intenta ingresar un comando de valor numerico correcto [1-16]")

        # 7) ¿Que personas comparten tu mismo MBTI?.
        if (comando == 7):
            self.listarPersonasRegistradas()
            try:
                prompt: str = input("Ingrese su nombre ---> ")

                resultado: str = "[ " + self.formatearNombre(prompt) + " ]\n"
                for nombre in self.dataBase.personalidadCompartidaCon(nombre=self.deformatearNombre(prompt)):
                    resultado += self.formatearNombre(nombre) + "\n"

                self.view.mostrarConsulta(resultado)
            except(TypeError, Exception):
                print("Error, porfavor, intenta ingresar un comando correcto (Verifica su nombre)")

        # 8) ¿Que MBTIs tienen una X compatibilidad contigo?.
        if (comando == 8):
            self.listarPersonasRegistradas()
            self.listarTiposCompatibles()
            try:
                prompt1: str = input("Ingrese su nombre ---> ")
                prompt2: int = int(input("Ingrese la compatibilidad [1-5] ---> "))
                compatibilidad: str = self.dataBase.listarTipoCompatibilidad()[
                    prompt2]  # Obtenemos la compatibilidad ingresada

                resultado: str = "[ " + self.formatearNombre(prompt1) + " ][ " + self.formatearTexto(
                    compatibilidad) + " ]\n"

                for nombre in self.dataBase.queMBTIsTienesCompatibilidad(nombre=self.deformatearNombre(prompt1),
                                                                         compatibilidad=compatibilidad):
                    resultado += self.formatearNombre(nombre) + "\n"

                self.view.mostrarConsulta(resultado)
            except(TypeError, Exception):
                print("Error, porfavor, intenta ingresar un comando correcto (Verifica su nombre)")
                print("Error, porfavor, intenta ingresar un comando de valor numerico correcto [1-5]")

        # 9) ¿Que personas tienen X compatibilidad con la tuya?.
        if (comando == 9):
            self.listarPersonasRegistradas()
            self.listarTiposCompatibles()
            try:
                prompt1: str = input("Ingrese su nombre ---> ")
                prompt2: int = int(input("Ingrese la compatibilidad [1-5] ---> "))
                compatibilidad: str = self.dataBase.listarTipoCompatibilidad()[
                    prompt2]  # Obtenemos la compatibilidad ingresada

                resultado: str = "[ " + self.formatearNombre(prompt1) + " ][ " + self.formatearTexto(
                    compatibilidad) + " ]\n"

                for nombre in self.dataBase.quePersonasTienesCompatibilidad(nombre=self.deformatearNombre(prompt1),
                                                                            compatibilidad=compatibilidad):
                    resultado += self.formatearNombre(nombre) + "\n"

                self.view.mostrarConsulta(resultado)
            except(TypeError, Exception):
                print("Error, porfavor, intenta ingresar un comando correcto (Verifica su nombre)")
                print("Error, porfavor, intenta ingresar un comando de valor numerico correcto [1-5]")

        # 10) Lista todas la personas que se encuentran en la base de datos.
        if (comando == 10):
            self.listarPersonasRegistradas()
        # 11) Lista los tipos de compatibilidad de los MBTI.
        if (comando == 11):
            self.listarPersonasRegistradas()
        # 12) Salir
        if (comando == 12):
            print("Hasta pronto :]")


# -----------------------------------------------PRUEBAS--------------------------------------#
if __name__ == '__main__':
    controlador = ViewModel(modelo=BD("bd"), vista=ScreenCLI())

    print(controlador.formatearNombre("fisher_price"))
    print(controlador.deformatearNombre("Fisher Price"))

    print(controlador.formatearTexto("mala_idea"))
    print(controlador.formatearTexto("racional"))

    controlador.listarTiposCompatibles()
    controlador.listarPersonalidades()
    controlador.listarPersonasRegistradas()
