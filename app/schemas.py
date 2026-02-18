from pydantic import BaseModel


class TareaCreate(BaseModel):
    titulo: str
    completada: bool


class TareaResponse(BaseModel):
    id: int
    titulo: str
    completada: bool

    class Config:
        from_attributes = True


class TareaUpdate(BaseModel):
    titulo: str
    completada: bool




