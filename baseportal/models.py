from django.db import models
from django.core.validators import FileExtensionValidator
from slugger.fields import AutoSlugField

# Create your models here.
class PublishedJournal(models.Model):
    name=models.CharField(max_length=50)
    description=models.TextField(blank=True)
    published_date=models.DateField()
    upload=models.FileField(validators=[FileExtensionValidator(["pdf"])])
    preview_image=models.ImageField()
    slug=AutoSlugField(populate_from="name", unique=True, editable=False)
    def __str__(self):
        return self.name
