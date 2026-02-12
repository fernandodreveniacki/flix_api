# Flix API

Flix API é uma API RESTful desenvolvida com Django e Django REST Framework para gerenciamento de filmes, gêneros, atores e avaliações.

O projeto foi estruturado de forma modular, utilizando separação por apps, modelagem relacional consistente e princípios de organização voltados para escalabilidade e manutenção.

---

## Arquitetura

A aplicação segue o padrão MVT (Model–View–Template) do Django, utilizando o Django REST Framework para exposição de endpoints RESTful.

Cada domínio da aplicação foi isolado em um app independente:

- actors
- genres
- movies
- reviews

Essa abordagem favorece:

- Baixo acoplamento
- Alta coesão
- Facilidade de manutenção
- Evolução futura para microsserviços (se necessário)

---

## Modelagem de Dados

Relacionamentos implementados:

- Movie → ForeignKey → Genre
- Movie → ManyToMany → Actor
- Review → ForeignKey → Movie

Principais decisões:

- Uso de relacionamentos explícitos para garantir integridade referencial.
- Separação da entidade Review para permitir múltiplas avaliações por filme.
- Possibilidade futura de associação de Review a User (extensível).

---

## Tecnologias Utilizadas

- Python 3.12+
- Django
- Django REST Framework
- PostgreSQL
- Git

---

## Versionamento da API

A API segue padrão de versionamento via URL:

/api/v1/


## Endpoints

### Movies
- CRUD completo via /api/v1/movies/
- GET    /api/v1/movies/
- POST   /api/v1/movies/
- GET    /api/v1/movies/{id}/
- PUT    /api/v1/movies/{id}/
- DELETE /api/v1/movies/{id}/

### Actors
- CRUD completo via /api/v1/actors/
- GET    /api/v1/actors/
- POST   /api/v1/actors/
- GET    /api/v1/actors/{id}/
- PUT    /api/v1/actors/{id}/
- DELETE /api/v1/actors/{id}/

### Genres
- CRUD completo via /api/v1/genres/
- GET    /api/v1/genres/
- POST   /api/v1/genres/
- GET    /api/v1/genres/{id}/
- PUT    /api/v1/genres/{id}/
- DELETE /api/v1/genres/{id}/

### Reviews
- CRUD completo via /api/v1/reviews/
- GET    /api/v1/reviews/
- POST   /api/v1/reviews/
- GET    /api/v1/reviews/{id}/
- PUT    /api/v1/reviews/{id}/
- DELETE /api/v1/reviews/{id}/

---

## Recursos Implementados

- ViewSets para padronização dos endpoints
- Serializers
- Relacionamentos aninhados
- Filtros via query parameters
- Admin customizado
- Organização modular por domínio

---

## Estrutura do Projeto

flix_api/
│
├── actors/
│ ├── migrations/
| ├── admin.py
│ ├── apps.py
│ ├── models.py
│ ├── serializers.py
│ ├── tests.py
│ ├── urls.py
│ └── views.py
│
├── app/
│ ├── asgi.py
│ ├── settings.py
│ ├── urls.py
│ └── wsgi.py
|
├── genres/
│ ├── migrations/
| ├── admin.py
│ ├── apps.py
│ ├── models.py
│ ├── serializers.py
│ ├── tests.py
│ ├── urls.py
│ └── views.py
|
├── movies/
│ ├── migrations/
| ├── admin.py
│ ├── apps.py
│ ├── models.py
│ ├── serializers.py
│ ├── tests.py
│ ├── urls.py
│ └── views.py
|
├── reviews/
│ ├── migrations/
| ├── admin.py
│ ├── apps.py
│ ├── models.py
│ ├── serializers.py
│ ├── tests.py
│ ├── urls.py
│ └── views.py
|
├── .gitignore
├── manage.py
└── README.md

## Como Executar

### 1. Clonar o repositório

```bash
    git clone https://github.com/fernandodreveniacki/flix_api.git
    cd flix_api
```

### 2. Criar e ativar ambiente virtual
```bash
    python -m venv venv
    Linux - source venv/bin/activate
    Windows - venv/scripts/activate
```

### 3. Instalar dependências
```bash
    pip install -r requirements.txt
```

### 4. Aplicar migrações
```bash
    python manage.py migrate
```

### 5. Executar servidor
```bash
    python manage.py runserver
```

## Futuras atualizações
- Autenticação com JWT
- Testes automatizados (pytest)

## Autor
### Fernando Augusto Dreveniacki
