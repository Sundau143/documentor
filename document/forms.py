from django import forms
from .models import Document
from tinymce.widgets import TinyMCE

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ['name', 'group', 'content']
        widgets = {
            'content': TinyMCE(attrs={'cols': 80, 'rows': 10}),
        }
