# 📚 LibraryFlow

![Python](https://img.shields.io/badge/Python-3.12+-blue?logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-Web%20App-009688?logo=fastapi)
![SQLite](https://img.shields.io/badge/SQLite-Database-003B57?logo=sqlite)
![Status](https://img.shields.io/badge/Status-v2.1.0--beta-orange)

Sistema web de gestão de bibliotecas desenvolvido com Python, FastAPI e SQLite para gerenciamento de usuários, acervo, empréstimos e devoluções.

**Versão Atual:** v2.1.0-beta

O LibraryFlow surgiu a partir da modernização de uma aplicação acadêmica originalmente desenvolvida em terminal (CLI), sendo posteriormente reestruturado para uma arquitetura web completa utilizando FastAPI, SQLite e uma interface administrativa moderna.

O projeto tem como objetivo consolidar conhecimentos em desenvolvimento web, arquitetura de software, banco de dados relacionais e construção de interfaces responsivas.

---

# 📖 Visão Geral

O LibraryFlow centraliza o gerenciamento de bibliotecas em uma única plataforma, permitindo controlar usuários, acervo e movimentações de forma simples e organizada.

Entre os principais recursos estão:

* Gestão de usuários
* Controle de acervo
* Registro de empréstimos
* Controle de devoluções
* Dashboard administrativo
* Temas claro e escuro
* Interface responsiva

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

## 👤 Gestão de Usuários

* Cadastro de usuários
* Autenticação de acesso
* Validação de credenciais
* Controle de permissões

## 📚 Gestão de Acervo

* Cadastro de livros
* Atualização de registros
* Controle de disponibilidade
* Organização do catálogo

## 🔄 Empréstimos e Devoluções

* Registro de empréstimos
* Associação entre usuários e livros
* Controle de devoluções
* Atualização automática de disponibilidade

## 📊 Dashboard Administrativo

* Total de livros cadastrados
* Livros disponíveis
* Livros emprestados
* Usuários registrados
* Resumo operacional da biblioteca

## 🎨 Interface Moderna

* Layout responsivo
* Tema claro
* Tema escuro
* Alternância dinâmica de tema

---

# 🛠 Tecnologias Utilizadas

## Backend

* Python 3.12+
* FastAPI
* SQLAlchemy
* SQLite

## Frontend

* HTML5
* CSS3
* JavaScript

## Controle de Versão

* Git
* GitHub

---

# 📁 Estrutura do Projeto

```text
libraryflow/
│
├── app/
│   ├── models/
│   ├── routes/
│   ├── services/
│   └── database/
│
├── static/
│   ├── css/
│   ├── js/
│   └── images/
│
├── templates/
│
├── database/
│   └── libraryflow.db
│
├── main.py
├── requirements.txt
└── README.md
```

---

# 🎯 Objetivos do Projeto

* Aplicar conceitos modernos de desenvolvimento web
* Desenvolver APIs utilizando FastAPI
* Utilizar banco de dados relacional
* Criar interfaces modernas e responsivas
* Consolidar conhecimentos em backend e frontend
* Demonstrar boas práticas de desenvolvimento de software

---

# 🗺 Roadmap

## ✅ Concluído

* Estruturação da arquitetura web
* Interface de login
* Dashboard administrativo
* Sistema de temas claro e escuro
* Organização modular do projeto
* Documentação técnica inicial

## 🚧 Em Desenvolvimento

* Cadastro de usuários
* Cadastro de livros
* Controle de empréstimos
* Persistência completa em SQLite
* Integração das regras de negócio

## 🔮 Futuro

* Histórico completo de movimentações
* Controle de multas
* Controle de perfis de acesso
* Pesquisa avançada de livros
* API REST documentada com Swagger
* Relatórios administrativos

---

# 📊 Status

🟡 Em desenvolvimento ativo

Atualmente o projeto encontra-se em evolução contínua, com foco na implementação dos módulos de negócio e integração completa com banco de dados.

---

# 👨‍💻 Autor

**Arthur Almeida**

Projeto desenvolvido para evolução prática em desenvolvimento de software, banco de dados e aplicações web modernas.
