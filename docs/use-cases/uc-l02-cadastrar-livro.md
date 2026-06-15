# 📚 UC-L02 - Cadastrar Livro

## 1. Visão Geral

Este caso de uso descreve o processo de cadastro de novos livros no acervo do LibraryFlow.

O cadastro de livros é responsável por registrar novas obras na biblioteca, permitindo seu gerenciamento, consulta e futura utilização em empréstimos.

---

## 2. Metadados

| Campo          | Descrição                            |
| -------------- | ------------------------------------ |
| ID             | **UC-L02**                               |
| Nome           | Cadastrar Livro                      |
| Ator Principal | Bibliotecário                        |
| Módulo         | Livros                               |
| Gatilho        | Bibliotecário seleciona "Novo Livro" |
| Prioridade     | ⭐⭐⭐⭐⭐ - Essencial             |
| Complexidade   | ⭐⭐☆☆☆ - Baixa                    |
| Status         | Implementado                         |

---

## 3. Objetivo

Permitir o registro de novos livros no acervo da biblioteca.

---

## 4. Pré-condições

* O usuário deve estar autenticado.
* O módulo de livros deve estar acessível.
* O sistema deve possuir conexão com o banco de dados.

---

## 5. Fluxo Principal

1. O bibliotecário acessa o módulo **Livros**.
2. O bibliotecário seleciona a opção **Novo Livro**.
3. O sistema exibe o formulário de cadastro.
4. O bibliotecário informa:

   * Título
   * Autor
   * Categoria
   * Ano de publicação
   * Quantidade de exemplares
5. O bibliotecário confirma a operação.
6. O sistema valida os dados informados.
7. O sistema registra o livro no banco de dados.
8. O sistema atualiza a listagem do acervo.
9. O novo livro passa a ficar disponível para consulta.

---

## 6. Fluxos Alternativos

### FA01 - Campo obrigatório não preenchido

1. O bibliotecário deixa um campo obrigatório vazio.
2. O sistema identifica a inconsistência.
3. O sistema exibe mensagem de validação.
4. O cadastro não é concluído.

### FA02 - Quantidade inválida

1. O bibliotecário informa quantidade menor que 1.
2. O sistema rejeita a operação.
3. O sistema solicita correção dos dados.

### FA03 - Ano inválido

1. O bibliotecário informa um ano inválido.
2. O sistema exibe mensagem de erro.
3. O cadastro permanece pendente até correção.

---

## 7. Critérios de Aceitação

* O livro deve ser persistido no banco de dados.
* O livro deve aparecer imediatamente na listagem.
* Os campos obrigatórios devem ser validados.
* Não deve ser possível cadastrar livros sem título.
* Não deve ser possível cadastrar livros sem autor.
* Não deve ser possível cadastrar quantidade inferior a 1.
* Não deve ser possível cadastrar ano inválido.

---

## 8. Regras de Negócio Relacionadas

| Código | Regra                                    |
| ------ | ---------------------------------------- |
| **BR-L01** | Livro deve possuir título                |
| **BR-L02** | Livro deve possuir autor                 |
| **BR-L03** | Quantidade de exemplares deve ser válida |
| **BR-L04** | Livro deve possuir categoria             |
| **BR-L05** | Ano de publicação deve ser válido        |

---

## 9. Requisitos Relacionados

| Código | Requisito          |
| ------ | ------------------ |
| **RF001**  | Cadastro de Livros |

---

## 10. Módulos Relacionados

| Módulo      | Relacionamento                                |
| ----------- | --------------------------------------------- |
| Livros      | Módulo principal                              |
| Dashboard   | Atualização dos indicadores do acervo         |
| Empréstimos | Utiliza livros cadastrados para movimentações |

---

## 11. Resultado Esperado

Ao concluir o cadastro, o livro deve ser registrado com sucesso no sistema e ficar imediatamente disponível para consulta e gerenciamento.

---

## 12. Status de Implementação

Implementado na versão atual do LibraryFlow.

---

**Última atualização:** Junho de 2026 | **Versão:** v0.5.0-beta
