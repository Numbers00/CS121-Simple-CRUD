from django.core.files import File
from django.db import models

class Author(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    country_of_origin = models.CharField(max_length=255)
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)
    slug = models.SlugField()

    class Meta:
        ordering = ('first_name',)
    
    def __str__(self):
        return self.first_name

    def get_image(self):
        if self.image:
            return 'http://127.0.0.1:8000' + self.image.url
        return ''
    
    def get_absolute_url(self):
        return f'/{self.slug}/'

class Book(models.Model):
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)
    book_title = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    number_of_pages = models.IntegerField()
    language = models.CharField(max_length=255)
    slug = models.SlugField()

    class Meta:
        ordering = ('-book_title',)
    
    def __str__(self):
        return self.book_title
    
    def get_absolute_url(self):
        return f'/{self.author.slug}/{self.slug}/'