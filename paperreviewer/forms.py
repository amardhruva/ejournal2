from django.forms.models import ModelForm
from paperreviewer.models import PaperReview, PaperReviewRequest


class ReviewPaperForm(ModelForm):
    class Meta:
        model=PaperReview
        fields=("review_status", "comments_to_author", "comments_to_editor")

class ReviewRequestForm(ModelForm):
    class Meta:
        model=PaperReviewRequest
        fields=('status',)
