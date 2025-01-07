import math
import re


def search(docs, query):
    if query == "":
        return docs

    term_query = list(
        map(lambda x: "".join(re.findall(r"\w+", x)).lower(), query.split())
    )

    index = build_reverse_index(docs)
    tf_idf_dict = {}
    for term in term_query:  # проходим по массиву слов в запросе
        # проходим по всем документов где встретилось слово
        for doc_id in index.get(term, []):
            # считаем tf, idf, tf_idf для каждого слова в документе
            lenDoc = index[term][doc_id]["lenDoc"]
            termFreqInDoc = index[term][doc_id]["termFreqInDoc"]
            tf = termFreqInDoc / lenDoc

            termCount = len(index[term])
            docsCount = len(docs)
            idf = math.log2(1 + (docsCount - termCount + 1) / (termCount + 0.5))

            tf_idf = tf * idf

            if doc_id in tf_idf_dict:
                # если в документе встретилось несколько слов из запроса,
                # то все tf_idf для каждого слова суммируются для этого дока
                tf_idf_dict[doc_id] = tf_idf_dict[doc_id] + tf_idf
            else:
                tf_idf_dict[doc_id] = tf_idf

    sorted_dict = dict(
        sorted(tf_idf_dict.items(), key=lambda x: x[1], reverse=True)
    )
    return list(sorted_dict.keys())
    # return sorted(
    #     [doc for doc in docs if doc["id"] in tf_idf_dict.keys()],
    #     key=lambda doc: tf_idf_dict[doc["id"]],
    #     reverse=True,
    # )


def build_reverse_index(docs):
    index = {}
    for doc in docs:
        words = doc["text"].split()

        for word in words:
            term = "".join(
                re.findall(r"\w+", word)
            ).lower()  # term обработанное слово

            if term in index:
                if doc["id"] in index[term]:
                    index[term][doc["id"]]["termFreqInDoc"] += 1
                    index[term][doc["id"]]["lenDoc"] = len(doc["text"].split())
                else:
                    index[term][doc["id"]] = {
                        "termFreqInDoc": 1,
                        "lenDoc": len(doc["text"].split()),
                    }
            else:
                index[term] = {
                    doc["id"]: {
                        "termFreqInDoc": 1,
                        "lenDoc": len(doc["text"].split()),
                    }
                }

    return index
