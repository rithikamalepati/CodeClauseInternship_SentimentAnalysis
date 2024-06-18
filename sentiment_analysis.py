from textblob import TextBlob
def sentiment_analysis(sentence):
    blob = TextBlob(sentence)
    sentiment = blob.sentiment.polarity
    if sentiment > 0:
        return "Positive"
    elif sentiment < 0:
        return "Negative"
    else:
        return "Neutral"
sentence = input("Enter a sentence or review:")
print("sentiment:",sentiment_analysis(sentence))    
      