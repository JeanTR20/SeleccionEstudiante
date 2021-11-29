from sqlalchemy import Column, Integer, String, ForeignKey

from .declarative_base import Base


class Profesor(Base):
    __tablename__ = 'profesor'

    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    descripcion = Column(String)
    asignatura = Column(Integer, ForeignKey('asignatura.id'))
