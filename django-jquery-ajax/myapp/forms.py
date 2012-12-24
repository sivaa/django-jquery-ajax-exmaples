from django import forms
from ckeditor.widgets import CKEditorWidget

from myapp.models import Post

class PostForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget())
    class Meta:
        model = Post