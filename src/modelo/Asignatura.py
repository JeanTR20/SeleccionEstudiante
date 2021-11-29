from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from .declarative_base import Base


class Asignatura(Base):
    __tablename__ = 'asignatura'

    id = Column(Integer, primary_key=True)
    asignatura = Column(String)
    hora = Column(Integer)
    minuto = Column(Integer)
    descripcion = Column(String)
    estudiantes = relationship('Estudiante', secondary='estudiante_asignatura')
    profesores = relationship('Profesor', cascade='all, delete, delete-orphan')


class EstudianteAsginatura(Base):
    __tablename__ = 'estudiante_asignatura'

    asignatura_id = Column(
        Integer,
        ForeignKey('asignatura.id'),
        primary_key=True)

    estudiante_id = Column(
        Integer,
        ForeignKey('estudiante.id'),
        primary_key=True)
