import nltk
from nltk.corpus import stopwords


nltk.download('stopwords')

def remove_stopwords(file_name):
    with open(file_name, 'r') as file:
        passage = file.read()

    words = nltk.word_tokenize(passage)

    stop_words = set(stopwords.words('english'))
    filtered_words = [word for word in words if word.lower() not in stop_words]

    filtered_passage = ' '.join(filtered_words)

    return filtered_passage
  
file_path = 'C:\\AI LAB algortithm\\NLTK\\text.txt'

filtered_text = remove_stopwords(file_path)

print("Filtered text without stopwords:")
print(filtered_text)
