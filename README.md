# 📚 LibraryFlow

Sistema de gestão de bibliotecas desenvolvido em Python para gerenciamento de usuários, acervo e circulação de livros.

O projeto implementa autenticação de usuários, cadastro e controle de livros, empréstimos e devoluções, utilizando persistência de dados em arquivos CSV e princípios de Programação Orientada a Objetos (POO). Seu objetivo é demonstrar a aplicação prática de conceitos de desenvolvimento de software, manipulação de arquivos, segurança de dados e implementação de regras de negócio.

---

## 🚀 Funcionalidades

### 👤 Gestão de Usuários

* Cadastro de novos usuários
* Autenticação por e-mail e senha
* Validação de credenciais de acesso
* Armazenamento seguro de senhas utilizando SHA-256

### 📖 Gestão do Acervo

* Cadastro de livros
* Listagem completa dos exemplares cadastrados
* Controle de disponibilidade dos livros
* Identificação única para cada registro

### 🔄 Controle de Empréstimos

* Registro de empréstimos de livros
* Associação de livros aos usuários
* Registro automático de data e horário da operação
* Atualização de status do exemplar

### ↩️ Controle de Devoluções

* Registro de devolução de livros
* Atualização automática da disponibilidade
* Remoção do histórico ativo de empréstimo

---

## 🛠 Tecnologias Utilizadas

* Python 3
* Programação Orientada a Objetos (POO)
* CSV (Persistência de Dados)
* Hashlib (SHA-256)
* Datetime
* OS
* Time

---

## 📁 Estrutura do Projeto

```txt
library-management-system/
├── main.py
├── usuarios.csv
├── livros.csv
└── README.md
```

### Descrição dos Arquivos

| Arquivo      | Descrição                                                            |
| ------------ | -------------------------------------------------------------------- |
| main.py      | Aplicação principal contendo as regras de negócio e fluxo do sistema |
| usuarios.csv | Base de dados dos usuários cadastrados                               |
| livros.csv   | Base de dados do acervo e movimentações                              |
| README.md    | Documentação do projeto                                              |

---

## 📂 Estrutura dos Dados

### usuarios.csv

Armazena os dados dos usuários cadastrados:

* Nome
* E-mail
* Senha criptografada (SHA-256)

### livros.csv

Armazena os dados do acervo:

* ID do Livro
* Título
* Autor
* Ano de Publicação
* Status (Disponível ou Emprestado)
* Histórico de Empréstimos

---

## 🔒 Segurança

As senhas dos usuários não são armazenadas em texto puro.

O sistema utiliza o algoritmo SHA-256 para gerar hashes criptográficos antes da gravação dos dados, garantindo maior segurança no armazenamento das credenciais.

---

## 🎯 Objetivos do Projeto

* Aplicar conceitos de Programação Orientada a Objetos
* Implementar autenticação de usuários
* Desenvolver regras de negócio para gestão de bibliotecas
* Trabalhar com persistência de dados em arquivos CSV
* Consolidar conhecimentos em desenvolvimento Python

---

## 📈 Possíveis Evoluções

* Migração para banco de dados SQLite
* Desenvolvimento de interface web
* Dashboard administrativo
* Sistema de pesquisa avançada
* Relatórios de empréstimos e devoluções
* Controle de multas e reservas
* API REST para integração com outros sistemas

---

## 📌 Status do Projeto

**Versão Atual:** v1.0

✅ Funcionalidades principais implementadas

✅ Sistema operacional e funcional

🚧 Planejada evolução para versão web com banco de dados relacional

---

## 👨‍💻 Autor

Desenvolvido por Arthur Almeida como projeto de estudos e prática em desenvolvimento de software utilizando Python.
