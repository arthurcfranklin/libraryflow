# Setup - LibraryFlow

## 1. Visão Geral

Este documento descreve os procedimentos necessários para configurar e executar o LibraryFlow em ambiente local de desenvolvimento.

O objetivo é garantir que qualquer desenvolvedor consiga instalar as dependências, configurar o ambiente e executar a aplicação de forma consistente.

---

## 2. Metadados

| Campo                   | Descrição   |
| ----------------------- | ----------- |
| Documento               | **Setup**       |
| Projeto                 | **LibraryFlow** |
| Categoria               | **Ambiente**    |
| Status                  | **Ativo**       |
| Versão Atual do Sistema | **v0.5.0-beta** |
| Versão do Documento     | **v1.0**        |

---

## 3. Objetivo

Fornecer instruções para instalação, configuração e execução do LibraryFlow em ambiente local.

---

## 4. Requisitos do Ambiente

### Software Necessário

| Software | Versão Recomendada |
| -------- | ------------------ |
| Python   | **3.13+**              |
| Git      | **2.0+**               |
| SQLite   | **Integrado**          |
| VS Code  | **Opcional**           |

---

## Sistema Operacional

### Ambientes suportados:

* Windows 10
* Windows 11
* Linux
* macOS

---

## 5. Clonando o Projeto

Clone o repositório:

```bash
git clone https://github.com/arthurcfranklin/libraryflow.git
```

Acesse a pasta:

```bash
cd libraryflow
```

---

## 6. Ambiente Virtual

### Criar Ambiente Virtual

**Windows:**

```powershell
python -m venv .venv
```

**Linux:**

```bash
python3 -m venv .venv
```

---

### Ativar Ambiente Virtual

**Windows:**

```powershell
.venv\Scripts\activate
```

**Linux:**

```bash
source .venv/bin/activate
```

---

## 7. Instalação de Dependências

Instale os pacotes do projeto:

```bash
pip install -r requirements.txt
```

---

## Dependências Principais

* FastAPI
* SQLAlchemy
* Jinja2
* Uvicorn
* Pydantic

---

## 8. Estrutura do Projeto

```text
libraryflow/
│
├── app/
├── docs/
├── static/
├── templates/
├── database/
├── main.py
├── requirements.txt
└── README.md
```

---

## 9. Banco de Dados

### Banco Atual

O projeto utiliza **SQLite**.

Arquivo padrão:

```text
database/libraryflow.db
```

---

## Inicialização

O banco será criado automaticamente caso não exista.

---

## 10. Executando a Aplicação

Inicie o servidor:

```bash
uvicorn main:app --reload
```

---

## Resultado Esperado

Servidor iniciado:

```text
INFO: Uvicorn running on http://127.0.0.1:8000
```

---

## 11. Acessando a Aplicação

Após iniciar o servidor:

```text
http://127.0.0.1:8000
```

---

## Rotas Principais

| Rota       | Descrição   |
| ---------- | ----------- |
| /          | **Home**        |
| /dashboard | **Dashboard**   |
| /books     | **Livros**      |
| /users     | **Usuários**    |
| /loans     | **Empréstimos** |
| /login     | **Login**       |

---

## 12. Documentação FastAPI

Documentação automática:

```text
http://127.0.0.1:8000/docs
```

---

Documentação alternativa:

```text
http://127.0.0.1:8000/redoc
```

---

## 13. Fluxo de Desenvolvimento

### Atualizar Dependências

```bash
pip install -r requirements.txt
```

---

### Executar Aplicação

```bash
uvicorn main:app --reload
```

---

### Verificar Alterações

A aplicação utiliza recarga automática através do parâmetro:

```text
--reload
```

---

## 14. Boas Práticas

* Utilizar ambiente virtual dedicado.
* Não versionar arquivos temporários.
* Manter dependências atualizadas.
* Validar funcionamento antes de realizar commits.

---

## 15. Documentos Relacionados

* architecture.md
* database.md
* api.md
* troubleshooting.md

---

## 16. Status do Documento

Em manutenção contínua conforme evolução da infraestrutura do projeto.

---

**Última atualização:** Junho de 2026 | **Versão:** v1.0
