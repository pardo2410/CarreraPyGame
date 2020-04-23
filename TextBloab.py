from textblob import TextBlob
wiki = TextBlob("Python is a high-level, general-purpose programming language.")
print(wiki.translate(to='es'))
print(wiki.translate(to='nl'))
