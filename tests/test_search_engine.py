import unittest

from search_engine.search_engine import search


class TestSearchFunction(unittest.TestCase):
    def setUp(self):
        # Подготовка тестовых данных
        self.docs = [
            # {"id": "doc1", "text": "This is a test document."},
            # {"id": "doc2", "text": "Another document for testing."},
            # {"id": "doc3", "text": "Testing the search function."},
            # {
            #     "id": "doc4",
            #     "text": "This document does not contain the search string.",
            # },
            # {"id": "doc5", "text": "Search within the document."},
            # {"id": "doc6", "text": "Search within the document test!"},
            {
                "id": "doc1",
                "text": "I can't shoot straight unless I've had a pint!",
            },
            {"id": "doc2", "text": "Don't shoot shoot shoot that thing at me."},
            {"id": "doc3", "text": "I'm your shooter."},
        ]

    def test_search_found(self):
        # Тест на успешный поиск
        query = "shoot"
        expected_result = [
            {"id": "doc2", "text": "Don't shoot shoot shoot that thing at me."},
            {
                "id": "doc1",
                "text": "I can't shoot straight unless I've had a pint!",
            },
        ]
        self.assertEqual(search(self.docs, query), expected_result)

    def test_search_found_2(self):
        # Тест на успешный поиск
        query = "pint!"
        expected_result = [
            {
                "id": "doc1",
                "text": "I can't shoot straight unless I've had a pint!",
            },
        ]
        self.assertEqual(search(self.docs, query), expected_result)

    def test_search_not_found(self):
        # Тест на случай, когда строка не найдена
        query = "not found"
        expected_result = []
        self.assertEqual(search(self.docs, query), expected_result)
    
    def test_search_empty_docs(self):
        # Тест на пустой список документов
        query = "test"
        expected_result = []
        self.assertEqual(search([], query), expected_result)
    
    def test_search_empty_query(self):
        # Тест на пустую строку запроса
        query = ""
        expected_result = (
            self.docs
        )  # Если запрос пустой, должны вернуть все документы
        self.assertEqual(search(self.docs, query), expected_result)
    
    def test_search_case_sensitive(self):
        # Тест на чувствительность к регистру
        query = "Test"
        expected_result = []
        self.assertEqual(search(self.docs, query), expected_result)


if __name__ == "__main__":
    unittest.main()
