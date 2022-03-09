from django import forms
from .models import Post
from ckeditor.widgets import CKEditorWidget

class PostForm(forms.ModelForm):
    body = forms.CharField(widget=CKEditorWidget(), label='Text editor')
    class Meta:
        model = Post
        fields=('body',)