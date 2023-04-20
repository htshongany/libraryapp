from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
	slug = models.SlugField(max_length=200, unique=True)

	def __str__(self):
		return self.slug


class Book(models.Model):
	pdf_url = models.URLField(max_length=200, null=False)
	title = models.CharField(max_length=200, null=False)
	slug = models.SlugField(max_length=200, unique=True)
	published = models.BooleanField(default=False)
	description = models.TextField(blank=True , null=True)
	pub_date = models.DateField(auto_now_add=True)
	update_date = models.DateField(auto_now=True)
	pdf_cover_image = models.ImageField(upload_to ='cover-images', default='cover.jpg')


	author = models.ForeignKey(User, on_delete=models.CASCADE)
	category = models.ForeignKey(Category, on_delete=models.CASCADE)

	def __str__(self):
		return self.title