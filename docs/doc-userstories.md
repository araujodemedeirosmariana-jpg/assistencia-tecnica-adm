# Documento Lista de User Stories

Documento construído a partir do **Modelo BSI - Doc 004 - Lista de User Stories**.

---

## Descrição

Este documento descreve os User Stories criados a partir da Lista de Requisitos no Documento de Visão do projeto Sistema de Gestão de Assistência Técnica.

---

## Histórico de revisões

| Data       | Versão  | Descrição                                      | Autor   |
|------------|--------|-----------------------------------------------|--------|
| 30/03/2026 | 0.1.0  | Criação inicial da lista de User Stories      | Jadson |
| 31/03/2026 | 1.0.0  | Documento completo com User Stories revisado  | Equipe |

---

# 📌 USER STORIES

---

## US01 - Cadastrar Cliente

**Descrição:**  
Permite cadastrar clientes com nome, endereço, contato e CPF.

**Requisitos:** RF01  

**Prioridade:** Essencial  
**Estimativa:** 4h  

**Responsáveis:**  
- Analista: Jadson  
- Desenvolvedor: Jadson  
- Revisor: Mariana  
- Testador: Jadson  

**Testes de Aceitação:**  
- Cadastro realizado com sucesso  
- CPF duplicado gera erro  
- Campos obrigatórios devem ser validados  

---

## US02 - Atualizar Cliente

**Descrição:**  
Permite atualizar dados de clientes cadastrados.

**Requisitos:** RF01  

**Prioridade:** Essencial  
**Estimativa:** 3h  

**Responsáveis:**  
- Analista: Mariana  
- Desenvolvedor: Mariana  
- Revisor: Jadson  
- Testador: Mariana  

**Testes de Aceitação:**  
- Dados atualizados corretamente  
- Cliente inexistente retorna erro  

---

## US03 - Excluir Cliente

**Descrição:**  
Permite remover clientes do sistema.

**Requisitos:** RF01  

**Prioridade:** Importante  
**Estimativa:** 3h  

**Responsáveis:**  
- Analista: Jadson  
- Desenvolvedor: Jadson  
- Revisor: Mariana  
- Testador: Jadson  

**Testes de Aceitação:**  
- Cliente removido com sucesso  
- Erro ao excluir cliente inexistente  

---

## US04 - Cadastrar Equipamento

**Descrição:**  
Permite cadastrar equipamentos vinculados a clientes.

**Requisitos:** RF04  

**Prioridade:** Essencial  
**Estimativa:** 4h  

**Responsáveis:**  
- Analista: Mariana  
- Desenvolvedor: Mariana  
- Revisor: Jadson  
- Testador: Mariana  

**Testes de Aceitação:**  
- Equipamento cadastrado com sucesso  
- Cliente inválido gera erro  

---

## US05 - Vincular Equipamento ao Cliente

**Descrição:**  
Permite associar um equipamento a um cliente existente.

**Requisitos:** RF04  

**Prioridade:** Essencial  
**Estimativa:** 3h  

**Responsáveis:**  
- Analista: Jadson  
- Desenvolvedor: Jadson  
- Revisor: Mariana  
- Testador: Jadson  

**Testes de Aceitação:**  
- Equipamento vinculado corretamente  
- Cliente inexistente gera erro  

---

## US06 - Criar Ordem de Serviço

**Descrição:**  
Permite registrar uma nova ordem de serviço.

**Requisitos:** RF03  

**Prioridade:** Essencial  
**Estimativa:** 5h  

**Responsáveis:**  
- Analista: Mariana  
- Desenvolvedor: Mariana  
- Revisor: Jadson  
- Testador: Mariana  

**Testes de Aceitação:**  
- OS criada com sucesso  
- Cliente obrigatório  

---

## US07 - Atualizar Status da OS

**Descrição:**  
Permite atualizar o status da ordem de serviço.

**Requisitos:** RF03  

**Prioridade:** Essencial  
**Estimativa:** 3h  

**Responsáveis:**  
- Analista: Jadson  
- Desenvolvedor: Jadson  
- Revisor: Mariana  
- Testador: Jadson  

**Testes de Aceitação:**  
- Status atualizado  
- Status inválido gera erro  

---

## US08 - Vincular Equipamentos à OS

**Descrição:**  
Permite associar equipamentos a uma ordem de serviço.

**Requisitos:** RF03  

**Prioridade:** Essencial  
**Estimativa:** 4h  

**Responsáveis:**  
- Analista: Mariana  
- Desenvolvedor: Mariana  
- Revisor: Jadson  
- Testador: Mariana  

**Testes de Aceitação:**  
- Equipamento vinculado à OS  
- Equipamento inexistente gera erro  

---

## US09 - Registrar Visita Técnica

**Descrição:**  
Permite registrar visitas técnicas vinculadas a uma OS.

**Requisitos:** RF05  

**Prioridade:** Importante  
**Estimativa:** 4h  

**Responsáveis:**  
- Analista: Jadson  
- Desenvolvedor: Jadson  
- Revisor: Mariana  
- Testador: Jadson  

**Testes de Aceitação:**  
- Visita registrada com sucesso  
- OS inválida gera erro  

---

## US10 - Gerenciar Funcionários

**Descrição:**  
Permite cadastrar e gerenciar funcionários.

**Requisitos:** RF02  

**Prioridade:** Essencial  
**Estimativa:** 5h  

**Responsáveis:**  
- Analista: Mariana  
- Desenvolvedor: Mariana  
- Revisor: Jadson  
- Testador: Mariana  

**Testes de Aceitação:**  
- Funcionário cadastrado  
- Dados inválidos geram erro  

---

## US11 - Gerar Conta da OS

**Descrição:**  
Gera automaticamente uma conta ao criar/encerrar OS.

**Requisitos:** RF06  

**Prioridade:** Essencial  
**Estimativa:** 4h  

**Responsáveis:**  
- Analista: Jadson  
- Desenvolvedor: Jadson  
- Revisor: Mariana  
- Testador: Jadson  

**Testes de Aceitação:**  
- Conta gerada automaticamente  
- Valor correto  

---

## US12 - Marcar Conta como Paga

**Descrição:**  
Permite atualizar status da conta para paga.

**Requisitos:** RF07  

**Prioridade:** Essencial  
**Estimativa:** 3h  

**Responsáveis:**  
- Analista: Mariana  
- Desenvolvedor: Mariana  
- Revisor: Jadson  
- Testador: Mariana  

**Testes de Aceitação:**  
- Conta marcada como paga  
- Conta inexistente gera erro  

---