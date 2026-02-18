from sqlalchemy.orm import Session
import models
import schemas


def crear_tarea(db: Session, tarea: schemas.TareaCreate):
    nueva_tarea = models.Tarea(
        titulo=tarea.titulo,
        completada=tarea.completada
    )

    db.add(nueva_tarea)
    db.commit()
    db.refresh(nueva_tarea)

    return nueva_tarea


def obtener_tareas(db: Session):
    return db.query(models.Tarea).all()


def actualizar_tarea(db: Session, tarea_id: int, datos: schemas.TareaUpdate):

    tarea = db.query(models.Tarea).filter(models.Tarea.id == tarea_id).first()

    if not tarea:
        return None

    tarea.titulo = datos.titulo
    tarea.completada = datos.completada

    db.commit()
    db.refresh(tarea)

    return tarea



def eliminar_tarea(db: Session, tarea_id: int):

    tarea = db.query(models.Tarea).filter(models.Tarea.id == tarea_id).first()

    if not tarea:
        return None

    db.delete(tarea)
    db.commit()

    return tarea


