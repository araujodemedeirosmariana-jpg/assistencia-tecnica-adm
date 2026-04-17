# Modelo de Dados

## 📊 Diagrama Entidade-Relacionamento (DER)


```mermaid
erDiagram
    USUARIO {
        int id PK
        string email
        string senha
    }
    
    CLIENTE {
        int id PK
        string nome
        string endereco
        string contato
        string tipo
    }
    
    CLIENTE_PF {
        int id PK
        string cpf
        date data_nascimento
    }
    
    CLIENTE_PJ {
        int id PK
        string cnpj
        string razao_social
        string nome_fantasia
    }
    
    FUNCIONARIO {
        int id PK
        string nome
        string cpf
        string contato
        float salario
        string tipo
        date data_admissao
        string horario_expediente
        string status
    }
    
    TECNICO {
        int id PK
        string especialidade
        string certificacoes
        int nivel_experiencia
        float comissao_percentual
    }
    
    ADMINISTRATIVO {
        int id PK
        string cargo
        string setor
        float bonus_fixo
    }
    
    ORDEM_SERVICO {
        int id PK
        date data_abertura
        date data_encerramento
        string descricao_problema
        string status
        float valor_total
        int garantia_dias
        int cliente_id FK
        int tecnico_id FK
    }
    
    EQUIPAMENTO {
        int id PK
        string codigo
        string tipo
        string marca
        string modelo
        int quantidade
    }
    
    VISITA_TECNICA {
        int id PK
        date data_agendamento
        date data_realizacao
        string resultado
        int os_id FK
        int tecnico_id FK
    }
    
    CONTA_RECEBER {
        int id PK
        float valor
        date data_emissao
        date data_vencimento
        date data_pagamento
        string status_pagamento
        int os_id FK
    }
    
    ORDEM_SERVICO_EQUIPAMENTO {
        int os_id FK
        int equipamento_id FK
        int quantidade
    }
    
    USUARIO ||--o| CLIENTE : "pode ser"
    USUARIO ||--o| FUNCIONARIO : "pode ser"
    CLIENTE ||--o| CLIENTE_PF : "classificado PF"
    CLIENTE ||--o| CLIENTE_PJ : "classificado PJ"
    FUNCIONARIO ||--o| TECNICO : "classificado TECNICO"
    FUNCIONARIO ||--o| ADMINISTRATIVO : "classificado ADMINISTRATIVO"
    CLIENTE ||--o{ ORDEM_SERVICO : "solicita"
    TECNICO ||--o{ ORDEM_SERVICO : "responsavel"
    TECNICO ||--o{ VISITA_TECNICA : "realiza"
    ORDEM_SERVICO ||--o{ VISITA_TECNICA : "gera"
    ORDEM_SERVICO ||--|| CONTA_RECEBER : "gera"
    ORDEM_SERVICO ||--o{ ORDEM_SERVICO_EQUIPAMENTO : "contem"
    EQUIPAMENTO ||--o{ ORDEM_SERVICO_EQUIPAMENTO : "utilizado"
```
### Descrição das Entidades

Entidade                          |	Descrição   |
---------                         | ----------- |
Usuário	   | Entidade base para autenticação, contendo credenciais de acesso (email e senha). |
Cliente	   | Entidade base para clientes, contendo atributos comuns a qualquer cliente (nome, endereço, contato). Possui uma especialização total e disjunta para CPF e CNPJ. |
Cliente CPF	| Especialização da entidade Cliente. Armazena dados específicos de Pessoa Física: CPF e data de nascimento. |
Cliente CNPJ	| Especialização da entidade Cliente. Armazena dados específicos de Pessoa Jurídica: CNPJ, razão social e nome fantasia. |
Funcionário	 | Herda de Usuário. Armazena dados profissionais, diferenciando Técnico e Administrativo (especialização total e disjunta). |
Técnico | Especialização da entidade Funcionario. Armazena dados específicos como especialidade, certificações, nível de experiência e comissão percentual. Responsável pela execução de Ordens de Serviço e Visitas Técnicas.|
Administrativo | Especialização da entidade Funcionario. Armazena dados específicos como cargo, setor, bônus fixo e horário de expediente. Responsável por atividades administrativas e gestão. |
Ordem de Serviço | Núcleo do sistema, registra cada solicitação de serviço, seu status, valor, e vincula cliente e técnico responsável. |
Equipamento	| Representa os itens que serão reparados ou utilizados nos serviços. Contém informações como código, tipo, marca, modelo e quantidade disponível. |
Ordem de Serviço Equipamento | Tabela de relacionamento muitos-para-muitos entre OS e Equipamento. Armazena a quantidade de cada equipamento utilizado em uma determinada OS. |
Visita Técnica | Vinculada a uma OS, registra agendamentos e realizações de atendimentos presenciais. |
Conta a Receber	| Gerada automaticamente ao encerrar uma OS, registra o valor a ser pago pelo cliente. |

