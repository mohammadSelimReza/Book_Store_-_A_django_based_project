from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class CategoryModel(models.Model):
    name = models.CharField(max_length=30,unique=True)
    slug = models.SlugField(max_length=100,unique=True, null=True, blank=True)
    
    def __str__(self) -> str:
        return self.name
    
class BookModel(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField(upload_to='images/')
    borrowing_price = models.DecimalField(max_digits=6,decimal_places=2)
    author_name = models.CharField(max_length=50)
    edition = models.CharField(max_length=50)
    language = models.CharField(max_length=50)
    slug = models.SlugField(max_length=300,unique=True,blank=True)
    category = models.ManyToManyField(CategoryModel)
    
    def __str__(self) -> str:
        return self.title
    
class BookReview(models.Model):
    user = models.ForeignKey(User,related_name='review',on_delete=models.CASCADE)
    book = models.ForeignKey(BookModel,related_name='review',on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)
    comment_body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['created']
        indexes = [
            models.Index(fields=['created']),
        ]
    
    def __str__(self) -> str:
        return f"commented by {self.user.username} on {self.book.title}"