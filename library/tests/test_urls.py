from django.test import  SimpleTestCase
from django.urls import reverse , resolve
from library.views import index , get_pdf_detail , get_pdf_preview , search_by_title , get_pdf_by_category

# Create your tests here.

class TestUrls(SimpleTestCase):

    def test_index_urls_is_resolved(self):
        url = reverse('library:index')
        self.assertEquals(resolve(url).func, index)

    def test_get_pdf_detail_urls_is_resolved(self):
        url = reverse('library:book-detail', args=[1])
        self.assertEquals(resolve(url).func, get_pdf_detail)
    
    def test_get_pdf_preview_urls_is_resolved(self):
        url = reverse('library:book-preview', args=[1])
        self.assertEquals(resolve(url).func, get_pdf_preview )
    def test_search_by_title_urls_is_resolved(self):

        url = reverse('library:search-results')
        self.assertEquals(resolve(url).func, search_by_title)

    def test_get_pdf_by_category_urls_is_resolved(self):
        url = reverse('library:book-category', args=[1])
        self.assertEquals(resolve(url).func, get_pdf_by_category)