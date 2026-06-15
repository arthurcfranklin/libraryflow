# 📊 UC-D01 - Consultar Dashboard

## 1. Visão Geral

Este caso de uso descreve o processo de visualização do Dashboard do LibraryFlow.

O Dashboard tem como objetivo fornecer uma visão consolidada das principais informações do sistema, permitindo acesso rápido a indicadores operacionais, atalhos para módulos e informações relevantes para a administração da biblioteca.

---

## 2. Metadados

| Campo          | Descrição                        |
| -------------- | -------------------------------- |
| ID             | **UC-D01**                           |
| Nome           | Consultar Dashboard              |
| Ator Principal | Bibliotecário                    |
| Módulo         | Dashboard                        |
| Gatilho        | Bibliotecário acessa o Dashboard |
| Prioridade     | ⭐⭐⭐⭐⭐ - Essencial                  |
| Complexidade   | ⭐⭐☆☆☆ - Baixa                      |
| Status         | Implementado                     |

---

## 3. Objetivo

Permitir que o bibliotecário visualize informações consolidadas da biblioteca em uma única interface.

---

## 4. Pré-condições

* O usuário deve estar autenticado.
* O sistema deve estar operacional.
* O Dashboard deve estar acessível.

---

## 5. Fluxo Principal

1. O bibliotecário acessa o Dashboard.
2. O sistema carrega as informações disponíveis.
3. O sistema exibe os indicadores operacionais.
4. O sistema exibe os atalhos para os módulos disponíveis.
5. O bibliotecário consulta as informações apresentadas.
6. O bibliotecário pode navegar para outros módulos através dos atalhos.

---

## 6. Fluxos Alternativos

### FA01 - Falha no carregamento de informações

1. O bibliotecário acessa o Dashboard.
2. O sistema encontra falha ao carregar uma ou mais informações.
3. O sistema exibe mensagem informativa.
4. O Dashboard permanece acessível.

### FA02 - Ausência de dados

1. O Dashboard é acessado.
2. O sistema não encontra informações para exibir.
3. O sistema apresenta valores vazios ou padrão.
4. A navegação permanece disponível.

---

## 7. Critérios de Aceitação

* O Dashboard deve carregar sem erros.
* Os indicadores devem ser exibidos corretamente.
* Os atalhos devem redirecionar para os módulos correspondentes.
* O sistema deve manter consistência visual com os demais módulos.
* A navegação deve ocorrer sem necessidade de recarregamento manual da aplicação.

---

## 8. Regras de Negócio Relacionadas

| Código | Regra               |
| ------ | ------------------- |
| **BR-I01** | Consistência visual |
| **BR-I02** | Suporte a temas     |
| **BR-A01** | Acesso restrito     |

---

## 9. Requisitos Relacionados

| Código | Requisito                |
| ------ | ------------------------ |
| **RF014**  | Indicadores Operacionais |
| **RF015**  | Movimentações Recentes   |

---

## 10. Módulos Relacionados

| Módulo      | Relacionamento                    |
| ----------- | --------------------------------- |
| Dashboard   | Módulo principal                  |
| Livros      | Fonte de indicadores do acervo    |
| Usuários    | Fonte de indicadores de usuários  |
| Empréstimos | Fonte de indicadores operacionais |

---

## 11. Resultado Esperado

Ao acessar o Dashboard, o bibliotecário deve obter uma visão geral do sistema e conseguir navegar rapidamente para os módulos disponíveis.

---

## 12. Status de Implementação

Implementado parcialmente na versão atual do LibraryFlow.

Observação: indicadores dinâmicos e movimentações recentes ainda estão em evolução.

---

**Última atualização:** Junho de 2026 | **Versão:** v0.5.0-beta
