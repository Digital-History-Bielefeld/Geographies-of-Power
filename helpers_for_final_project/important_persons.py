# Import the necessary libraries
import spacy # Import the spacy library for the NLP model
from collections import Counter # Import the Counter library to count the number of times a person appears in the text
from spacy.matcher import Matcher # Import the Matcher library to get the context of the person
from wordcloud import WordCloud # Import the WordCloud library to visualize the context of the person

# Load the English model from spacy
nlp = spacy.load("en_core_web_sm")

# Define the functions to get the most important persons and their context
# The text parameter is the text you want to analyze, top_n is the number of most important persons you want to get with a default value of 5, 
def get_most_frequent_persons(text, top_n=5, merge_names=[], remove_names=[]):
    
    # Load the text into the nlp model
    doc = nlp(text)

    # Get the persons from the text (filteres by the label PERSON) and store them in a list called persons
    persons = []
    for ent in doc.ents:
        if ent.label_ == "PERSON":
            persons.append(ent.text)

    # Merge the names in the merge_names list to the first name in the list
    for list in merge_names:
      for i in range(len(persons)):
        if persons[i] in list:
          persons[i] = list[0]
    
    # Remove the names in the remove_names list from the persons list
    for name in remove_names:
      for person in persons:
        if person == name:
          persons.remove(person)

    # Count the number of times each person appears in the persons list with the Counter library
    person_counts = Counter(persons)
    # Get the top_n most common persons
    most_important_persons = person_counts.most_common(top_n)

    # Return the most important persons
    return most_important_persons

# Get the context of the person in the text
# The text parameter is the text you want to analyze, person_names is the name of the person you want to get the context of
def get_person_context(text, person_names):
    # Load the text into the nlp model
    doc = nlp(text)
    
    # Create a Matcher object. The Matcher is used to match sequences of tokens based on patterns
    matcher = Matcher(nlp.vocab)
    
    # Add the person_names to the matcher. The pattern is the name of the person in lowercase, so it is case-insensitive. It is a spaCy feature, see https://spacy.io/usage/rule-based-matching
    for person_name in person_names:
        pattern = [{"LOWER": person_name.lower()}]
        matcher.add("PERSON_NAME", [pattern])
    
    # Get the matches of the person_names in the text
    matches = matcher(doc)
    
    # Get the context words of the person_names
    context_words = []
    for match_id, start, end in matches:
        # Get the sentence of the match. This is where the person_name appears and also the context
        span = doc[start:end].sent

        # Get the lemma of the token if it is a noun, verb, or adjective
        for token in span:
            if token.pos_ in ["NOUN", "VERB", "ADJ"]:
                context_words.append(token.lemma_)

    # Count the number of times each context word appears in the context_words list with the Counter library
    context_counter = Counter(context_words)
    # Return the most common context words
    return context_counter.most_common()

# Visualize the context of the person in a wordcloud.
# The context_counter parameter is the context of the person, filename is the name of the file where the wordcloud will be saved with a default value of wordcloud.png
def visualize_wordcloud(context_counter, filename="wordcloud.png"):
    # Create a WordCloud object with the context_counter. The width is 800, height is 400, and the background color is white. The .generate_from_frequencies() method generates the wordcloud from the context_counter. You can find more information about the WordCloud library here: https://amueller.github.io/word_cloud/index.html
    wordcloud = WordCloud(width=800, height=400, background_color="white").generate_from_frequencies(dict(context_counter))
    
    # Save the wordcloud as a file with the filename
    wordcloud.to_file(filename)
    # Print the filename where the wordcloud is saved
    print(f"Saved as {filename}") 

# Load the text from the file
with open("sources_full/SWP_No._072.txt") as file:
    text = file.read()

# Call the get_most_frequent_persons function to get the most important persons in the text.
# Use the Names you want to merge or remove and pass them as below
most_important_persons = get_most_frequent_persons(text, top_n=15, merge_names=[["Elizabeth How", "Elizabeth", "Eliz"], ["James How", "James"], ["goode ollever", "goode"]], remove_names=["bin"])

# Print the most important persons
print("The most mentioned persons are:")
for person, count in most_important_persons:
    print(f"{person}: {count} times")

# Call the get_person_context function to get the context of the person in the text.
# Use the name (with different writings) you want to get the context of and pass it as below
context_counter = get_person_context(text, ["goode ollever", "goode"])
# Call the visualize_wordcloud function to visualize the context of the person in a wordcloud
visualize_wordcloud(context_counter)
