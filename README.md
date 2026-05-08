# M06T04 - Sticky Notes Application Part 1

This is a complete Django project for the Sticky Notes task.

## Project structure

- `manage.py`
- `sticky_notes/` (project settings, URL config, WSGI)
- `notes/` (app with model, views, URLs, admin, templates, migrations)
- `requirements.txt`

## Setup

1. Create and activate a virtual environment.
2. Install dependencies:
   - `pip install -r requirements.txt`
3. Apply migrations:
   - `python manage.py migrate`
4. Run server:
   - `python manage.py runserver`

## Main routes

- `/` - list notes
- `/add/` - create note
- `/<id>/edit/` - edit note
- `/<id>/delete/` - delete note

## Submission note

Submit this entire `M06T04` folder (or a ZIP of it), excluding the virtual environment folder.
