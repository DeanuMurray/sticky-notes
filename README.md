# Sticky Notes Application

A simple Django web application for creating, viewing, editing, and deleting sticky notes.

## Requirements

- Python 3.10+
- Django 4.2+

## Setup

```bash
python -m venv venv
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Visit **http://127.0.0.1:8000/** in your browser.

## Running Tests

```bash
python manage.py test
```

Expected output: all 10 tests pass with `OK`.

## Features

- View all notes on the home page
- Add a new note (title + content)
- Edit an existing note
- Delete a note with confirmation

## Project Structure

```
M06T05/
├── manage.py
├── requirements.txt
├── sticky_github.txt        # GitHub repository link
├── diagrams/
│   ├── use_case.svg         # Use case diagram
│   ├── class_diagram.svg    # Class diagram
│   └── sequence_diagram.svg # Sequence diagram (Add Note flow)
├── notes/                   # Django app
│   ├── models.py            # Note model
│   ├── views.py             # Class-based views (CRUD)
│   ├── urls.py              # URL patterns
│   ├── tests.py             # Comprehensive unit tests
│   ├── templates/notes/     # HTML templates
│   └── migrations/
└── sticky_notes/            # Django project settings
```

## URL Routes

| URL              | View             | Description           |
|------------------|------------------|-----------------------|
| `/`              | NoteListView     | List all notes        |
| `/add/`          | NoteCreateView   | Add a new note        |
| `/<pk>/edit/`    | NoteUpdateView   | Edit an existing note |
| `/<pk>/delete/`  | NoteDeleteView   | Delete a note         |
