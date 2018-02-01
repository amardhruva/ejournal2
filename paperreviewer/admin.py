from django.contrib import admin
from paperreviewer.models import PaperReview, PaperReviewRequest

# Register your models here.
@admin.register(PaperReview)
class PaperReviewAdmin(admin.ModelAdmin):
    list_display=["paper","review_status"]
admin.site.register(PaperReviewRequest)
