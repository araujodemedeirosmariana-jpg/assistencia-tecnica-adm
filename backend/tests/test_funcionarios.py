import pytest
from unittest.mock import Mock, patch
from datetime import date
from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.routers.funcionarios import (
    create_funcionario,
    read_funcionarios,
    read_funcionario,
    update_funcionario,
    delete_funcionario,
    desativar_funcionario,
    create_tecnico,
    create_administrativo
)
from app.schemas import (
    FuncionarioCreate,
    FuncionarioUpdate,
    TecnicoCreate,
    AdministrativoCreate
)
from app import models

# ============================================
# Fixtures para dados de teste
# ============================================

@pytest.fixture
def mock_db():
    """Fixture que fornece um Mock do banco de dados"""
    return Mock(spec=Session)

@pytest.fixture
def funcionario_valido():
    """Fixture com dados válidos de funcionário"""
    return FuncionarioCreate(
        nome="João Silva",
        cpf="123.456.789-00",
        contato="(11) 99999-8888",
        salario=3500.00,
        tipo="TECNICO",
        data_admissao=date(2024, 1, 15),
        horario_expediente="08:00-18:00",
        status="ATIVO"
    )

@pytest.fixture
def tecnico_valido():
    """Fixture com dados válidos de técnico"""
    return TecnicoCreate(
        funcionario_id=1,
        especialidade="Eletrônica",
        certificacoes="Certificação Técnica Nível 3",
        nivel_experiencia=3,
        comissao_percentual=5.0
    )

# ============================================
# 1. TESTES DE CREATE (INSERIR)
# ============================================

class TestCreateFuncionario:
    """Testes para operação de criação de funcionário"""
    
    def test_create_funcionario_success(self, mock_db, funcionario_valido):
        """
        CT001: Cadastrar funcionário com dados válidos
        Verifica se o funcionário é adicionado ao banco corretamente
        """
        # Arrange: Configurar mock para retornar None (CPF não existe)
        mock_db.query.return_value.filter.return_value.first.return_value = None
        
        # Act: Executar a função
        result = create_funcionario(funcionario_valido, mock_db)
        
        # Assert: Verificar se as chamadas ocorreram
        mock_db.add.assert_called_once()
        mock_db.commit.assert_called_once()
        mock_db.refresh.assert_called_once()
    
    def test_create_funcionario_cpf_duplicado(self, mock_db, funcionario_valido):
        """
        CT002: Tentar cadastrar com CPF já existente
        Deve retornar erro 400 - Bad Request
        """
        # Arrange: Simular CPF já existente
        mock_db.query.return_value.filter.return_value.first.return_value = Mock()
        
        # Act & Assert: Verificar se exceção é lançada
        with pytest.raises(HTTPException) as exc:
            create_funcionario(funcionario_valido, mock_db)
        
        assert exc.value.status_code == status.HTTP_400_BAD_REQUEST
        assert "CPF já cadastrado" in str(exc.value.detail)
    
    def test_create_funcionario_cpf_invalido(self):
        """
        CT003: Tentar cadastrar com CPF em formato inválido
        Deve falhar na validação do Pydantic
        """
        with pytest.raises(ValueError):
            funcionario_invalido = FuncionarioCreate(
                nome="Teste",
                cpf="12345678900",  # Formato inválido (sem pontos e traço)
                contato="(11) 99999-8888",
                salario=3500.00,
                tipo="TECNICO",
                data_admissao=date(2024, 1, 15)
            )
    
    def test_create_tecnico_success(self, mock_db, tecnico_valido):
        """
        CT004: Especializar funcionário como técnico
        Verifica se os dados do técnico são salvos
        """
        # Arrange: Simular funcionário existente do tipo TECNICO
        mock_funcionario = Mock(tipo="TECNICO")
        mock_db.query.return_value.filter.return_value.first.return_value = mock_funcionario
        
        # Configurar retorno para verificação de técnico existente
        mock_db.query.return_value.filter.return_value.first.side_effect = [
            mock_funcionario,  # Primeira chamada: verificar funcionário
            None               # Segunda chamada: verificar se já é técnico
        ]
        
        # Act
        result = create_tecnico(tecnico_valido, mock_db)
        
        # Assert
        mock_db.add.assert_called_once()
        mock_db.commit.assert_called_once()
    
    def test_create_tecnico_funcionario_nao_tecnico(self, mock_db, tecnico_valido):
        """
        CT005: Tentar especializar funcionário que não é técnico
        Deve retornar erro 400
        """
        # Arrange: Funcionário do tipo ADMINISTRATIVO
        mock_funcionario = Mock(tipo="ADMINISTRATIVO")
        mock_db.query.return_value.filter.return_value.first.return_value = mock_funcionario
        
        # Act & Assert
        with pytest.raises(HTTPException) as exc:
            create_tecnico(tecnico_valido, mock_db)
        
        assert exc.value.status_code == status.HTTP_400_BAD_REQUEST
        assert "não é do tipo TÉCNICO" in str(exc.value.detail)

