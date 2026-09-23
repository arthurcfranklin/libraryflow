# LibraryFlow

Sistema web de gestão de bibliotecas desenvolvido com FastAPI, SQLAlchemy e SQLite.

![Python](https://img.shields.io/badge/Python-3.13+-3776AB?style=flat&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-Aplica%C3%A7%C3%A3o%20Web-009688?style=flat&logo=fastapi&logoColor=white)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-ORM-D71F00?style=flat)
![SQLite](https://img.shields.io/badge/SQLite-Banco%20de%20Dados-003B57?style=flat&logo=sqlite&logoColor=white)
![Status](https://img.shields.io/badge/Status-Beta-1F6FEB?style=flat)
![Licença](https://img.shields.io/badge/Licen%C3%A7a-MIT-2EA44F?style=flat)

## Visão Geral

O LibraryFlow é uma aplicação web para gestão de bibliotecas, desenvolvida para gerenciar acervos bibliográficos e fornecer uma base para fluxos de usuários, empréstimos e circulação.

O projeto surgiu a partir de uma aplicação acadêmica originalmente desenvolvida em linha de comando e posteriormente foi reestruturado como uma aplicação web utilizando FastAPI. Seu desenvolvimento é orientado por arquitetura de software, persistência de dados, modelagem de sistemas, documentação técnica e evolução incremental.

O LibraryFlow encontra-se atualmente em fase beta. A aplicação possui arquitetura web modular, gestão completa de livros, recursos de busca, persistência com SQLite, integração com SQLAlchemy, dashboard administrativo e temas claro e escuro.

**Versão atual:** `v0.5.0-beta`

## Capturas de Tela

### Login

![Interface de login do LibraryFlow](static/images/login.png)

### Dashboard — Tema Claro

![Dashboard do LibraryFlow utilizando o tema claro](static/images/dashboard-light.png)

### Dashboard — Tema Escuro

![Dashboard do LibraryFlow utilizando o tema escuro](static/images/dashboard-dark.png)

## Funcionalidades

### Gestão de Livros

- Cadastrar livros
- Consultar o acervo
- Pesquisar no acervo
- Editar informações dos livros
- Excluir livros
- Persistir dados com SQLite
- Gerenciar operações de banco de dados por meio do SQLAlchemy ORM

### Interface

- Dashboard administrativo
- Temas claro e escuro
- Interface responsiva
- Modais interativos
- Sistema de notificações

### Estrutura da Aplicação

- Aplicação web baseada em FastAPI
- SQLAlchemy ORM
- Banco de dados SQLite
- Templates Jinja2
- Organização modular
- Camadas de aplicação definidas

## Tecnologias

| Área | Tecnologias |
| --- | --- |
| Backend | Python 3.13+, FastAPI |
| Persistência | SQLAlchemy, SQLite |
| Templates | Jinja2 |
| Frontend | HTML5, CSS3, JavaScript |
| Versionamento | Git, GitHub |

## Arquitetura

O LibraryFlow utiliza uma estrutura em camadas que separa a interface web, o roteamento, os serviços da aplicação, a camada de persistência e o banco de dados.

```text
Usuário
  │
  ▼
Templates Jinja2
  │
  ▼
Rotas FastAPI
  │
  ▼
Camada de Serviços
  │
  ▼
SQLAlchemy ORM
  │
  ▼
Banco de Dados SQLite
```

Essa separação mantém as responsabilidades de interface, lógica da aplicação e persistência organizadas conforme o projeto evolui.

Para uma descrição detalhada da arquitetura, consulte [`docs/architecture.md`](docs/architecture.md).

## Estrutura do Projeto

```text
LibraryFlow/
├── app/
│   ├── database/
│   ├── models/
│   ├── routes/
│   └── services/
├── database/
├── docs/
│   └── use-cases/
├── static/
│   ├── css/
│   ├── images/
│   └── js/
├── templates/
│   └── partials/
├── main.py
├── requirements.txt
└── README.md
```

O projeto separa a lógica da aplicação, persistência, documentação técnica, recursos estáticos e templates renderizados pelo servidor em diretórios dedicados.

## Primeiros Passos

O LibraryFlow requer Python 3.13 ou superior.

Clone o repositório:

```bash
git clone https://github.com/arthurcfranklin/libraryflow.git
cd libraryflow
```

Crie e ative um ambiente virtual e, em seguida, instale as dependências do projeto de acordo com a configuração do repositório.

As instruções detalhadas para configuração do ambiente e execução da aplicação estão disponíveis em [`docs/setup.md`](docs/setup.md).

## Documentação

A documentação técnica é mantida em [`docs/`](docs/) e evolui juntamente com a aplicação.

| Documento | Descrição |
| --- | --- |
| [Arquitetura](docs/architecture.md) | Arquitetura da aplicação e decisões estruturais |
| [Requisitos](docs/requirements.md) | Requisitos funcionais e não funcionais |
| [Regras de Negócio](docs/business-rules.md) | Regras de negócio implementadas pelo sistema |
| [Casos de Uso](docs/use-cases/use-cases.md) | Casos de uso e fluxos relacionados |
| [Banco de Dados](docs/database.md) | Modelo de dados e documentação da persistência |
| [API](docs/api.md) | Documentação da API e interfaces da aplicação |
| [Design](docs/design.md) | Especificações da interface e design |
| [Configuração](docs/setup.md) | Configuração do ambiente de desenvolvimento e da aplicação |
| [Solução de Problemas](docs/troubleshooting.md) | Problemas conhecidos e procedimentos de diagnóstico |
| [Changelog](docs/changelog.md) | Histórico de alterações do projeto |
| [Roadmap](docs/roadmap.md) | Evolução planejada do projeto |
| [Contribuição](docs/contributing.md) | Diretrizes de desenvolvimento e contribuição |

## Releases

| Versão | Marco |
| --- | --- |
| `v0.1.0-alpha` | Arquitetura Web Inicial |
| `v0.2.0-alpha` | Dashboard e Sistema de Temas |
| `v0.3.0-alpha` | Fundação da Gestão de Livros |
| `v0.4.0-beta` | CRUD Completo de Livros |
| `v0.5.0-beta` | Estrutura de Documentação e Governança |

## Roadmap

### Concluído

- [x] Arquitetura web
- [x] Dashboard administrativo
- [x] Sistema de temas
- [x] CRUD completo de livros
- [x] Persistência com SQLite
- [x] Integração com SQLAlchemy
- [x] Estrutura modular da aplicação
- [x] Documentação técnica
- [x] Fluxo de releases
- [x] Governança do projeto

### `v0.6.0-beta` — Gestão de Usuários

- [ ] Cadastrar usuários
- [ ] Consultar usuários
- [ ] Editar usuários
- [ ] Excluir usuários

### `v0.7.0-beta` — Gestão de Empréstimos

- [ ] Empréstimos
- [ ] Devoluções
- [ ] Controle de disponibilidade

### `v0.8.0-beta` — Autenticação

- [ ] Autenticação
- [ ] Gerenciamento de sessão
- [ ] Proteção de rotas

### `v0.9.0-beta` — Administração

- [ ] Relatórios administrativos
- [ ] Recursos de auditoria
- [ ] Recursos de gestão

### `v1.0.0`

- [ ] Release estável

## Licença

O LibraryFlow é distribuído sob a [Licença MIT](LICENSE).

---

Desenvolvido por **Arthur Franklin** · [Read in English](README.md) · [Licença MIT](LICENSE)
