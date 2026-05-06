from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List, Optional
from datetime import date
from pydantic import BaseModel
from app import models
from app.database import get_db

router = APIRouter(prefix="/funcionarios", tags=["funcionarios"])

# Schemas
class FuncionarioBase(BaseModel):
    nome: str
    cpf: str
    contato: Optional[str] = None
    salario: float
    tipo: str
    data_admissao: date
    horario_expediente: Optional[str] = None
    status: str = "ATIVO"

class FuncionarioCreate(FuncionarioBase):
    pass

class FuncionarioResponse(FuncionarioBase):
    id: int
    class Config:
        from_attributes = True

class TecnicoBase(BaseModel):
    especialidade: str
    certificacoes: Optional[str] = None
    nivel_experiencia: Optional[int] = 1
    comissao_percentual: float = 0.0

class TecnicoCreate(TecnicoBase):
    funcionario_id: int

class TecnicoResponse(TecnicoBase):
    id: int
    class Config:
        from_attributes = True

class AdministrativoBase(BaseModel):
    cargo: str
    setor: Optional[str] = None
    bonus_fixo: float = 0.0

class AdministrativoCreate(AdministrativoBase):
    funcionario_id: int

class AdministrativoResponse(AdministrativoBase):
    id: int
    class Config:
        from_attributes = True

# CRUD Funcionario
@router.post("/", response_model=FuncionarioResponse)
def create_funcionario(funcionario: FuncionarioCreate, db: Session = Depends(get_db)):
    existing = db.query(models.Funcionario).filter(models.Funcionario.cpf == funcionario.cpf).first()
    if existing:
        raise HTTPException(status_code=400, detail="CPF já cadastrado")
    
    db_funcionario = models.Funcionario(**funcionario.model_dump())
    db.add(db_funcionario)
    db.commit()
    db.refresh(db_funcionario)
    return db_funcionario

@router.get("/", response_model=List[FuncionarioResponse])
def read_funcionarios(
    skip: int = 0, 
    limit: int = 100, 
    tipo: Optional[str] = Query(None),
    status: Optional[str] = Query(None),
    db: Session = Depends(get_db)
):
    query = db.query(models.Funcionario)
    if tipo:
        query = query.filter(models.Funcionario.tipo == tipo)
    if status:
        query = query.filter(models.Funcionario.status == status)
    
    return query.offset(skip).limit(limit).all()

@router.get("/{funcionario_id}", response_model=FuncionarioResponse)
def read_funcionario(funcionario_id: int, db: Session = Depends(get_db)):
    funcionario = db.query(models.Funcionario).filter(models.Funcionario.id == funcionario_id).first()
    if not funcionario:
        raise HTTPException(status_code=404, detail="Funcionário não encontrado")
    return funcionario

# CRUD Tecnico
@router.post("/tecnico", response_model=TecnicoResponse)
def create_tecnico(tecnico: TecnicoCreate, db: Session = Depends(get_db)):
    funcionario = db.query(models.Funcionario).filter(models.Funcionario.id == tecnico.funcionario_id).first()
    if not funcionario:
        raise HTTPException(status_code=404, detail="Funcionário não encontrado")
    if funcionario.tipo != "TECNICO":
        raise HTTPException(status_code=400, detail="Funcionário não é do tipo TÉCNICO")
    
    existing = db.query(models.Tecnico).filter(models.Tecnico.id == tecnico.funcionario_id).first()
    if existing:
        raise HTTPException(status_code=400, detail="Funcionário já cadastrado como técnico")
    
    db_tecnico = models.Tecnico(**tecnico.model_dump())
    db.add(db_tecnico)
    db.commit()
    db.refresh(db_tecnico)
    return db_tecnico

# CRUD Administrativo
@router.post("/administrativo", response_model=AdministrativoResponse)
def create_administrativo(administrativo: AdministrativoCreate, db: Session = Depends(get_db)):
    funcionario = db.query(models.Funcionario).filter(models.Funcionario.id == administrativo.funcionario_id).first()
    if not funcionario:
        raise HTTPException(status_code=404, detail="Funcionário não encontrado")
    if funcionario.tipo != "ADMINISTRATIVO":
        raise HTTPException(status_code=400, detail="Funcionário não é do tipo ADMINISTRATIVO")
    
    existing = db.query(models.Administrativo).filter(models.Administrativo.id == administrativo.funcionario_id).first()
    if existing:
        raise HTTPException(status_code=400, detail="Funcionário já cadastrado como administrativo")
    
    db_administrativo = models.Administrativo(**administrativo.model_dump())
    db.add(db_administrativo)
    db.commit()
    db.refresh(db_administrativo)
    return db_administrativo

@router.get("/tecnico/{tecnico_id}", response_model=TecnicoResponse)
def read_tecnico(tecnico_id: int, db: Session = Depends(get_db)):
    tecnico = db.query(models.Tecnico).filter(models.Tecnico.id == tecnico_id).first()
    if not tecnico:
        raise HTTPException(status_code=404, detail="Técnico não encontrado")
    return tecnico

@router.get("/administrativo/{adm_id}", response_model=AdministrativoResponse)
def read_administrativo(adm_id: int, db: Session = Depends(get_db)):
    administrativo = db.query(models.Administrativo).filter(models.Administrativo.id == adm_id).first()
    if not administrativo:
        raise HTTPException(status_code=404, detail="Administrativo não encontrado")
    return administrativo
