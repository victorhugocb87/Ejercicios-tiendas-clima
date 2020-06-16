class Tienda:
    def __init__(self):
        self.nombre = []
        self.descripcion = []
        self.direccion = []
        self.categoria = []
        self.estado = []
    def verificarNumero(self, dato):
        if dato.isdigit():
            return True
        else:
            return False

    def menu(self):
        opciones="""
            ***********MENU DEL SISTEMA************
            1.- AGREGAR TIENDA
            2.- MOSTRAR TODAS LAS TIENDAS
            3.- BUSCAR TIENDAS POR CATEGORIA
            4.- ACTUALIZAR PRODUCTOS DE TIENDA
        """
        print(opciones)
        dato = input("Elija una Opcion: \n")
        if self.verificarNumero(dato):
            eleccion = int(dato)
        else:
            print("Debe digitar solo Numeros..!!")
            self.menu()
        self.opciones(eleccion)

    def opciones(self, eleccion):
        if (eleccion == 1):
            print(self.agregarTienda())
            self.menu()
        elif (eleccion == 2):
            self.mostrar()
            self.menu()
        elif (eleccion == 3):
            print(self.usuarioBuscar())
            self.menu()
        elif (eleccion == 4):
            print(self.actualizarDescripcion())
            self.menu()
        elif (eleccion == 5):
            print("Transacciones Realizadas")
            self.menu()
        else:
            print("Elija una opcion del menu")
            self.menu()

    def agregarTienda(self):
        nombre = input("Digite el nombre de la tienda: \n")
        descripcion = input("Digite la descripcion \n")
        direccion = input("Digite la direccion \n")
        categoria = input("Digite la categoria \n")
        print(self.guardarTienda(nombre, descripcion, direccion, categoria))
        agregarOtro = input("Desea Registrar mas tiendas \n")
        if (agregarOtro == 's' or agregarOtro == 'S'):
            self.agregarTienda()
        return "Tiendas agregadas exitosamente"

    def guardarTienda(self, nombre, descripcion, direccion, categoria):
        self.nombre.append(nombre)
        self.descripcion.append(descripcion)
        self.direccion.append(direccion)
        self.categoria.append(categoria)
        self.estado.append(1)
        return "Tienda {} registrada exitosamente..!!".format(nombre)

    def mostrar(self):
        for i in range(len(self.categoria)):
            self.detalle(i)

    def detalle(self, posicion):
        print("*******TIENDA {} **********".format(self.nombre[posicion]))
        print("Productos: {}".format(self.descripcion[posicion]))
        print("Direccion: {}".format(self.direccion[posicion]))
        print("Categoria: {}".format(self.categoria[posicion]))
        pass

    def usuarioBuscar(self):
        categoria = input("Escriba la categoria a buscar: \n")
        return self.buscarCategoria(categoria)

    def buscarCategoria(self, categoria):
            encontrado = False
            for i in range(len(self.nombre)):
                if (self.categoria[i] == categoria):
                    encontrado = True
                    self.detalle(i)
            if encontrado == False:
                print("No se encontraron resultados con la categoria {}".format(categoria))
            pass

    def verTienda(self):
        posicion = int(input("Digite la Posicion \n"))
        self.detalle(posicion)
        pass

    def actualizarDescripcion(self):
        posicion = self.usuarioBuscarTienda()
        descripcioActual = self.descripcion[posicion]
        descripcionNueva = input("Agregar datos a la descripcion {}".format(descripcioActual))
        descripcioActualizada = descripcioActual + " " + descripcionNueva
        return self.guardarActDescripcion(descripcioActualizada, posicion)

    def guardarActDescripcion(self, descripcion, posicion):
        self.descripcion[posicion]=descripcion
        return "Tienda Actualizada Exitosamente"

    def usuarioBuscarTienda(self):
        tienda = input("Digite el nombre de la tienda")
        posicion = self.nombre.index(tienda)
        self.detalle(posicion)
        return posicion


tiendas = Tienda()
tiendas.guardarTienda("Pollos Kiky", "Cuarto de pollo 15bs", "Doble via LG, 5to Anillo", "Restaurant")
tiendas.guardarTienda("Centro Informatico", "TV Box Xiaomi 500 bs", "Comercial Neval #42", "Electronica")
tiendas.guardarTienda("El tren rojo", "Hamburguesa 12 bs", "2do Anillo", "Hamburgueseria")
tiendas.guardarTienda("Ferreteria San Jorge", "Carretilla Acerada 350 bs", "Doble via LG, 7to Anillo", "Ferreteria")
tiendas.menu()
