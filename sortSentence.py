from faker import Faker
import random

faker = Faker()

def sort_sentence_alphabetically(sentence):
    words = sentence.split()
    sorted_words = sorted(words)
    sorted_sentence = ' '.join(sorted_words)
    return sorted_sentence

random_names = [faker.name() for _ in range(100)]


names_string = ', '.join(random_names)

sorted_sentence = sort_sentence_alphabetically(names_string)
print("Original Sentence:", names_string)
print("Sentence sorted alphabetically:", sorted_sentence)