# ============================================
# 2. TESTES DE READ (CONSULTAR)
# ============================================

class TestReadFuncionario:
    """Testes para operação de consulta de funcionários"""
    
    def test_read_funcionarios_success(self, mock_db):
        """
        CT006: Listar todos os funcionários
        Verifica se retorna a lista corretamente
        """
        # Arrange: Mock da lista de funcionários
        mock_funcionarios = [
            Mock(id=1, nome="João", tipo="TECNICO", status="ATIVO"),
            Mock(id=2, nome="Maria", tipo="ADMINISTRATIVO", status="ATIVO"),
            Mock(id=3, nome="Pedro", tipo="TECNICO", status="FERIAS")
        ]
        mock_db.query.return_value.offset.return_value.limit.return_value.all.return_value = mock_funcionarios
        
        # Act
        result = read_funcionarios(db=mock_db)
        
        # Assert
        assert len(result) == 3
        assert result[0].nome == "João"
        assert result[1].tipo == "ADMINISTRATIVO"
    
    def test_read_funcionarios_com_filtro_tipo(self, mock_db):
        """
        CT007: Listar funcionários filtrando por tipo
        Verifica se o filtro é aplicado corretamente
        """
        # Arrange
        mock_query = Mock()
        mock_db.query.return_value = mock_query
        mock_query.filter.return_value.offset.return_value.limit.return_value.all.return_value = [Mock(nome="João")]
        
        # Act
        result = read_funcionarios(tipo="TECNICO", db=mock_db)
        
        # Assert: Verificar se o filtro foi aplicado
        mock_query.filter.assert_called_once()
    
    def test_read_funcionarios_com_filtro_status(self, mock_db):
        """
        CT008: Listar funcionários filtrando por status
        """
        # Arrange
        mock_query = Mock()
        mock_db.query.return_value = mock_query
        mock_query.filter.return_value.offset.return_value.limit.return_value.all.return_value = [Mock(nome="João")]
        
        # Act
        result = read_funcionarios(status="ATIVO", db=mock_db)
        
        # Assert
        mock_query.filter.assert_called_once()
    
    def test_read_funcionarios_paginacao(self, mock_db):
        """
        CT009: Listar funcionários com paginação
        Verifica se skip e limit são aplicados
        """
        # Arrange
        mock_query = Mock()
        mock_db.query.return_value = mock_query
        
        # Act
        result = read_funcionarios(skip=10, limit=20, db=mock_db)
        
        # Assert: Verificar se paginação foi aplicada
        mock_query.offset.assert_called_with(10)
        mock_query.offset.return_value.limit.assert_called_with(20)
    
    def test_read_funcionario_by_id_success(self, mock_db):
        """
        CT010: Buscar funcionário por ID existente
        Verifica se retorna os dados corretos
        """
        # Arrange
        mock_funcionario = Mock(id=1, nome="João Silva", cpf="123.456.789-00")
        mock_db.query.return_value.filter.return_value.first.return_value = mock_funcionario
        
        # Act
        result = read_funcionario(1, mock_db)
        
        # Assert
        assert result.id == 1
        assert result.nome == "João Silva"
    
    def test_read_funcionario_by_id_not_found(self, mock_db):
        """
        CT011: Buscar funcionário por ID inexistente
        Deve retornar erro 404
        """
        # Arrange
        mock_db.query.return_value.filter.return_value.first.return_value = None
        
        # Act & Assert
        with pytest.raises(HTTPException) as exc:
            read_funcionario(999, mock_db)
        
        assert exc.value.status_code == status.HTTP_404_NOT_FOUND
        assert "não encontrado" in str(exc.value.detail)
    
    def test_read_funcionarios_lista_vazia(self, mock_db):
        """
        CT012: Listar funcionários quando não há registros
        Deve retornar lista vazia
        """
        # Arrange
        mock_db.query.return_value.offset.return_value.limit.return_value.all.return_value = []
        
        # Act
        result = read_funcionarios(db=mock_db)
        
        # Assert
        assert result == []
        assert len(result) == 0

