drop table docentes;
drop table areas;
drop table asignaturas;

CREATE TABLE docentes
   ( id_docentes            NUMBER not null
   , nombre                VARCHAR2(60) not null
   , apellidomaterno       VARCHAR2(60) not null
   , apellidopaterno       VARCHAR2(60) not null
   , email                 VARCHAR2(60) 
   , numerotelefono        VARCHAR2(20)
   , id_areas       VARCHAR2(10)
   , salario               NUMBER not null
   , id_asignaturas        NUMBER
   , direccion             VARCHAR2(100)
   ) ;
   
CREATE TABLE asignaturas
   ( id_asignaturas      NUMBER
   , nombre_asignaturas VARCHAR2(30)
   ) ;
   
CREATE TABLE areas
   ( id_areas  VARCHAR2(10)
   , nombre_areas VARCHAR2(35)
   , min_salary NUMBER
   , max_salary NUMBER
   ) ;
--------------------------------------------------
 ALTER TABLE docentes ADD 
  CONSTRAINT docentes_PK 
  PRIMARY KEY(id_docentes); 
  
  ALTER TABLE asignaturas ADD 
  CONSTRAINT asignaturas_PK 
  PRIMARY KEY(id_asignaturas ); 
 
  ALTER TABLE areas ADD 
  CONSTRAINT areas_PK 
  PRIMARY KEY(id_areas ); 
---------------------------------------------------
ALTER TABLE docentes ADD (
  CONSTRAINT docentes_asignaturas_FK 
 FOREIGN KEY (id_asignaturas ) 
 REFERENCES asignaturas (id_asignaturas ));
 
  ALTER TABLE docentes ADD (
  CONSTRAINT docentes_areas_FK 
 FOREIGN KEY (id_areas ) 
 REFERENCES areas (id_areas ));