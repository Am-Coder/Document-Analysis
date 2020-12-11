# pip install keybert
from keybert import KeyBERT
from DatasetHandler import DataHandler

model = KeyBERT('distilbert-base-nli-mean-tokens')

dh = DataHandler("Data.xlsx")
df = dh.get_dataframe()
extracted_keywords = []
for abs in df['Abstract']:
    keywords = model.extract_keywords(abs)
    extracted_keywords.append(keywords)



# doc = """
#          Supervised learning is the machine learning task of learning a function that
#          maps an input to an output based on example input-output pairs.[1] It infers a
#          function from labeled training data consisting of a set of training examples.[2]
#          In supervised learning, each example is a pair consisting of an input object
#          (typically a vector) and a desired output value (also called the supervisory signal). 
#          A supervised learning algorithm analyzes the training data and produces an inferred function, 
#          which can be used for mapping new examples. An optimal scenario will allow for the 
#          algorithm to correctly determine the class labels for unseen instances. This requires 
#          the learning algorithm to generalize from the training data to unseen situations in a 
#          'reasonable' way (see inductive bias).
#       """
# keywords = model.extract_keywords(doc)

# #Here set keyphrase_length to set the length of the resulting keywords/keyphrases:

# model.extract_keywords(doc, keyphrase_ngram_range=(1, 1), stop_words=None)
# """ output 
#  ['learning', 
#  'training', 
#  'algorithm', 
#  'class', 
#  'mapping']
#  """
 
# #To extract keyphrases, simply set keyphrase_length to 2 or higher depending on the number of words you would like in the resulting keyphrases:

# model.extract_keywords(doc, keyphrase_ngram_range=(1, 2), stop_words=None)
# """ output
# ['learning algorithm',
#  'learning machine',
#  'machine learning',
#  'supervised learning',
#  'learning function']
# """
 
# #To diversity the results, we take the 2 x top_n most similar words/phrases to the document. Then, we take all top_n combinations from the 2 x top_n words and extract the 
# #combination that are the least similar to each other by cosine similarity.

# model.extract_keywords(doc, keyphrase_ngram_range=(3, 3), stop_words='english', 
#                            use_maxsum=True, nr_candidates=20, top_n=5)
# """ output
# ['set training examples',
#  'generalize training data',
#  'requires learning algorithm',
#  'superivsed learning algorithm',
#  'learning machine learning']
#  """
