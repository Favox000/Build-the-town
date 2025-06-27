from django.db import models
from django.utils.text import slugify
# Create your models here.
class BlogPost(models.Model):
    title = models.CharField(max_length=200, verbose_name="Název")
    trailer = models.CharField(max_length=1500, verbose_name="Upoutávka")
    text = models.TextField(verbose_name="Text příspěvku")
    author = models.CharField(max_length=100, verbose_name="Jméno autora")
    visible = models.BooleanField(default=True, verbose_name="Viditelný")
    issue_date = models.DateTimeField(verbose_name="Čas vydání")
    reading_time = models.PositiveIntegerField(verbose_name="Čas čtení")
    image = models.ImageField(upload_to="blog_app/cover_images", blank=True, null=True, verbose_name="Obrázek")
    slug = models.SlugField(unique=True, max_length=200, verbose_name="URL název", blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.title} ({self.author}, {self.issue_date})"