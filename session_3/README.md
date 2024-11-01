# Python Project - Part 1

Now you have learned the basics of the Python programming language. From now on, you will work with Python as you would in a real-world project. For this you often work with libraries and frameworks with a specific purpose. You can think of libraries as a collection of functions and methods that allows you to perform many actions without writing your own code. This libraries you can combine with your own code to create a project.
Python can be used for many different purposes, such as:
- Web development
- Data analysis
- Machine learning
- Automation
- Game development
- Web scraping
- For nearly everything else you can think of

For historians and other humanities scholars Python is a great tool for text analysis - especially when working with large amounts of text. 
In the next two sessions we will work with the following libraries:
- [Beautiful Soup](https://beautiful-soup-4.readthedocs.io/en/latest/): A library for web scraping, which allows you to extract data from HTML and XML files (so web pages).
- [Requests](https://requests.readthedocs.io/en/latest/): A library for sending HTTP requests. This is useful when you want to get data from a website.
- [spaCy](https://spacy.io/): A library for natural language processing (NLP). This library allows you to work with text data, such as analyzing text, extracting information, and more.

With this project you will learn how to work with these libraries and how to combine them to create a project. You will learn how to extract information from these texts, analyze them, and visualize the results. You will also learn how to work with web data, such as scraping data from websites. For this you will work with a (small) dataset of historical sources. This will give you a good foundation for working with Python in the future. Building on this, larger projects can be developed, such as Topic Modeling (a method for finding topics in a big collection of texts) or Sentiment Analysis (a method for determining the sentiment of a text) and more.

So let's get started with the first part!

## Modules, Packages and Libraries

### Libraries

A library in Python is a collection of packages and modules bundled together, usually designed for a specific purpose or task. Libraries make it easy to perform complex tasks without needing to write all the code yourself. For example, the popular library requests helps you handle HTTP requests. You first install it (usually via pip install requests) and then import it into your script.
To install it with pip, you can use the following command in your terminal:

```bash
pip install requests
```

Then you are ready to use this library in your code:

```python

import requests

# Using the requests library to get a webpage
response = requests.get("https://example.com")
print(response.status_code)  # Output: 200 if the page loads successfully
```

Libraries like requests, pandas, and numpy are widely used to extend Python’s functionality for specific tasks, such as data processing, web development, and scientific computing. You can find nearly any library you need on the [Python Package Index (PyPI)](https://pypi.org/). 

---

### pip
**pip** is Python's package manager, which makes it easy to install and manage libraries from the Python Package Index (PyPI). With `pip`, you can install libraries and packages from the command line or terminal without manually downloading files. For example, to install the `requests` library, you would use:

```bash
pip install requests
```

After running this command, you can import and use `requests` in your code. `pip` also allows you to uninstall packages or check which ones are installed with commands like `pip uninstall` and `pip list`.

---

### Virtual Environments
In our case you don't need to use virtual environments, because we work in a GitHub Codespace. But it is good to know what they are and how to use them for your own (and local) projects.

**Virtual Environments** allow you to create isolated Python environments for different projects, so that each environment has its own set of packages and dependencies. This is useful when working on multiple projects that may require different versions of the same libraries. To create a virtual environment, navigate to your project folder in the terminal and run:

```bash
python -m venv myenv
```

This creates a virtual environment named `myenv`. But you can name it whatever you want, one common name is `.venv`.
To activate it, use:

- On Windows: `myenv\Scripts\activate`
- On macOS/Linux: `source myenv/bin/activate`

Once activated, any packages you install with `pip` will be specific to that environment. To exit the virtual environment, simply type `deactivate`.

---

### Documentation
When working with libraries, it is important to read the documentation to understand how to use them. The documentation provides information on the library's functions, classes, and methods, as well as examples and best practices. You can find the documentation for most libraries on their official websites or on the Python Package Index (PyPI). You should get used to reading documentation and using it as a reference when working with new libraries.
Also for your own code it is good practice to write documentation. This makes it easier for others (and yourself) to understand your code. You can write documentation using comments in your code, or by using docstrings (multi-line comments) at the beginning of your functions and classes. This is especially important when working on larger projects or collaborating with others.

---

## Natural Language Processing (NLP)

**Natural Language Processing (NLP)** is a field of artificial intelligence that focuses on the interaction between computers and humans using natural language. NLP is used to analyze, understand, and generate human language in a valuable way. It is used in many applications, such as chatbots, language translation, sentiment analysis, and more. NLP involves many tasks, such as tokenization, part-of-speech tagging, named entity recognition, and more. Theoretically, NLP is a tool of computer linguistics, but in practice it is used in a wide range of applications. For example, it is used in search engines, spam filters, and machine translation. Lawyers use it to search relevant information in thousands of legal documents in seconds, financial analysts use it to analyze news and social media to predict stock prices, and historians use it to analyze large amounts of text data. Libraries like [spaCy](https://spacy.io/) and [NLTK](https://www.nltk.org/) provide tools and resources for working with text data and NLP tasks. Below you will find a glossary of some important terms in NLP.

### spaCy

#### What is spaCy?
spaCy is a natural language processing framework. It is designed to be fast and efficient, and it comes with pre-trained models and resources for various NLP tasks. spaCy provides tools and resources for tokenization, part-of-speech tagging, named entity recognition, and more. It is widely used in academia and industry for text analysis and NLP tasks. spaCy has a good documentation, which you can find [here](https://spacy.io/usage). 

#### Loading spaCy Models

After installing spaCy, you can load a pre-trained model for a specific language. For example, to load the English model, you can use:

```python
import spacy

nlp = spacy.load("en_core_web_sm")
```

This loads the English model with the small pipeline, which includes vocabulary, syntax, and named entities. You can also load other models, such as the medium or large pipeline, depending on your needs.
You can find a list of available models on the [spaCy website](https://spacy.io/usage/models). You can also train your own models using spaCy, but this requires a large amount of annotated data and computational resources. Some self-trained models are available on [Hugging Face](https://huggingface.co/), a open-source platform that provides tools and models for natural language processing (NLP) and machine learning

#### Containers in spaCy
spaCy uses containers to process and analyze text data. The main containers in spaCy are:
- `Doc`: A container for accessing linguistic annotations and linguistic analysis.
- `Token`: A container for accessing individual tokens in a `Doc`.
- `Span`: A container for accessing a slice of a `Doc`.

For example, you can create a `Doc` object from a text string and access its tokens and annotations:

```python
import spacy

nlp = spacy.load("en_core_web_sm") # Load the English model

doc = nlp("Apple is headquartered in Cupertino, California.") # Create a Doc object

for token in doc:
    print(token.text, token.pos_, token.dep_) # Print the token text, part-of-speech tag, and dependency label

span = doc[2:4] # Create a Span object
print(span.text) # Output: "headquartered in"
```

#### Sentences

```python	
import spacy

nlp = spacy.load("en_core_web_sm") # Load the English model

doc = nlp("Apple is headquartered in Cupertino, California. The company's address is One Apple Park Way. The CEO is Tim Cook.") # Create a Doc object

for sent in doc.sents:
    print(sent.text) # Output: "Apple is headquartered in Cupertino, California.", "The company's address is One Apple Park Way.", "The CEO is Tim Cook."


```

#### Tokens

A token objects contains a lot of information. Some of the attributes are:
- `text`: The original text of the token.
- `lemma_`: The base form of the token.
- `pos_`: The part-of-speech tag of the token.
- `dep_`: The dependency label of the token.
- `head`: The syntactic head token of the token.
- `ent_type_`: The named entity type of the token.

```python
import spacy

nlp = spacy.load("en_core_web_sm") # Load the English model

doc = nlp("Apple is headquartered in Cupertino, California.") # Create a Doc object

for token in doc:
    print(token.text) # Output: "Apple", "is", "headquartered", "in", "Cupertino", ",", "California", "."
    print(token.lemma_) # Output: "Apple", "be", "headquarter", "in", "Cupertino", ",", "California", "."
    print(token.pos_) # Output: "PROPN", "AUX", "VERB", "ADP", "PROPN", "PUNCT", "PROPN", "PUNCT"
    print(token.dep_) # Output: "nsubj", "aux", "ROOT", "prep", "pobj", "punct", "appos", "punct"
    print(token.head.text) # Output: "headquartered", "headquartered", "headquartered", "headquartered", "in", "headquartered", "California", "headquartered"
    print(token.ent_type_) # Output: "ORG", "", "", "", "GPE", "", "GPE", ""
```

Some POS tags:
- `PROPN`: Proper noun
- `AUX`: Auxiliary verb
- `VERB`: Verb
- `ADP`: Adposition (preposition or postposition)
- `PUNCT`: Punctuation
- `ADJ`: Adjective
- `NOUN`: Noun


Some dependency labels:
- `nsubj`: Nominal subject
- `aux`: Auxiliary
- `ROOT`: Root
- `prep`: Prepositional modifier
- `pobj`: Object of preposition
- `appos`: Appositional modifier

Some entity types:
- `ORG`: Organization
- `GPE`: Geopolitical entity
- `PERSON`: Person
- `DATE`: Date
- `CARDINAL`: Cardinal number


### Glossary

#### Token
A **token** is a single unit of text, such as a word or punctuation mark. It can also refer to a sequence of words that are treated as a single unit, such as "New York" or "United States". Tokenization is the process of breaking text into tokens. A token is more than just a word, because it has additional information, such as its position in the text, part-of-speech tag, and more.

#### Tokenization
**Tokenization** is the process of breaking text into smaller units, such as words or sentences. This is an essential step in NLP, as it allows you to analyze and process text data. For example, the sentence "Hello, world!" can be tokenized into two words: "Hello" and "world". Tokenization can be done at different levels, such as word-level, sentence-level, or character-level, depending on the task.

#### Part-of-Speech Tagging
**Part-of-Speech (POS) tagging** is the process of assigning a part of speech (such as noun, verb, adjective, etc.) to each word in a sentence. This is useful for understanding the grammatical structure of a sentence and extracting information from text data. For example, in the sentence "The cat is sleeping", the word "cat" is tagged as a noun, "is" as a verb, and "sleeping" as a verb.

#### Named Entity Recognition
**Named Entity Recognition (NER)** is the process of identifying and classifying named entities in text data, such as names of people, organizations, locations, dates, and more. This is useful for extracting information and understanding the context of text data. For example, in the sentence "Apple is headquartered in Cupertino, California", "Apple" is recognized as an organization, and "Cupertino, California" as a location.

#### Lemmatization
**Lemmatization** is the process of reducing words to their base or root form, called a lemma. This is useful for normalizing text data and reducing inflectional forms to a common base form. For example, the words "running", "ran", and "runs" can be lemmatized to the base form "run".

#### Stop Words
**Stop words** are common words that are often filtered out during text preprocessing, as they do not carry much meaning or information. Examples of stop words include "the", "is", "and", "in", and more. Removing stop words can help reduce noise and improve the quality of text analysis.

#### Corpus
A **corpus** is a collection of text data, such as a set of documents, articles, or books. Corpora are used for training and testing NLP models, as well as for analyzing and extracting information from text data. For example, a corpus of historical documents can be used to study language patterns, topics, and trends over time.

#### Document
A **document** is a single piece of text data and collection of tokens. It can be a sentence, paragraph, article, or any other unit of text. Documents are used for text analysis, classification, and information extraction. For example, a document can be analyzed for sentiment, named entities, or topics.
