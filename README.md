# Sistema de Limpeza - Arquitetura DDD + MVC

Projeto desenvolvido para fins educacionais na Faculdade UNG.

O objetivo deste projeto é demonstrar na prática:

* MVC
* DDD (Domain Driven Design)
* Repository Pattern
* Application Service
* Aggregate Root
* Value Objects
* Clean Code
* Separação de responsabilidades
* Persistência em JSON
* Dependency Injection

---

# Tecnologias utilizadas

* Python 3.11+
* Flet
* JSON
* Programação Orientada a Objetos
* DDD
* MVC

---

# Objetivo pedagógico

Este projeto foi criado para que os alunos possam compreender:

* como estruturar projetos profissionais
* como separar regras de negócio
* como organizar camadas
* como desacoplar persistência
* como aplicar SOLID
* como implementar DDD em Python
* como estruturar aplicações escaláveis

---

# Estrutura do projeto

```text
src/
│
├── domain/
│   ├── aggregates/
│   ├── entities/
│   ├── exceptions/
│   ├── repositories/
│   ├── services/
│   └── value_objects/
│
├── application/
│   ├── dto/
│   ├── services/
│   └── use_cases/
│
├── infrastructure/
│   ├── mappers/
│   ├── persistence/
│   │   └── json/
│   └── services/
│
├── presentation/
│   ├── constructors/
│   ├── controllers/
│   └── views/
│
└── app.py
```

---

# Diagrama Banco de Dados

# Diagrama Banco de Dados — Sistema de Controle de Estoque


    PRODUTO {
        int id_produto PK
        varchar nome
        varchar marca
        varchar unidade
        int id_categoria FK
    }

    CATEGORIA {
        int id_categoria PK
        varchar tipo
    }

    ESTOQUE {
        int id_estoque PK
        int id_produto FK
        decimal quantidade
    }

    MOVIMENTO {
        int id_movimento PK
        int id_produto FK
        int id_funcionario FK
        int id_sala FK
        varchar tipo_movimento
        decimal quantidade
        datetime data_movimento
    }

    FUNCIONARIO {
        int id_funcionario PK
        varchar nome
        varchar email
    }

    SALA {
        int id_sala PK
        varchar numero_sala
        varchar andar
    }

    CATEGORIA ||--o{ PRODUTO : possui

    PRODUTO ||--|| ESTOQUE : controla

    PRODUTO ||--o{ MOVIMENTO : movimenta

    FUNCIONARIO ||--o{ MOVIMENTO : realiza

    SALA ||--o{ MOVIMENTO : destino

# Explicação das camadas

# DOMAIN

Contém:

* entidades
* regras de negócio
* aggregates
* value objects
* contratos de repository
* exceptions

A camada Domain NÃO conhece:

* Flet
* JSON
* Banco de dados
* Interface gráfica

---

# APPLICATION

Responsável por:

* casos de uso
* orquestração do domínio
* DTOs
* Application Services

---

# INFRASTRUCTURE

Responsável por:

* persistência
* arquivos JSON
* mappers
* serviços externos

---

# PRESENTATION

Responsável por:

* controllers
* views
* interface gráfica
* eventos

---

# Requisitos

Antes de executar o projeto instale:

* Python 3.11 ou superior
* pip

---

# Como clonar o projeto

```bash
git clone https://github.com/SEU-USUARIO/sistema-limpeza-ddd.git
```

---

# Entrar na pasta do projeto

```bash
cd sistema-limpeza-ddd
```

---

# Criar ambiente virtual

## Windows

```bash
python -m venv venv
```

---

# Ativar ambiente virtual

## Windows

```bash
venv\Scripts\activate
```

## Linux / Mac

```bash
source venv/bin/activate
```

---

# Instalar dependências

```bash
pip install -r requirements.txt
```

---

# Dependências principais

```text
flet
```

---

# Executar o projeto

```bash
python src/app.py
```

---

# Fluxo da arquitetura

```text
VIEW
 ↓
CONTROLLER
 ↓
APPLICATION SERVICE
 ↓
USE CASE
 ↓
DOMAIN
 ↓
REPOSITORY
 ↓
INFRASTRUCTURE
```

---

# Exemplo de DDD aplicado

## Entity

```python
class Produto:
    pass
```

---

## Aggregate Root

```python
class ProdutoAggregate:
    pass
```

---

## Value Object

```python
class Dinheiro:
    pass
```

---

## Repository Pattern

```python
class ProdutoRepository:
    pass
```

---

## Use Case

```python
class CadastrarProduto:
    pass
```

---

# Conceitos trabalhados em aula

Durante o desenvolvimento os alunos irão praticar:

* POO
* Encapsulamento
* Herança
* Abstração
* Polimorfismo
* SOLID
* MVC
* DDD
* Repository Pattern
* Dependency Injection
* DTO
* Aggregate Root
* Value Objects
* Services
* Use Cases
* JSON Persistence

---

# Melhorias futuras

O projeto foi estruturado para permitir futuras implementações:

* SQLite
* PostgreSQL
* FastAPI
* APIs REST
* autenticação JWT
* testes unitários
* CQRS
* Event Sourcing
* Docker
* Clean Architecture

---

# Regras importantes do projeto

## Controllers

Controllers NÃO devem:

* acessar JSON diretamente
* criar entidades
* validar regras de negócio
* acessar persistência

---

## Views

Views NÃO devem:

* salvar dados
* validar domínio
* acessar repositories

---

## Domain

Domain NÃO pode conhecer:

* Flet
* banco de dados
* interface gráfica
* JSON

---

# Convenções utilizadas

## Nome de arquivos

```text
snake_case
```

---

## Nome de classes

```text
PascalCase
```

---

## Métodos e variáveis

```text
snake_case
```

---

# Como os alunos devem estudar este projeto

Recomendação:

1. Entender primeiro MVC
2. Entender separação de responsabilidades
3. Estudar o fluxo do controller
4. Entender os Use Cases
5. Entender Repository Pattern
6. Entender Aggregate Root
7. Entender Value Objects
8. Estudar Dependency Injection
9. Refatorar novas funcionalidades
10. Implementar novas entidades

---

# Exercícios sugeridos

Os alunos podem implementar:

* edição de produto
* exclusão de produto
* categorias
* estoque
* movimentações
* autenticação
* banco SQLite
* API REST
* relatórios

---

# Exemplo de evolução do sistema

```text
ProdutoAggregate
 ├── Produto
 ├── Estoque
 ├── Categoria
 └── Movimentacao
```

---

# Professor responsável

Rogério Sobral Ribeiro

Faculdade UNG

Curso:

* Análise e Desenvolvimento de Sistemas
* Ciência da Computação
* Sistemas de Informação

---

# Licença

Projeto desenvolvido exclusivamente para fins educacionais.

Uso livre para estudos e aprendizagem.
