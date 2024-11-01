## This is the full solution of Session 4. 

import spacy
from collections import Counter
from spacy.matcher import Matcher
from wordcloud import WordCloud

nlp = spacy.load("en_core_web_md")

def get_most_frequent_persons(text, top_n=5, merge_names=[], remove_names=[]):
    doc = nlp(text)

    # persons = [ent.text for ent in doc.ents if ent.label_ == "PERSON"] # short writing
    persons = []
    for ent in doc.ents:
        if ent.label_ == "PERSON":
            persons.append(ent.text)

    for list in merge_names:
      for i in range(len(persons)):
        if persons[i] in list:
          persons[i] = list[0]
    
    for name in remove_names:
      for person in persons:
        if person == name:
          persons.remove(person)

    person_counts = Counter(persons)
    most_important_persons = person_counts.most_common(top_n)

    return most_important_persons

def get_person_context(text, person_names):
    doc = nlp(text)
    
    matcher = Matcher(nlp.vocab)
    
    for person_name in person_names:
        pattern = [{"LOWER": person_name.lower()}]
        matcher.add("PERSON_NAME", [pattern])
    
    matches = matcher(doc)
    
    context_words = []
    for match_id, start, end in matches:
        span = doc[start:end].sent

        for token in span:
            if token.pos_ in ["NOUN", "VERB", "ADJ"]:
                context_words.append(token.lemma_)

    context_counter = Counter(context_words)
    return context_counter.most_common()
    
def visualize_wordcloud(context_counter, filename="wordcloud.png"):
    wordcloud = WordCloud(width=800, height=400, background_color="white").generate_from_frequencies(dict(context_counter))
    
    wordcloud.to_file(filename)
    print(f"Saved as {filename}") 

with open("sources_full/SWP_No._072.txt") as file:
    text = file.read()

most_important_persons = get_most_frequent_persons(text, top_n=15, merge_names=[["Elizabeth How", "Elizabeth", "Eliz"], ["James How", "James"], ["goode ollever", "goode"]])

print("The most mentioned persons are:")
for person, count in most_important_persons:
    print(f"{person}: {count} times")

context_counter = get_person_context(text, ["goode ollever", "goode"])
visualize_wordcloud(context_counter)
