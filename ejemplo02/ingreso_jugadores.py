from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from genera_tablas import Club, Jugador
from configuracion import cadena_base_datos
engine = create_engine(cadena_base_datos)


Session = sessionmaker(bind=engine)
session = Session()
clubs=open("data/datos.txt","r")
registroc=clubs.readlines();
print(registroc)

clubes2 = session.query(Club).all()
for s in clubes2:
    for r in registroc:
       pos=r.split(";")[1]
       dor=r.split(";")[2]
       nom=r.split(";")[3].replace("\n","")
       print(r.split(";"))
       juga=Jugador(club_id=s.nombre,posicion=pos,dorsal=dor,nombre=nom)
       session.add(juga)
       
session.commit()
