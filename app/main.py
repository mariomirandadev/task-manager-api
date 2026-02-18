from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from fastapi import HTTPException


import database
import models
import schemas
import crud

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()


@app.post("/creacion", response_model=schemas.TareaResponse)
def crear_tarea(tarea: schemas.TareaCreate, db: Session = Depends(database.get_db)):
    return crud.crear_tarea(db, tarea)


@app.get("/tareas", response_model=list[schemas.TareaResponse])
def listar_tareas(db: Session = Depends(database.get_db)):
    return crud.obtener_tareas(db)


@app.put("/tareas/{tarea_id}", response_model=schemas.TareaResponse)
def actualizar_tarea(
    tarea_id: int,
    datos: schemas.TareaUpdate,
    db: Session = Depends(database.get_db)
):

    tarea = crud.actualizar_tarea(db, tarea_id, datos)

    if not tarea:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")

    return tarea


@app.delete("/tareas/{tarea_id}", response_model=schemas.TareaResponse)
def eliminar_tarea(tarea_id: int, db: Session = Depends(database.get_db)):

    tarea = crud.eliminar_tarea(db, tarea_id)

    if not tarea:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")

    return tarea
