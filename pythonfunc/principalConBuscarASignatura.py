import operaciones
import modelo

op=operaciones.operacion()
lista1=[]
lista2=[]
lista3=[]


#op.agregarAsignatura(25,"CONSTRUCCION")
lista1= op.obtenerAsignatura2(177)

for reg in lista1:
    print("Values:", reg.idAsig, reg.nombreAsig)
    

#op.actualizarAsignatura(24,"COCINA")

lista2= op.obtenerAsignatura2(177)

for reg in lista2:
    print("Values:", reg.idAsig, reg.nombreAsig)
    
#op.eliminarAsignatura(24)

