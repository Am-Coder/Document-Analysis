#pip install rake-nltk
from rake_nltk import Metric, Rake
from DatasetHandler import DataHandler

dh = DataHandler("Data.xlsx")
df = dh.get_dataframe()
extracted_keywords = []
for abs in df['Abstract']:
    r = Rake(min_length=1, max_length=3)
    r.extract_keywords_from_text(abs)
    #r.get_ranked_phrases()
    #r.get_ranked_phrases_with_scores()
    result = r.get_ranked_phrases_with_scores()
    topResult = result[:5]
    extracted_keywords.append(topResult)
