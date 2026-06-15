# 👤 UC-U01 - Cadastrar Usuário

## 1. Visão Geral

Este caso de uso descreve o processo de cadastro de usuários no LibraryFlow.

O cadastro de usuários permite registrar pessoas que poderão utilizar os serviços da biblioteca, incluindo empréstimos, devoluções e consultas relacionadas ao acervo.

---

## 2. Metadados

| Campo          | Descrição                              |
| -------------- | -------------------------------------- |
| ID             | **UC-U01**                                 |
| Nome           | Cadastrar Usuário                      |
| Ator Principal | Bibliotecário                          |
| Módulo         | Usuários                               |
| Gatilho        | Bibliotecário seleciona "Novo Usuário" |
| Prioridade     | ⭐⭐⭐⭐⭐ - Essencial                        |
| Complexidade   | ⭐⭐☆☆☆ - Baixa                            |
| Status         | Planejado                              |

---

## 3. Objetivo

Permitir o cadastro de novos usuários na biblioteca.

---

## 4. Pré-condições

* O usuário deve estar autenticado.
* O módulo de usuários deve estar acessível.
* O sistema deve possuir conexão com o banco de dados.

---

## 5. Fluxo Principal

1. O bibliotecário acessa o módulo **Usuários**.
2. O bibliotecário seleciona a opção **Novo Usuário**.
3. O sistema exibe o formulário de cadastro.
4. O bibliotecário informa os dados necessários:

   * Nome completo
   * E-mail
   * Matrícula ou identificação
   * Telefone (opcional)
5. O bibliotecário confirma o cadastro.
6. O sistema valida os dados informados.
7. O sistema registra o usuário no banco de dados.
8. O sistema atualiza a listagem de usuários.

---

## 6. Fluxos Alternativos

### **FA01** - Campo obrigatório não preenchido

1. O bibliotecário deixa um campo obrigatório vazio.
2. O sistema identifica a inconsistência.
3. O sistema exibe mensagem de validação.
4. O cadastro não é concluído.

### **FA02** - Usuário já cadastrado

1. O bibliotecário tenta cadastrar um usuário já existente.
2. O sistema identifica a duplicidade.
3. O sistema informa que o usuário já está registrado.
4. O cadastro não é concluído.

### **FA03** - E-mail inválido

1. O bibliotecário informa um e-mail inválido.
2. O sistema rejeita a operação.
3. O sistema solicita correção dos dados.

---

## 7. Critérios de Aceitação

* O usuário deve ser persistido no banco de dados.
* O usuário deve aparecer imediatamente na listagem.
* Campos obrigatórios devem ser validados.
* Não deve ser possível cadastrar usuários duplicados.
* O sistema deve validar o formato do e-mail.

---

## 8. Regras de Negócio Relacionadas

| Código | Regra                               |
| ------ | ----------------------------------- |
| **BR-U01** | Usuário deve possuir identificação  |
| **BR-U02** | Usuário deve possuir cadastro ativo |

---

## 9. Requisitos Relacionados

| Código | Requisito            |
| ------ | -------------------- |
| **RF006**  | Cadastro de Usuários |

---

## 10. Módulos Relacionados

| Módulo      | Relacionamento                                  |
| ----------- | ----------------------------------------------- |
| Usuários    | Módulo principal                                |
| Empréstimos | Utiliza usuários cadastrados para movimentações |
| Dashboard   | Atualização dos indicadores operacionais        |

---

## 11. Resultado Esperado

Ao concluir a operação, o usuário deve ser registrado com sucesso no sistema e ficar disponível para futuras movimentações de empréstimo.

---

## 12. Status de Implementação

Planejado para versões futuras do LibraryFlow.

---

**Última atualização:** Junho de 2026 | **Versão:** v0.5.0-beta