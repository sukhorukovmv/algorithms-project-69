import re


def search(docs, query):
    if query == "":
        return docs
    term_query = "".join(re.findall(r"\w+", query)).lower()

    result = []
    rel_count = 0
    for doc in docs:
        for token in doc["text"].split():  # token необработанное слово
            term = "".join(
                re.findall(r"\w+", token)
            ).lower()  # term обработанное слово

            if term_query == term:
                rel_count += 1
                # result.append(doc)

        if rel_count != 0:
            result.append(
                {
                    "rel_count": rel_count,
                    "doc": doc,
                },
            )
            rel_count = 0

    result.sort(key=lambda x: x["rel_count"], reverse=True)
    print(result)
    return [item["doc"] for item in result]
