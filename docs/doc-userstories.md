# Documento Lista de User Stories

Documento construído a partir do **Modelo BSI - Doc 004 - Lista de User Stories**.

---

## Descrição

Este documento descreve os User Stories criados a partir da Lista de Requisitos no Documento de Visão do projeto Sistema de Gestão de Assistência Técnica.

---

## Histórico de revisões

| Data       | Versão | Descrição                                     | Autor  |
|------------|--------|-----------------------------------------------|--------|
| 30/03/2026 | 0.1.0  | Criação inicial da lista de User Stories      | Jadson |
| 31/03/2026 | 1.0.0  | Documento completo com User Stories revisado  | Jadson |
| 17/04/2026 | 1.1.0  | Correção de inconsistências e adição de novas US12 a US14 | Mariana |

---

# 📌 USER STORIES

---

## US01 - Cadastrar Cliente

**Descrição:**  
Permite cadastrar clientes com nome, endereço, contato e documento (CPF para Pessoa Física ou CNPJ para Pessoa Jurídica), conforme o tipo de cliente.

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
- CPF/CNPJ inválido (formato incorreto) gera erro  
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

## US03 - Desativar Cliente

**Descrição:**  
Permite desativar clientes do sistema. 

**Requisitos:** RF01  

**Prioridade:** Importante  
**Estimativa:** 3h  

**Responsáveis:**  
- Analista: Jadson  
- Desenvolvedor: Jadson  
- Revisor: Mariana  
- Testador: Jadson  

**Testes de Aceitação:**  
- Cliente destivado com sucesso  
- Erro ao desativar cliente inexistente  

---

## US04 - Cadastrar Equipamento

**Descrição:**  
Permite cadastrar equipamentos.

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
- Código duplicado gera erro

---

## US05 - Criar Ordem de Serviço

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
- Técnico deve estar ATIVO e ter especialização TECNICO 
- Cliente obrigatório  

---

## US06 - Atualizar Status da OS

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

## US07 - Vincular Equipamentos à OS

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

## US08 - Registrar Visita Técnica

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

## US09 - Gerenciar Funcionários

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
- Consulta por nome, CPF, tipo ou status retorna resultados corretos 
- Dados inválidos geram erro  

---

## US10 - Encerrar OS e Gerar Conta

**Descrição:**  
Permite encerrar uma Ordem de Serviço (status FINALIZADA) e gera automaticamente uma CONTA_RECEBER com valor_total da OS, data_emissão atual e data_vencimento calculada.

**Requisitos:** RF03, RF06  

**Prioridade:** Essencial  
**Estimativa:** 5h  

**Responsáveis:**  
- Analista: Jadson  
- Desenvolvedor: Jadson  
- Revisor: Mariana  
- Testador: Jadson  

**Testes de Aceitação:**  
- OS encerrada com sucesso (status FINALIZADA)
- Conta gerada automaticamente ao encerrar a OS  
- Valor correto 
- Data_emissão = data atual
- Data_vencimento calculada corretamente
- OS sem valor_total válido impede encerramento 

---

## US11 - Marcar Conta como Paga

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
- Conta com status PAGO não pode ser alterada novamente 
- Conta inexistente gera erro  

---

## US12 - Realizar Login no Sistema 

**Descrição:**
Permite que usuários (clientes e funcionários) realizem autenticação no sistema com e-mail e senha, conforme tabela USUARIO.

**Requisitos:** RF08 

**Prioridade:** Essencial
**Estimativa:** 5h

**Responsáveis:**
- Analista: Jadson
- Desenvolvedor: Mariana
- Revisor: Jadson
- Testador: Mariana

**Testes de Aceitação:**
- Login realizado com sucesso com credenciais válidas
- E-mail ou senha incorretos geram erro
- Apenas usuários ativos (cliente não desativado / funcionário ativo) podem acessar
- Sessão expira após inatividade (30 minutos)
- Senha deve ser armazenada de forma criptografada no banco de dados

---

## US13 - Relatório de Ordens de Serviço por Período 

**Descrição:**
Permite gerar um relatório de ordens de serviço filtrado por período de abertura, status e técnico responsável, com opção de exportação (PDF/CSV).

**Requisitos:** RF03

**Prioridade:** Importante
**Estimativa:** 6h

**Responsáveis:**
- Analista: Mariana
- Desenvolvedor: Mariana
- Revisor: Jadson
- Testador: Mariana

**Testes de Aceitação:**
- Relatório gerado com sucesso no período selecionado
- Filtro por status funciona
- Filtro por técnico funciona
- Exibe: ID da OS, cliente, data_abertura, data_encerramento, status, valor_total
- Exibe totalizadores (quantidade de OS e valor total no período)
- Período inválido (data_fim < data_início) gera erro
- Opção de exportar para PDF e CSV funciona

---

## US14 - Controle de Garantia 

**Descrição:**
Permite consultar e controlar o período de garantia das ordens de serviço finalizadas, com alerta para garantias próximas do vencimento ou já expiradas.

**Requisitos:** RF03

**Prioridade:** Importante
**Estimativa:** 5h

**Responsáveis:**
- Analista: Jadson
- Desenvolvedor: Jadson
- Revisor: Mariana
- Testador: Jadson

**Testes de Aceitação:**
- Exibe OS com garantia ativa (dentro do prazo)
- Exibe OS com garantia expirada (data_encerramento + garantia_dias < data atual)
- Alerta visual para garantias que vencem em até 7 dias
- Consulta por cliente ou equipamento
- Exibe quantidade de dias restantes de garantia
- Permite registrar atendimento em garantia (nova OS vinculada)

---

# Matriz de Rastreabilidade - Requisitos Funcionais x User Stories

| ID | Requisito Funcional | User Stories | Total |
|:---|:---|:---|:---:|
| RF01 | Gerenciar Clientes | US01, US02, US03 | 3 |
| RF02 | Gerenciar Funcionários | US09 | 1 |
| RF03 | Gerenciar Ordens de Serviço | US05, US06, US07, US10, US13, US14 | 6 |
| RF04 | Gerenciar Equipamentos | US04 | 1 |
| RF05 | Registrar Visita Técnica | US08 | 1 |
| RF06 | Gerar Contas a Receber | US10 | 1 |
| RF07 | Registrar Pagamento | US11 | 1 |
| RF08 | Autenticação de Usuários | US12 | 1 |

## 📊 Estatísticas

- **Total de Requisitos Funcionais:** 8
- **Total de User Stories:** 14
- **Média de US por RF:** 1.75