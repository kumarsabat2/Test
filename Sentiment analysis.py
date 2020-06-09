def RPAChallenge(text):
    from textblob import TextBlob
    from textblob.sentiments import NaiveBayesAnalyzer
    import nltk
    sent = TextBlob(text)
    polarity      = sent.sentiment.polarity
    subjectivity = sent.sentiment.subjectivity
    sent = TextBlob(text,analyzer = NaiveBayesAnalyzer())
    classification = sent.sentiment.classification
    positive      = sent.sentiment.p_pos
    negative      = sent.sentiment.p_neg
    print("Feedback is :" + classification,positive,negative)
    
  



m = "Awesome product"

RPAChallenge(m)
