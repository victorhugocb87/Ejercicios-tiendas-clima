class Climas:
    def __init__(self):
        self.codigo = []
        self.ciudad = []
        self.temp_Minima = []
        self.temp_Maxima = []
        self.zona = []
        self.estado = []

    def menu(self):
        opciones = """
    **************MENU CLIMA DE BOLIVIA***********

            1.-REGISTRAR CIUDAD
            2.-MOSTRAR CLIMAS DE CIUDADES
            3-.MOSTRAR PROMEDIO DE TEMPERATURAS MINIMAS 
            4.-MOSTRAR TEMPERATURA MAS BAJA 
            5.-MOSTRAR TEMPERATURA MAS ALTA 
            6.-SALIR

        """
        print(opciones)
        elegir = int(input("Elija una opcion del menu: \n"))
        if (elegir == 1):
            print(self.agregarClima())
            self.volverMenu()
        elif (elegir == 2):
            print(self.mostrarClima())
            self.volverMenu()
        elif (elegir == 3):
            print(self.promedioMin())
            self.volverMenu()
        elif (elegir == 4):
            pass
        elif (elegir == 5):
            print(self.promedioMax())
            self.volverMenu()
        elif (elegir == 6):
            print("Gracias por utilizar el sistema")
        else:
            print("Elija una opcion del menu!")
            self.menu()

    def agregarClima(self):
        codigo = input("Agrege el Codigo para el departamento: \n")
        ciudad = input("Digite la ciudad : \n")
        temp_Minima = input("Temperatura minima: \n")
        temp_Maxima = input("Temperatura maxima: \n")
        zona = input("Digite la zona: \n")
        print(self.guardarClima(codigo, ciudad, temp_Minima, temp_Maxima, zona))
        agregarOtro = input("Desea agregar otro departamento? y/n \n")
        if (agregarOtro == 'y' or agregarOtro == 'Y'):
            self.agregarClima()
        return "Se Registro Exitosamente"

    def guardarClima(self, codigo, ciudad, temperaturaMinima, temperaturaMaxima, zona):
        self.codigo.append(codigo)
        self.ciudad.append(ciudad)
        self.temp_Minima.append(temperaturaMinima)
        self.temp_Maxima.append(temperaturaMaxima)
        self.zona.append(zona)
        self.estado.append(1)
        return "Departamento {} agregado correctamente".format(codigo)

    def mostrarClima(self):
        if (self.codigo):
            for posicion in range(len(self.zona)):
                self.descripcion(posicion)
            return "Departamento cargado correctamente"
        else:
            return "Todavia no hay datos registrados"

    def descripcion(self, posicion):
        print("********DEPARTAMENTO {} REGISTRADO DE CORRECTAMENTE********".format(self.codigo[posicion]))
        print("ciudad {}".format(self.ciudad[posicion]))
        print("Temperatura minima  {}".format(self.temp_Minima[posicion]))
        print("Temperatura maxima {}".format(self.temp_Maxima[posicion]))
        print("zona {}".format(self.zona[posicion]))
        print("******************BOLIVIA**************************")
        pass

    def volverMenu(self):
        eleccion = input("Desea volver al menu? s/n: \n")
        if (eleccion == "s" or eleccion == "S"):
            self.menu()

    def registrar(self):
        codigo = int(input("Agregue un codigo: \n"))
        ciudad = input("Agregar nueva ciudad: \n")
        minima = int(input("Tempertura minima: \n"))
        maxima = int(input("Temperatura maxima: \n"))
        zona = (input("agregue una zona"))
        print(self.guardar(codigo, ciudad, minima, maxima, zona))
        pass

    def guardar(self, codigo, ciudad, minima, maxima, zona):
        self.codigo.append(codigo)
        self.ciudad.append(ciudad)
        self.temp_Minima.append(minima)
        self.temp_Maxima.append(maxima)
        self.zona.append(zona)
        self.estado.append(1)
        return "Ciudad {} registrada exitosamente.!! ".format(ciudad)

    def mostrar(self):
        for i in range(len(self.ciudad)):
            self.detalle(i)
        return "**********************************"

    def detalle(self, posicion):
        print("Codigo de ciudad {} ".format(self.codigo[posicion]))
        print("Nombre de la ciudad: {} ".format(self.ciudad[posicion]))
        print("Temperatura Minima: {} ".format(self.temp_Minima[posicion]))
        print("Temperatura Maxima: {} ".format(self.temp_Maxima[posicion]))
        print("Zona: {} ".format(self.zona[posicion]))
        print("***********************************")

    def promedioMin(self, ):
        print("***Temperaturas minimas***")
        for i in range(len(self.zona)):
            print(self.temp_Minima[i], ("  "), self.zona[i])
        suma = 0
        for i in range(len(self.zona)):
            suma += self.temp_Minima[i]
        return "*********"

    def promedioMax(self, ):
        print("***TEmperaturas maximas***")
        for i in range(len(self.zona)):
            print(self.temp_Maxima[i], ("  "), self.zona[i])
        suma = 0
        for i in range(len(self.zona)):
            suma += self.temp_Maxima[i]
        pass


climas = Climas()
climas.guardar(1, "SANTA CRUZ", 15, 29, "Llano")
climas.guardar(2, "BENI", 17, 31, "Llano")
climas.guardar(3, "PANDO", 18, 30, "Llano")
climas.guardar(4, "LA PAZ", 1, 13, "Altiplano")
climas.guardar(5, "ORURO", 2, 15, "Altiplano")
climas.guardar(6, "POTOSI", 2, 14, "Altiplano")
climas.guardar(7, "CBBA", 5, 18, "Valle")
climas.guardar(8, "SUCRE", 9, 23, "Valle")
climas.guardar(9, "TARIJA", 10, 25, "Valle")
climas.menu()

