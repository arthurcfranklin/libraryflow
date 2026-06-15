# 📚 UC-L01 - Consultar Acervo

## 1. Visão Geral

Este caso de uso descreve o processo de consulta dos livros cadastrados no acervo do LibraryFlow.

A consulta do acervo permite que o bibliotecário visualize os registros disponíveis no sistema, incluindo informações como título, autor, ano, categoria, quantidade de exemplares e status de disponibilidade.

---

## 2. Metadados

| Campo | Descrição |
|---|---|
| ID | **UC-L01** |
| Nome | Consultar Acervo |
| Ator Principal | Bibliotecário |
| Módulo | Livros |
| Gatilho | Bibliotecário acessa o módulo Livros |
| Prioridade | ⭐⭐⭐⭐⭐ - Essencial |
| Complexidade | ⭐☆☆☆☆ - Muito Baixa |
| Status | **Implementado** |

---

## 3. Objetivo

Permitir que o bibliotecário visualize os livros cadastrados no acervo da biblioteca.

---

## 4. Pré-condições

- O usuário deve estar autenticado.
- O módulo de livros deve estar disponível.
- O sistema deve possuir acesso à base de dados.

---

## 5. Fluxo Principal

1. O bibliotecário acessa o módulo **Livros**.
2. O sistema consulta os registros existentes no banco de dados.
3. O sistema exibe a listagem de livros cadastrados.
4. O bibliotecário visualiza as informações disponíveis.
5. O sistema mantém os dados sem alteração.

---

## 6. Fluxos Alternativos

### **FA01** - Acervo vazio

1. O bibliotecário acessa o módulo **Livros**.
2. O sistema não encontra registros cadastrados.
3. O sistema exibe uma mensagem informando que não há livros cadastrados.
4. O sistema mantém disponível a opção de cadastro de novo livro.

---

## 7. Critérios de Aceitação

- A tela de livros deve carregar corretamente.
- A listagem deve exibir todos os livros cadastrados.
- O sistema deve exibir título, autor, ano, categoria, exemplares e status.
- Caso não existam livros cadastrados, o sistema deve apresentar uma mensagem adequada.
- A consulta não deve alterar nenhum dado do sistema.

---

## 8. Regras de Negócio Relacionadas

| Código | Regra |
|---|---|
| **BR-I01** | Consistência visual |
| **BR-D01** | Livro disponível para empréstimo |
| **BR-D02** | Livro indisponível |

---

## 9. Requisitos Relacionados

| Código | Requisito |
|---|---|
| **RF004** | Consulta de Acervo |
| **RF005** | Controle de Disponibilidade |

---

## 10. Módulos Relacionados

| Módulo | Relacionamento |
|---|---|
| Livros | Fonte principal dos dados exibidos |
| Dashboard | Pode utilizar informações do acervo para indicadores |
| Empréstimos | Depende da disponibilidade dos livros |

---

## 11. Resultado Esperado

Ao acessar o módulo **Livros**, o bibliotecário deve conseguir visualizar o acervo cadastrado de forma clara, organizada e sem realizar alterações nos registros.

---

## 12. Status de Implementação

Implementado na versão atual do LibraryFlow.

---

**Última atualização:** Junho de 2026 | **Versão:** v0.5.0-beta