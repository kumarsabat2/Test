def RPAChallenge(message):
    from textblob import TextBlob
    line = message
    blob = TextBlob(line)
    print(blob.sentiment)



m = "I love tea"

RPAChallenge(m)
