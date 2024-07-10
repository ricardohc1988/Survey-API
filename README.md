# Survey API using Django REST Framework
This project implements a RESTful API for managing surveys and collecting anonymous responses. 
Built with Django and Django REST Framework, it provides endpoints to create surveys, manage questions and choices, and collect answers anonymously.

## Features

-**Surveys:** Create, retrieve, update, and delete surveys.
-**Questions:** Manage questions within surveys, ensuring uniqueness.
-**Choices:** Add choices to questions and manage their options.
-**Answers:** Allow anonymous users to submit responses to survey questions.
-**Permissions:** Differentiate access based on user roles (admin, authenticated, anonymous).

## Installation

1. Clone the repository:

```bash
git clone https://github.com/username/survey-api-django-rest.git
```

2. Navigate into the project directory:

```bash
cd survey-api-django-rest
```

3. Install dependencies using Pipenv:

```bash
pipenv install
```

4. Activate the virtual environment:

```bash
pipenv shell
```

5. Apply migrations:

```bash
python manage.py migrate
```

## API Endpoints

### Surveys

- `GET /surveys/`: Retrieve list of surveys.
- `POST /surveys/`: Create a new survey.
- `GET /surveys/<id>/`: Retrieve details of a specific survey.
- `PUT /surveys/<id>/`: Update a specific survey.
- `PATCH /surveys/<id>/`: Partially update a specific survey.
- `DELETE /surveys/<id>/`: Delete a specific survey.

### Questions

- `GET /questions/`: Retrieve list of questions.
- `POST /questions/`: Create a new question.
- `GET /questions/<id>/`: Retrieve details of a specific question.
- `PUT /questions/<id>/`: Update a specific question.
- `PATCH /questions/<id>/`: Partially update a specific question.
- `DELETE /questions/<id>/`: Delete a specific question.

### Choices

- `GET /choices/`: Retrieve list of choices.
- `POST /choices/`: Create a new choice.
- `GET /choices/<id>/`: Retrieve details of a specific choice.
- `PUT /choices/<id>/`: Update a specific choice.
- `PATCH /choices/<id>/`: Partially update a specific choice.
- `DELETE /choices/<id>/`: Delete a specific choice.

### Answers

- `POST /answers/`: Create an anonymous answer to a question. Accessible to everyone.
- `GET /answers/`: Retrieve a list of all answers. Accessible to authenticated users.
- `GET /answers/<id>/`: Retrieve details of a specific answer. Accessible to authenticated users.
