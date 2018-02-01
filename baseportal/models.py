from django.db import models
from django.core.validators import FileExtensionValidator

# Create your models here.
class PublishedJournal(models.Model):
    name=models.CharField(max_length=50)
    description=models.TextField(blank=True)
    published_date=models.DateField()
    upload=models.FileField(validators=[FileExtensionValidator(["pdf"])])
    preview_image=models.ImageField()
    def __str__(self):
        return self.name
