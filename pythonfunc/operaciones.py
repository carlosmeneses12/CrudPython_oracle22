import cx_Oracle

from modelo import asignaturas

class operacion:
    
   
    def obtenerAsignaturas(self):
        connection = cx_Oracle.connect(
                    user="evaluacion",
                    password="123",
                    dsn="localhost/xe")
        cursor = connection.cursor()
        cursor.execute('SELECT ID_ASIGNATURAS, NOMBRE_ASIGNATURAS FROM EVALUACION.ASIGNATURAS')
        lista=[]
        for id, nombreAsig in cursor:
            p1=asignaturas(id,nombreAsig)
            lista.append(p1)
            print("Values:", id, nombreAsig)
        cursor.close()
        connection.close()
        return lista
    
    def obtenerAsignaturas(self, idAsig):
        connection = cx_Oracle.connect(
                    user="evaluacion",
                    password="123",
                    dsn="localhost/xe")
        cursor = connection.cursor()
        cursor.execute("""SELECT ID_ASIGNATURAS, NOMBRE_ASIGNATURAS
                          FROM EVALUACION.ASIGNATURAS 
                          WHERE ID_DEPARTMENTO =: ID """,
                          ID=idAsig
                       )
        lista=[]
        for id, nombreAsig in cursor:
            p1= asignaturas(id,nombreAsig)
            lista.append(p1)
            #print("Values:", id, nombreDept)
        cursor.close()
        connection.close()
        return lista

    def obtenerAsignatura2(self, idAsig):
        connection = cx_Oracle.connect(
                    user="evaluacion",
                    password="123",
                    dsn="localhost/xe")
        cursor = connection.cursor()
        cursor.execute("""SELECT ID_ASIGNATURAS, NOMBRE_ASIGNATURAS 
                       FROM EVALUACION.ASIGNATURAS
                       WHERE ID_ASIGNATURAS=:0""",(idAsig,))
        lista=[]
        for id, nombreAsig in cursor:
            p1=asignaturas(id,nombreAsig)
            lista.append(p1)
            
        cursor.close()
        connection.close()
        return lista
    
    def agregarAsignatura(self,idAsig,nombreAsig):
        connection = cx_Oracle.connect(
                    user="evaluacion",
                    password="123",
                    dsn="localhost/xe")
        cursor = connection.cursor()
        cursor.execute("""INSERT INTO ASIGNATURAS 
                          (ID_ASIGNATURAS, NOMBRE_ASIGNATURAS) 
                           VALUES (:0,:1) """,
                          (idAsig,nombreAsig)
                       )
        

        connection.commit()
        cursor.close()
        connection.close()

    def eliminarAsignatura(self,idAsig):
        connection = cx_Oracle.connect(
                    user="evaluacion",
                    password="123",
                    dsn="localhost/xe")
        cursor = connection.cursor()
        cursor.execute("""DELETE FROM ASIGNATURAS 
                          WHERE ID_ASIGNATURAS =:0 """
                          ,
                          (idAsig,)
                       )
        

        connection.commit()
        cursor.close()
        connection.close()

    def actualizarAsignatura(self,idAsig,nombreAsig):
        connection = cx_Oracle.connect(
                    user="evaluacion",
                    password="123",
                    dsn="localhost/xe")
        cursor = connection.cursor()
        cursor.execute("""UPDATE ASIGNATURAS 
                          SET NOMBRE_ASIGNATURAS =:0 
                          WHERE ID_ASIGNATURAS =:1"""
                          ,
                          (nombreAsig,idAsig)
                       )  

        connection.commit()
        cursor.close()
        connection.close()

   
    def buscarAsignatura(self,nombreAsig):
        connection = cx_Oracle.connect(
                    user="evaluacion",
                    password="123",
                    dsn= "localhost/xe")
        cursor1 = connection.cursor()
        cursor1.execute("SELECT * FROM ASIGNATURAS "+
                        " WHERE  UPPER (NOMBRE_ASIGNATURAS) LIKE upper('%"+nombreAsig+"%')"
                        #,
                       # (idAsig,nombreAsig)
                        )
        lista=[]
        for id, nombreAsig in cursor1:
            print("EL id es: ",id)
            print("Nombre de asignatura: ",nombreAsig)
            c1=asignaturas(id,nombreAsig)
            lista.append(c1)
        
        #print(lista)
        
        cursor1.close()
        connection.close()
        return lista
    






    def TotalAsignaturas(self):
            connection2 = cx_Oracle.connect(
                        user="evaluacion",
                        password="123",
                        dsn= "localhost/xe")
            cursor21 = connection2.cursor()
            
            cursor21.execute("SELECT COUNT(*) as contador FROM ASIGNATURAS")
            datos = cursor21.fetchone()
            #for contador in cursor21:
                 #print("EL contador es: ",contador)

            num=datos[0]
            print(num)
            cursor21.close()
            connection2.close()



    def BuscarconM(self):
        connection = cx_Oracle.connect(
            user = "evaluacion",
            password = "123",
            dsn = "localhost/xe")
        cursor1 = connection.cursor()
        cursor1.execute("SELECT NOMBRE_ASIGNATURAS  FROM ASIGNATURAS WHERE NOMBRE_ASIGNATURAS LIKE 'M%'")

        datos = cursor1.fetchall()
      
        cursor1.close()
        print("las asignaturas que comienzan con M son : ",datos)
        connection.close()
        
    



            
            

        
