# Regras de Negócio - LibraryFlow

Este documento define as regras de negócio que orientam o funcionamento do LibraryFlow. As regras descritas aqui são independentes da implementação técnica e representam o comportamento esperado da aplicação.

---

## 1. Domínio: Livros (Books)

### BR-L01 - **Livro deve possuir título**
- **Regra:** Todo livro cadastrado deve possuir um título informado.
- **Objetivo:** Garantir a correta identificação dos livros cadastrados.

---

### BR-L02 - **Livro deve possuir autor**

- **Regra:** Todo livro cadastrado deve possuir um autor informado.
- **Objetivo:** Garantir a identificação da autoria das obras cadastradas.


---

### BR-L03 - **Quantidade de exemplares deve ser válida**

- **Regra:** A quantidade de exemplares deve ser igual ou superior a 1.
- **Objetivo:** Garantir a consistência do controle de acervo.
---

### BR-L04 - **Livro deve possuir categoria**

- **Regra:** Todo livro cadastrado deve possuir uma categoria.
- **Objetivo:** Permitir a organização e classificação do acervo.
---

### BR-L05 - **Ano de publicação deve ser válido**

- **Regra:** O ano informado deve representar um ano válido.
- **Objetivo:** Garantir a integridade das informações bibliográficas.

---

## 2. Domínio: Disponibilidade (Availability)

### BR-D01 - **Livro disponível para empréstimo**

- **Regra:** Um livro será considerado disponível quando houver ao menos um exemplar disponível para empréstimo.
- **Objetivo:** Determinar quando um livro pode ser emprestado.

---

### BR-D02 - **Livro indisponível**
- **Regra:** Um livro será considerado indisponível quando todos os exemplares estiverem emprestados.
- **Objetivo:** Evitar empréstimos acima da quantidade disponível.

---

## 3. Domínio: Usuários (Users)

### BR-U01 - **Usuário deve possuir identificação**

- **Regra:** Todo usuário cadastrado deve possuir nome e identificador válido.
- **Objetivo:** Garantir a identificação dos usuários da biblioteca.

---

### BR-U02 - **Usuário deve possuir cadastro ativo**

- **Regra:** Apenas usuários ativos poderão realizar empréstimos.
- **Objetivo:** Garantir que apenas usuários autorizados utilizem os serviços da biblioteca.

---

## 4. Domínio: Empréstimos (Loans)

### BR-E01 - **Empréstimo vinculado a usuário**
- **Regra:** Todo empréstimo deve estar associado a um usuário cadastrado.
- **Objetivo:** Garantir a rastreabilidade das movimentações.


---

### BR-E02 - **Empréstimo vinculado a livro**
- **Regra:** Todo empréstimo deve estar associado a um livro cadastrado.
- **Objetivo:** Garantir a rastreabilidade do acervo.

---

### BR-E03 - **Não emprestar livro indisponível**
- **Regra:** O sistema não deve permtiir empréstimo de livros indisponíveis.
- **Objetivo:** Preservar a consistência da disponibilidade do acervo.

---

### BR-E04 - **Atualização automática de disponibilidade**
- **Regra:** Ao registrar um empréstimo ou devolução, o sistema deve atualizar automaticamente a disponibilidade do livro.
- **Objetivo:** Manter a disponibilidade dos livros sincronizada com as movimentações.

---

### BR-E05 - **Devolução de empréstimo ativo**
- **Regra:** Somente empréstimos ativos poderão ser devolvidos.
- **Objetivo:** Evitar inconsistências nas movimentações.

---

## 5. Domínio: Autenticação (Authentication)

### BR-A01 - **Acesso restrito**
- **Regra:** Somente usuários autenticados poderão acessar áreas administrativas do sistema.
- **Objetivo:** Garantir a segurança das áreas administrativas.

---

### BR-A02 - **Encerramento de sessão**
- **Regra:** O usuário poderá encerrar sua sessão a qualquer momento.
- **Objetivo:** Permitir o encerramento seguro da utilização do sistema.

---

## 6. Domínio: Interface (Interface)

### BR-I01 - **Consistência visual**
- **Regra:** Todos os módulos devem seguir o mesmo padrão visual do sistema.
- **Objetivo:** Garantir uma experiência uniforme ao usuário.

---

### BR-I02 - **Suporte a temas**
- **Regra:** O sistema deve permitir alternância entre tema claro e escuro.
- **Objetivo:** Melhorar a experiência de utilização da plataforma.

---

## 7. Domínio: Auditoria e Evolução (Audit and Progress)

### BR-AU01 - **Histórico de alterações**
- **Regra:** Alterações relevantes deverão ser registradas em releases e changelog do projeto.
- **Objetivo:** Garantir rastreabilidade da evolução do projeto.

---

**Última atualização:** Junho de 2026 | **Versão:** v0.5.0-beta