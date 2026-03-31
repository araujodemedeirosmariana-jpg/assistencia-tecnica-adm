# Modelo de Dados

## 📊 Diagrama Entidade-Relacionamento (DER)

```mermaid
erDiagram
    CLIENTE {
        int id_cliente
        string nome
        string endereco
        string contato
        string cpf
    }

    FUNCIONARIO {
        int id_funcionario
        string nome
        string endereco
        string contato
        string horario
        float salario
        string cnpj
        boolean ativo
    }

    EQUIPAMENTO {
        int id_equipamento
        string tipo
        string marca
        string modelo
        string numero_serie
        int id_cliente
    }

    ORDEM_SERVICO {
        int id_os
        int id_cliente
        string descricao
        string status
        date data_abertura
        date data_encerramento
    }

    CONTA {
        int id_conta
        int id_os
        float valor
        string tipo
        string status
    }

    VISITA_TECNICA {
        int id_visita
        int id_os
        int tecnico
        date data
        string horario
        string observacoes
    }

    ORDEM_SERVICO_EQUIPAMENTO {
        int id_os
        int id_equipamento
    }

    CLIENTE ||--o{ EQUIPAMENTO : possui
    CLIENTE ||--o{ ORDEM_SERVICO : solicita
    FUNCIONARIO ||--o{ VISITA_TECNICA : realiza
    ORDEM_SERVICO ||--o{ VISITA_TECNICA : possui
    ORDEM_SERVICO ||--o{ CONTA : gera
    ORDEM_SERVICO ||--o{ ORDEM_SERVICO_EQUIPAMENTO : vincula
    EQUIPAMENTO ||--o{ ORDEM_SERVICO_EQUIPAMENTO : pertence