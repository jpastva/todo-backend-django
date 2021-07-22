# todo-backend-django

This is a simple backend for a To Do application using the Django framework.

New features added include:

- Option to display only completed (http://127.0.0.1:8000/todos/done) or pending (http://127.0.0.1:8000/todos/pending) tasks
- 'created' field added to ToDoItem model, to allow tasks to be sorted by oldest creation date (http://127.0.0.1:8000/todos/oldest) to focus on clearing out the cobwebs

The app included an 'order' field, which was utilized for the default sort criteria for the list. This is problematic, as it can be difficult to know a preferred list order as a to do list grows, and there is currently no way to re-order existing tasks. However, it was maintained as part of the original app functionality.

## Installation

1. Clone the repository to a local directory.
2. Create virtual environment to store dependencies.
3. Install requirements<br />
   `pip install -r requirements.txt`
4. Initialize database<br />
   `python manage.py makemigrations'<br /> 'python manage.py migrate`
5. Run local server to view at http://127.0.0.1:8000/<br />
   `python manage.py runserver`
