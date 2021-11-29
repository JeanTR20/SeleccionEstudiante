from src.modelo.declarative_base import engine, Base, session
from src.modelo.Estudiante import Estudiante

class Coleccion():

    def __init__(self):
        Base.metadata.create_all(engine)

    def agregar_estudiante(self, nombre, ciclo, apellido, escala):
        busqueda = session.query(Estudiante).filter(Estudiante.nombre == nombre).all()
        if len(busqueda) == 0:
            student = Estudiante(nombre=nombre, ciclo=ciclo, apellido=apellido, escala=escala)
            session.add(student)
            session.commit()
            return True
        else:
            return False

    def editar_estudiante(self, estudiante_id, nombre, ciclo, apellido, escala):
        busqueda = session.query(Estudiante).filter(Estudiante.nombre == nombre, Estudiante.id != estudiante_id).all()
        if len(busqueda) == 0:
            estudiante = session.query(Estudiante).filter(Estudiante.id == estudiante_id).first()
            estudiante.nombre = nombre
            estudiante.ciclo = ciclo
            estudiante.apellido = apellido
            estudiante.escala = escala
            session.commit()
            return True
        else:
            return False

    def dar_estudiante_por_id(self, estudiante_id):
        return session.query(Estudiante).get(estudiante_id).__dict__
