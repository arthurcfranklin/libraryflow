# Casos de Uso - LibraryFlow

Este documento centraliza os casos de uso do LibraryFlow e serve como índice de navegação para os fluxos funcionais documentados individualmente.

---

# Visão Geral

Os casos de uso descrevem as interações entre os atores do sistema e as funcionalidades disponibilizadas pelo LibraryFlow.

Cada caso de uso possui documentação própria contendo:

* Objetivo
* Metadados
* Fluxo Principal
* Fluxos Alternativos
* Critérios de Aceitação
* Regras de Negócio Relacionadas
* Requisitos Relacionados
* Módulos Relacionados

---

# Ator Principal

## Bibliotecário

Usuário responsável pela administração do sistema, incluindo:

* Gerenciamento de livros
* Gerenciamento de usuários
* Controle de empréstimos
* Controle de devoluções
* Consulta de indicadores operacionais

---

# Módulo de Livros

| ID     | Caso de Uso      | Status         |
| ------ | ---------------- | -------------- |
| **UC-L01** | Consultar Acervo | ✅ Implementado |
| **UC-L02** | Cadastrar Livro  | ✅ Implementado |
| **UC-L03** | Editar Livro     | ✅ Implementado |
| **UC-L04** | Excluir Livro    | ✅ Implementado |

### Arquivos

* `uc-l01-consultar-acervo.md`
* `uc-l02-cadastrar-livro.md`
* `uc-l03-editar-livro.md`
* `uc-l04-excluir-livro.md`

---

# Módulo Dashboard

| ID     | Caso de Uso         | Status                       |
| ------ | ------------------- | ---------------------------- |
| **UC-D01** | Consultar Dashboard | ⚠️ Parcialmente Implementado |

### Arquivos

* `uc-d01-consultar-dashboard.md`

---

# Módulo de Usuários

| ID     | Caso de Uso        | Status       |
| ------ | ------------------ | ------------ |
| **UC-U01** | Cadastrar Usuário  | 📝 Planejado |
| **UC-U02** | Consultar Usuários | 📝 Planejado |

### Arquivos

* `uc-u01-cadastrar-usuario.md`
* `uc-u02-consultar-usuarios.md`

---

# Módulo de Empréstimos

| ID     | Caso de Uso          | Status       |
| ------ | -------------------- | ------------ |
| **UC-E01** | Registrar Empréstimo | 📝 Planejado |
| **UC-E02** | Registrar Devolução  | 📝 Planejado |

### Arquivos

* `uc-e01-registrar-emprestimo.md`
* `uc-e02-registrar-devolucao.md`

---

# Estatísticas

| Categoria                  | Quantidade |
| -------------------------- | ---------- |
| Casos de Uso Totais        | 9          |
| Implementados              | 4          |
| Parcialmente Implementados | 1          |
| Planejados                 | 4          |

---

# Rastreabilidade

Os casos de uso possuem relação direta com:

* `requirements.md`
* `business-rules.md`
* `architecture.md`
* `roadmap.md`

---

**Última atualização:** Junho de 2026 | **Versão:** v0.5.0-beta