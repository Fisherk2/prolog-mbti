from pyswip import Prolog

class BD():
    """
    Clase que contiene la base de datos de prolog.
    """

    def __init__(self, nombre_fichero: str):
        """
        Clase que contiene la base de datos de prolog.
        :param nombre_fichero: Nombre del fichero .pl que se encuentra en la raiz del proyecto: <nombre_fichero>.pl
        """
        # Cargamos el archivo .pl
        self.p = Prolog()
        self.p.consult(nombre_fichero + ".pl")

    def quePersonalidadEs(self, mbti: str) -> str:
        """
        Funcion que consulta que tipo de personalidad pertenece al MBTI en cuestion.
        :param mbti: MBTI que se desea consultar.
        :return: La personalidad que pertenece a ese MBTI.
        """
        # Separamos por cada una de las caracteristicas de un MBTI
        mente = list(mbti)[0]
        energia = list(mbti)[1]
        naturaleza = list(mbti)[2]
        tactica = list(mbti)[3]

        consulta = self.p.query(
            "personalidad(" + mente + "," + energia + "," + naturaleza + "," + tactica + ", Personalidad)")
        # Como es un diccionario de tamaño 1, solo ocupamos el primer indice y su clave
        rawString: str = list(consulta)[0]["Personalidad"]
        # Devolvemos la cadena sin guion bajo y empezando con mayuscula.
        return rawString

    def queMBTIes(self, nombre: str) -> str:
        """
        Funcion que determina que tipo de MBTI pertenede a X persona de la lista disponible de la base de datos.
        :param nombre: Nombre de la persona que se encuentra en la base de datos.
        :return: MBTI de la persona consultada.
        """
        consulta = self.p.query("personas(" + nombre + ", MBTI)")
        # Como es un diccionario de tamaño 1, solo ocupamos el primer indice y su clave
        rawString: str = list(consulta)[0]["MBTI"]
        # Devolvemos la cadena sin guion bajo y empezando con mayuscula.
        return rawString

    def acercaDe(self, mbti: str) -> str:
        """
        Funcion que consulta que caracteristicas pertenece al MBTI.
        :param mbti: MBTI a consultar.
        :return: Un arreglo de caracteristicas que pertenece al MBTI.
        """
        # Separamos por cada una de las caracteristicas de un MBTI
        mente = list(mbti)[0]
        energia = list(mbti)[1]
        naturaleza = list(mbti)[2]
        tactica = list(mbti)[3]

        # Consultas ya convertidas a una cadena cruda.
        mind: str = list(self.p.query("mente(M, " + mente + ")"))[0]["M"]
        energy: str = list(self.p.query("energia(E, " + energia + ")"))[0]["E"]
        nature: str = list(self.p.query("naturaleza(N, " + naturaleza + ")"))[0]["N"]
        tactic: str = list(self.p.query("tactica(T, " + tactica + ")"))[0]["T"]
        return mind + ", " + energy + ", " + nature + ", " + tactic

    def queTanCompatibleEs(self, mbti_1: str, mbti_2: str) -> str:
        """
        Funcion que determina que tan compatible es un MBTI con otro.
        :param mbti_1: MBTI a comparar.
        :param mbti_2: MBTI a comparar.
        :return: Que tan compatible es entre el primer y segundo MBTI.
        """
        consulta = self.p.query("queTanCompatible(" + mbti_1 + ", " + mbti_2 + ", Compatibilidad)")
        # Como es un diccionario de tamaño 1, solo ocupamos el primer indice y su clave
        rawString: str = list(consulta)[0]["Compatibilidad"]
        # Devolvemos la cadena sin guion bajo y empezando con mayuscula.
        return rawString

    def queCompatibleEresCon(self, tu_nombre: str, otro_nombre: str) -> str:
        """
        Funcion que determina que tan compatible eres con una persona.
        :param tu_nombre: Tu nombre que quieres consultar.
        :param otro_nombre: El nombre de la persona que quieres comparar.
        :return: Nivel de compatibilidad entre esas dos personas.
        """
        consulta = self.p.query("queCompatibleEresCon(" + tu_nombre + ", " + otro_nombre + ", Compatibilidad)")
        # Como es un diccionario de tamaño 1, solo ocupamos el primer indice y su clave
        rawString: str = list(consulta)[0]["Compatibilidad"]
        # Devolvemos la cadena sin guion bajo y empezando con mayuscula.
        return rawString

    def personasTipoMBTI(self, mbti: str) -> list[str]:
        """
        Funcion que consulta que personas pertenecen a tal MBTI.
        :param mbti: El MBTI a consultar.
        :return: Lista de personas que pertenecen al MBTI.
        """
        consulta = self.p.query("personasTipoMBTI(" + mbti + ", Personas)")
        lista: list[str] = []

        # Devuelve el diccionario
        for solucion in list(consulta):
            # Devuelve una solucion con un arreglo en Prolog
            for persona in solucion["Personas"]:
                # Agarramos elemento por elemento y lo agregamos a la lista.
                lista.append((str(persona)))

        return lista

    def personalidadCompartidaCon(self, nombre: str) -> list[str]:
        """
        Funcion que consulta que personas comparten tu mismo MBTI.
        :param nombre: Tu nombre a consultar.
        :return: Lista de personas que pertenecen a tu MBTI.
        """
        consulta = self.p.query("personalidadCompartidaCon(" + nombre + ", Personas)")
        lista: list[str] = []

        # Devuelve el diccionario
        for solucion in list(consulta):
            # Devuelve una solucion con un arreglo en Prolog
            for persona in solucion["Personas"]:
                # Agarramos elemento por elemento y lo agregamos a la lista.
                lista.append((str(persona)))

        return lista

    def queMBTIsTienesCompatibilidad(self, nombre: str, compatibilidad: str) -> list[str]:
        """
        Funcion que consulta que MBTIs tienen una X compatibilidad contigo.
        :param nombre: El nombre a consultar.
        :param compatibilidad: Nivel de compatibilidad a consultar.
        :return: Lista de MBTIs que tienen la compatibilidad consultada.
        """
        consulta = self.p.query("queMBTIsTienesCompatibilidad(" + nombre + ", " + compatibilidad + ", MBTIs)")
        lista: list[str] = []

        # Devuelve el diccionario
        for solucion in list(consulta):
            # Devuelve una solucion con un arreglo en Prolog
            for mbti in solucion["MBTIs"]:
                # Agarramos elemento por elemento y lo agregamos a la lista.
                lista.append((str(mbti)))

        return lista

    def quePersonasTienesCompatibilidad(self, nombre: str, compatibilidad: str) -> list[str]:
        """
        Funcion que consulta las personas que tienen X compatibilidad con la tuya.
        :param nombre: El nombre a consultar.
        :param compatibilidad: Nivel de compatibilidad a consultar.
        :return: Lista de personas que son X compatibilidad con el nombre de la persona.
        """
        # Obtenemos los MBTIs que tienen X compatibilidad con el nombre.
        listaMBTIs: list[str] = self.queMBTIsTienesCompatibilidad(nombre=nombre, compatibilidad=compatibilidad)

        listaNombres: list[str] = []

        # Por cada MBTI, extraemos las personas que pertenezcan a dicho MBTI.
        for mbti in listaMBTIs:
            for persona in self.personasTipoMBTI(mbti):
                listaNombres.append(persona)

        return listaNombres

    def listarPersonas(self) -> list[str]:
        """
        Metodo que lista todas la personas que se encuentran en la base de datos.
        :return: Lista de personas de la base de datos.
        """
        consulta = self.p.query("listarPersonas(Personas)")
        lista: list[str] = []

        # Devuelve el diccionario
        for solucion in list(consulta):
            # Devuelve una solucion con un arreglo en Prolog
            for persona in solucion["Personas"]:
                # Agarramos elemento por elemento y lo agregamos a la lista.
                lista.append((str(persona)))

        return lista

    def listarTipoCompatibilidad(self) -> dict:
        """
        Metodo que devuelve los tipos de compatibilidad de los MBTI.
        :return: Lista de tipos de compatibilidad.
        """
        consulta = self.p.query("listarTipoCompatibilidad(Compatibilidades)")
        compatibilidades: dict[int: str] = {}  # Diccionario que establece todas las compatibilidades

        # Devuelve el diccionario
        for solucion in list(consulta):
            # Devuelve una solucion con un arreglo en Prolog
            for i in range(len(solucion["Compatibilidades"])):
                # Generamos la clave valor de cada una de las compatibilidades {i: "compatibilidad"}
                compatibilidades[i + 1] = str(solucion["Compatibilidades"][i])

        return compatibilidades

    def listarMBTIs(self) -> dict:
        """
        Metodo que devuelve las 16 personalidades disponibles.
        :return: Lista de las 16 personalidades disponibles.
        """
        consulta = self.p.query(
            "personalidad(Mente, Energia, Naturaleza, Tactica, _)")  # El ultimo parametro no lo necesitamos

        personalidades: dict[int: str] = {}  # Diccionario que establece todas las 16 personalidades
        lista: list[str] = []

        # Devuelve el diccionario
        for solucion in list(consulta):
            # Agarramos elemento por elemento y lo agregamos a la lista.
            for i in range(len(solucion["Mente"])):
                # Por cada caracteristica, lo concatenamos y añadimos a la lista.
                lista.append(
                    str(
                        solucion["Mente"][i] +
                        solucion["Energia"][i] +
                        solucion["Naturaleza"][i] +
                        solucion["Tactica"][i]
                    )
                )

        # Generamos la clave valor de cada una de las personalidades {i: "mbti"}
        for i in range(len(lista)):
            personalidades[i + 1] = lista[i]

        return personalidades


# -----------------------------------------------PRUEBAS--------------------------------------#
if __name__ == '__main__':
    baseDatos = BD(nombre_fichero="bd")

    print(baseDatos.queTanCompatibleEs("estp", "istj"))
    print(type(baseDatos.queTanCompatibleEs("estp", "istj")))
    print(baseDatos.acercaDe("istj"))
    print(baseDatos.personasTipoMBTI("istj"))
    print(type(baseDatos.personasTipoMBTI("istj")))
    print(baseDatos.personalidadCompartidaCon("elon_musk"))
    print(baseDatos.queCompatibleEresCon("fisher", "elon_musk"))
    print(baseDatos.queMBTIsTienesCompatibilidad(nombre="fisher", compatibilidad="match_ideal"))
    print(baseDatos.listarPersonas())

    print(baseDatos.quePersonalidadEs("istj"))
    print(baseDatos.queMBTIes("fisher"))
    print(baseDatos.quePersonasTienesCompatibilidad(nombre="fisher", compatibilidad="unilateral"))
    print(baseDatos.listarMBTIs())

    print(baseDatos.listarTipoCompatibilidad())
