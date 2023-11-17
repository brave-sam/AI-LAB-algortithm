import nltk
import random
from nltk.corpus import movie_reviews

nltk.download('movie_reviews')
nltk.download('punkt')


documents = [(list(movie_reviews.words(fileid)), category)
             for category in movie_reviews.categories()
             for fileid in movie_reviews.fileids(category)]

random.shuffle(documents)

all_words = []
for w in movie_reviews.words():
    all_words.append(w.lower())

all_words = nltk.FreqDist(all_words)

word_features = list(all_words.keys())[:3000]  

def document_features(document):
    words = set(document)
    features = {}
    for word in word_features:
        features[word] = (word in words)
    return features

featuresets = [(document_features(d), c) for (d,c) in documents]

classifier = nltk.NaiveBayesClassifier.train(featuresets)


sentence = '''Python is a high-level, general-purpose programming language. Its design philosophy emphasizes code readability with the use of significant indentation.[32]

Python is dynamically typed and garbage-collected. It supports multiple programming paradigms, including structured (particularly procedural), object-oriented and functional programming. It is often described as a "batteries included" language due to its comprehensive standard library.[33][34]

Guido van Rossum began working on Python in the late 1980s as a successor to the ABC programming language and first released it in 1991 as Python 0.9.0.[35] Python 2.0 was released in 2000. Python 3.0, released in 2008, was a major revision not completely backward-compatible with earlier versions. Python 2.7.18, released in 2020, was the last release of Python 2.[36]

Python consistently ranks as one of the most popular programming languages'''

features = document_features(sentence.split())
classification = classifier.classify(features)
print(f"Sentence: {sentence}")
print(f"Classification: {classification}")
