from sqlalchemy import (
    Column, Integer, String, Float, Date, ForeignKey, Text, CheckConstraint
)
from sqlalchemy.orm import relationship
from app.database import Base

class Usuario(Base):
    __tablename__ = "usuario"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(150), unique=True, nullable=False)
    senha = Column(String(255), nullable=False)

class Cliente(Base):
    __tablename__ = "cliente"
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(150), nullable=False)
    endereco = Column(String(200))
    contato = Column(String(20))
    tipo = Column(String(2), CheckConstraint("tipo IN ('PF','PJ')"), nullable=False)

class ClientePF(Base):
    __tablename__ = "cliente_pf"
    id = Column(Integer, ForeignKey("cliente.id"), primary_key=True)
    cpf = Column(String(14), unique=True, nullable=False)
    data_nascimento = Column(Date, nullable=False)

class ClientePJ(Base):
    __tablename__ = "cliente_pj"
    id = Column(Integer, ForeignKey("cliente.id"), primary_key=True)
    cnpj = Column(String(18), unique=True, nullable=False)
    razao_social = Column(String(150), nullable=False)
    nome_fantasia = Column(String(100))

class Funcionario(Base):
    __tablename__ = "funcionario"
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(150), nullable=False)
    cpf = Column(String(14), unique=True, nullable=False)
    contato = Column(String(20))
    salario = Column(Float, nullable=False)
    tipo = Column(String(15), CheckConstraint("tipo IN ('TECNICO','ADMINISTRATIVO')"), nullable=False)
    data_admissao = Column(Date, nullable=False)
    horario_expediente = Column(String(50))
    status = Column(String(10), CheckConstraint("status IN ('ATIVO','FERIAS','AFASTADO','DESATIVADO')"))

class Tecnico(Base):
    __tablename__ = "tecnico"
    id = Column(Integer, ForeignKey("funcionario.id"), primary_key=True)
    especialidade = Column(String(100), nullable=False)
    certificacoes = Column(Text)
    nivel_experiencia = Column(Integer, CheckConstraint("nivel_experiencia BETWEEN 1 AND 5"))
    comissao_percentual = Column(Float, default=0.0)

class Administrativo(Base):
    __tablename__ = "administrativo"
    id = Column(Integer, ForeignKey("funcionario.id"), primary_key=True)
    cargo = Column(String(80), nullable=False)
    setor = Column(String(50))
    bonus_fixo = Column(Float, default=0.0)

class Equipamento(Base):
    __tablename__ = "equipamento"
    id = Column(Integer, primary_key=True, index=True)
    codigo = Column(String(15), unique=True, nullable=False)
    tipo = Column(String(20), nullable=False)
    marca = Column(String(20))
    modelo = Column(String(20))
    quantidade = Column(Integer, default=1)
    status = Column(String(10), default="ATIVO")

class OrdemServico(Base):
    __tablename__ = "ordem_servico"
    id = Column(Integer, primary_key=True, index=True)
    data_abertura = Column(Date, nullable=False)
    data_encerramento = Column(Date)
    descricao_problema = Column(Text, nullable=False)
    status = Column(String(20), default="ABERTA")
    valor_total = Column(Float, default=0.0)
    garantia_dias = Column(Integer, default=90)
    cliente_id = Column(Integer, ForeignKey("cliente.id"), nullable=False)
    tecnico_id = Column(Integer, ForeignKey("tecnico.id"))

    cliente = relationship("Cliente")
    tecnico = relationship("Tecnico")

class OrdemServicoEquipamento(Base):
    __tablename__ = "ordem_servico_equipamento"
    os_id = Column(Integer, ForeignKey("ordem_servico.id"), primary_key=True)
    equipamento_id = Column(Integer, ForeignKey("equipamento.id"), primary_key=True)
    quantidade = Column(Integer, default=1)

class VisitaTecnica(Base):
    __tablename__ = "visita_tecnica"
    id = Column(Integer, primary_key=True, index=True)
    data_agendamento = Column(Date, nullable=False)
    data_realizacao = Column(Date)
    resultado = Column(Text)
    os_id = Column(Integer, ForeignKey("ordem_servico.id"), nullable=False)
    tecnico_id = Column(Integer, ForeignKey("tecnico.id"), nullable=False)

class ContaReceber(Base):
    __tablename__ = "conta_receber"
    id = Column(Integer, primary_key=True, index=True)
    valor_original = Column(Float, nullable=False)
    multa = Column(Float, default=0.0)
    juros = Column(Float, default=0.0)
    valor_total = Column(Float, nullable=False)
    data_emissao = Column(Date, nullable=False)
    data_vencimento = Column(Date, nullable=False)
    data_pagamento = Column(Date)
    status_pagamento = Column(String(10), default="PENDENTE")
    forma_pagamento = Column(String(20))
    transacao_id = Column(String(100))
    os_id = Column(Integer, ForeignKey("ordem_servico.id"), nullable=False)