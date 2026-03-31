# 🛠️ Sistema de Assistência Técnica

## 📌 Objetivo

O Sistema de Assistência Técnica tem como objetivo facilitar o gerenciamento de clientes, equipamentos e ordens de serviço, proporcionando maior organização, controle e eficiência no atendimento técnico.

---

## 🚀 Funcionalidades

* Cadastro e gerenciamento de clientes
* Cadastro de equipamentos 
* Criação e controle de ordens de serviço
* Registro de visitas técnicas
* Gerenciamento de funcionários
* Controle financeiro através de contas (pendente, pago, cancelado)

---

## 💻 Tecnologias Utilizadas

* **Python**
* **FastAPI**
* **SQLite**
* **Git & GitHub**
* **VS Code**

---

## ⚙️ Arquitetura do Projeto

O sistema segue uma arquitetura modular, separando responsabilidades em camadas:

* `models/` → Representação das entidades e acesso ao banco
* `data/` → Banco de dados SQLite
* `docs/` → Documentação do projeto

---

## 📂 Documentação

Os artefatos do projeto estão disponíveis na pasta `/docs`:

* 📄 [Documento de Visão](docs/doc-visao.md)
* 📊 [Modelo de Dados](docs/doc-modelos.md)
* 📋 [User Stories](docs/doc-userstories.md)

---

## 🔧 Como Executar o Projeto

### 1. Clonar o repositório

```bash
git clone https://github.com/Jadson-Hipolito/assistencia-tecnica-ads
cd assistencia-tecnica-ads
```

### 2. Criar ambiente virtual

```bash
python -m venv venv
```

### 3. Ativar ambiente virtual

* Windows:

```bash
venv\Scripts\activate
```

* Linux/Mac:

```bash
source venv/bin/activate
```

### 4. Instalar dependências

```bash
pip install fastapi uvicorn
```

### 5. Executar o servidor

```bash
uvicorn main:app --reload
```

---

## 📚 Tutorial Utilizado

* https://fastapi.tiangolo.com/tutorial/sql-databases/

---

## 🌿 Metodologia de Desenvolvimento

O projeto segue a metodologia ágil com **GitFlow**:

* `main` → versão estável
* `develop` → desenvolvimento
* `feature/*` → novas funcionalidades

Pull Requests são utilizados para revisão de código antes da integração.

---

## 🔢 Versionamento

O projeto utiliza **Versionamento Semântico**:

```
MAJOR.MINOR.PATCH
```

Exemplo:

```
1.0.0
```

---

## 📝 Padrão de Commits

Utilizamos **Conventional Commits**:

* `feat:` nova funcionalidade
* `fix:` correção de bugs
* `docs:` documentação
* `chore:` tarefas gerais

---

## 👥 Equipe

* Jadson Hipólito de Almeida
* Mariana Araújo de Medeiros

---

## 🌐 AcademicDevFlow

O projeto também está sendo gerenciado na plataforma AcademicDevFlow, onde foram cadastrados feedbacks e organização da equipe.

---

## ✅ Status do Projeto

🚧 Em desenvolvimento

---

## 📌 Considerações Finais

Este projeto foi desenvolvido como atividade da disciplina de Engenharia de Software II, com foco na aplicação de boas práticas de versionamento, organização e desenvolvimento colaborativo.
