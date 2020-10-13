import nltk


#nltk.download('punkt')


text = """With the ever-increasing amount of data being accessible over the web, the need to make recommendation systems more and more accurate is pressing. The approaches involving the semantic comparison of documents tend to become infeasible when querying a very large amount of data. This problem is not just restricted to a few domains but is slowly and gradually becoming a part of almost all the domains involving look-up for bulk data. The same goes for the research community as well. Research paper recommendation aims to recommend new articles that match researchers’ interests. It has become an attractive area of study since the number of scholarly papers increases exponentially. There are already approaches that make use of personalized suggestions based on user information but these approaches deal with the issues of lack of data for a newly registered user. This problem is referred to as cold-start. Cold-start problem occurs when trying to suggest a newly registered user regarding whom we don’t have much data and hence the recommendations systems are not able to figure out what to suggest."""

sentence_tokens = nltk.sent_tokenize(text)
print("----------------------------------Sentence Tokens----------------------------------")
print (sentence_tokens)


word_tokens = nltk.word_tokenize(text)
print("----------------------------------Word Tokens----------------------------------")
print (word_tokens)