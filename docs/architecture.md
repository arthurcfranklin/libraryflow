# Arquitetura Técnica - LibraryFlow

## Visão Geral

O LibraryFlow é uma aplicação web para gerenciamento de bibliotecas desenvolvida com Python e FastAPI.

O sistema foi projetado utilizando uma arquitetura em camadas, separando responsabilidades entre interface, processamento de requisições, regras de negócio e persistência de dados. Essa abordagem facilita manutenção, escalabilidade e futuras evoluções do projeto.

---

## Arquitetura da Aplicação

```text
Usuário
   │
   ▼
Templates (Jinja2)
   │
   ▼
FastAPI Routes
   │
   ▼
Services Layer
   │
   ▼
SQLAlchemy ORM
   │
   ▼
SQLite Database
```

---

## Fluxo de Processamento

1. O usuário interage com a interface web.
2. Os templates Jinja2 renderizam as páginas dinâmicas.
3. As rotas FastAPI recebem e processam as requisições HTTP.
4. A camada de serviços executa as regras de negócio.
5. O SQLAlchemy realiza operações de persistência.
6. O SQLite armazena os dados da aplicação.

---

## Estrutura do Projeto

```text
libraryflow/
│
├── app/
│   ├── database/
│   ├── models/
│   ├── routes/
│   └── services/
│
├── database/
│   └── libraryflow.db
│
├── docs/
│
├── static/
│   ├── css/
│   ├── js/
│   └── images/
│
├── templates/
│   ├── partials/
│   ├── home.html
│   ├── dashboard.html
│   ├── books.html
│   ├── users.html
│   ├── loans.html
│   └── login.html
│
├── main.py
├── requirements.txt
└── README.md
```

---

## Camadas da Aplicação

### **Templates (Jinja2)**

Responsáveis pela renderização da interface do usuário.

Responsabilidades:

* Exibição de dados
* Renderização de páginas HTML
* Componentização visual
* Integração com CSS e JavaScript

---

### **FastAPI Routes**

Responsáveis pelo gerenciamento das requisições HTTP.

Responsabilidades:

* Receber requisições do cliente
* Encaminhar operações para a camada de serviços
* Retornar respostas para a interface

---

### **Services Layer**

Responsável pela implementação das regras de negócio.

Responsabilidades:

* Cadastro de registros
* Atualização de informações
* Exclusão de registros
* Validações operacionais
* Regras funcionais da aplicação

---

### **SQLAlchemy ORM**

Responsável pelo mapeamento objeto-relacional.

Responsabilidades:

* Manipulação de entidades
* Consultas ao banco de dados
* Persistência de informações
* Abstração de comandos SQL

---

### **SQLite Database**

Banco de dados utilizado atualmente pelo projeto.

Características:

* Banco relacional local
* Baixa complexidade operacional
* Facilidade de implantação
* Adequado para o estágio atual do projeto

---

## **Tecnologias Utilizadas**

### **Backend**

* Python 3.13
* FastAPI
* SQLAlchemy
* SQLite

### **Frontend**

* HTML5
* CSS3
* JavaScript
* Jinja2

### **Controle de Versão**

* Git
* GitHub

---

## Decisões Arquiteturais

### **Arquitetura em Camadas**

Adotada para reduzir acoplamento entre componentes e facilitar manutenção futura.

### **SQLAlchemy ORM**

Utilizado para abstrair consultas SQL e simplificar operações de persistência.

### **SQLite**

Escolhido por sua simplicidade e facilidade de configuração durante o desenvolvimento.

### **Jinja2**

Permite renderização dinâmica de conteúdo sem necessidade de frameworks frontend adicionais.

---

## Evoluções Futuras

Evoluções arquiteturais planejadas:

* Sistema de autenticação
* Controle de permissões por perfil
* API REST documentada
* Migração opcional para PostgreSQL
* Dashboard com métricas dinâmicas
* Histórico de movimentações
* Testes automatizados

---

## Status Atual

**Última atualização:** Junho de 2026 | **Versão:** v0.5.0-beta