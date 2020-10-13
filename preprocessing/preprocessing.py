import nltk

#nltk.download('wordnet')

from nltk.stem import PorterStemmer
from nltk.stem import LancasterStemmer
from nltk.stem import WordNetLemmatizer

#create an object of class PorterStemmer
porter = PorterStemmer()

#create an object of class LancasterStemmer
lancaster=LancasterStemmer()

print("---------------Porter Stemmer---------------")
print(porter.stem("papers"))
print(porter.stem("is"))
print(porter.stem("am"))
print(porter.stem("are"))
print(porter.stem("was"))
print(porter.stem("works"))
print(porter.stem("worked"))
print(porter.stem("working"))

print("---------------Lancaster Stemmer---------------")

print(lancaster.stem("papers"))
print(lancaster.stem("is"))
print(lancaster.stem("am"))
print(lancaster.stem("are"))
print(lancaster.stem("was"))
print(lancaster.stem("works"))
print(lancaster.stem("worked"))
print(lancaster.stem("working"))



#create an object of class WordNetLemmatizer
wordnet_lemmatizer = WordNetLemmatizer()

print("---------------WordNet Lemmatizer---------------")

print(wordnet_lemmatizer.lemmatize("papers"))
print(wordnet_lemmatizer.lemmatize("is"))
print(wordnet_lemmatizer.lemmatize("am"))
print(wordnet_lemmatizer.lemmatize("are"))
print(wordnet_lemmatizer.lemmatize("was"))
print(wordnet_lemmatizer.lemmatize("works"))
print(wordnet_lemmatizer.lemmatize("worked"))
print(wordnet_lemmatizer.lemmatize("working"))

print("---------------WordNet Lemmatizer with pos---------------")

print(wordnet_lemmatizer.lemmatize("papers", pos="v"))
print(wordnet_lemmatizer.lemmatize("is", pos="v"))
print(wordnet_lemmatizer.lemmatize("am", pos="v"))
print(wordnet_lemmatizer.lemmatize("are", pos="v"))
print(wordnet_lemmatizer.lemmatize("was", pos="v"))
print(wordnet_lemmatizer.lemmatize("works", pos="v"))
print(wordnet_lemmatizer.lemmatize("worked", pos="v"))
print(wordnet_lemmatizer.lemmatize("working", pos="v"))

