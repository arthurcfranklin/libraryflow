# Levantamento de Requisitos - LibraryFlow

Este documento define os requisitos funcionais e não funcionais do LibraryFlow, servindo como referência para desenvolvimento, documentação, testes e evolução da plataforma.

---

# 1. Visão Geral e Objetivo

O LibraryFlow é uma aplicação web desenvolvida para centralizar o gerenciamento de bibliotecas em uma única plataforma.

O sistema permite o controle de acervo, usuários e empréstimos por meio de uma interface moderna, intuitiva e organizada, proporcionando maior eficiência operacional e rastreabilidade das informações.

---

# 2. Requisitos Funcionais (RF)

### 2.1 Módulo de Livros

- **RF001 (Cadastro de Livros):** O sistema deve permitir o cadastro de livros contendo: título, autor, categoria, ano de publicação da obra e quantidade de exemplares.

- **RF002 (Edição de Livros):** O sistema deve permitir a atualização das informações de livros previamente cadastrados.

- **RF003 (Exclusão de Livros):** O sistema deve permitir a remoção de livros do acervo.

- **RF004 (Consulta de Acervo):** O sistema deve permitir a visualização dos livros cadastrados.

- **RF005 (Controle de Disponibilidade):** O sistema deve exibir a disponibilidade dos livros para empréstimo.

---

### 2.2 Módulo de Usuários

- **RF006 (Cadastro de Usuários):** O sistema deve permitir o cadastro de usuários da biblioteca.

- **RF007 (Edição de Usuários):** O sistema deve permitir a atualização das informações dos usuários.

- **RF008 (Exclusão de Usuários):** O sistema deve permitir a remoção de usuários cadastrados.

- **RF009 (Consulta de Usuários):** O sistema deve permitir a visualização dos usuários cadastrados.

---

### 2.3 Módulo de Empréstimos

- **RF010 (Registro de Empréstimos):** O sistema deve permitir registrar empréstimos de livros.

- **RF001 (Registro de Devoluções):** O sistema deve permitir registrar devoluções de livros.

- **RF012 (Consulta de Empréstimos):** O sistema deve permitir visualizar empréstimos ativos e finalizados

- **RF013 (Atualização Automática de Disponibilidade):** O sistema deve atualizar automaticamente a disponibilidade dos livros após empréstimos e devoluções.

---

### 2.4 Dashboard

- **RF014 (Indicadores Operacionais):** O sistema deve apresentar indicadores operacionais da biblioteca.

-  **RF015 ():** O sistema deve apresentar movimentações recentes realizadas no sistema.

---

### 2.5 Autenticação

- **RF016 (Login):** O sistema deve permitir autenticação de usuários.

- **RF017 (Logout):** O sistema deve permitir o encerramento de sessão.


---

## 3. Requisitos Não Funcionais (RNF)

| ID     | Categoria      | Descrição                                                                   |
| ------ | -------------- | --------------------------------------------------------------------------- |
| **RNF001** | **Interface**      | O sistema deve possuir interface web responsiva.                            |
| **RNF002** | **Interface**      | O sistema deve oferecer suporte a tema claro e escuro.                      |
| **RNF003** | **Usabilidade**    | A interface deve manter consistência visual em todos os módulos.            |
| **RNF004** | **Arquitetura**    | O sistema deve utilizar arquitetura em camadas.                             |
| **RNF005** | **Arquitetura**    | O código deve seguir organização modular.                                   |
| **RNF006** | **Arquitetura**    | As regras de negócio devem permanecer desacopladas da interface.            |
| **RNF007** | **Banco de Dados** | O sistema deve utilizar persistência relacional.                            |
| **RNF008** | **Banco de Dados** | Os dados devem ser armazenados em SQLite durante a fase inicial do projeto. |
| **RNF009** | **Governança**     | O projeto deve utilizar Git para versionamento.                             |
| **RNF010** | **Governança**     | O código-fonte deve ser mantido em repositório GitHub.                      |
| **RNF011** | **Documentação**   | O projeto deve possuir documentação técnica.                                |
| **RNF012** | **Documentação**   | O projeto deve possuir documentação funcional.                              |
| **RNF013** | **Governança**   | O projeto deve manter histórico de releases e mudanças.                       |

---

## 4. Roadmap e Priorização

### **Must Have (MVP)**

Funcionalidades essenciais para operação básica do sistema.
- CRUD de Livros
- Persistência em SQLite
- Dashboard Administrativo
- Interface Web
- Tema Claro e Escuro

---

### **Should Have (v0.6)**
Funcionalidades planejadas para a próxima fase de evolução.
- CRUD de Usuários
- Estrutura de Empréstimos
- Home Administrativa
- Componentização da Interface

---

### **Could Have (v0.8)**
Funcionalidades desejáveis para aumento de maturidade da aplicação.
- Sistema de Autenticação Completo
- Controle de Permissões
- Histórico de Movimentações
- Dashboard Dinâmico

---

### **Future (v1.0)**

Funcionalidades previstas para a primeira versão estável.

* PostgreSQL
* API REST Documentada
* Dashboard Analítico
* Auditoria de Operações
* Testes Automatizados

---

## 5. Status dos Requisitos

| Requisito | Status       |
| --------- | ------------ |
| RF001     | **Implementado** |
| RF002     | **Implementado** |
| RF003     | **Implementado** |
| RF004     | **Implementado** |
| RF005     | **Implementado** |
| RF006     | **Planejado**    |
| RF007     | **Planejado**    |
| RF008     | **Planejado**    |
| RF009     | **Planejado**    |
| RF010     | **Planejado**    |
| RF011     | **Planejado**    |
| RF012     | **Planejado**    |
| RF013     | **Planejado**    |
| RF014     | **Parcial**      |
| RF015     | **Parcial**      |
| RF016     | **Planejado**    |
| RF017     | **Planejado**    |

---

## 6. Referências e Rastreabilidade

## Arquitetura

Consulte:

```text
docs/architecture.md
```

---

## Regras de Negócio

Consulte:

```text
docs/business-rules.md
```

---

## Casos de Uso

Consulte:

```text
docs/use-cases.md
```

---

## Banco de Dados

Consulte:

```text
docs/database.md
```

---

## API

Consulte:

```text
docs/api.md
```

---

**Última atualização:** Junho de 2026 | **Versão:** v0.5.0-beta
