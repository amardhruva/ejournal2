from django.contrib import admin
from paperauthor.models import Paper, Category, ReviewerEmail, Keyword

# Register your models here.
@admin.register(Paper)
class PaperAdmin(admin.ModelAdmin):
    list_display=('title','author','category','review_status')
    list_filter=('paperreview__review_status', 'category',)
    search_fields=("title",)

admin.site.register(Category)
admin.site.register(Keyword)
admin.site.register(ReviewerEmail)
