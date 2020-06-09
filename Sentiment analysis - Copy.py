def RPAChallenge(message):
    from textblob import TextBlob
    line = message
    blob = TextBlob(line)
    print(blob.sentiment)
    print()



m = "I love tea"

RPAChallenge(m)
