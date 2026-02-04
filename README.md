# mvcPython

Projeto didatico em Python puro que demonstra a arquitetura MVC (Model-View-Controller) sem uso de frameworks. O sistema roda no terminal e permite cadastrar e buscar pessoas em memoria.

## Objetivo
- Mostrar a separacao clara de responsabilidades entre Model, View e Controller.
- Servir como base simples para estudar organizacao de codigo em Python.

## Funcionalidades
- Cadastrar pessoa (nome, idade, altura)
- Buscar pessoa pelo nome
- Menu interativo no terminal

## Estrutura MVC
- `src/models`: entidades e repositorios (armazenamento em memoria)
- `src/views`: interacao com o usuario via terminal
- `src/controllers`: validacao e orquestracao das regras
- `src/main`: construtores e fluxo de execucao

## Como executar
1. Tenha Python 3 instalado
2. No terminal, execute:

```bash
python run.py
```

## Fluxo rapido
- `run.py` chama `start()` em `src/main/process_handle.py`
- O menu inicial decide entre cadastro, busca ou sair
- Cada opcao conecta View -> Controller -> Model

## Observacoes
- Os dados sao mantidos apenas em memoria (lista interna do repositorio)
- Sem frameworks: foco total em MVC com Python puro


---

## Arquitetura de pastas
```
├── 📁 src
│   ├── 📁 controllers
│   │   ├── 🐍 __init__.py
│   │   ├── 🐍 people_finder_controller.py
│   │   └── 🐍 people_register_controller.py
│   ├── 📁 main
│   │   ├── 📁 constructor
│   │   │   ├── 🐍 __init__.py
│   │   │   ├── 🐍 introduction_process.py
│   │   │   ├── 🐍 people_finder_constructor.py
│   │   │   └── 🐍 people_register_constructor.py
│   │   ├── 🐍 __init__.py
│   │   └── 🐍 process_handle.py
│   ├── 📁 models
│   │   ├── 📁 connections
│   │   ├── 📁 entities
│   │   │   ├── 🐍 __init__.py
│   │   │   └── 🐍 person.py
│   │   ├── 📁 repository
│   │   │   ├── 🐍 __init__.py
│   │   │   └── 🐍 person_repository.py
│   │   └── 🐍 __init__.py
│   ├── 📁 views
│   │   ├── 🐍 __init__.py
│   │   ├── 🐍 first_view.py
│   │   ├── 🐍 people_finder_view.py
│   │   └── 🐍 people_register_view.py
│   └── 🐍 __init__.py
├── ⚙️ .gitignore
└── 🐍 run.py
```