# Contributing - LibraryFlow

Este documento define as diretrizes para contribuição no LibraryFlow. O objetivo é garantir consistência no desenvolvimento, organização das entregas e qualidade do código ao longo da evolução do projeto.

---

## 1. Metadados

| Campo                   | Descrição    |
| ----------------------- | ------------ |
| Documento               | Contributing |
| Projeto                 | LibraryFlow  |
| Categoria               | Governança   |
| Status                  | Ativo        |
| Versão Atual do Sistema | v0.5.0-beta  |
| Versão do Documento     | v1.0         |

---

## 2. Objetivo

Estabelecer padrões para desenvolvimento, documentação, versionamento e colaboração dentro do projeto.

---

## 3. Fluxo de Desenvolvimento

O desenvolvimento do LibraryFlow segue o fluxo:

```text
Roadmap
    ↓
Milestone
    ↓
Issue
    ↓
Implementação
    ↓
Documentação
    ↓
Commit
    ↓
Release
```

---

## 4. Estrutura de Branches

Atualmente o projeto utiliza a branch principal:

```text
main
```

---

## Evolução Futura

Conforme o crescimento do projeto, poderá ser adotado:

```text
main
├── develop
├── feature/*
├── fix/*
└── docs/*
```

---

## 5. Padrão de Commits

Os commits devem seguir uma convenção simples e padronizada.

---

### **feat**

Nova funcionalidade.

Exemplo:

```text
feat: implement users module
```

---

### **fix**

Correção de problemas.

Exemplo:

```text
fix: resolve sidebar rendering issue
```

---

### **docs**

Alterações de documentação.

Exemplo:

```text
docs: add database documentation
```

---

### **refactor**

Refatoração sem alteração funcional.

Exemplo:

```text
refactor: reorganize services layer
```

---

### **style**

Alterações visuais.

Exemplo:

```text
style: improve dashboard layout
```

---

### chore**

Tarefas administrativas.

Exemplo:

```text
chore: update dependencies
```

---

## 6. Boas Práticas de Desenvolvimento

Antes de realizar um commit:

* Validar funcionamento da aplicação.
* Revisar alterações realizadas.
* Atualizar documentação quando necessário.
* Evitar código não utilizado.
* Manter consistência com a arquitetura definida.

---

## 7. Boas Práticas de Documentação

Sempre que uma funcionalidade relevante for criada:

* Atualizar roadmap.md quando necessário.
* Atualizar changelog.md.
* Atualizar documentação técnica relacionada.
* Atualizar casos de uso impactados.

---

### Documentos Relacionados

Possíveis atualizações:

```text
requirements.md
business-rules.md
use-cases.md
database.md
api.md
roadmap.md
changelog.md
```

---

## 8. Issues

As funcionalidades devem ser registradas através de Issues sempre que possível.

---

### Exemplo

```text
Título:
Implement Users Management Module

Descrição:
Implementar CRUD completo de usuários conforme requisitos RF006 a RF009.
```

---

## 9. Pull Requests

Antes de aprovar um Pull Request deve-se verificar:

* Funcionamento da funcionalidade.
* Qualidade do código.
* Consistência visual.
* Atualização da documentação.
* Compatibilidade com a arquitetura do projeto.

---

## 10. Releases

As releases devem representar marcos relevantes do projeto.

---

### Estrutura

```text
vMAJOR.MINOR.PATCH
```

Exemplo:

```text
v0.5.0-beta
```

---

### Requisitos para Release

* Funcionalidade concluída.
* Código validado.
* Documentação atualizada.
* Changelog atualizado.

---

## 11. Milestones

As milestones representam objetivos maiores do produto.

---

### Milestones Atuais

| Milestone               | Status    |
| ----------------------- | --------- |
| Users Management Module | **Planejado** |
| Loans Management Module | **Planejado** |
| Authentication Module   | **Planejado** |
| Stable Release v1.0.0   | **Futuro**    |

---

## 12. Qualidade do Projeto

O projeto busca manter:

* Código limpo
* Documentação atualizada
* Arquitetura consistente
* Evolução incremental
* Versionamento organizado

---

## 13. Filosofia do Projeto

O LibraryFlow é desenvolvido com foco em:

* Simplicidade
* Organização
* Escalabilidade
* Manutenibilidade
* Boas práticas de engenharia de software

---

## 14. Documentos Relacionados

* roadmap.md
* architecture.md
* requirements.md
* use-cases.md
* changelog.md

---

## 15. Status do Documento

Em manutenção contínua conforme evolução do projeto.

---

**Última atualização:** Junho de 2026 | **Versão:** v1.0