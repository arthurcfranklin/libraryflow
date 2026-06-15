# Troubleshooting - LibraryFlow

## Visão Geral

Este documento reúne problemas comuns encontrados durante instalação, configuração e execução do LibraryFlow, juntamente com suas possíveis causas e soluções.

O objetivo é reduzir o tempo de diagnóstico e facilitar a resolução de incidentes em ambientes de desenvolvimento.

---

## 1. Metadados

| Campo                   | Descrição       |
| ----------------------- | --------------- |
| Documento               | **Troubleshooting** |
| Projeto                 | **LibraryFlow**     |
| Categoria               | **Suporte Técnico** |
| Status                  | **Ativo**           |
| Versão Atual do Sistema | **v0.5.0-beta**     |
| Versão do Documento     | **v1.0**            |

---

## 2. Objetivo

Documentar problemas recorrentes e procedimentos de correção relacionados ao LibraryFlow.

---

## 3. Problemas de Ambiente Virtual

### **TRB-001 - Ambiente virtual não ativa**

### Sintoma

Ao executar:

```powershell
.venv\Scripts\activate
```

ocorre erro de execução.

### Possível Causa

Política de execução do PowerShell bloqueando scripts.

### Solução

Executar:

```powershell
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
```

Reabrir o terminal e tentar novamente.

---

## 5. Problemas de Dependências

### **TRB-002 - requirements.txt não instala**

### Sintoma

Erro durante:

```bash
pip install -r requirements.txt
```

### Possíveis Causas

* Python não instalado corretamente.
* Ambiente virtual não ativado.
* Pip desatualizado.

### Solução

Atualizar o pip:

```bash
python -m pip install --upgrade pip
```

Tentar novamente.

---

### **TRB-003 - Módulo não encontrado**

### Sintoma

```text
ModuleNotFoundError
```

### Possível Causa

Dependência não instalada.

### Solução

Reinstalar dependências:

```bash
pip install -r requirements.txt
```

---

## 6. Problemas de Inicialização

### **TRB-004 - Uvicorn não inicia**

### Sintoma

Erro ao executar:

```bash
uvicorn main:app --reload
```

### Possíveis Causas

* Arquivo principal incorreto.
* Dependências ausentes.
* Ambiente virtual desativado.

### Solução

Verificar:

```bash
pip install -r requirements.txt
```

e confirmar a existência do arquivo:

```text
main.py
```

---

## **TRB-005 - Porta já em uso**

### Sintoma

```text
Address already in use
```

### Possível Causa

Outra aplicação utilizando a porta 8000.

### Solução

Executar em outra porta:

```bash
uvicorn main:app --reload --port 8001
```

---

## 7. Problemas de Templates

### **TRB-006 - Template não encontrado**

### Sintoma

```text
TemplateNotFound
```

### Possível Causa

Arquivo HTML inexistente ou caminho incorreto.

### Solução

Verificar:

```text
templates/
```

Confirmar que o template existe e que o nome está correto.

---

## 8. Problemas de Banco de Dados

### **TRB-007 - Banco SQLite não encontrado**

### Sintoma

Erro relacionado ao arquivo de banco.

### Possível Causa

Arquivo ausente ou caminho incorreto.

### Solução

Verificar:

```text
database/libraryflow.db
```

Caso necessário, recriar o banco.

---

### **TRB-008 - Erro de SQLAlchemy**

### Sintoma

Falha ao consultar ou gravar registros.

### Possível Causa

Modelos desatualizados ou inconsistência entre ORM e banco.

### Solução

Verificar:

* Models
* Estrutura do banco
* Configuração da sessão SQLAlchemy

---

## 9. Problemas de Rotas

### **TRB-009 - Erro 404**

### Sintoma

Página não encontrada.

### Possível Causa

Rota inexistente ou incorreta.

### Solução

Verificar:

* Definição da rota
* Arquivos de rotas
* URL acessada

---

### **TRB-010 - Erro 500**

### Sintoma

```text
Internal Server Error
```

### Possível Causa

Erro interno da aplicação.

### Solução

Consultar logs do terminal para identificar a exceção gerada.

---

## 10. Problemas de Interface

### **TRB-011 - Estilos não carregam**

### Sintoma

Página sem CSS.

### Possível Causa

Arquivos estáticos não encontrados.

### Solução

Verificar:

```text
static/
```

e a configuração do FastAPI para arquivos estáticos.

---

### **TRB-012 - Tema não altera**

### Sintoma

Alternância entre tema claro e escuro não funciona.

### Possível Causa

Falha no JavaScript ou armazenamento local do navegador.

### Solução

* Limpar cache.
* Verificar console do navegador.
* Validar scripts JavaScript.

---

## 11. Boas Práticas de Diagnóstico

Ao investigar problemas:

1. Verificar logs do terminal.
2. Confirmar ambiente virtual ativo.
3. Confirmar instalação das dependências.
4. Validar estrutura do projeto.
5. Testar em ambiente limpo quando possível.

---

## 12. Documentos Relacionados

* setup.md
* architecture.md
* database.md
* api.md

---

## 13. Status do Documento

Em atualização contínua conforme novos problemas forem identificados.

---

**Última atualização:** Junho de 2026
**Versão:** v1.0