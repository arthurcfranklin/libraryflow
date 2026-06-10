# 📚 LibraryFlow

Sistema web de gestão de bibliotecas desenvolvido para gerenciamento de usuários, acervo e circulação de livros.

O projeto tem como objetivo modernizar uma aplicação originalmente desenvolvida em terminal, evoluindo-a para uma solução web completa utilizando Python, FastAPI e SQLite. A plataforma permite autenticação de usuários, gerenciamento de livros, controle de empréstimos e devoluções, além de fornecer uma interface intuitiva para administração do acervo.

---

## 🚀 Funcionalidades

### 👤 Gestão de Usuários

* Cadastro de usuários
* Login seguro com autenticação
* Criptografia de senhas utilizando SHA-256
* Controle de acesso ao sistema

### 📚 Gestão de Acervo

* Cadastro de livros
* Edição de informações
* Exclusão de registros
* Controle de disponibilidade

### 🔄 Empréstimos

* Registro de empréstimos
* Associação entre usuários e livros
* Registro automático de data e horário
* Atualização automática do status dos exemplares

### ↩️ Devoluções

* Registro de devoluções
* Atualização automática da disponibilidade
* Histórico de movimentações

### 📊 Dashboard

* Total de livros cadastrados
* Livros disponíveis
* Livros emprestados
* Indicadores operacionais

---

## 🛠 Tecnologias Utilizadas

### Backend

* Python 3.12+
* FastAPI
* SQLite
* SQLAlchemy

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

```txt
libraryflow/
├── app/
│   ├── routes/
│   ├── models/
│   ├── services/
│   ├── database/
│   └── templates/
│
├── static/
│   ├── css/
│   ├── js/
│   └── images/
│
├── database/
│   └── libraryflow.db
│
├── main.py
├── requirements.txt
└── README.md
```

---

## 📌 Funcionalidades Planejadas

* Dashboard administrativo
* Pesquisa avançada de livros
* Histórico completo de empréstimos
* Controle de reservas
* Gestão de multas
* Controle de perfis de acesso
* API REST documentada com Swagger

---

## 🎯 Objetivos do Projeto

* Aplicar conceitos de desenvolvimento web com Python
* Implementar arquitetura em camadas
* Utilizar banco de dados relacional
* Desenvolver uma interface moderna e responsiva
* Demonstrar boas práticas de desenvolvimento de software

---

## 📈 Evolução do Projeto

### Versão 1.0

Aplicação CLI utilizando:

* Python
* Programação Orientada a Objetos
* Arquivos CSV

### Versão 2.0 (Atual)

Migração para arquitetura web utilizando:

* FastAPI
* SQLite
* HTML/CSS/JavaScript
* Dashboard administrativo

---

## 📌 Status

🚧 Em desenvolvimento

Atualmente em processo de migração da versão CLI para uma arquitetura web moderna.

---

## 👨‍💻 Autor

Arthur Almeida

Projeto desenvolvido para evolução prática em desenvolvimento de software, back-end Python e aplicações web.
