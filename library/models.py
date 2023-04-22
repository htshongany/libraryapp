from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

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
	description = RichTextField(blank=True , null=True)
	pub_date = models.DateField(auto_now_add=True)
	update_date = models.DateField(auto_now=True)
	pdf_cover_image = models.ImageField(upload_to ='cover-images', default='cover.jpg')


	author = models.ForeignKey(User, on_delete=models.CASCADE)
	category = models.ForeignKey(Category, on_delete=models.CASCADE)

	@staticmethod
	def add_preview_to_google_drive_link(link):
		"""
		add a preview at the end of the google drive link if it does not exist 
		"""
		link = link.split('/')
		if link[-1] != "preview":
			link[-1] = 'preview'
		return "/".join(link)

	def save(self, *args, **kwargs):
		self.pdf_url = self.driver_preview(self.pdf_url)

		super(Book, self).save(*args, **kwargs)

	def __str__(self):
		return self.title