from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from PIL import Image

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
	description = RichTextField(blank=True , null=True , max_length=4000)
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
		
	def resize_image(self, width=678, height=960):
		"""
		Resizes the book's cover image to the specified width and height.
		"""
		
		image = Image.open(self.pdf_cover_image.path)

		if image.width == 1357 and image.height == 1920:
			pass
		else:
			image = image.resize((width, height))
			image.save(self.pdf_cover_image.path)

	def save(self, *args, **kwargs):
		self.pdf_url = self.add_preview_to_google_drive_link(self.pdf_url)
		super(Book, self).save(*args, **kwargs)
		self.resize_image(1357, 1920)

	def __str__(self):
		return self.title