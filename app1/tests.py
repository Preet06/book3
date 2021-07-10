from django.test import TestCase
from django.test import TestCase
from django.urls import reverse
# Create your tests here.
from .models import Book

class app1Tests(TestCase):

    def setUp(self):
        self.book = Book.objects.create(
        Book_Name='A good title',
        Author='Nice body content',
        Genre='Genre',
        Language='Language')


  

    def test_book_create_view(self):
        response = self.client.post(reverse('add'), {
        'Book_Name': 'New Book_Name',
        'Author': 'New Author',
        'Genre': 'New Genre',
        'Language': 'New Language'})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Book.objects.last().Book_Name, 'New Book_Name')
        self.assertEqual(Book.objects.last().Author, 'New Author')
        self.assertEqual(Book.objects.last().Genre, 'New Genre')
        self.assertEqual(Book.objects.last().Language, 'New Language')

    def test_book_detail_view(self):
        response = self.client.get('/post/1/')
        no_response = self.client.get('/post/100000/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'A good title')
        self.assertTemplateUsed(response, 'post_detail.html')      







