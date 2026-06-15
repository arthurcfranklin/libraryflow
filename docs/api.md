# API - LibraryFlow

## 1. **Visão Geral**

Este documento descreve as rotas HTTP utilizadas pelo LibraryFlow, incluindo rotas implementadas, rotas planejadas e responsabilidades de cada endpoint.

Atualmente, o LibraryFlow utiliza FastAPI com renderização de templates Jinja2. Portanto, as rotas documentadas representam tanto páginas renderizadas quanto operações de formulário.

---

## 2. **Metadados**

| Campo                   | Descrição        |
| ----------------------- | ---------------- |
| Documento               | **API**              |
| Projeto                 | **LibraryFlow**      |
| Framework               | **FastAPI**          |
| Renderização            | **Jinja2 Templates** |
| Status                  | **Em Evolução**      |
| Versão Atual do Sistema | **v0.5.0-beta**      |
| Versão do Documento     | **v1.0**             |

---

## 3. **Objetivo**

Documentar as rotas da aplicação, seus métodos HTTP, responsabilidades e relação com os módulos funcionais do sistema.

---

## 4. **Rotas Implementadas**

### 4.1 - Home

| Método | Rota | Descrição                                            |
| ------ | ---- | ---------------------------------------------------- |
| GET    | `/`  | Renderiza a página inicial administrativa do sistema |

### Responsabilidade

Exibir a home interna do LibraryFlow com atalhos para os principais módulos.

---

## 4.2 - **Login**

| Método | Rota     | Descrição                 |
| ------ | -------- | ------------------------- |
| GET    | `/login` | Renderiza a tela de login |

### Responsabilidade
Exibir a interface de autenticação do sistema.

### Observação
A autenticação real ainda está planejada para versões futuras.

---

## 4.3 - **Dashboard**

| Método | Rota         | Descrição                            |
| ------ | ------------ | ------------------------------------ |
| GET    | `/dashboard` | Renderiza o dashboard administrativo |

### Responsabilidade

Exibir indicadores e informações gerais da aplicação.

### Status

Parcialmente implementado.

---

## 4.4 - **Livros**

### Listar Livros

| Método | Rota     | Descrição                              |
| ------ | -------- | -------------------------------------- |
| GET    | `/books` | Renderiza a página de gestão de livros |

### Responsabilidade

Consultar o banco de dados e exibir os livros cadastrados.

### Requisitos Relacionados

* **RF004**
* **RF005**

---

### Cadastrar Livro

| Método | Rota     | Descrição              |
| ------ | -------- | ---------------------- |
| POST   | `/books` | Cadastra um novo livro |

### Responsabilidade

Receber os dados do formulário, validar as informações e persistir o livro no banco de dados.

### Campos Esperados

| Campo    | Tipo    | Obrigatório |
| -------- | ------- | ----------- |
| title    | String  | Sim         |
| author   | String  | Sim         |
| year     | Integer | Sim         |
| category | String  | Sim         |
| copies   | Integer | Sim         |

### Requisitos Relacionados

* **RF001**

### Regras Relacionadas

* **BR-L01**
* **BR-L02**
* **BR-L03**
* **BR-L04**
* **BR-L05**

---

### Excluir Livro

| Método | Rota                      | Descrição                  |
| ------ | ------------------------- | -------------------------- |
| POST   | `/books/{book_id}/delete` | Exclui um livro cadastrado |

### Parâmetros

| Parâmetro | Tipo    | Descrição              |
| --------- | ------- | ---------------------- |
| book_id   | Integer | Identificador do livro |

### Responsabilidade

Remover o livro selecionado do banco de dados.

### Requisitos Relacionados

* **RF003**

---

### Editar Livro

| Método | Rota                    | Descrição                     |
| ------ | ----------------------- | ----------------------------- |
| POST   | `/books/{book_id}/edit` | Atualiza os dados de um livro |

### Parâmetros

| Parâmetro | Tipo    | Descrição              |
| --------- | ------- | ---------------------- |
| book_id   | Integer | Identificador do livro |

### Campos Esperados

| Campo    | Tipo    | Obrigatório |
| -------- | ------- | ----------- |
| title    | String  | Sim         |
| author   | String  | Sim         |
| year     | Integer | Sim         |
| category | String  | Sim         |
| copies   | Integer | Sim         |

