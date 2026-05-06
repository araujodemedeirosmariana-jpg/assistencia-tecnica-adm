from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app import models, schemas
from app.database import get_db

router = APIRouter(prefix="/equipamentos", tags=["equipamentos"])

@router.post("/", response_model=schemas.EquipamentoResponse)
def create_equipamento(equipamento: schemas.EquipamentoCreate, db: Session = Depends(get_db)):
    db_equipamento = models.Equipamento(**equipamento.dict())
    db.add(db_equipamento)
    db.commit()
    db.refresh(db_equipamento)
    return db_equipamento

@router.get("/", response_model=List[schemas.EquipamentoResponse])
def read_equipamentos(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    equipamentos = db.query(models.Equipamento).offset(skip).limit(limit).all()
    return equipamentos

@router.get("/{equipamento_id}", response_model=schemas.EquipamentoResponse)
def read_equipamento(equipamento_id: int, db: Session = Depends(get_db)):
    equipamento = db.query(models.Equipamento).filter(models.Equipamento.id == equipamento_id).first()
    if not equipamento:
        raise HTTPException(status_code=404, detail="Equipamento não encontrado")
    return equipamento

@router.put("/{equipamento_id}", response_model=schemas.EquipamentoResponse)
def update_equipamento(equipamento_id: int, equipamento: schemas.EquipamentoCreate, db: Session = Depends(get_db)):
    db_equipamento = db.query(models.Equipamento).filter(models.Equipamento.id == equipamento_id).first()
    if not db_equipamento:
        raise HTTPException(status_code=404, detail="Equipamento não encontrado")
    for key, value in equipamento.dict().items():
        setattr(db_equipamento, key, value)
    db.commit()
    db.refresh(db_equipamento)
    return db_equipamento

@router.delete("/{equipamento_id}")
def delete_equipamento(equipamento_id: int, db: Session = Depends(get_db)):
    db_equipamento = db.query(models.Equipamento).filter(models.Equipamento.id == equipamento_id).first()
    if not db_equipamento:
        raise HTTPException(status_code=404, detail="Equipamento não encontrado")
    db.delete(db_equipamento)
    db.commit()
    return {"message": "Equipamento removido com sucesso"}