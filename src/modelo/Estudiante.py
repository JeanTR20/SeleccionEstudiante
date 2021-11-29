import enum

from sqlalchemy import Column, Integer, String, Enum
from sqlalchemy.orm import relationship

from .declarative_base import Base


class Escala(enum.Enum):
    Escala1 = 1
    Escala2 = 2
    Escala3 = 3


class Estudiante(Base):
    __tablename__ = 'estudiante'

    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    ciclo = Column( Integer )
    apellido = Column(String)
    escala = Column(Enum(Escala))
    asignaturas = relationship('Asignatura', secondary='estudiante_asignatura')
