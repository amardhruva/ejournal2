from django.contrib import admin
from paperauthor.models import Paper, Category, ReviewerEmail, Keyword
from django.core.mail import send_mail
from django.conf import settings
from django.urls import reverse
import textwrap

def send_review_selection_email(request,reviewer, paper):
    subject="You have been selected for review"
    visiturl=request.build_absolute_uri(reverse("paperreviewer:showpaper", kwargs={"paperslug":paper.slug}))
    message=textwrap.dedent("""\
        You have been selected as reviewer by the admin. Good luck
        Paper Title: {}
        Visit {}""").format(paper.title, visiturl)
    
    send_mail(subject, message, settings.ADMIN_EMAIL, [reviewer.email])

# Register your models here.
@admin.register(Paper)
class PaperAdmin(admin.ModelAdmin):
    list_display=('title','author','category','review_status')
    list_filter=('paperreview__review_status', 'category',)
    search_fields=("title",)
    def save_model(self, request, obj, form, change):
        reviewer=obj.reviewer
        if (reviewer is not None) and ("reviewer" in form.changed_data):
            send_review_selection_email(request,reviewer, obj)
        super().save_model(request, obj, form, change)

admin.site.register(Category)
admin.site.register(Keyword)
admin.site.register(ReviewerEmail)
