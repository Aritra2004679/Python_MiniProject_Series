import nltk
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('stopwords')

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from textblob import TextBlob

#Read sentence from a file
with open("input.txt","r") as file:
    sentences = file.readlines()
stop_words = set(stopwords.words('english'))

print("SENTIMENT ANALYSIS USING NLP")
print("="*60)

for i,sentence in enumerate(sentences,start = 1):
    sentence = sentence.strip()

    #Tokenization
    tokens = word_tokenize(sentence)

    #Stopword Removal
    filtered_tokens = [
    word for word in tokens
    if word.lower() not in stop_words and word.isalpha()]
    processed_text = " ".join(filtered_tokens)

    #Sentiment Analysis
    blob = TextBlob(processed_text)
    polarity = blob.sentiment.polarity

    if polarity > 0:
        sentiment = "Positive"
    elif polarity < 0:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"

    print("Tokens:", tokens)
    print("After Stopword Removal:", processed_text)
    print("Polarity:", polarity)
    print("Sentiment:", sentiment)

print("\nAnalysis Completed.")