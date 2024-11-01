import spacy
from spacy import displacy

nlp = spacy.load('en_core_web_sm')
# doc = nlp("I am learning Natural Language Processing.")
# doc =nlp("Apple is a company and is located in California. It was founded by Steve Jobs.")

# for token in doc:
#     print(token.text)

# for ent in doc.ents:
#     print(ent.text, ent.label_)

# displacy.serve(doc, style="ent")

with open("sources_full/SWP_No._072.txt", "r") as file:
    text = file.read()

doc = nlp(text)

displacy.serve(doc, style="ent", options={"ents": ["ORG", "PERSON"], "colors": {"ORG": "#ec8a75", "PERSON": "#75c3ec"}})
