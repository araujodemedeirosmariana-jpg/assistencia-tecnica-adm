from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from sqlalchemy import func, and_
from datetime import date, datetime
from typing import Optional
from app.database import get_db
from app import models

router = APIRouter(prefix="/relatorios", tags=["relatorios"])

@router.get("/ordens-servico")
def relatorio_ordens_servico(
    data_inicio: Optional[date] = Query(None, description="Data inicial do período"),
    data_fim: Optional[date] = Query(None, description="Data final do período"),
    status: Optional[str] = Query(None, description="Filtrar por status da OS"),
    tecnico_id: Optional[int] = Query(None, description="Filtrar por técnico responsável"),
    db: Session = Depends(get_db)
):
    """
    Relatório de Ordens de Serviço com filtros por período, status e técnico.
    """
    query = db.query(models.OrdemServico)
    
    # Aplicar filtros
    if data_inicio:
        query = query.filter(models.OrdemServico.data_abertura >= data_inicio)
    if data_fim:
        query = query.filter(models.OrdemServico.data_abertura <= data_fim)
    if status:
        query = query.filter(models.OrdemServico.status == status)
    if tecnico_id:
        query = query.filter(models.OrdemServico.tecnico_id == tecnico_id)
    
    ordens = query.all()
    
    # Calcular totais
    quantidade = len(ordens)
    valor_total = sum(os.valor_total for os in ordens)
    
    # Preparar dados para o relatório
    dados_relatorio = []
    for os in ordens:
        cliente = db.query(models.Cliente).filter(models.Cliente.id == os.cliente_id).first()
        dados_relatorio.append({
            "id": os.id,
            "cliente": cliente.nome if cliente else "N/A",
            "cliente_id": os.cliente_id,
            "data_abertura": os.data_abertura.isoformat(),
            "data_encerramento": os.data_encerramento.isoformat() if os.data_encerramento else None,
            "status": os.status,
            "valor_total": os.valor_total,
            "garantia_dias": os.garantia_dias,
            "descricao_problema": os.descricao_problema[:100] + "..." if len(os.descricao_problema) > 100 else os.descricao_problema
        })
    
    return {
        "periodo": {
            "data_inicio": data_inicio.isoformat() if data_inicio else None,
            "data_fim": data_fim.isoformat() if data_fim else None
        },
        "filtros_aplicados": {
            "status": status,
            "tecnico_id": tecnico_id
        },
        "resumo": {
            "quantidade_total": quantidade,
            "valor_total_geral": valor_total,
            "valor_medio": valor_total / quantidade if quantidade > 0 else 0
        },
        "ordens": dados_relatorio
    }

@router.get("/faturamento")
def relatorio_faturamento(
    data_inicio: date = Query(..., description="Data inicial do período"),
    data_fim: date = Query(..., description="Data final do período"),
    db: Session = Depends(get_db)
):
    """
    Relatório de faturamento por período.
    """
    # Ordens finalizadas no período
    ordens = db.query(models.OrdemServico).filter(
        and_(
            models.OrdemServico.data_encerramento >= data_inicio,
            models.OrdemServico.data_encerramento <= data_fim,
            models.OrdemServico.status == "FINALIZADA"
        )
    ).all()
    
    # Pagamentos no período
    contas = db.query(models.ContaReceber).filter(
        and_(
            models.ContaReceber.data_pagamento >= data_inicio,
            models.ContaReceber.data_pagamento <= data_fim,
            models.ContaReceber.status_pagamento == "PAGO"
        )
    ).all()
    
    faturamento_os = sum(os.valor_total for os in ordens)
    faturamento_recebido = sum(conta.valor_total for conta in contas)
    
    return {
        "periodo": {
            "data_inicio": data_inicio.isoformat(),
            "data_fim": data_fim.isoformat()
        },
        "faturamento_emitido": {
            "valor": faturamento_os,
            "quantidade_os": len(ordens)
        },
        "faturamento_recebido": {
            "valor": faturamento_recebido,
            "quantidade_pagamentos": len(contas)
        },
        "diferenca": faturamento_os - faturamento_recebido
    }

@router.get("/tecnicos")
def relatorio_tecnicos(
    data_inicio: Optional[date] = Query(None),
    data_fim: Optional[date] = Query(None),
    db: Session = Depends(get_db)
):
    """
    Relatório de produtividade dos técnicos.
    """
    query = db.query(
        models.Tecnico.id,
        models.Funcionario.nome,
        func.count(models.OrdemServico.id).label("total_os"),
        func.sum(models.OrdemServico.valor_total).label("valor_total")
    ).join(
        models.Funcionario, models.Tecnico.id == models.Funcionario.id
    ).outerjoin(
        models.OrdemServico, models.Tecnico.id == models.OrdemServico.tecnico_id
    )
    
    if data_inicio:
        query = query.filter(models.OrdemServico.data_abertura >= data_inicio)
    if data_fim:
        query = query.filter(models.OrdemServico.data_abertura <= data_fim)
    
    resultados = query.group_by(models.Tecnico.id, models.Funcionario.nome).all()
    
    dados_tecnicos = []
    for tecnico in resultados:
        dados_tecnicos.append({
            "id": tecnico.id,
            "nome": tecnico.nome,
            "total_ordens": tecnico.total_os or 0,
            "valor_total_gerado": float(tecnico.valor_total) if tecnico.valor_total else 0
        })
    
    return {
        "periodo": {
            "data_inicio": data_inicio.isoformat() if data_inicio else None,
            "data_fim": data_fim.isoformat() if data_fim else None
        },
        "tecnicos": dados_tecnicos
    }

@router.get("/garantias")
def relatorio_garantias(
    dias_alerta: int = Query(7, description="Dias antes do vencimento para alerta"),
    db: Session = Depends(get_db)
):
    """
    Relatório de garantias ativas, próximas do vencimento e expiradas.
    """
    hoje = date.today()
    
    ordens = db.query(models.OrdemServico).filter(
        models.OrdemServico.status == "FINALIZADA"
    ).all()
    
    ativas = []
    expirando = []
    expiradas = []
    
    for os in ordens:
        if not os.data_encerramento:
            continue
        
        data_garantia = os.data_encerramento + date.timedelta(days=os.garantia_dias)
        dias_restantes = (data_garantia - hoje).days
        
        dados_os = {
            "id": os.id,
            "cliente_id": os.cliente_id,
            "data_encerramento": os.data_encerramento.isoformat(),
            "garantia_dias": os.garantia_dias,
            "data_vencimento_garantia": data_garantia.isoformat(),
            "dias_restantes": dias_restantes
        }
        
        if dias_restantes < 0:
            expiradas.append(dados_os)
        elif dias_restantes <= dias_alerta:
            expirando.append(dados_os)
        else:
            ativas.append(dados_os)
    
    return {
        "data_consulta": hoje.isoformat(),
        "dias_alerta": dias_alerta,
        "garantias_ativas": {
            "quantidade": len(ativas),
            "lista": ativas
        },
        "garantias_expiradas": {
            "quantidade": len(expiradas),
            "lista": expiradas
        },
        "garantias_expiradas": {
            "quantidade": len(expiradas),
            "lista": expiradas
        }
    }
