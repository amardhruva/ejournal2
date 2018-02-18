from django.contrib import admin

from paperauthor.models import Paper
from paperreviewer.models import PaperReview, PaperReviewRequest


# Register your models here.
@admin.register(PaperReview)
class PaperReviewAdmin(admin.ModelAdmin):
    list_display = ("paper", "review_status", "review_complete")
    search_fields = ("paper__title",)
    actions = ["complete_review","undo_complete_review"]
    def complete_review(self, request, queryset):
        Paper.objects.filter(paperreview__in=queryset).update(review_complete=True)
    def undo_complete_review(self, request, queryset):
        Paper.objects.filter(paperreview__in=queryset).update(review_complete=False)

@admin.register(PaperReviewRequest)
class PaperReviewRequestAdmin(admin.ModelAdmin):
    exclude = ('status',)
    list_display = ('paper', 'reviewer', 'status')
