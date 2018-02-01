from django.contrib import admin
from paperreviewer.models import PaperReview, PaperReviewRequest

# Register your models here.
admin.site.register(PaperReview)
admin.site.register(PaperReviewRequest)
