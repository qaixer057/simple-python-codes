# pip install textblob
from textblob import TextBlob
import time

# call the classifier
def sentiment_texblob(sentence):

    classifier = TextBlob(sentence)
    polarity = classifier.sentiment.polarity
    subjectivity = classifier.sentiment.subjectivity

    return polarity, subjectivity


sentences = [
    "I hate chocolate",
    "My cat is adorable ❤️❤️",
    "I can't wait for Halloween!!!",  # neutral by vader and postive by openai
    "This sucks. I'm bored 😠",
    "I can't stand homework",  # neutral by vader and negative by openai
]

time_start = time.time()
for sentence in sentences:
    result = sentiment_texblob(sentence)
    print("#################################")
    print(sentence)
    print(result)
    print("##################################")
time_end = time.time()
print(f"Time taken: {time_end - time_start} seconds")
