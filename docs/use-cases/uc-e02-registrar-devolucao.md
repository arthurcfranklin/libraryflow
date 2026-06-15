# 📖 UC-E02 - Registrar Devolução

## 1. Visão Geral

Este caso de uso descreve o processo de registro de devoluções de livros no LibraryFlow.

A funcionalidade permite finalizar empréstimos ativos, registrar a data de devolução e atualizar automaticamente a disponibilidade do livro no acervo.

---

## 2. Metadados

| Campo | Descrição |
|---|---|
| ID | **UC-E02** |
| Nome | Registrar Devolução |
| Ator Principal | Bibliotecário |
| Módulo | Empréstimos |
| Gatilho | Bibliotecário seleciona a opção "Devolver" em um empréstimo ativo |
| Prioridade | ⭐⭐⭐⭐⭐ - Essencial |
| Complexidade | ⭐⭐⭐☆☆ - Média |
| Status | Planejado |

---

## 3. Objetivo

Permitir o registro de devoluções de livros emprestados.

---

## 4. Pré-condições

- O usuário deve estar autenticado.
- O módulo de empréstimos deve estar acessível.
- O empréstimo deve existir no sistema.
- O empréstimo deve estar ativo.
- O sistema deve possuir conexão com o banco de dados.

---

## 5. Fluxo Principal

1. O bibliotecário acessa o módulo **Empréstimos**.
2. O bibliotecário localiza um empréstimo ativo.
3. O bibliotecário seleciona a opção **Devolver**.
4. O sistema exibe uma confirmação de devolução.
5. O bibliotecário confirma a operação.
6. O sistema registra a data de devolução.
7. O sistema altera o status do empréstimo para finalizado.
8. O sistema atualiza a disponibilidade do livro.
9. O sistema exibe confirmação da operação.

---

## 6. Fluxos Alternativos

### **FA01** - Cancelamento da Devolução

1. O sistema exibe a confirmação de devolução.
2. O bibliotecário seleciona **Cancelar**.
3. O sistema encerra a operação.
4. Nenhuma alteração é realizada.

### **FA02** - Empréstimo não encontrado

1. O sistema tenta localizar o empréstimo.
2. O empréstimo não é encontrado.
3. O sistema exibe mensagem de erro.
4. A devolução não é realizada.

### **FA03** - Empréstimo já finalizado

1. O bibliotecário seleciona um empréstimo já finalizado.
2. O sistema identifica que a devolução já foi registrada.
3. O sistema bloqueia a operação.
4. O sistema informa que o empréstimo já foi finalizado.

### **FA04** - Falha no registro da devolução

1. O sistema tenta registrar a devolução.
2. Ocorre erro durante a gravação.
3. O sistema exibe mensagem de erro.
4. Nenhuma alteração é persistida.

---

## 7. Critérios de Aceitação

- A devolução deve ser registrada no banco de dados.
- O empréstimo deve ter status atualizado para finalizado.
- A data de devolução deve ser registrada.
- A disponibilidade do livro deve ser atualizada automaticamente.
- Não deve ser possível devolver empréstimos inexistentes.
- Não deve ser possível devolver empréstimos já finalizados.
- O sistema deve confirmar a operação ao usuário.

---

## 8. Regras de Negócio Relacionadas

| Código | Regra |
|---|---|
| **BR-E04** | Atualização automática de disponibilidade |
| **BR-E05** | Devolução de empréstimo ativo |
| **BR-D01** | Livro disponível para empréstimo |
| **BR-D02** | Livro indisponível |

---

## 9. Requisitos Relacionados

| Código | Requisito |
|---|---|
| **RF011** | Registro de Devoluções |
| **RF013** | Atualização Automática de Disponibilidade |

---

## 10. Módulos Relacionados

| Módulo | Relacionamento |
|---|---|
| Empréstimos | Módulo principal |
| Livros | Disponibilidade atualizada após devolução |
| Usuários | Usuário vinculado ao empréstimo |
| Dashboard | Atualização dos indicadores operacionais |

---

## 11. Resultado Esperado

Ao concluir a operação, o empréstimo deve ser finalizado com sucesso, a data de devolução deve ser registrada e o livro deve retornar à disponibilidade do acervo.

---

## 12. Status de Implementação

Planejado para versões futuras do LibraryFlow.

---

**Última atualização:** Junho de 2026 | **Versão:** v0.5.0-beta