---

## Entidade-Relacionamento

### Dicionário de Dados

|   Tabela   | USUARIO |
| ---------- | ----------- |
| Descrição  | Armazena as credenciais de autenticação dos usuários do sistema. |
| Observação | É uma entidade abstrata/base para autenticação. Um usuário pode ser cliente ou funcionário, mas não ambos simultaneamente. |

|  Nome         | Descrição                        | Tipo de Dado | Tamanho | Restrições de Domínio |
| ------------- | -------------------------------- | ------------ | ------- | --------------------- |
| id | Identificador único gerado pelo SGBD	| SERIAL | --- | PK / Identity |
| e-mail | e-mail do usuário utilizado para login  | VARCHAR | 150 | Unique / Not Null |
| senha  | Senha criptografada do usuário | VARCHAR | 255 | Not Null |

|   Tabela   | CLIENTE |
| ---------- | ----------- |
| Descrição  | Armazena as informações gerais dos clientes da assistência técnica. |
| Observação | Clientes podem ser Pessoa Física (PF) ou Pessoa Jurídica (PJ). A diferenciação é feita pelo campo classificado, com dados complementares armazenados nas tabelas Cliente_PF e Cliente_PJ. |

|  Nome         | Descrição                        | Tipo de Dado | Tamanho | Restrições de Domínio |
| ------------- | -------------------------------- | ------------ | ------- | --------------------- |
| id | Identificador único | SERIAL | --- | PK / Identity |
| nome | Nome completo do cliente (PF) ou razão social (PJ) | VARCHAR | 150 | Not Null |
| endereco  | Endereço completo do cliente | VARCHAR | 200 | --- |
| contato | Telefone para contato | VARCHAR | 20 | --- |
| tipo | Classificação do cliente (PF ou PJ) | VARCHAR | 2 | com CHECK (tipo IN ('PF','PJ')) |

|   Tabela   | CLIENTE_PF |
| ---------- | ----------- |
| Descrição  | Armazena informações específicas de clientes do tipo Pessoa Física. |
| Observação | Todo cliente PF deve ter um registro correspondente na tabela Cliente.|

|  Nome         | Descrição                        | Tipo de Dado | Tamanho | Restrições de Domínio |
| ------------- | -------------------------------- | ------------ | ------- | --------------------- |
| id | Identificador único(FK para CLIENTE) | INT | --- | PK / FK |
| cpf | Cadastro de Pessoa Física | VARCHAR | 14 | Unique / Not Null |
| data_nascimento  | Data de nascimento do cliente | DATE | --- | Not Null |

|   Tabela   | CLIENTE_PJ |
| ---------- | ----------- |
| Descrição  | Armazena informações específicas de clientes do tipo Pessoa Jurítica. |
| Observação | Todo cliente PJ deve ter um registro correspondente na tabela Cliente.|

|  Nome         | Descrição                        | Tipo de Dado | Tamanho | Restrições de Domínio |
| ------------- | -------------------------------- | ------------ | ------- | --------------------- |
| id | Identificador único(FK para CLIENTE) | INT | --- | PK / FK |
| cnpj | Cadastro Nacional da Pessoa Jurídica | VARCHAR | 18 | Unique / Not Null |
| razao_social  | Razão social da empresa | VARCHAR | 150 | Not Null |
| nome_fantasia | Nome fantasia da empresa | VARCHAR | 100 | --- |

|   Tabela   | FUNCIONARIO |
| ---------- | ----------- |
| Descrição  | Armazena as informações gerais dos funcionários da assistência técnica. |
| Observação | Funcionários podem ser técnico ou administrativo. A diferenciação é feita pelo campo classificado, com dados complementares armazenados nas tabelas Técnico e Administrativo. |

