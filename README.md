# M06T04 - Sticky Notes Application Part 1

A Django web application for creating, viewing, editing, and deleting sticky notes, built using the Model-View-Template (MVT) architecture with full CRUD functionality.

## Requirements

- Python 3.10+
- Django 4.2+

## Setup

```bash
python -m venv .venv
# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate

pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Visit **http://127.0.0.1:8000/** in your browser.

## Running Tests

```bash
python manage.py test
```

Expected output: all 12 tests pass with `OK`.

## Features

- View all notes on the home page (newest first)
- Add a new note (title + content)
- Edit an existing note
- Delete a note with confirmation

## Project Structure

```
M06T04/
├── manage.py
├── db.sqlite3
├── requirements.txt
├── sticky_github.txt        # GitHub repository link
├── diagrams/
│   ├── use_case.drawio      # Use case diagram source
│   ├── use_case.svg         # Use case diagram (exported)
│   ├── class.drawio         # Class diagram source
│   ├── class_diagram.svg    # Class diagram (exported)
│   ├── sequence.drawio      # Sequence diagram source
│   └── sequence_diagram.svg # Sequence diagram (exported)
├── notes/                   # Django app
│   ├── models.py            # Note model
│   ├── views.py             # Class-based views (CRUD)
│   ├── forms.py             # NoteForm
│   ├── urls.py              # URL patterns
│   ├── admin.py             # Admin registration
│   ├── tests.py             # Unit tests (12 tests)
│   ├── templates/
│   │   ├── base.html        # Base template
│   │   └── notes/           # Note-specific templates
│   ├── static/notes/        # CSS styles
│   └── migrations/
└── sticky_notes/            # Django project settings
    ├── settings.py
    ├── urls.py
    └── wsgi.py
```

## URL Routes

| URL              | View             | Description           |
|------------------|------------------|-----------------------|
| `/`              | NoteListView     | List all notes        |
| `/add/`          | NoteCreateView   | Add a new note        |
| `/<pk>/edit/`    | NoteUpdateView   | Edit an existing note |
| `/<pk>/delete/`  | NoteDeleteView   | Delete a note         |

