from django.test import TestCase
from django.urls import reverse

from .models import Note


class NoteModelTests(TestCase):
    """Tests for the Note model."""

    def test_note_str_returns_title(self):
        note = Note(title="Buy milk", content="Semi-skimmed")
        self.assertEqual(str(note), "Buy milk")

    def test_note_creation_saves_fields(self):
        Note.objects.create(title="Meeting notes", content="Review Q1 results")
        note = Note.objects.get(title="Meeting notes")
        self.assertEqual(note.content, "Review Q1 results")
        self.assertIsNotNone(note.created_at)

    def test_notes_ordered_newest_first(self):
        from django.utils import timezone
        import datetime
        old = Note.objects.create(title="Old note", content="First")
        new = Note.objects.create(title="New note", content="Second")
        old.created_at = timezone.now() - datetime.timedelta(days=1)
        old.save()
        notes = list(Note.objects.all())
        self.assertEqual(notes[0].title, "New note")
        self.assertEqual(notes[1].title, "Old note")


class NoteListViewTests(TestCase):
    """Tests for the note list (home) view."""

    def test_list_view_returns_200(self):
        response = self.client.get(reverse("notes:list"))
        self.assertEqual(response.status_code, 200)

    def test_list_view_shows_existing_notes(self):
        Note.objects.create(title="Visible note", content="Some content")
        response = self.client.get(reverse("notes:list"))
        self.assertContains(response, "Visible note")

    def test_list_view_shows_empty_message_when_no_notes(self):
        response = self.client.get(reverse("notes:list"))
        self.assertContains(response, "No notes yet")


class NoteCreateViewTests(TestCase):
    """Tests for creating a new note."""

    def test_create_view_get_loads_form(self):
        response = self.client.get(reverse("notes:add"))
        self.assertEqual(response.status_code, 200)

    def test_create_note_post_saves_and_redirects(self):
        response = self.client.post(
            reverse("notes:add"),
            {"title": "New note", "content": "Hello world"},
            follow=True,
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Note.objects.count(), 1)
        self.assertEqual(Note.objects.first().title, "New note")

    def test_create_note_with_empty_title_shows_error(self):
        response = self.client.post(
            reverse("notes:add"),
            {"title": "", "content": "Some content"},
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Note.objects.count(), 0)


class NoteUpdateViewTests(TestCase):
    """Tests for editing an existing note."""

    def setUp(self):
        self.note = Note.objects.create(title="Original", content="Old content")

    def test_update_view_get_loads_form(self):
        response = self.client.get(reverse("notes:edit", args=[self.note.pk]))
        self.assertEqual(response.status_code, 200)

    def test_update_note_post_changes_title(self):
        self.client.post(
            reverse("notes:edit", args=[self.note.pk]),
            {"title": "Updated title", "content": "New content"},
        )
        self.note.refresh_from_db()
        self.assertEqual(self.note.title, "Updated title")


class NoteDeleteViewTests(TestCase):
    """Tests for deleting a note."""

    def setUp(self):
        self.note = Note.objects.create(title="To delete", content="Gone soon")

    def test_delete_view_get_shows_confirmation(self):
        response = self.client.get(reverse("notes:delete", args=[self.note.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "To delete")

    def test_delete_note_post_removes_note(self):
        self.client.post(reverse("notes:delete", args=[self.note.pk]))
        self.assertEqual(Note.objects.count(), 0)
