class asignaturas:
    
    def __init__ (self , idAsig,nombreAsig):
        self.idAsig = idAsig
        self.nombreAsig = nombreAsig

    def __str__ ( self ):
       
        return self.nombreAsig
    
    def getIdAsig(self):
        return self.idAsig
    
    def getNombreAsig(self):
        return self.nombreAsig
    
    def setIdAsig(self,idAsig):
        self.idAsig  =idAsig   

    def setNombreAsig(self,nombreAsig):
        self.nombreAsig  =nombreAsig 
           
    
class docentes:
    def __init__ (self , 
                  idDocente,
                  nombreDocente,
                  apellidoMaterno,
                  apellidoPaterno,
                  email,
                  numeroTelefono,
                  idAreas,
                  salario,
                  idasignaturas,
                  direccion,
                  ):
        self.idDocente = idDocente
        self.nombreDocente = nombreDocente
        self.apellidoMaterno = apellidoMaterno
        self.apellidoPaterno = apellidoPaterno
        self.email = email
        self.numeroTelefono = numeroTelefono
        self.idAreas = idAreas
        self.salario = salario
        self.idasignaturas = idasignaturas
        self.direccion = direccion

    def __str__ ( self ):
        # Retornamos el nombre de la persona
        return self.nombreDocente
    
    def getIdDocente(self):
        return self.idDocente
    
    def getNombreEmpleado(self):
        return self.nombreDocente
 
    def getApellidoMaterno(self):
        return self.apellidoMaterno
    
    def getApellidoPaterno(self):
        return self.apellidoPaterno
    
    def getEmail(self):
        return self.email      

    def getNumeroTelefono(self):
        return self.numeroTelefono     
    
    def getIdAreas(self):
        return self.idAreas   

    def getSalario(self):
        return self.salario          

    def getIdAsignaturas(self):
        return self.idAsignaturas  

    def getDireccion(self):
        return self.direccion     

##seters
    def setIdDocente(self,idDocente):
        self.idDocente=idDocente
    
    def setNombreDocente(self,nombreDocente):
        self.nombreDocente=nombreDocente
 
    def setApellidoMaterno(self,apellidoMaterno):
        self.apellidoMaterno=apellidoMaterno
    
    def setApellidoPaterno(self,apellidoPaterno):
        self.apellidoPaterno=apellidoPaterno
    
    def setEmail(self,email):
        self.email  =email    

    def setNumeroTelefono(self,numeroTelefono):
        self.numeroTelefono =numeroTelefono    

    def setIdAreas(self,idAreas):
        self.idAreas=idAreas    

    def setSalario(self,salario):
        self.salario =salario 


    def setIdAsignaturas(self,idAsignaturas):
        self.idAsignaturas =idAsignaturas

    def setDireccion(self,direccion):
        self.direccion = direccion
