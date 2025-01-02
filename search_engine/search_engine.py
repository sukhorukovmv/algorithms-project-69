def search(docs, query):
    result = []
    for doc in docs:
        if query + " " in doc['text']:
            result.append(doc)

    return result
