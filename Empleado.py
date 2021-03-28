class Empleado:
    
    #def __init__(self, nombre, apellido, celular, direccion, dni, fnac, fing, leg, hijos=0, est=True):
    def __init__(self, dato):
        # self.nombre= nombre
        # self.apellido= apellido
        # self.celular= celular
        # self.direccion= direccion
        # self.dni= dni
        # self.fNacimiento= fnac
        # self.fIngreso= fing
        # self.legajo= leg
        # self.estado= est
        # self.hijos= hijos
        self.nombre= dato['Nombre']
        self.apellido= dato['Apellido']
        self.celular= dato['Celular']
        self.direccion= dato['Direccion']
        self.dni= dato['D.N.I']
        self.fNacimiento= dato['Fecha de nacimiento']
        self.fIngreso= dato['Fecha de ingreso']
        self.legajo= dato['Legajo']
        self.estado= dato['Estado']
        self.hijos= dato['Hijos']
        self.vacunado= dato['Vacuna']
    
    def nuevo(self, dato={}):
        self.nombre= dato['Nombre']
        self.apellido= dato['Apellido']
        self.celular= dato['Celular']
        self.direccion= dato['Direccion']
        self.dni= dato['D.N.I']
        self.fNacimiento= dato['Fecha de nacimiento']
        self.fIngreso= dato['Fecha de ingreso']
        self.legajo= dato['Legajo']
        self.estado= dato['Estado']
        self.hijos= dato['Hijos']

    def getNombre(self):
        return self.nombre

    def setNombre(self, nombre):
        self.nombre= nombre

    def getApellido(self):
        return self.apellido

    def setApellido(self, apellido):
        self.apellido= apellido

    def getCelular(self):
        return self.celular
    
    def setCelular(self, celular):
        self.celular= celular

    def getDireccion(self):
        return self.direccion
    
    def setDireccion(self, direccion):
        self.direccion= direccion

    def getDni(self):
        return self.dni

    def getFechaNacimiento(self):
        return self.fNacimiento

    def setFechaNacimiento(self, fecha):
        self.fNacimiento= fecha

    def getFechaingreso(self):
        return self.fIngreso

    def setFechaingreso(self, fecha):
        self.fIngreso= fecha
    
    def getLegajo(self):
        return self.legajo

    def setLegajo(self, legajo):
        self.legajo= legajo
    
    def getEstado(self):
        return self.estado
    
    def setEstado(self, estado):
        self.estado= estado

    def getEstadoStr(self):
        if self.getEstado():
            return "Activo"
        else:
            return "Inactivo"
            
    def getHijos(self):
        return self.hijos
    
    def setHijos(self, hijos):
        self.hijos= hijos

    def getApellidoyNombre(self):
        cadena = self.getApellido() + ' ' + self.getNombre()
        return cadena

    def getVacunado(self):
        return self.vacunado

    def setVacunado(self, vacunado):
        self.vacunado= vacunado

    def datos(self):
        dato = {}
        dato['Apellido'] = self.getApellido()
        dato['Nombre'] = self.getNombre()
        dato['Direccion'] = self.getDireccion()
        dato['Celular'] = self.getCelular()
        dato['D.N.I'] = self.getDni()
        dato['Estado'] = self.getEstado()
        dato['Fecha de ingreso'] = self.getFechaingreso()
        dato['Fecha de nacimiento'] = self.getFechaNacimiento()
        dato['Hijos'] = self.getHijos()
        dato['Legajo'] = self.getLegajo()
        dato['Vacuna'] = self.getVacunado()
        return dato
    
    def __str__(self):
        
        s0= 'Apellido: ' + self.getApellido()+ '\n' 
        s1= 'Nombre: '+ self.getNombre()+ '\n'
        s2= 'Dirección: '+ self.getDireccion()+ '\n'
        s3= 'Celular: '+ str(self.getCelular())+ '\n'
        s4= 'D.N.I: '+ str(self.getDni())+ '\n'
        if self.getEstado():
            s5= 'Estado: Activo \n'
        else:
            s5= 'Estado: Baja \n'     
        s6= 'Fecha de ingreso: '+ self.getFechaingreso()+ '\n'
        s7= 'Fecha de nacimiento: '+ self.getFechaNacimiento()+ '\n'
        s8= 'Cantidad de hijos: '+ str(self.getHijos())+ '\n'
        s9= 'Número de legajo: '+ str(self.getLegajo())+ '\n'
        if self.getVacunado():
            s10= 'Está vacunado'
        else:
            s10= 'Falta vacunar'
        return  s0+s1+s2+s3+s4+s5+s6+s7+s8+s9+s10

    def numeroFechaNacimiento(self):
        fecha= self.getFechaNacimiento()
        x= fecha.split('/')
        cadena= x[2] + x[1] + x[0]
        return cadena
    
    def numeroFechaIngreso(self):
        fecha= self.getFechaingreso()
        x= fecha.split('/')
        cadena= x[2] + x[1] + x[0]
        return cadena