# Database - LibraryFlow

## 1. Visão Geral

Este documento descreve a estrutura de banco de dados do LibraryFlow, incluindo entidades implementadas, entidades planejadas e relacionamentos previstos para evolução do sistema.

O banco de dados atual utiliza SQLite, integrado à aplicação por meio do SQLAlchemy ORM.

---

## 2. Metadados

| Campo                   | Descrição   |
| ----------------------- | ----------- |
| Documento               | **Database**    |
| Projeto                 | **LibraryFlow** |
| Banco Atual             | **SQLite**      |
| ORM                     | **SQLAlchemy**  |
| Status                  | **Em Evolução** |
| Versão Atual do Sistema | **v0.6.0-beta** |
| Versão do Documento     | **v1.2**        |

---

## 3. Objetivo

Documentar a estrutura de dados do LibraryFlow, servindo como referência para desenvolvimento, manutenção, evolução do banco e implementação de novos módulos.

---

# 4. Banco Atual

## SQLite

O SQLite é utilizado na fase inicial do projeto por sua simplicidade, facilidade de configuração e compatibilidade com o estágio atual da aplicação.

Arquivo atual do banco:

```text
database/libraryflow.db
```

---

# 5. Entidades Implementadas

## 5.1 books

A entidade `books` representa os livros cadastrados no acervo.

### Campos

| Campo    | Tipo    | Obrigatório | Descrição                    |
| -------- | ------- | ----------- | ---------------------------- |
| id       | Integer | Sim         | Identificador único do livro |
| title    | String  | Sim         | Título do livro              |
| author   | String  | Sim         | Autor do livro               |
| year     | Integer | Sim         | Ano de publicação            |
| category | String  | Sim         | Categoria do livro           |
| copies   | Integer | Sim         | Quantidade de exemplares     |
| status   | String  | Sim         | Status de disponibilidade    |

### Regras Relacionadas

| Código | Regra                                    |
| ------ | ---------------------------------------- |
| BR-L01 | Livro deve possuir título                |
| BR-L02 | Livro deve possuir autor                 |
| BR-L03 | Quantidade de exemplares deve ser válida |
| BR-L04 | Livro deve possuir categoria             |
| BR-L05 | Ano de publicação deve ser válido        |

### Requisitos Relacionados

| Código | Requisito                   |
| ------ | --------------------------- |
| RF001  | Cadastro de Livros          |
| RF002  | Edição de Livros            |
| RF003  | Exclusão de Livros          |
| RF004  | Consulta de Acervo          |
| RF005  | Controle de Disponibilidade |

---

## 5.2 users

A entidade `users` representa os usuários cadastrados no sistema.

### Campos

| Campo        | Tipo    | Obrigatório | Descrição                      |
| ------------ | ------- | ----------- | ------------------------------ |
| id           | Integer | Sim         | Identificador único do usuário |
| name         | String  | Sim         | Nome completo                  |
| email        | String  | Sim         | E-mail do usuário              |
| registration | String  | Sim         | Matrícula ou identificação     |
| status       | String  | Sim         | Status do cadastro             |

### Regras Relacionadas

| Código | Regra                               |
| ------ | ----------------------------------- |
| BR-U01 | Usuário deve possuir identificação  |
| BR-U02 | Usuário deve possuir cadastro ativo |

### Requisitos Relacionados

| Código | Requisito            |
| ------ | -------------------- |
| RF006  | Cadastro de Usuários |
| RF007  | Edição de Usuários   |
| RF008  | Exclusão de Usuários |
| RF009  | Consulta de Usuários |

---

# 6. Entidades Planejadas

## 6.1 loans

A entidade `loans` representará os empréstimos realizados no sistema.

### Campos Planejados

| Campo       | Tipo     | Obrigatório | Descrição                         |
| ----------- | -------- | ----------- | --------------------------------- |
| id          | Integer  | Sim         | Identificador único do empréstimo |
| user_id     | Integer  | Sim         | Referência ao usuário             |
| book_id     | Integer  | Sim         | Referência ao livro               |
| loan_date   | DateTime | Sim         | Data do empréstimo                |
| due_date    | DateTime | Sim         | Data prevista de devolução        |
| return_date | DateTime | Não         | Data real da devolução            |
| status      | String   | Sim         | Status do empréstimo              |
| created_at  | DateTime | Sim         | Data de criação do registro       |

### Regras Relacionadas

| Código | Regra                                     |
| ------ | ----------------------------------------- |
| **BR-E01** | Empréstimo vinculado a usuário            |
| **BR-E02** | Empréstimo vinculado a livro              |
| **BR-E03** | Não emprestar livro indisponível          |
| **BR-E04** | Atualização automática de disponibilidade |
| **BR-E05** | Devolução de empréstimo ativo             |

### Requisitos Relacionados

| Código | Requisito                                 |
| ------ | ----------------------------------------- |
| **RF010**  | Registro de Empréstimos                   |
| **RF011**  | Registro de Devoluções                    |
| **RF012**  | Consulta de Empréstimos                   |
| **RF013**  | Atualização Automática de Disponibilidade |

---

# 7. Relacionamentos Planejados

```text
users
  │
  └──< loans >──
              │
              books
```

## Descrição

* Um usuário poderá possuir vários empréstimos.
* Um livro poderá estar associado a vários registros de empréstimo ao longo do tempo.
* Cada empréstimo deverá estar vinculado a um único usuário e a um único livro.

---

# 8. Modelo Relacional

```text
books
├── id
├── title
├── author
├── year
├── category
├── copies
└── status

users
├── id
├── name
├── email
├── status

loans
├── id
├── user_id
├── book_id
├── loan_date
├── due_date
├── return_date
├── status
└── created_at
```

---

# 9. Decisões de Modelagem

## SQLite na fase inicial

O SQLite foi adotado pela facilidade de uso e por atender ao estágio atual do projeto.

## SQLAlchemy ORM

O SQLAlchemy foi utilizado para mapear entidades Python para tabelas relacionais, reduzindo acoplamento direto com SQL.

## Separação por entidades

As entidades foram planejadas para representar os principais domínios do sistema:

* Livros
* Usuários
* Empréstimos

---

# 10. Evoluções Futuras

Possíveis evoluções para o banco de dados:

* Migração para PostgreSQL
* Implementação de migrations com Alembic
* Criação de índices
* Controle de auditoria
* Histórico de movimentações
* Registro de timestamps em todas as entidades
* Normalização de status em tabelas auxiliares

---

# 11. Documentos Relacionados

* architecture.md
* requirements.md
* business-rules.md
* use-cases.md
* roadmap.md

---

## 12. Status do Documento

Em manutenção contínua conforme evolução do modelo de dados.

---

**Última atualização:** Junho de 2026 | **Versão:** v1.2
