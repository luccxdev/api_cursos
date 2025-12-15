# API de Cursos

API RESTful para gestão de cursos, desenvolvida em Flask com operacões CRUD completas.

## Quick Start

```bash
git clone https://github.com/luccxdev/api_cursos.git
cd api_cursos
pip install flask
python app.py
```

API rodando em: `http://localhost:5000`

## Endpoints

- **GET** `/cursos` - Listar todos os cursos
- **POST** `/cursos` - Criar novo curso
- **GET** `/cursos/<id>` - Obter curso por ID
- **PUT** `/cursos/<id>` - Atualizar curso
- **DELETE** `/cursos/<id>` - Deletar curso

## Stack

- Python 3.7+
- Flask
- JSON