|  Nome         | Descrição                        | Tipo de Dado | Tamanho | Restrições de Domínio |
| ------------- | -------------------------------- | ------------ | ------- | --------------------- |
| id | Identificador único | SERIAL | --- | PK / Identity |
| nome | Nome completo do Funcionário  | VARCHAR | 150 | Not Null |
| cpf |	Cadastro de Pessoa Física |	VARCHAR | 14 | Unique / Not Null |
| contato | Telefone para contato | VARCHAR | 20 | --- |
| salario |	Salário base do funcionário | DECIMAL(10,2) | --- |	Not Null |
| tipo | Classificação do funcionário (técnico ou administrativo) | VARCHAR | 2 | CHECK (tipo IN ('TECNICO','ADMINISTRATIVO')) / Not Null |
| data_admissao	| Data de contratação |	DATE | --- | Not Null |
| horario_expediente | Horário de trabalho | VARCHAR | 50 |	--- |
| status |	Situação do funcionário	| VARCHAR |	10	| CHECK (status IN ('ATIVO','FERIAS','AFASTADO','DESATIVADO'))

|   Tabela   | TECNICO |
| ---------- | ----------- |
| Descrição  | Responsável pela execução de Ordens de Serviço e Visitas Técnicas. Armazena dados específicos como especialidade, certificações, nível de experiência e comissão percentual. |
| Observação | Especialização da tabela FUNCIONARIO. Todo técnico deve ter um registro correspondente na tabela FUNCIONARIO com tipo = 'TECNICO'. |

|  Nome         | Descrição                        | Tipo de Dado | Tamanho | Restrições de Domínio |
| ------------- | -------------------------------- | ------------ | ------- | --------------------- |
| id | Identificador único(FK para FUNCIONARIO) | INT | --- | PK / FK |
| especialidade | Área de atuação principal | VARCHAR | 100 | Not Null |
| certificacoes  | Certificações técnicas (formato JSON ou texto) | TEXT| --- | --- |
| nivel_experiencia | Nível hierárquico (1-5) | INT | --- | CHECK (nivel_experiencia BETWEEN 1 AND 5) |
|comissao_percentual | Percentual de comissão sobre serviços | DECIMAL(5,2) | --- |	DEFAULT 0.00, CHECK (comissao_percentual >= 0) |

|   Tabela   | ADMINISTRATIVO |
| ---------- | ----------- |
| Descrição  | Responsável pela gestão, emissão de contas, cadastro de clientes etc. |
| Observação | Especialização da tabela FUNCIONARIO. Todo administrato deve ter um registro correspondente na tabela FUNCIONARIO com tipo = 'ADMINISTRATIVO'. |

|  Nome         | Descrição                        | Tipo de Dado | Tamanho | Restrições de Domínio |
| ------------- | -------------------------------- | ------------ | ------- | --------------------- |
| id | Identificador único(FK para FUNCIONARIO) | INT | --- | PK / FK |
| cargo | Cargo administrativo | VARCHAR | 80 | Not Null |
| setor | Nível hierárquico (1-5) | INT | --- | CHECK (nivel_experiencia BETWEEN 1 AND 5) |
|bonus_fixo | Bônus mensal fixo | DECIMAL(10,2) | --- |	DEFAULT 0.00 |

|   Tabela   | ORDEM_SERVICO |
| ---------- | ----------- |
| Descrição  | Núcleo do sistema. Registra cada solicitação de serviço, seu status, valor total, datas de abertura e encerramento, além de vincular cliente solicitante e técnico responsável. |
| Observação | Uma OS é aberta para cada atendimento solicitado. Ao ser finalizada, gera automaticamente uma CONTA_RECEBER. |

|  Nome         | Descrição                        | Tipo de Dado | Tamanho | Restrições de Domínio |
| ------------- | -------------------------------- | ------------ | ------- | --------------------- |
| id | Identificador único da OS | SERIAL | --- | PK / Identity |
| data_abertura | Data de criação da Ordem de Serviço  | DATE | --- | NOT NULL / DEFAULT CURRENT_DATE |
| data_encerramento  | Data de conclusão do serviço | DATE | --- | --- |
| descricao_problema | Descrição detalhada do problema relatado pelo cliente | TEXT | --- |	NOT NULL |
| status | Situação atual da Ordem de Serviço |	VARCHAR | 20 | CHECK (status IN ('ABERTA', 'EM_ANDAMENTO', 'AGUARDANDO_PECA', 'FINALIZADA', 'CANCELADA')) / DEFAULT 'ABERTA' |
| valor_total |	Valor total do serviço (mão de obra + equipamentos) | DECIMAL(10,2) | --- |	DEFAULT 0.00 |
| garantia_dias | Dias de garantia do serviço prestado | INT | --- |  DEFAULT 90 |
| cliente_id | Referência ao cliente solicitante | INT | --- | FK para CLIENTE(id) / NOT NULL |
| tecnico_id | Referência ao técnico responsável | INT | --- | FK para TECNICO(id) |

