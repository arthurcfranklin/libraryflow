# 📚 LibraryFlow

![Python](https://img.shields.io/badge/Python-3.13+-blue?logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-Web%20App-009688?logo=fastapi)
![SQLite](https://img.shields.io/badge/SQLite-Database-003B57?logo=sqlite)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-ORM-red)
![HTML5](https://img.shields.io/badge/HTML5-Frontend-E34F26?logo=html5\&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-Styling-1572B6?logo=css3\&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-Frontend-F7DF1E?logo=javascript\&logoColor=black)

Sistema web de gestão de bibliotecas desenvolvido com Python, FastAPI, SQLAlchemy e SQLite.

---

# 📊 Status

🟢 Em desenvolvimento ativo

**Versão Atual:** v0.5.0-beta

O projeto encontra-se em fase beta, com arquitetura consolidada, CRUD completo de livros, documentação técnica formalizada e roadmap definido para os próximos módulos.

---

# 📖 Sobre o Projeto

O LibraryFlow é uma aplicação web para gerenciamento de bibliotecas, desenvolvida com foco em arquitetura de software, persistência de dados, modelagem de sistemas e boas práticas de engenharia de software.

O projeto surgiu a partir da evolução de uma aplicação acadêmica originalmente desenvolvida em terminal (CLI), sendo posteriormente reestruturado para uma arquitetura web moderna baseada em FastAPI.

Além do desenvolvimento da aplicação, o projeto possui documentação técnica, governança de desenvolvimento, roadmap evolutivo e histórico formal de releases.

---

# 🎯 Objetivos

* Gerenciar acervos bibliográficos
* Controlar empréstimos e devoluções
* Gerenciar usuários da biblioteca
* Consolidar conhecimentos em desenvolvimento web
* Aplicar conceitos de arquitetura de software
* Praticar modelagem e documentação de sistemas

---

# 📸 Screenshots

## 🔐 Tela de Login

![Login](static/images/login.png)

## ☀️ Dashboard — Tema Claro

![Dashboard Light](static/images/dashboard-light.png)

## 🌙 Dashboard — Tema Escuro

![Dashboard Dark](static/images/dashboard-dark.png)

---

# ✨ Funcionalidades

## 📚 Gestão de Livros

* Cadastro de livros
* Consulta de livros
* Edição de livros
* Exclusão de livros
* Persistência em SQLite
* Integração com SQLAlchemy ORM

## 🎨 Interface

* Tema claro
* Tema escuro
* Dashboard administrativo
* Interface responsiva
* Modais interativos
* Sistema de notificações

## ⚙️ Arquitetura

* FastAPI
* SQLAlchemy ORM
* SQLite
* Jinja2 Templates
* Organização modular
* Camadas de aplicação definidas

---

# 🏗️ Arquitetura

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

# 🛠️ Tecnologias Utilizadas

## Backend

* Python 3.13+
* FastAPI
* SQLAlchemy
* SQLite

## Frontend

* HTML5
* CSS3
* JavaScript
* Jinja2

## Versionamento

* Git
* GitHub

---

# 📚 Documentação

Toda a documentação técnica do projeto encontra-se disponível em:

```text
docs/
```

## Documentos Disponíveis

* Architecture Documentation
* Requirements Documentation
* Business Rules Documentation
* Use Cases Documentation
* Database Documentation
* API Documentation
* Design Documentation
* Setup Guide
* Troubleshooting Guide
* Changelog
* Contribution Guidelines
* Product Roadmap

---

# 🚀 Releases

| Versão       | Descrição                              |
| ------------ | -------------------------------------- |
| v0.1.0-alpha | Initial Web Architecture               |
| v0.2.0-alpha | Dashboard and Theme System             |
| v0.3.0-alpha | Books Management Foundation            |
| v0.4.0-beta  | Complete Books CRUD                    |
| v0.5.0-beta  | Documentation and Governance Framework |

---

# 🗺️ Roadmap

## ✅ Concluído

* Arquitetura Web
* Dashboard Administrativo
* Sistema de Temas
* CRUD Completo de Livros
* Persistência SQLite
* Integração SQLAlchemy
* Estrutura Modular
* Documentação Técnica Completa
* Sistema de Releases
* Governança do Projeto

## 🚧 Próxima Versão — v0.6.0-beta

### Users Management Module

* Cadastro de usuários
* Consulta de usuários
* Edição de usuários
* Exclusão de usuários

## 🔮 Futuras Versões

### v0.7.0-beta

* Empréstimos
* Devoluções
* Controle de disponibilidade

### v0.8.0-beta

* Autenticação
* Controle de sessão
* Proteção de rotas

### v0.9.0-beta

* Relatórios administrativos
* Funcionalidades de auditoria
* Recursos de gestão

### v1.0.0

* Stable Release

---
