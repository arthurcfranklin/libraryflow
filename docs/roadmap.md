# 🗺️ Roadmap - LibraryFlow

## 1. Visão Geral

Este documento descreve a evolução planejada do LibraryFlow, registrando o histórico de versões já entregues e o planejamento das futuras versões do sistema.

O roadmap serve como referência para desenvolvimento, gestão de produto, releases e milestones do projeto.

---

## 2. Metadados

| Campo                   | Descrição       |
| ----------------------- | --------------- |
| Documento               | **Roadmap**         |
| Projeto                 | **LibraryFlow**     |
| Responsável             | **Arthur Franklin** |
| Status                  | **Em Evolução**     |
| Versão Atual do Sistema | **v0.5.0-beta**     |
| Versão do Documento     | **v1.0**            |

---

## 3. Objetivo

Definir a evolução funcional e técnica do LibraryFlow, proporcionando rastreabilidade entre requisitos, casos de uso, releases e milestones.

---

# 4. Histórico de Evolução

## v0.1.0-alpha

### Objetivo

Estabelecer a base inicial da aplicação web.

### Entregas

* Estrutura inicial do projeto
* Configuração do FastAPI
* Estrutura de templates
* Organização inicial da arquitetura

### Status

✅ Concluído

---

## **v0.2.0-alpha**

### Objetivo

Implementar as primeiras funcionalidades do módulo de livros.

### Entregas

* Cadastro de livros
* Persistência em SQLite
* Integração com SQLAlchemy

### Status

✅ Concluído

---

## **v0.3.0-alpha**

### Objetivo

Expandir o gerenciamento do acervo.

### Entregas

* Consulta de livros
* Edição de livros
* Exclusão de livros
* Evolução do CRUD de livros

### Status

✅ Concluído

---

## **v0.4.0-beta**

### Objetivo

Melhorar a experiência de uso da aplicação.

### Entregas

* Dashboard inicial
* Melhorias visuais
* Estruturação da navegação
* Tema claro e escuro

### Status

✅ Concluído

---

## **v0.5.0-beta**

### Objetivo

Consolidar a estrutura visual e documental do projeto.

### Entregas

* Home administrativa
* Sidebar recolhível
* Componentização de templates
* Estrutura documental
* Requisitos
* Regras de negócio
* Casos de uso
* Arquitetura

### Status

✅ Concluído

---

# 5. Status Atual

## Versão Atual

```text
v0.5.0-beta
```

## Funcionalidades Disponíveis

### Livros

* Cadastro de livros
* Consulta de acervo
* Edição de livros
* Exclusão de livros

### Dashboard

* Home administrativa
* Dashboard inicial
* Navegação entre módulos

### Interface

* Tema claro e escuro
* Sidebar recolhível
* Componentização de layouts

### Arquitetura

* FastAPI
* SQLAlchemy
* SQLite
* Jinja2

---

# 6. Roadmap de Evolução

## **v0.6.0-beta**

### Objetivo

Implementar o módulo de usuários.

### Funcionalidades Planejadas

* Cadastro de usuários
* Consulta de usuários
* Edição de usuários
* Exclusão de usuários

### Casos de Uso Relacionados

* UC-U01
* UC-U02

### Status

🟡 Planejado

---

## **v0.7.0-beta**

### Objetivo

Implementar o módulo de empréstimos.

### Funcionalidades Planejadas

* Registro de empréstimos
* Registro de devoluções
* Atualização automática de disponibilidade

### Casos de Uso Relacionados

* UC-E01
* UC-E02

### Status

🟡 Planejado

---

## **v0.8.0-beta**

### Objetivo

Implementar autenticação e controle de acesso.

### Funcionalidades Planejadas

* Login
* Logout
* Proteção de rotas
* Controle de sessão

### Requisitos Relacionados

* RF016
* RF017

### Status

🟡 Planejado

---

## **v0.9.0-beta**

### Objetivo

Expandir funcionalidades administrativas.

### Funcionalidades Planejadas

* Histórico de movimentações
* Dashboard dinâmico
* Pesquisa avançada
* Filtros de consulta

### Status

🟡 Planejado

---

## **v1.0.0**

### Objetivo

Primeira versão estável do LibraryFlow.

### Funcionalidades Planejadas

* Sistema completo de biblioteca
* Correções de bugs
* Estabilidade operacional
* Melhorias de usabilidade
* Documentação consolidada

### Status

⚪ Futuro

---

# 7. Melhorias Futuras

## Banco de Dados

* PostgreSQL
* Migrações automatizadas

---

## API

* API REST documentada
* OpenAPI expandido

---

## Segurança

* Controle de permissões
* Perfis de acesso
* Auditoria de operações

---

## Qualidade

* Testes automatizados
* Pipeline CI/CD
* Cobertura de testes

---

# 8. Milestones Planejadas

| Milestone               | Versão      |
| ----------------------- | ----------- |
| Users Management Module | **v0.6.0-beta** |
| Loans Management Module | **v0.7.0-beta** |
| Authentication Module   | **v0.8.0-beta** |
| Administrative Features | **v0.9.0-beta** |
| Stable Release          | **v1.0.0**      |

---

# 9. Critérios para **v1.0.0**

Para atingir a primeira versão estável, o projeto deverá possuir:

* CRUD completo de Livros
* CRUD completo de Usuários
* Controle de Empréstimos
* Controle de Devoluções
* Sistema de Autenticação
* Dashboard funcional
* Documentação atualizada
* Releases documentadas
* Milestones concluídas

---

# 10. Documentos Relacionados

* architecture.md
* requirements.md
* business-rules.md
* use-cases.md
* changelog.md

---

## 11. Status do Documento

Em manutenção contínua conforme evolução do produto.

---

**Última atualização:** Junho de 2026 | **Versão:** v1.0