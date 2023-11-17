import string

def remove_punctuation(input_string):
    punctuations = string.punctuation
    result_string = input_string.translate(str.maketrans('', '', punctuations))
    return result_string

input_string = "Hello! How are you doing? This is an example, string!"
cleaned_string = remove_punctuation(input_string)
print("Original String:", input_string)
print("String without punctuation:", cleaned_string)