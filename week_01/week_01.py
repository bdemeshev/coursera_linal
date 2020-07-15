# TF-IDF векторизация документов

documents = [
"привет линейная",
"привет дорогая линейная алгебра"
]

from sklearn.feature_extraction.text import TfidfVectorizer
tfidf_vectorizer = TfidfVectorizer()
tfidf_matrix = tfidf_vectorizer.fit_transform(documents)

tfidf_array = tfidf_matrix.toarray()
tfidf_array[0, :]
tfidf_array[1, :]
