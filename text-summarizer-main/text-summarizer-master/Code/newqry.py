import os
import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer

# Download NLTK resources
nltk.download('punkt')
nltk.download('stopwords')

# Initialize NLTK components
stop_words = set(stopwords.words('english'))
stemmer = SnowballStemmer('english')

# Define function to preprocess text
def preprocess_text(text):
    sentences = sent_tokenize(text)
    preprocessed_sentences = []
    for sentence in sentences:
        words = word_tokenize(sentence)
        preprocessed_words = [stemmer.stem(word.lower()) for word in words if word.isalpha() and word.lower() not in stop_words]
        preprocessed_sentence = ' '.join(preprocessed_words)
        preprocessed_sentences.append(preprocessed_sentence)
    return preprocessed_sentences

# Define function to read text from file
def read_text_from_file(file_path):
    with open(file_path, 'r') as file:
        text = file.read()
    return text

# Define function to generate summary
def generate_summary(text):
    preprocessed_sentences = preprocess_text(text)
    summary = ' '.join(preprocessed_sentences)
    return summary

# Define file paths
current_directory = os.path.dirname(os.path.abspath(__file__))
data_directory = os.path.join(current_directory, '..', 'Data')
file_paths = [
    os.path.join(data_directory, 'gift-of-magi.txt'),
    os.path.join(data_directory, 'the-skylight-room.txt'),
    os.path.join(data_directory, 'the-cactus.txt')
]

# Process each file
for file_path in file_paths:
    if os.path.exists(file_path):
        text = read_text_from_file(file_path)
        summary = generate_summary(text)
        print("Summary for", file_path, ":\n", summary)
        print()
    else:
        print("File not found:", file_path)
