from django.test import TestCase
from django.contrib.auth.models import User
from library.models import Book , Category
from django.conf import settings



class TestModel(TestCase):

    def setUp(self):
        self.book_cover_image_file_path = str(settings.MEDIA_ROOT)+'\cover.jpg'
        self.pdf_url = "https://drive.google.com/file/d/1mHfxyE9AJjTTQujyV-SunANJlrrBG7wx/preview"

        self.book_category = Category.objects.create(
            slug='math-info',
            )

        self.book_author = User.objects.create(
            username='johndoe',
            password='password123',
            email='johndoe@example.com',
            first_name='John',
            last_name='Doe',
            )
        self.book = Book.objects.create(
            pdf_url = "https://drive.google.com/file/d/1mHfxyE9AJjTTQujyV-SunANJlrrBG7wx/view?usp=share_link" ,
            title = 'philosophie',
            slug = "philosophie-I",
            # published = True,
            description = 'mathematique : algebre II ',
            author = self.book_author,
            category = self.book_category,
            )

    def test_book_is_created(self):
        self.assertEqual(self.book.published, False)
        self.assertEqual(self.book.pdf_cover_image.path , self.book_cover_image_file_path)
        self.assertIsNotNone(self.book.author)
        self.assertIsNotNone(self.book.category)
        self.assertIsNotNone(self.book.slug)
        self.assertIsNotNone(self.book.title)
        self.assertIsNotNone(self.book.description)
        self.assertIsNotNone(self.book.pdf_url)


    def test_add_preview_to_google_drive_link(self):
        self.assertEqual(self.book.add_preview_to_google_drive_link(self.book.pdf_url), self.pdf_url)
        self.assertEqual(self.book.add_preview_to_google_drive_link(self.pdf_url), self.pdf_url)


