import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
nltk.download('averaged_perceptron_tagger')
# from nltk.stem import WordNetLemmatizer
# from nltk.stem import PorterStemmer
# from nltk.stem import LancasterStemmer
# from nltk.stem import SnowballStemmer
# from nltk.stem import RegexpStemmer
# from nltk.stem import IsriStemmer
# from nltk.stem import RSLPStemmer

english_stop_word = set(stopwords.words('english'))
# lemmatizer = WordNetLemmatizer()
# stemmer = PorterStemmer()
# stemmer2 = LancasterStemmer()
# stemmer3 = SnowballStemmer('english')
# # stemmer4 = RegexpStemmer('ing$',)
# stemmer5 = IsriStemmer()
# stemmer6 = RSLPStemmer()
sentence = '''
Python is a high-level, general-purpose programming language. Its design philosophy emphasizes code readability with the use of significant indentation.[32]

Python is dynamically typed and garbage-collected. It supports multiple programming paradigms, including structured (particularly procedural), object-oriented and functional programming. It is often described as a "batteries included" language due to its comprehensive standard library.[33][34]

Guido van Rossum began working on Python in the late 1980s as a successor to the ABC programming language and first released it in 1991 as Python 0.9.0.[35] Python 2.0 was released in 2000. Python 3.0, released in 2008, was a major revision not completely backward-compatible with earlier versions. Python 2.7.18, released in 2020, was the last release of Python 2.[36]

Python consistently ranks as one of the most popular programming languages.
'''
tokens = word_tokenize(sentence)
words=[w for w in tokens if w not in english_stop_word]
tagged = nltk.pos_tag(words)
for i in tagged:
  print(i)