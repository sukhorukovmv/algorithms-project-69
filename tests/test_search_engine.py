import unittest
import os

from search_engine.search_engine import search
from search_engine.search_engine import build_reverse_index


class TestSearchFunction(unittest.TestCase):
    def setUp(self):
        self.docs = [
            {
                "id": "doc1",
                "text": "I can't shoot straight unless I've had a pint!",
            },
            {"id": "doc2", "text": "Don't shoot shoot shoot that thing at me."},
            {"id": "doc3", "text": "I'm your shooter."},
        ]

    # def test_search_found(self):
    #     self.assertEqual(search(self.docs, "shoot"), ["doc2", "doc1"])
    #
    # def test_search_found_2(self):
    #     self.assertEqual(search(self.docs, "pint!"), ["doc1"])
    #
    # def test_search_found_3(self):
    #     self.assertEqual(search(self.docs, "shoot at me"), ["doc2", "doc1"])
    #
    # def test_search_not_found(self):
    #     self.assertEqual(search(self.docs, "not found"), [])
    #
    # def test_search_empty_docs(self):
    #     self.assertEqual(search([], "test"), [])
    #
    # def test_search_empty_query(self):
    #     self.assertEqual(search(self.docs, ""), self.docs)
    #
    # def test_search_case_sensitive(self):
    #     self.assertEqual(search(self.docs, "Test"), [])
    #
    # def test_reverse_index(self):
    #     expected_index = {
    #         "i": {"doc1": {"termFreqInDoc": 1, "lenDoc": 9}},
    #         "cant": {"doc1": {"termFreqInDoc": 1, "lenDoc": 9}},
    #         "shoot": {
    #             "doc1": {"termFreqInDoc": 1, "lenDoc": 9},
    #             "doc2": {"termFreqInDoc": 3, "lenDoc": 8},
    #         },
    #         "straight": {"doc1": {"termFreqInDoc": 1, "lenDoc": 9}},
    #         "unless": {"doc1": {"termFreqInDoc": 1, "lenDoc": 9}},
    #         "ive": {"doc1": {"termFreqInDoc": 1, "lenDoc": 9}},
    #         "had": {"doc1": {"termFreqInDoc": 1, "lenDoc": 9}},
    #         "a": {"doc1": {"termFreqInDoc": 1, "lenDoc": 9}},
    #         "pint": {"doc1": {"termFreqInDoc": 1, "lenDoc": 9}},
    #         "dont": {"doc2": {"termFreqInDoc": 1, "lenDoc": 8}},
    #         "that": {"doc2": {"termFreqInDoc": 1, "lenDoc": 8}},
    #         "thing": {"doc2": {"termFreqInDoc": 1, "lenDoc": 8}},
    #         "at": {"doc2": {"termFreqInDoc": 1, "lenDoc": 8}},
    #         "me": {"doc2": {"termFreqInDoc": 1, "lenDoc": 8}},
    #         "im": {"doc3": {"termFreqInDoc": 1, "lenDoc": 3}},
    #         "your": {"doc3": {"termFreqInDoc": 1, "lenDoc": 3}},
    #         "shooter": {"doc3": {"termFreqInDoc": 1, "lenDoc": 3}},
    #     }
    #     self.assertEqual(build_reverse_index(self.docs), expected_index)

    def test_simple_search(self):
        expectedDocIds = [
            "garbage_patch_NG",
            "garbage_patch_ocean_clean",
            "garbage_patch_wiki",
        ]

        dir_path = "./tests/test_data/"
        docs = []
        for file_name in expectedDocIds:
            with open(os.path.join(dir_path, file_name), "r") as f:
                file_text = f.read()

            docs.append({"id": file_name, "text": file_text})

        self.assertEqual(search(docs, "trash island"), expectedDocIds)


# test('simple search', async () => {
#   const searchText = 'trash island';
#   const docIds = ['garbage_patch_NG', 'garbage_patch_ocean_clean', 'garbage_patch_wiki'];
#
#   const documentsPaths = await Promise.all(docIds.map(getDocumentText));
#   const result = await solution(documentsPaths, searchText);
#
#   expect(result).toEqual(docIds);
# });


if __name__ == "__main__":
    unittest.main()