# ============================================
# 3. TESTES DE UPDATE (ATUALIZAR)
# ============================================

class TestUpdateFuncionario:
    """Testes para operação de atualização de funcionários"""
    
    def test_update_funcionario_success(self, mock_db):
        """
        CT013: Atualizar dados de funcionário existente
        Verifica se os campos são modificados corretamente
        """
        # Arrange: Mock do funcionário existente
        mock_funcionario = Mock(
            id=1, 
            nome="João Antigo", 
            cpf="123.456.789-00", 
            salario=3000.00,
            contato="(11) 99999-1111"
        )
        mock_db.query.return_value.filter.return_value.first.return_value = mock_funcionario
        
        update_data = FuncionarioUpdate(
            nome="João Atualizado",
            salario=4500.00,
            contato="(11) 88888-2222"
        )
        
        # Act
        result = update_funcionario(1, update_data, mock_db)
        
        # Assert: Verificar se os atributos foram atualizados
        assert mock_funcionario.nome == "João Atualizado"
        assert mock_funcionario.salario == 4500.00
        assert mock_funcionario.contato == "(11) 88888-2222"
        mock_db.commit.assert_called_once()
        mock_db.refresh.assert_called_once()
    
    def test_update_funcionario_parcial(self, mock_db):
        """
        CT014: Atualizar apenas alguns campos (PATCH)
        Campos não enviados devem permanecer inalterados
        """
        # Arrange
        mock_funcionario = Mock(
            id=1, 
            nome="João",
            salario=3000.00,
            contato="(11) 99999-1111",
            horario_expediente="08:00-18:00"
        )
        mock_db.query.return_value.filter.return_value.first.return_value = mock_funcionario
        
        # Atualizar apenas o salário
        update_data = FuncionarioUpdate(salario=5000.00)
        
        # Act
        result = update_funcionario(1, update_data, mock_db)
        
        # Assert: Apenas salário deve mudar
        assert mock_funcionario.salario == 5000.00
        assert mock_funcionario.nome == "João"  # Permanece igual
        assert mock_funcionario.contato == "(11) 99999-1111"  # Permanece igual
    
    def test_update_funcionario_not_found(self, mock_db):
        """
        CT015: Atualizar funcionário inexistente
        Deve retornar erro 404
        """
        # Arrange
        mock_db.query.return_value.filter.return_value.first.return_value = None
        update_data = FuncionarioUpdate(nome="Teste")
        
        # Act & Assert
        with pytest.raises(HTTPException) as exc:
            update_funcionario(999, update_data, mock_db)
        
        assert exc.value.status_code == status.HTTP_404_NOT_FOUND
    
    def test_update_funcionario_sem_dados(self, mock_db):
        """
        CT016: Atualizar sem enviar dados
        Deve retornar erro de validação
        """
        # Arrange
        mock_funcionario = Mock(id=1)
        mock_db.query.return_value.filter.return_value.first.return_value = mock_funcionario
        
        update_data = FuncionarioUpdate()  # Nenhum campo enviado
        
        # Act & Assert
        with pytest.raises(Exception):
            update_funcionario(1, update_data, mock_db)

# ============================================
# 4. TESTES DE DELETE (REMOVER/DESATIVAR)
# ============================================

