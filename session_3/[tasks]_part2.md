# Natural Language Processing with spaCy

## Installation

a) Check the documentation for the installation instructions: https://spacy.io/usage

b) You see, that you can install spaCy via pip. You also need some more packages and the language model:
```bash
pip install -U pip setuptools wheel
pip install -U spacy
python -m spacy download en_core_web_sm
```
The language model is the smallest one, which means it is faster but less accurate. You can also download a larger model, if you need more features.

c) Create a new Python file and call it `nlp.py`.

d) Import the spaCy library and load the English language model, as explained in the documentation: https://spacy.io/usage/models#download 

```python
import spacy

nlp = spacy.load("en_core_web_sm")
```

e) Now you can use the spaCy library to process text. For example, you can create a new document and print the tokens:

```python
doc = nlp("This is a sentence.")
```
Do this with a the sentence "I am learning Natural Language Processing.".

f) You can now iterate over the tokens (`in doc`) and print the text of each token with `token.text`.

g) In the readme-file of Session 3 and in [spaCy's 101](https://spacy.io/usage/spacy-101#annotations-token) you have some more examples, what you can do with a text. Play around with the possibilities. Use different text inputs and try out the different attributes of the tokens.

h) Now we want to  try out the named entity recognition (NER). You can do this with `doc.ents`. Print the text and the label of the entities of "Apple is a company and is located in California. It was founded by Steve Jobs.".

Here you have a list of the [entity types](https://spacy.io/models/en#en_core_web_sm-labels) that the english spaCy model can recognize:

| Type | Description |
| --- | --- |
| CARDINAL | Numerals that do not fall under another type |
| DATE | Absolute or relative dates or periods |
| EVENT | Named hurricanes, battles, wars, sports events, etc. |
| FAC | Buildings, airports, highways, bridges, etc. |
| GPE | Countries, cities, states |
| LANGUAGE | Any named language |
| LAW | Named documents made into laws |
| LOC | Non-GPE locations, mountain ranges, bodies of water |
| MONEY | Monetary values, including unit |
| NORP | Nationalities or religious or political groups |
| ORDINAL | "first", "second", etc. |
| ORG | Companies, agencies, institutions, etc. |
| PERCENT | Percentage, including "%" |
| PERSON | People, including fictional |
| PRODUCT | Objects, vehicles, foods, etc. (not services) |
| QUANTITY | Measurements, as of weight or distance |
| TIME | Times smaller than a day |
| WORK_OF_ART | Titles of books, songs, etc. |

i) You can also visualize the entities with displaCy: https://spacy.io/usage/visualizers. For this you need to import displacy under your spaCy import with `from spacy import displacy`. 

j) Then run the `displacy.serve()` function. Pass the `doc` and the style=`ent` as arguments.

k) Open the link in your browser and see the visualization of the entities.

l) You can also define which entities you want to see. You can pass a list of entity types as an argument to the `displacy.serve()` function. For example: `displacy.serve(doc, style="ent", options={"ents": ["ORG", "PERSON"]})`. This will only show the entities of the types "ORG" and "PERSON". Play around with the options.

m) Now you know how to use spaCy and how to visualize the entities. But we don't want to use this little example text. We want to use a text from a file. By now you should know how to work with files in Python. Read the text from the file `text.txt` and process it with spaCy. Print the tokens and the entities.
- Read the text from the file with the `with open()` statement and the `r` mode. As a text file, you can use the "sources_full/SWP_No._072.txt" file from part 1 of this session.
- Save the text in a variable `text` and process it with `nlp()` (instead of the example text).
- Use displaCy to visualize the entities, play around with the options.

**Optional:**

a) If you want, you can play around with the colors and the other options of the visualizer. You can find the documentation [here](https://spacy.io/usage/visualizers#ent).
- To change the colors, you can pass a dictionary with the colors as an argument to the `displacy.serve()` function. The keys are the entity types and the values are the colors. You can use the colors in the format `#hex` or the color names. For example: `colors={"ORG": "red", "PERSON": "blue"}` or `colors={"ORG": "#ec8a75", "PERSON": "#75c3ec"}`. You can find a color picker [here](https://htmlcolorcodes.com/).

b) If you are used to work with HTML and CSS, you can also save the visualization as a HTML file and change the style there. You can do this with the `displacy.render()` function. Pass the `doc` and the style=`ent` as arguments. You can also pass the colors and the options as arguments. Save the output in a variable and write it to a file. For example:

```python
html = displacy.render(doc, style="ent", options={"ents": ["ORG", "PERSON"], "colors": {"ORG": "red", "PERSON": "blue"}})
with open("entities.html", "w", encoding="utf-8") as file:
    file.write(html)
```
