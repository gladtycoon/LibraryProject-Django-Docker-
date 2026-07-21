from django.test import TestCase
from .models import Author, Book, Review

class ModelTests(TestCase):
    """Тесты для моделей приложения."""

    def test_author_str_representation(self):
        """
        Проверяет, что строковое представление автора возвращает
        его полное имя в формате "Имя Фамилия".
        """
        author = Author.objects.create(
            first_name="Лев",
            last_name="Толстой",
            birth_date="1828-09-09"
        )
        self.assertEqual(str(author), "Лев Толстой")

    def test_book_str_representation(self):
        """
        Проверяет, что строковое представление книги возвращает её название.
        """
        author = Author.objects.create(
            first_name="Фёдор",
            last_name="Достоевский",
            birth_date="1821-11-11"
        )
        book = Book.objects.create(
            title="Преступление и наказание",
            publication_date="1866-01-01",
            author=author
        )
        self.assertEqual(str(book), "Преступление и наказание")

    def test_author_book_relationship(self):
        """
        Проверяет, что связь между автором и книгой работает корректно:
        автору можно добавить книги, и они правильно возвращаются через related_name.
        """
        author = Author.objects.create(
            first_name="Михаил",
            last_name="Булгаков",
            birth_date="1891-05-15"
        )
        book1 = Book.objects.create(
            title="Мастер и Маргарита",
            publication_date="1966-01-01",
            author=author
        )
        book2 = Book.objects.create(
            title="Собачье сердце",
            publication_date="1925-01-01",
            author=author
        )

        books_by_author = author.books.all()
        self.assertEqual(books_by_author.count(), 2)
        self.assertIn(book1, books_by_author)
        self.assertIn(book2, books_by_author)