|   Tabela   | EQUIPAMENTO |
| ---------- | ----------- |
| Descrição  | Representa os itens que serão utilizados nos serviços prestados. |
| Observação | Um equipamento pode ser utilizado em múltiplas Ordens de Serviço, e uma OS pode utilizar múltiplos equipamentos (relacionamento N:N). |

|  Nome         | Descrição                        | Tipo de Dado | Tamanho | Restrições de Domínio |
| ------------- | -------------------------------- | ------------ | ------- | --------------------- |
| id | Identificador único da equipamento | SERIAL | --- | PK / Identity |
| codigo | Código de identificação do equipamento  | VARCHAR | 15 | UNIQUE / NOT NULL |
| tipo  | Tipo/categoria do equipamento | VARCHAR | 20 | NOT NULL |
| marca | Marca do equipamento | VARCHAR | 20 |	--- |
| modelo | Modelo do equipamento | VARCHAR | 20 | --- |
| quantidade | Quantidade disponível em estoque | INT | --- | DEFAULT 1 / CHECK (quantidade >= 0) |

|   Tabela   | ORDEM_SERVICO_EQUIPAMENTO |
| ---------- | ----------- |
| Descrição  | Tabela de relacionamento muitos-para-muitos entre Ordem de Serviço e Equipamento. |
| Observação | Permite registrar quais equipamentos foram utilizados em cada OS, com quantidade. |

|  Nome         | Descrição                        | Tipo de Dado | Tamanho | Restrições de Domínio |
| ------------- | -------------------------------- | ------------ | ------- | --------------------- |
| os_id | Referência à Ordem de Serviço | INT | --- | FK para ORDEM_SERVICO(id) / PK Composite |
| equipamento_id | Referência ao Equipamento  | INT | --- | FK para EQUIPAMENTO(id) / PK Composite |
| quantidade | Quantidade do equipamento utilizada na OS | INT | --- | DEFAULT 1 / CHECK (quantidade > 0) |

|   Tabela   | VISITA_TECNICA |
| ---------- | ----------- |
| Descrição  | Vinculada a uma OS, registra agendamentos e realizações de atendimentos presenciais. |
| Observação | A visita só pode ser atribuída a um técnico válido (especialização de FUNCIONARIO). |

|  Nome         | Descrição                        | Tipo de Dado | Tamanho | Restrições de Domínio |
| ------------- | -------------------------------- | ------------ | ------- | --------------------- |
| id | Identificador único da visita | SERIAL | --- | PK / Identity |
| data_agendamento | Data agendada para a visita técnica  | DATE | --- | NOT NULL |
| data_realizacao  | Data em que a visita foi efetivamente realizada | DATE | --- | --- |
| resultado | Descrição do resultado da visita técnica | TEXT | --- | --- |
| os_id | Referência à Ordem de Serviço | INT | --- | FK para ORDEM_SERVICO(id) / NOT NULL |
| tecnico_id | Referência ao técnico responsável | INT | --- | FK para TECNICO(id)/ NOT NULL |

|   Tabela   | CONTA_RECEBER |
| ---------- | ----------- |
| Descrição  | Gerada automaticamente ao encerrar uma OS, registra o valor a ser pago pelo cliente e controla o status do pagamento. |
| Observação | O status muda de PENDENTE para PAGO quando o pagamento é registrado. |

|  Nome         | Descrição                        | Tipo de Dado | Tamanho | Restrições de Domínio |
| ------------- | -------------------------------- | ------------ | ------- | --------------------- |
| id | Identificador único do pagamento | SERIAL | --- | PK / Identity |
| valor | Valor a ser recebido do cliente  | DECIMAL(10,2) | --- | NOT NULL / CHECK (valor > 0) |
| data_emissao  | Data de emissão da conta | DATE | --- | NOT NULL / DEFAULT CURRENT_DATE |
| data_vencimento  | Data de vencimento da conta | DATE | --- | NOT NULL |
| data_pagamento  | Data em que a conta foi paga | DATE | --- | --- |
| status_pagamento | Situação atual do pagamento | VARCHAR | 10 | CHECK (status_pagamento IN ('PENDENTE', 'PAGO', 'VENCIDO', 'CANCELADO')) / DEFAULT 'PENDENTE' |
| os_id | Referência à Ordem de Serviço | INT | --- | FK para ORDEM_SERVICO(id) / NOT NULL |
