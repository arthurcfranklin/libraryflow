# 📚 UC-L04 - Excluir Livro

## 1. Visão Geral

Este caso de uso descreve o processo de remoção de livros cadastrados no LibraryFlow.

A funcionalidade permite excluir registros do acervo quando não forem mais necessários, mantendo a base de dados organizada e atualizada.

---

## 2. Metadados

| Campo          | Descrição                                                       |
| -------------- | --------------------------------------------------------------- |
| ID             | **UC-L04**                                                          |
| Nome           | Excluir Livro                                                   |
| Ator Principal | Bibliotecário                                                   |
| Módulo         | Livros                                                          |
| Gatilho        | Bibliotecário seleciona a opção "Excluir" em um livro existente |
| Prioridade     | ⭐⭐⭐⭐⭐ - Essencial                                                 |
| Complexidade   | ⭐⭐☆☆☆ - Baixa                                                     |
| Status         | Implementado                                                    |

---

## 3. Objetivo

Permitir a remoção de livros cadastrados no acervo.

---

## 4. Pré-condições

* O usuário deve estar autenticado.
* O livro deve existir no sistema.
* O módulo de livros deve estar acessível.
* O sistema deve possuir conexão com o banco de dados.

---

## 5. Fluxo Principal

1. O bibliotecário acessa o módulo **Livros**.
2. O bibliotecário localiza o livro desejado.
3. O bibliotecário seleciona a opção **Excluir**.
4. O sistema exibe uma confirmação de exclusão.
5. O bibliotecário confirma a operação.
6. O sistema remove o registro do banco de dados.
7. O sistema atualiza a listagem do acervo.

---

## 6. Fluxos Alternativos

### **FA01** - Cancelamento da Exclusão

1. O sistema exibe a confirmação de exclusão.
2. O bibliotecário seleciona **Cancelar**.
3. O sistema encerra a operação.
4. Nenhuma alteração é realizada.

### **FA02** - Livro não encontrado

1. O sistema tenta localizar o registro.
2. O livro não é encontrado.
3. O sistema exibe mensagem de erro.
4. A exclusão não é realizada.

### **FA03** - Falha na Exclusão

1. O sistema encontra o registro.
2. Ocorre uma falha durante a remoção.
3. O sistema informa o erro ao usuário.
4. O registro permanece no banco de dados.

---

## 7. Critérios de Aceitação

* O livro deve ser removido do banco de dados.
* O livro não deve mais aparecer na listagem.
* A operação deve exigir confirmação do usuário.
* O cancelamento não deve alterar os dados.
* O sistema deve tratar falhas sem corromper registros.

---

## 8. Regras de Negócio Relacionadas

| Código | Regra                     |
| ------ | ------------------------- |
| **BR-L01** | Livro deve possuir título |
| **BR-L02** | Livro deve possuir autor  |
| **BR-I01** | Consistência visual       |

---

## 9. Requisitos Relacionados

| Código | Requisito          |
| ------ | ------------------ |
| **RF003**  | Exclusão de Livros |

---

## 10. Módulos Relacionados

| Módulo      | Relacionamento                             |
| ----------- | ------------------------------------------ |
| Livros      | Módulo principal                           |
| Dashboard   | Atualização dos indicadores do acervo      |
| Empréstimos | Pode ser impactado por registros removidos |

---

## 11. Resultado Esperado

Ao concluir a operação, o livro deve ser removido com sucesso do sistema e deixar de aparecer no acervo.

---

## 12. Status de Implementação

Implementado na versão atual do LibraryFlow.

---

**Última atualização:** Junho de 2026 | **Versão:** v0.5.0-beta
