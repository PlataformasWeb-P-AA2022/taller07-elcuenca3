from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from genera_tablas import Club, Jugador
from configuracion import cadena_base_datos
engine = create_engine(cadena_base_datos)


Session = sessionmaker(bind=engine)
session = Session()
clubs=open("data/datos.txt","r")
registroc=clubs.readlines();

hola = session.query(Club).all()

for r in hola:
    print("%s" % (r.nombre))