class TestDeleteFuncionario:
    """Testes para operação de remoção de funcionários"""
    
    def test_desativar_funcionario_success(self, mock_db):
        """
        CT017: Desativar funcionário (soft delete)
        Deve mudar status para DESATIVADO
        """
        # Arrange
        mock_funcionario = Mock(id=1, status="ATIVO")
        mock_db.query.return_value.filter.return_value.first.return_value = mock_funcionario
        
        # Act
        result = desativar_funcionario(1, mock_db)
        
        # Assert
        assert mock_funcionario.status == "DESATIVADO"
        assert result["message"] == "Funcionário desativado com sucesso"
        mock_db.commit.assert_called_once()
    
    def test_desativar_funcionario_already_inactive(self, mock_db):
        """
        CT018: Desativar funcionário já inativo
        Deve funcionar normalmente (mantém DESATIVADO)
        """
        # Arrange
        mock_funcionario = Mock(id=1, status="DESATIVADO")
        mock_db.query.return_value.filter.return_value.first.return_value = mock_funcionario
        
        # Act
        result = desativar_funcionario(1, mock_db)
        
        # Assert
        assert mock_funcionario.status == "DESATIVADO"
        mock_db.commit.assert_called_once()
    
    def test_desativar_funcionario_not_found(self, mock_db):
        """
        CT019: Desativar funcionário inexistente
        Deve retornar erro 404
        """
        # Arrange
        mock_db.query.return_value.filter.return_value.first.return_value = None
        
        # Act & Assert
        with pytest.raises(HTTPException) as exc:
            desativar_funcionario(999, mock_db)
        
        assert exc.value.status_code == status.HTTP_404_NOT_FOUND
    
    def test_delete_tecnico_sem_os_success(self, mock_db):
        """
        CT020: Remover técnico que não tem OS em aberto
        Deve permitir remoção
        """
        # Arrange
        mock_funcionario = Mock(id=1, tipo="TECNICO")
        mock_db.query.return_value.filter.return_value.first.return_value = mock_funcionario
        
        # Simular que não há OS em aberto
        mock_db.query.return_value.filter.return_value.first.return_value = None
        
        # Act
        result = delete_funcionario(1, mock_db)
        
        # Assert
        mock_db.delete.assert_called_once_with(mock_funcionario)
        assert result["message"] == "Funcionário removido com sucesso"
    
    def test_delete_tecnico_com_os_aberta_fails(self, mock_db):
        """
        CT021: Remover técnico que tem OS em aberto
        Deve retornar erro 400
        """
        # Arrange
        mock_funcionario = Mock(id=1, tipo="TECNICO")
        
        # Configurar side_effect para diferentes chamadas
        mock_db.query.return_value.filter.return_value.first.side_effect = [
            mock_funcionario,      # Primeira chamada: verificar funcionário
            Mock()                 # Segunda chamada: OS em aberto encontrada
        ]
        
        # Act & Assert
        with pytest.raises(HTTPException) as exc:
            delete_funcionario(1, mock_db)
        
        assert exc.value.status_code == status.HTTP_400_BAD_REQUEST
        assert "ordens de serviço em aberto" in str(exc.value.detail)
    
    def test_delete_administrativo_success(self, mock_db):
        """
        CT022: Remover administrativo (não tem restrição de OS)
        Deve permitir remoção diretamente
        """
        # Arrange
        mock_funcionario = Mock(id=1, tipo="ADMINISTRATIVO")
        mock_db.query.return_value.filter.return_value.first.return_value = mock_funcionario
        
        # Act
        result = delete_funcionario(1, mock_db)
        
        # Assert
        mock_db.delete.assert_called_once()
        assert result["message"] == "Funcionário removido com sucesso"
    
    def test_delete_funcionario_not_found(self, mock_db):
        """
        CT023: Remover funcionário inexistente
        Deve retornar erro 404
        """
        # Arrange
        mock_db.query.return_value.filter.return_value.first.return_value = None
        
        # Act & Assert
        with pytest.raises(HTTPException) as exc:
            delete_funcionario(999, mock_db)
        
        assert exc.value.status_code == status.HTTP_404_NOT_FOUND

# ============================================
# TESTES PARAMETRIZADOS
# ============================================

class TestFuncionarioValidacoes:
    """Testes parametrizados para validações diversas"""
    
    @pytest.mark.parametrize("campo,valor,deve_passar", [
        ("nome", "João", True),
        ("nome", "A", False),  # Muito curto
        ("nome", "A" * 151, False),  # Muito longo
        ("salario", 1000.00, True),
        ("salario", -100.00, False),  # Negativo
        ("tipo", "TECNICO", True),
        ("tipo", "ADMINISTRATIVO", True),
        ("tipo", "GERENTE", False),  # Inválido
        ("status", "ATIVO", True),
        ("status", "INATIVO", False),  # Inválido
    ])
    def test_validacao_campos(self, campo, valor, deve_passar):
        """Testes parametrizados para validação de campos"""
        dados = {
            "nome": "João Silva",
            "cpf": "123.456.789-00",
            "contato": "(11) 99999-8888",
            "salario": 3500.00,
            "tipo": "TECNICO",
            "data_admissao": date(2024, 1, 15)
        }
        dados[campo] = valor
        
        if deve_passar:
            # Deve criar sem exceção
            obj = FuncionarioCreate(**dados)
            assert getattr(obj, campo) == valor
        else:
            # Deve lançar exceção de validação
            with pytest.raises(Exception):
                FuncionarioCreate(**dados)