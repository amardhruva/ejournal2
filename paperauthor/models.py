import uuid
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from slugger.fields import AutoSlugField
from django.core.exceptions import ValidationError
from django.core.validators import FileExtensionValidator


private_storage = FileSystemStorage(location=settings.SENDFILE_ROOT)


# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=50)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "categories"

class Keyword(models.Model):
    name=models.CharField(max_length=50)
    def __str__(self):
        return self.name

class ReviewerEmail(models.Model):
    email=models.EmailField()
    def __str__(self):
        return self.email

class Paper(models.Model):
    author=models.ForeignKey(User, on_delete=models.CASCADE,
                             limit_choices_to={'groups__name': "author"})
    title=models.CharField(max_length=50)
    description=models.TextField(max_length=1000, blank=True)
    category=models.ForeignKey(Category, on_delete=models.CASCADE)
    keywords=models.ManyToManyField(Keyword, blank=True)
    upload=models.FileField(storage=private_storage,
                             validators=[FileExtensionValidator(["pdf"])])
    reviewer_emails=models.ManyToManyField(ReviewerEmail, blank=True)
    reviewer = models.ForeignKey(User, null=True, blank=True,
                                 default=None, on_delete=models.SET_NULL,
                                 limit_choices_to={'groups__name': "reviewer"},
                                 related_name="reviewpaper")
    slug=AutoSlugField(populate_from="title", unique=True)
    track_id = models.UUIDField(unique=True, default=uuid.uuid4)
    def review_status(self):
        return self.paperreview.get_review_status_display()
    def is_reviewed(self):
        return hasattr(self, "paperreview")
    def __str__(self):
        return self.title
