# 📖 UC-E01 - Registrar Empréstimo

## 1. Visão Geral

Este caso de uso descreve o processo de registro de empréstimos de livros no LibraryFlow.

A funcionalidade permite associar um livro disponível a um usuário cadastrado, registrando a movimentação e atualizando automaticamente a disponibilidade do acervo.

---

## 2. Metadados

| Campo          | Descrição                                         |
| -------------- | ------------------------------------------------- |
| ID             | **UC-E01**                                            |
| Nome           | Registrar Empréstimo                              |
| Ator Principal | Bibliotecário                                     |
| Módulo         | Empréstimos                                       |
| Gatilho        | Bibliotecário seleciona a opção "Novo Empréstimo" |
| Prioridade     | ⭐⭐⭐⭐⭐ - Essencial                                   |
| Complexidade   | ⭐⭐⭐⭐☆ - Alta                                        |
| Status         | Planejado                                         |

---

## 3. Objetivo

Permitir o registro de empréstimos de livros para usuários cadastrados.

---

## 4. Pré-condições

* O usuário deve estar autenticado.
* O módulo de empréstimos deve estar acessível.
* O livro deve estar cadastrado no sistema.
* O usuário deve estar cadastrado no sistema.
* O livro deve possuir disponibilidade para empréstimo.
* O sistema deve possuir conexão com o banco de dados.

---

## 5. Fluxo Principal

1. O bibliotecário acessa o módulo **Empréstimos**.
2. O bibliotecário seleciona a opção **Novo Empréstimo**.
3. O sistema exibe o formulário de empréstimo.
4. O bibliotecário seleciona o usuário.
5. O bibliotecário seleciona o livro.
6. O sistema verifica a disponibilidade do livro.
7. O bibliotecário confirma a operação.
8. O sistema registra o empréstimo.
9. O sistema atualiza a disponibilidade do livro.
10. O sistema registra a data do empréstimo.
11. O sistema exibe confirmação da operação.

---

## 6. Fluxos Alternativos

### **FA01** - Livro indisponível

1. O bibliotecário seleciona um livro sem exemplares disponíveis.
2. O sistema identifica a indisponibilidade.
3. O sistema exibe mensagem informando que o empréstimo não pode ser realizado.
4. O processo é encerrado.

### **FA02** - Usuário não encontrado

1. O bibliotecário seleciona um usuário inexistente.
2. O sistema não localiza o cadastro.
3. O sistema exibe mensagem de erro.
4. O empréstimo não é realizado.

### **FA03** - Usuário inativo

1. O bibliotecário seleciona um usuário inativo.
2. O sistema identifica a restrição.
3. O sistema bloqueia a operação.
4. O sistema informa o motivo do bloqueio.

### **FA04** - Falha no registro

1. O sistema tenta registrar o empréstimo.
2. Ocorre erro durante a gravação.
3. O sistema exibe mensagem de erro.
4. Nenhuma alteração é persistida.

---

## 7. Critérios de Aceitação

* O empréstimo deve ser persistido no banco de dados.
* O sistema deve vincular corretamente livro e usuário.
* O sistema deve registrar data do empréstimo.
* O sistema deve atualizar automaticamente a disponibilidade do livro.
* Não deve ser possível emprestar livros indisponíveis.
* Não deve ser possível emprestar livros para usuários inválidos ou inativos.
* O sistema deve confirmar a operação ao usuário.

---

## 8. Regras de Negócio Relacionadas

| Código | Regra                                     |
| ------ | ----------------------------------------- |
| **BR-D01** | Livro disponível para empréstimo          |
| **BR-D02** | Livro indisponível                        |
| **BR-U02** | Usuário deve possuir cadastro ativo       |
| **BR-E01** | Empréstimo vinculado a usuário            |
| **BR-E02** | Empréstimo vinculado a livro              |
| **BR-E03** | Não emprestar livro indisponível          |
| **BR-E04** | Atualização automática de disponibilidade |

---

## 9. Requisitos Relacionados

| Código | Requisito                                 |
| ------ | ----------------------------------------- |
| **RF010**  | Registro de Empréstimos                   |
| **RF013**  | Atualização Automática de Disponibilidade |

---

## 10. Módulos Relacionados

| Módulo      | Relacionamento                           |
| ----------- | ---------------------------------------- |
| Empréstimos | Módulo principal                         |
| Livros      | Controle de disponibilidade              |
| Usuários    | Controle de usuários aptos ao empréstimo |
| Dashboard   | Atualização dos indicadores operacionais |

---

## 11. Resultado Esperado

Ao concluir a operação, o empréstimo deve ser registrado com sucesso, vinculando um usuário a um livro disponível e atualizando automaticamente a disponibilidade do acervo.

---

## 12. Status de Implementação

Planejado para versões futuras do LibraryFlow.

---

**Última atualização:** Junho de 2026 | **Versão:** v0.5.0-beta
