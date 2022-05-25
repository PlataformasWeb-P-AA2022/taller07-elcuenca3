from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_ # se importa el operador and

# se importa la clase(s) del 
# archivo genera_tablas
from genera_tablas import Club, Jugador

# se importa información del archivo configuracion
from configuracion import cadena_base_datos
# se genera enlace al gestor de base de
# datos
# para el ejemplo se usa la base de datos
# sqlite
engine = create_engine(cadena_base_datos)


Session = sessionmaker(bind=engine)
session = Session()
clubs=open("data/datos.txt","r")
registroc=clubs.readlines();
print(registroc)

    
for r in registroc:
    pos=r.split(";")[1]
    dor=r.split(";")[2]
    nom=r.split(";")[3].replace("\n","")
    print(r.split(";"))
    clubes2 = session.query(Club).filter_by(nombre=r.split(";")[0]).one()
    session.query(Club).all
    juga=Jugador(club_id=clubes2,posicion=pos,dorsal=dor,nombre=nom)
    session.add(juga)
       
session.commit()
