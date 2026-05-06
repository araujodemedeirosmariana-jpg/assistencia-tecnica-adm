from pydantic import BaseModel, EmailStr
from datetime import date
from typing import Optional, List

# Usuario
class UsuarioBase(BaseModel):
    email: EmailStr

class UsuarioCreate(UsuarioBase):
    senha: str

class UsuarioResponse(UsuarioBase):
    id: int
    class Config:
        from_attributes = True

# Cliente
class ClienteBase(BaseModel):
    nome: str
    endereco: Optional[str] = None
    contato: Optional[str] = None
    tipo: str  # PF ou PJ

class ClienteCreate(ClienteBase):
    pass

class ClientePFData(BaseModel):
    cpf: str
    data_nascimento: date

class ClientePJData(BaseModel):
    cnpj: str
    razao_social: str
    nome_fantasia: Optional[str] = None

class ClienteResponse(ClienteBase):
    id: int
    class Config:
        from_attributes = True

# Equipamento
class EquipamentoBase(BaseModel):
    codigo: str
    tipo: str
    marca: Optional[str] = None
    modelo: Optional[str] = None
    quantidade: int = 1

class EquipamentoCreate(EquipamentoBase):
    pass

class EquipamentoResponse(EquipamentoBase):
    id: int
    status: str
    class Config:
        from_attributes = True

# Ordem de Servico
class OrdemServicoBase(BaseModel):
    descricao_problema: str
    cliente_id: int
    tecnico_id: Optional[int] = None

class OrdemServicoCreate(OrdemServicoBase):
    pass

class OrdemServicoUpdate(BaseModel):
    descricao_problema: Optional[str] = None
    status: Optional[str] = None
    tecnico_id: Optional[int] = None

class OrdemServicoResponse(BaseModel):
    id: int
    data_abertura: date
    data_encerramento: Optional[date]
    descricao_problema: str
    status: str
    valor_total: float
    garantia_dias: int
    cliente_id: int
    tecnico_id: Optional[int]
    class Config:
        from_attributes = True

# Token
class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    email: Optional[str] = None