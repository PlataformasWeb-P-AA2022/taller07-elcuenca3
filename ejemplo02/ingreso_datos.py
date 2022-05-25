
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# se importa la clase(s) del 
# archivo genera_tablas
from genera_tablas import Club

# se importa información del archivo configuracion
from configuracion import cadena_base_datos
# se genera enlace al gestor de base de
# datos
# para el ejemplo se usa la base de datos
# sqlite
engine = create_engine(cadena_base_datos)

Session = sessionmaker(bind=engine)
session = Session()

# se crea un objetos de tipo Club 


clubs=open("data/datos_clubs.txt","r")
registroc=clubs.readlines();
print(registroc)
for r in registroc:
    nom=r.split(";")[0]
    dep=r.split(";")[1]
    fun=r.split(";")[2].replace("\n","")
    print(r.split(";"))
    equipo =Club(nombre=nom,deporte=dep,fundacion=fun)
    session.add(equipo)
 

       
session.commit()