### Responsabilidade

Atualizar as informações de um livro cadastrado.

### Requisitos Relacionados

* **RF002**

### Regras Relacionadas

* **BR-L01**
* **BR-L02**
* **BR-L03**
* **BR-L04**
* **BR-L05**

---

## 4.5 - **Usuários**

| Método | Rota     | Descrição                      |
| ------ | -------- | ------------------------------ |
| GET    | `/users` | Renderiza a página de usuários |

### Responsabilidade
Exibir a estrutura inicial do módulo de usuários.

### Status
Placeholder implementado. Funcionalidades de CRUD planejadas.

---

## 4.6 - **Empréstimos**

| Método | Rota     | Descrição                         |
| ------ | -------- | --------------------------------- |
| GET    | `/loans` | Renderiza a página de empréstimos |

### Responsabilidade

Exibir a estrutura inicial do módulo de empréstimos.

### Status

Placeholder implementado. Funcionalidades de empréstimo e devolução planejadas.

---

## 5. Rotas Planejadas

## 5.1 - **Usuários**

| Método | Rota                      | Descrição         | Status    |
| ------ | ------------------------- | ----------------- | --------- |
| GET    | `/users`                  | Listar usuários   | Planejado |
| POST   | `/users`                  | Cadastrar usuário | Planejado |
| POST   | `/users/{user_id}/edit`   | Editar usuário    | Planejado |
| POST   | `/users/{user_id}/delete` | Excluir usuário   | Planejado |

---

## 5.2 - **Empréstimos**

| Método | Rota                      | Descrição            | Status    |
| ------ | ------------------------- | -------------------- | --------- |
| GET    | `/loans`                  | Listar empréstimos   | Planejado |
| POST   | `/loans`                  | Registrar empréstimo | Planejado |
| POST   | `/loans/{loan_id}/return` | Registrar devolução  | Planejado |

---

## 5.3 - **Autenticação**

| Método | Rota      | Descrição          | Status    |
| ------ | --------- | ------------------ | --------- |
| GET    | `/login`  | Exibir login       | Parcial   |
| POST   | `/login`  | Autenticar usuário | Planejado |
| POST   | `/logout` | Encerrar sessão    | Planejado |

---

## 6. **Padrão de Respostas**

### **Rotas de Página**

As rotas `GET` renderizam templates HTML através do Jinja2.

Exemplo:

```text
GET /books
```

Resultado esperado:

```text
Renderização da página books.html
```

---

### **Rotas de Formulário**

As rotas `POST` processam dados enviados por formulários HTML.

Após a operação, o sistema redireciona o usuário para a página correspondente.

Exemplo:

```text
POST /books
```

Resultado esperado:

```text
Livro cadastrado e redirecionamento para /books
```

---

## 7. **Códigos de Status Utilizados**

| Código | Uso                                          |
| ------ | -------------------------------------------- |
| **200**    | Página renderizada com sucesso               |
| **303**    | Redirecionamento após operação de formulário |
| **404**    | Recurso não encontrado                       |
| **500**    | Erro interno do servidor                     |

---

## **8. Documentação OpenAPI**

O FastAPI disponibiliza automaticamente documentação interativa em:

```text
/docs
```

e documentação alternativa em:

```text
/redoc
```

### Observação

Como o sistema utiliza principalmente templates HTML e formulários, a documentação OpenAPI será mais relevante após a evolução para endpoints REST.

---

## **9. Relação com Arquitetura**

As rotas seguem o fluxo:

```text
Browser
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

## **10. Evoluções Futuras**

Possíveis melhorias na camada de API:

* Separação entre rotas HTML e rotas REST
* Criação de endpoints JSON
* Documentação OpenAPI expandida
* Padronização de responses
* Validação com schemas Pydantic
* Autenticação por sessão ou token
* Versionamento de API

---

## **11. Documentos Relacionados**

* architecture.md
* requirements.md
* business-rules.md
* use-cases.md
* database.md
* roadmap.md

---

## **12. Status do Documento**

Em manutenção contínua conforme evolução das rotas e endpoints da aplicação.

---

**Última atualização:** Junho de 2026 | **Versão:** v1.0