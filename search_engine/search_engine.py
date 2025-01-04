import re


def search(docs, query):
    if query == "":
        return docs

    term_query = list(
        map(lambda x: "".join(re.findall(r"\w+", x)).lower(), query.split())
    )

    print("term_query")
    print(term_query)

    result = []
    count = 0
    for doc in docs:
        word_count = {}
        for token in doc["text"].split():  # token необработанное слово
            term = "".join(
                re.findall(r"\w+", token)
            ).lower()  # term обработанное слово

            if term in term_query:
                word_count[term] = term
                count += 1

        if count != 0:
            result.append(
                {
                    "word_count": len(word_count),
                    "count": count,
                    "doc": doc,
                },
            )
            count = 0
            word_count.clear()

    print(result)
    result.sort(key=lambda x: (x["word_count"], x["count"]), reverse=True)
    print(result)
    return [item["doc"] for item in result]
