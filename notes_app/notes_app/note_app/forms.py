from django import forms

from notes_app.common.common import DisabledFormMixin
from notes_app.note_app.models import Note


class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = '__all__'

        labels = {
            'image_url': 'Link to Image',
        }


class DeleteNoteForm(NoteForm, DisabledFormMixin):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        DisabledFormMixin.__init__(self)