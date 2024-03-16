import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords

# Initialize NLTK
nltk.download('punkt')
nltk.download('stopwords')

# Function to preprocess text
def preprocess_text(text):
    # Tokenize text into sentences
    sentences = sent_tokenize(text)
    
    # Tokenize each sentence into words and remove stopwords
    tokens_list = [word_tokenize(sentence) for sentence in sentences]
    filtered_tokens = [[word.lower() for word in tokens if word.isalpha() and word.lower() not in stopwords.words('english')] for tokens in tokens_list]
    
    return filtered_tokens

# Function to generate summary from list of tokens
def generate_summary(tokens_list):
    # Join tokens back into sentences
    sentences = [' '.join(tokens) for tokens in tokens_list]
    
    # Return concatenated sentences as summary
    return ' '.join(sentences)

# Specify the full path to each text file
gift_of_magi_path = 'Data/gift-of-magi.txt'
the_skylight_room_path = 'Data/the-skylight-room.txt'
the_cactus_path = 'Data/the-cactus.txt'

# Open and read the text files
with open(gift_of_magi_path, 'r') as f1:
    text1 = f1.read()
with open(the_skylight_room_path, 'r') as f2:
    text2 = f2.read()
with open(the_cactus_path, 'r') as f3:
    text3 = f3.read()

# Preprocess text
tokens1 = preprocess_text(text1)
tokens2 = preprocess_text(text2)
tokens3 = preprocess_text(text3)

# Generate summary
summary1 = generate_summary(tokens1)
summary2 = generate_summary(tokens2)
summary3 = generate_summary(tokens3)

# Print summaries
print('gift of magi:\n', summary1)
print('\n\nthe skylight room:\n', summary2)
print('\n\nthe cactus:\n', summary3)
