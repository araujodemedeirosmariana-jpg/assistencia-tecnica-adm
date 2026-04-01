# Documento de Arquitetura do Software

## 🧭 Visão Geral

O Sistema de Gestão de Assistência Técnica segue uma arquitetura em camadas, separando responsabilidades entre interface, lógica de negócio e persistência de dados.

```mermaid
flowchart LR
    Usuario --> Frontend
    Frontend --> Backend
    Backend --> Banco

    subgraph Frontend
        UI[Interface Web]
    end

    subgraph Backend
        API[API REST - FastAPI]
        Regras[Regras de Negócio]
    end

    subgraph Banco
        DB[(SQLite)]
    end