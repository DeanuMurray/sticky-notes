"""Forms for the sticky notes application."""

from django import forms

from .models import Note


class NoteForm(forms.ModelForm):
    """Form for creating and editing sticky notes.

    Fields:
        title: Short title for the note.
        content: Full body text of the note.

    Meta:
        model: Note
        fields: title, content
    """

    class Meta:
        model = Note
        fields = ["title", "content"]
        widgets = {
            "title": forms.TextInput(
                attrs={"placeholder": "Note title"}
            ),
            "content": forms.Textarea(
                attrs={"rows": 6, "placeholder": "Write your note here…"}
            ),
        }
