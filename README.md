# todo-backend-django

This is a simple backend for a To Do application using the Django framework, enhanced from code forked from https://github.com/mihirk/todo-backend-django

New features added include:

- Option to display only completed (http://127.0.0.1:8000/todos/done) or pending (http://127.0.0.1:8000/todos/pending) tasks
- 'created' field added to ToDoItem model, to allow tasks to be sorted by oldest creation date (http://127.0.0.1:8000/todos/oldest) to focus on clearing out the cobwebs

The app included an 'order' field, which was utilized for the default sort criteria for the list. This is problematic, as it can be difficult to know a preferred list order as a to do list grows, and there is currently no way to re-order existing tasks. However, it was maintained as part of the original app functionality. This might be more useful as a priority assignment (High, Medium, Low), or due date.

## Installation (Windows examples)

1. Clone the repository to a local directory.
2. Create virtual environment to store dependencies and start virtual environment.
```
python -m venv myvenv
myvenv\Scripts\activate
```

3. Install requirements
```
pip install -r requirements.txt
```

5. Run local server to view at http://127.0.0.1:8000/
```
python manage.py runserver
```
Your browser should display a set of sample JSON To Dos from the database file (Firefox works well for this).

## Usage
View individual to do items by primary key, following example of: http://127.0.0.1:8000/todo/3 

Accepts GET, POST, PATCH, and DELETE requests.
Using a tool like Postman, add a new To Do:
```
POST /todos HTTP/1.1
Host: 127.0.0.1:8000
Content-Type: application/json

{"title":"Take out the trash","completed":false,"url":"","order":4}
```

or toggle an item as completed:
```
PATCH /todo/3 HTTP/1.1
Host: 127.0.0.1:8000
Content-Type: application/json

{"completed":true}
```
