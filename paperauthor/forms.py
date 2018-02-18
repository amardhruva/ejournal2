from django.forms.models import ModelForm
from paperauthor.models import Paper


class PaperForm(ModelForm):
    class Meta:
        model=Paper
        fields=('title', 'abstract', 'category', 'upload', 'keywords')