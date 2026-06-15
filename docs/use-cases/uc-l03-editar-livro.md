# 📚 UC-L03 - Editar Livro

## 1. Visão Geral

Este caso de uso descreve o processo de atualização das informações de livros cadastrados no LibraryFlow.

A funcionalidade permite corrigir, complementar ou atualizar dados do acervo sem a necessidade de excluir e recriar registros existentes.

---

## 2. Metadados

| Campo          | Descrição                                                      |
| -------------- | -------------------------------------------------------------- |
| ID             | **UC-L03**                                                         |
| Nome           | Editar Livro                                                   |
| Ator Principal | Bibliotecário                                                  |
| Módulo         | Livros                                                         |
| Gatilho        | Bibliotecário seleciona a opção "Editar" em um livro existente |
| Prioridade     | ⭐⭐⭐⭐⭐ - Essencial                                                |
| Complexidade   | ⭐⭐☆☆☆ - Baixa                                                    |
| Status         | Implementado                                                   |

---

## 3. Objetivo

Permitir a atualização das informações de livros previamente cadastrados.

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
3. O bibliotecário seleciona a opção **Editar**.
4. O sistema exibe o formulário preenchido com os dados atuais.
5. O bibliotecário altera as informações necessárias.
6. O bibliotecário confirma a alteração.
7. O sistema valida os dados informados.
8. O sistema atualiza o registro no banco de dados.
9. O sistema atualiza a listagem do acervo.

---

## 6. Fluxos Alternativos

### **FA01** - Campo obrigatório não preenchido

1. O bibliotecário remove uma informação obrigatória.
2. O sistema identifica a inconsistência.
3. O sistema exibe mensagem de validação.
4. A alteração não é salva.

### **FA02** - Quantidade inválida

1. O bibliotecário informa quantidade menor que 1.
2. O sistema rejeita a atualização.
3. O sistema solicita correção dos dados.

### **FA03** - Ano inválido

1. O bibliotecário informa um ano inválido.
2. O sistema exibe mensagem de erro.
3. A atualização permanece pendente até correção.

### **FA04** - Livro não encontrado

1. O livro é removido ou deixa de existir durante a operação.
2. O sistema não encontra o registro.
3. O sistema exibe mensagem de erro.
4. A operação é cancelada.

---

## 7. Critérios de Aceitação

* As alterações devem ser persistidas no banco de dados.
* Os novos dados devem ser exibidos imediatamente na listagem.
* Campos obrigatórios devem ser validados.
* O sistema não deve permitir informações inválidas.
* A atualização não deve gerar registros duplicados.

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

| Código | Requisito        |
| ------ | ---------------- |
| **RF002**  | Edição de Livros |

---

## 10. Módulos Relacionados

| Módulo      | Relacionamento                        |
| ----------- | ------------------------------------- |
| Livros      | Módulo principal                      |
| Dashboard   | Atualização dos indicadores do acervo |
| Empréstimos | Utiliza os dados atualizados do livro |

---

## 11. Resultado Esperado

Ao concluir a operação, as informações do livro devem ser atualizadas com sucesso e refletidas imediatamente no sistema.

---

## 12. Status de Implementação

Implementado na versão atual do LibraryFlow.

---

**Última atualização:** Junho de 2026 | **Versão:** v0.5.0-beta
