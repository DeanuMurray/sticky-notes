from django.test import TestCase
from django.urls import reverse

from .models import Note


class NoteViewsTests(TestCase):
    def test_note_list_page_loads(self):
        response = self.client.get(reverse("notes:list"))
        self.assertEqual(response.status_code, 200)

    def test_create_note(self):
        response = self.client.post(
            reverse("notes:add"),
            {"title": "Test", "content": "Sticky note"},
            follow=True,
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Note.objects.count(), 1)
