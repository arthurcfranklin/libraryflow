# 📚 LibraryFlow

Sistema web de gestão de bibliotecas desenvolvido com Python, FastAPI e SQLite para gerenciamento de usuários, acervo, empréstimos e devoluções.

O projeto foi originalmente desenvolvido como uma aplicação de terminal (CLI) durante o curso de Desenvolvimento de Sistemas no SENAI e atualmente está sendo modernizado para uma arquitetura web completa, com dashboard administrativo, interface responsiva, sistema de temas e banco de dados relacional.

---

## 🚀 Visão Geral

O LibraryFlow tem como objetivo centralizar o gerenciamento de bibliotecas por meio de uma plataforma intuitiva e moderna, permitindo o controle de usuários, livros, empréstimos e devoluções em um único ambiente.

Além de servir como sistema de gestão, o projeto também representa a evolução prática de conhecimentos em desenvolvimento web, arquitetura de software, banco de dados e experiência do usuário.

---

## 📸 Screenshots

### 🔐 Tela de Login

![Login](static/images/login.png)

### ☀️ Dashboard — Tema Claro

![Dashboard Light](static/images/dashboard-light.png)

### 🌙 Dashboard — Tema Escuro

![Dashboard Dark](static/images/dashboard-dark.png)

---

## ✨ Funcionalidades

### 👤 Gestão de Usuários

* Cadastro de usuários
* Autenticação de acesso
* Validação de credenciais
* Controle de permissões (planejado)

### 📚 Gestão de Acervo

* Cadastro de livros
* Atualização de registros
* Controle de disponibilidade
* Organização do catálogo

### 🔄 Empréstimos e Devoluções

* Registro de empréstimos
* Associação entre usuários e livros
* Controle de devoluções
* Atualização automática de status

### 📊 Dashboard Administrativo

* Total de livros cadastrados
* Livros disponíveis
* Livros emprestados
* Quantidade de usuários
* Visualização centralizada de movimentações

### 🎨 Interface Moderna

* Layout responsivo
* Tema claro
* Tema escuro
* Experiência focada em usabilidade

---

## 🛠 Tecnologias Utilizadas

### Backend

* Python 3.12+
* FastAPI
* SQLAlchemy
* SQLite

### Frontend

* HTML5
* CSS3
* JavaScript

### Segurança

* SHA-256
* Validação de dados
* Controle de autenticação

---

## 📁 Estrutura do Projeto

```text
libraryflow/
│
├── app/
│   ├── database/
│   ├── models/
│   ├── routes/
│   └── services/
│
├── static/
│   ├── css/
│   ├── js/
│   └── images/
│
├── templates/
│   ├── login.html
│   └── dashboard.html
│
├── database/
│
├── legacy_v1.py
├── main.py
├── requirements.txt
└── README.md
```

---

## 🎯 Objetivos do Projeto

* Evoluir uma aplicação CLI para uma arquitetura web moderna
* Aplicar conceitos de desenvolvimento web com Python
* Implementar banco de dados relacional
* Desenvolver interface administrativa responsiva
* Consolidar boas práticas de desenvolvimento de software

---

## 🗺 Roadmap

### ✅ Concluído

* Estrutura inicial do projeto
* Migração da arquitetura CLI
* Implementação do FastAPI
* Dashboard administrativo
* Sistema de temas (claro e escuro)
* Organização modular do projeto

### 🚧 Em Desenvolvimento

* Cadastro de livros
* Gestão de usuários
* Controle de empréstimos
* Integração completa com SQLite
* Persistência de dados

### 🔮 Futuro

* Pesquisa avançada de livros
* Histórico completo de movimentações
* Controle de multas
* Perfis de acesso
* API REST documentada com Swagger
* Relatórios administrativos

---

## 📈 Evolução do Projeto

### Versão 1.0

Aplicação CLI desenvolvida utilizando:

* Python
* Programação Orientada a Objetos
* Manipulação de arquivos CSV

### Versão 2.0 (Atual)

Migração para aplicação web utilizando:

* FastAPI
* SQLite
* HTML, CSS e JavaScript
* Dashboard administrativo
* Sistema de temas
* Estrutura modular

---

## 📌 Status

🚧 Em desenvolvimento ativo

O projeto encontra-se em processo de evolução da versão CLI para uma aplicação web completa, com foco em arquitetura moderna, experiência do usuário e gerenciamento eficiente de bibliotecas.

---

## 👨‍💻 Autor

**Arthur Almeida**

Projeto desenvolvido para evolução prática em desenvolvimento de software, Python, banco de dados e aplicações web modernas.
