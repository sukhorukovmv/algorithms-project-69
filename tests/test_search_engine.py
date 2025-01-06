import unittest

from search_engine.search_engine import search
from search_engine.search_engine import reverse_index


class TestSearchFunction(unittest.TestCase):
    def setUp(self):
        # Подготовка тестовых данных
        self.docs = [
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
        query = "pint!"
        expected_result = [
            {
                "id": "doc1",
                "text": "I can't shoot straight unless I've had a pint!",
            },
        ]
        self.assertEqual(search(self.docs, query), expected_result)

    def test_search_found_3(self):
        query = "shoot at me"
        expected_result = [
            {"id": "doc2", "text": "Don't shoot shoot shoot that thing at me."},
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

    def test_reverse_index(self):
        expected_index = {
            "i": {"doc1": {"termFreqInDoc": 1, "lenDoc": 9}},
            "cant": {"doc1": {"termFreqInDoc": 1, "lenDoc": 9}},
            "shoot": {
                "doc1": {"termFreqInDoc": 1, "lenDoc": 9},
                "doc2": {"termFreqInDoc": 3, "lenDoc": 8},
            },
            "straight": {"doc1": {"termFreqInDoc": 1, "lenDoc": 9}},
            "unless": {"doc1": {"termFreqInDoc": 1, "lenDoc": 9}},
            "ive": {"doc1": {"termFreqInDoc": 1, "lenDoc": 9}},
            "had": {"doc1": {"termFreqInDoc": 1, "lenDoc": 9}},
            "a": {"doc1": {"termFreqInDoc": 1, "lenDoc": 9}},
            "pint": {"doc1": {"termFreqInDoc": 1, "lenDoc": 9}},
            "dont": {"doc2": {"termFreqInDoc": 1, "lenDoc": 8}},
            "that": {"doc2": {"termFreqInDoc": 1, "lenDoc": 8}},
            "thing": {"doc2": {"termFreqInDoc": 1, "lenDoc": 8}},
            "at": {"doc2": {"termFreqInDoc": 1, "lenDoc": 8}},
            "me": {"doc2": {"termFreqInDoc": 1, "lenDoc": 8}},
            "im": {"doc3": {"termFreqInDoc": 1, "lenDoc": 3}},
            "your": {"doc3": {"termFreqInDoc": 1, "lenDoc": 3}},
            "shooter": {"doc3": {"termFreqInDoc": 1, "lenDoc": 3}},
        }
        self.assertEqual(reverse_index(self.docs), expected_index)

    def test_fuzzy_search():
        doc1 = "I can't shoot straight unless I've had a pint!"
        doc2 = "Don't shoot shoot shoot that thing at me."
        doc3 = "I'm your shooter."

        docs = [
            {"id": "doc1", "text": doc1},
            {"id": "doc2", "text": doc2},
            {"id": "doc3", "text": doc3},
        ]

        assert search(docs, "shoot at me") == ["doc2", "doc1"]

        doc1 = (
            "I can't shoot shoot shoot shoot shoot straight unless I've had a pint!"
        )
        doc2 = "Don't shoot that thing at me."
        doc3 = "I'm your shooter."

        docs = [
            {"id": "doc1", "text": doc1},
            {"id": "doc2", "text": doc2},
            {"id": "doc3", "text": doc3},
        ]

        assert search(docs, "shoot at me") == ["doc2", "doc1"]

if __name__ == "__main__":
    unittest.main()
