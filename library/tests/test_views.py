from django.test import TestCase , Client
from django.urls import reverse
from library.models import Book , Category
from django.contrib.auth.models import User

class TestViews(TestCase):

    def setUp(self):

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
            slug = "philosophie",
			published = True,
			description = 'mathematique : algebre II ',
            author = self.book_author,
            category = self.book_category,
			)

        self.client = Client()
        self.index_url = reverse('library:index')
        self.search_url = reverse('library:search-results')
        self.book_detail_url = reverse('library:book-detail',args=[self.book.slug])
        self.book_preview_url = reverse('library:book-preview', args=[self.book.slug])
        self.Book_category_url = reverse('library:book-category',args=[self.book_category.slug])


    def test_library_index_get(self):
        response = self.client.get(self.index_url)
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response, 'library/index.html')
        self.assertEquals(response.context['page_obj'].number, response.context['page_obj'].paginator.page(1).number)

    def test_library_search_by_title_get(self):
        response = self.client.get(self.search_url)
        self.assertEquals(response.status_code , 200)
        self.assertTemplateUsed('library/search-results.html')

    def test_library_get_pdf_detail_get(self):
        response = self.client.get(self.book_detail_url)
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed('library/book-view.html')

    def test_library_get_pdf_preview_get(self):
        response = self.client.get(self.book_preview_url)
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed('library/book-preview.html')

    def test_library_get_pdf_by_category_get(self):
        response = self.client.get(self.Book_category_url)
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed('library/book-category.html')