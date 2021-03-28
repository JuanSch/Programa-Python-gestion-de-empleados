class Prenda:

    def __init__(self, dato):
        self.producto = dato['Producto']
        self.tipo= dato['Tipo']
        self.marca= dato['Marca']
        self.certificado= dato['Certificado']
        self.cantidad= dato['Cantidad']
        self.fecha= dato['Fecha de entrega']
        self.dato= dato

    def getProducto(self):
        return self.producto
    
    def setProducto(self,producto):
        self.producto= producto
    
    def getTipo(self):
        return self.tipo
    
    def setTipo(self, tipo):
        self.tipo= tipo

    def getMarca(self):
        return self.marca

    def setMarca(self,marca):
        self.marca = marca
    
    def getCertificado(self):
        return self.certificado
    
    def setCertificado(self, certificado):
        self.certificado= certificado
    
    def getCantidad(self):
        return self.cantidad
    
    def setCantidad(self, cantidad):
        self.cantidad= cantidad
    
    def getFecha(self):
        return self.fecha

    def setFecha(self, fecha):
        self.fecha= fecha

    def __str__(self):
        s0 = "Producto: " + self.getProducto() + '\n'
        s1= "Tipo: " + self.getTipo() + '\n'
        s2= "Marca: " + self.getMarca() + '\n'
        if self.getCertificado():
            s3= "Posee certificación: Sí" + '\n'
        else:
            s3= "Posee certificación: Sí" + '\n'
        s4= "Cantidad: " + str(self.getCantidad()) + '\n'
        s5= "Fecha de entrega: " + self.getFecha()
        cadena = s0+s1+s2+s3+s4+s5
        return cadena

    def datos(self):
        dato = {}
        dato['Producto'] = self.getProducto()
        dato['Marca']  = self.getMarca()
        dato['Certificado'] = self.getCertificado()
        dato['Cantidad'] = self.getCantidad()
        dato['Fecha de entrega'] = self.getFecha()
        return dato 

class Entrega:
    def __init__(self, dni, nombre, prenda):
        self.nombre = nombre
        self.dni = dni
        lista = []
        lista.append(prenda)
        self.entregas = lista

    def getNombre(self):
        return self.nombre

    def setNombre(self, nombre):
        self.nombre = nombre

    def getDni(self):
        return self.dni

    def setDni(self, dni):
        self.dni = dni

    def getEntregas(self):
        return self.entregas
    
    def addEntrega (self, prenda):
        entregas= self.getEntregas()
        if len(entregas) < 18:
            entregas.append(prenda)
        else:
            entregas.pop(0)
            entregas.append(prenda)

    def getDatos(self):
        datos= {}
        datos['Nombre'] = self.nombre
        datos['DNI'] = self.dni
        lista = self.entregas
        listadic = []
        for entrega in lista:
            listadic.append(entrega)
        datos['Entregas'] = listadic
        return datos