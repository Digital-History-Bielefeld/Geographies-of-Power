# Python Project - Part 2

In this part of the project you will combine the learning from the previous sessions to answer some questions about the data. This content is a good exercise for tomorrow's final project. Afterwards, you should be ready to address your own questions to the material and answer them using simple Python methods. With this prepared data, you can then - if you want to continue working with Python - perform more complex analyses, such as topic modeling, sentiment analysis or social networks. 

## Questions
1. What are the 5 most important persons in the data set?
2. Why are the most important persons important? What is their role in the data set?

Try to answer these questions using Python - without looking at the data set.

## 1. What are the 5 most important persons in the data set?

To answer this question, you need to use spaCy's entity recognition. You need to save the names of the persons in a list and then count the number of times each name appears in the data set. Of course, this is just a statistical approach and the most common names are not necessarily the most important persons. But it is a good starting point to get an overview of the data set.
If you get stuck, you can find some hints below.

a)
- Add a new python file to your project and name it `important_persons.py`.
- Import spacy and load the English model.
- Define a new function called `get_most_frequent_persons` that takes a text as input and also a `top_n` parameter that defines how many persons you want to return. This top_n parameter should have a default value of 5.
- In the function, define a doc object using the nlp model and the text, you passed in as input.
- Create an empty list called `persons` and iterate over the entities in the doc object. If the entity is a person (`ent.label_ == "PERSON"`), append it to the list. 
- For counting the number of times each person appears in the data set, you can use the `Counter` class from the `collections` module. This is a helpful tool for counting the number of times each element appears in a list and returning the most common elements.
    - Counter: https://docs.python.org/3/library/collections.html#collections.Counter
    - .most_common(): https://docs.python.org/3/library/collections.html#collections.Counter.most_common
    - Try to understand how to use the Counter class and the most_common method. As a value for the most_common method, you can pass the top_n parameter.
    - Don't forget to import the Counter class at the beginning of your file: `from collections import Counter`.
- Return the most common persons from the data set.

Now you have defined a reusable function that you can use to find the most important persons in a data set. Let's go on and pass our data to the function.

- Open our prepared source ("sources_full/SWP_No._072.txt") with the "with open" statement and read the content. Save the content in a variable called `text` (our however you want to name it).
- Save the result of the `get_most_frequent_persons` function in a variable called `most_important_persons`. Pass the text as input to the function. 
- Interate over the `most_important_persons` and print the name of the person and the number of times they appear in the data set. In the for loop, you can use the following syntax: `for person, count in most_important_persons:`.
- What do you think about the results? Are they what you expected? Play around with the top_n parameter and see how the results change.

b)
The result is not perfect. There are some names that are not persons and some persons which are named differently. This we should fix. In the next steps we will clean the persons list and try to get the most common persons again. Try to think about how you could clean the list of persons. If you want, you can try to implement the cleaning process yourself. Else, you can follow the next steps.

Let's start with merging the names of the persons that are named differently but are the same person. For this we should give the function a list with lists of names that should be merged to one name (e.g. `["Merkel", "Angela Merkel"]`).

- We want to make our function as reusable as possible. So we could use this function also with other texts. Therefore, we should add a new parameter to the function called `merge_names`. - `merge_names` should get an empty list as a default value. When calling the function, you can pass a list of lists with names that should be merged to one name.
- Below your entity-iteration, write a new for-loop
- Interate over each list in the `merge_names` list
- Add a second for-loop that iterates over the indexes of the persons list with the range function. As a value for the range function, you can pass the length of the persons list.
- Check if the person at the current index is in the list. If yes, then change the value of the person (`persons[i]`) to the first name of the merge-list. 

c)
Now we want to have the possibility to exclude some persons from the list. This is especially useful if there are faulty names in the data set. 
- Add a new parameter to the function called `remove_names`. This parameter should have an empty list as a default value.
- Add a new for-loop below the merge-names for-loop. This for-loop should iterate over the `remove_names` list.
- In the for-loop, add another for-loop that iterates over the persons list.
- Check if person equals the name in the remove_names list. If yes, remove the person from the persons list.

Now you can use the function with the merge_names and remove_names parameters to clean the list of persons. Play around with it! You could for example merge "Elizabeth" and "Elizabeth How" with: `get_most_frequent_persons(text, merge_names=[["Elizabeth", "Elizabeth How"]])`. 

## 2. Why are the most important persons important? What is their role in the data set?

In step 1 we found out who the most important persons in the data set are. This is useful to get an overview of the data set and building on this. Now we want to get deeper into the data set and find out why the most important persons are important. For this, we have different possibilities.  One is to extract tokens or other entities that appear with the persons. This could give us a hint about the role of the persons in the data set.

First, we should consider what we need for this task.
  - We need a function that extracts the tokens in context of the persons. 
  - Maybe it is useful to pass only one person to the function, so we can analyze the context of each person separately and get a better overview.
  - We learned in the last session that there are different writings of the same person. So we need to handle this.
  - The context could be anything. So we need to decide which context we mean. We could for example extract the nouns or verbs that appear before and after the person to get an first impression. But this is up to you and you can decide what you want to extract and play around with it.

a)
- Write a new function called `get_person_context` that takes a text and a list of different writings of persons name (`person_names`) as input. The function should return the tokens in context of the person.
- Create a doc object with the nlp model and the text.
- We want to work with the Matcher class from spaCy (https://spacy.io/usage/rule-based-matching). With the Matcher class we can define patterns that we want to find in the text. We can use this to find the person in the text and then extract the context. Because this is a bit more complex, you can just follow my instructions and try to understand what happens there. Otherwise (or at home with more time) you can try to understand the Matcher class and implement it yourself. 
For this, we need to import the Matcher class at the beginning of the file: `from spacy.matcher import Matcher`.
- Create a variable called `matcher` and assign a new Matcher object to it. The Matcher object should be created with the nlp model. This looks like this: `matcher = Matcher(nlp.vocab)`.
- Iterate over each person_name in  `person_names` create a pattern for each person:
  - We want to match both upper and lower case names. Therefore, we should create a pattern that matches the person in the text. For this, we need to create a list with dictionaries. Each dictionary should have **the key "LOWER"** and the **value should be the lower case name of the person**. We can use the `person.lower()` method to get the lower case name.
  Create a variable `pattern` and assign the list with the dictionary to it.
  - Add the pattern to the matcher object with the `matcher.add` method. As a first parameter, you can pass a unique name for the pattern (e.g. `"PERSON_NAME"`) and as a second parameter the pattern (`[pattern]`). This looks like this: `matcher.add("PERSON_NAME", [pattern])`.
- Now we want to iterate over the matches in the text (the context-words). For this create a new variable called `context_words` and assign an empty list to it. 
- Iterate over the matches in the text with the matcher object. You can use the following syntax: `for match_id, start, end in matcher(doc):`. Match_id is the unique name of the pattern, start is the start index of the match and end is the end index of the match.
- Create a variable called `span` and assign the span of the match to it. You can get the span with the following syntax: `span = doc[start:end].sent`. This gives you the sentence of the match.
- Iterate over the tokens in the span.
- If `token.pos_` (which is the Part-of-Speech tag of the token) is in `["NOUN", "VERB", "ADJ"]`, append the `token.lemma_` to the context_words list. We use the lemma of the token to get the base form of the word.

Now you have a function that extracts the context of a person in the text. You can use this function to get an overview of words that appear with the most important persons in the data set. Call the function with the source-text and `["goode ollever", "goode"]` as arguments and print the result.
You get a big list with tons of words. Not very helpful. So let's refine the function a bit.

b) 
- First we want to add a counter to the function. This counter should count the number of times each word appears in the context. Therefore, you can use the Counter class from the collections module as we did in the first task.
- Create a new variable above the return statement inside your function. This variable could be called `context_counter`.
- Assign the result of the Counter class to the context_counter variable. As input for the Counter class, you can pass the `context_words`.
- Now return the most common words in the context with the most_common method of the context_counter. You can pass a number to the most_common method to get the most common words, if you want to.

With this we have a tuple with the most common words in the context of the person. You can now print the result of the function. Again: Not very helpful, just a big list of words. Let's try to visualize the data. One simple (although not the coolest) way to visualize the data is to use a word cloud. With this you can see the most common words in the context of the person. If you are interested in how this works, you can read everything about it here: http://amueller.github.io/word_cloud/generated/wordcloud.WordCloud.html. In order not to go beyond the scope of the course, I have already prepared the right settings and methods that you can easily apply.

- Install the wordcloud library with `pip install wordcloud`.
- Import the WordCloud class from the wordcloud module at the beginning of your file: `from wordcloud import WordCloud`.
- Create a new function called `visualize_wordcloud` that takes a list of tuples as input.
The tuples should have the word as the first element and the count as the second element (practially the result of the `get_person_context` method we implemented before).
Additionally, you can pass a filename as a second parameter. This filename should be the name of the file where the word cloud should be saved. You can use "wordcloud.png" as a default value. This could be practical if you want to save the word cloud to different files.
- To generate the wordcloud, create a new variable `wordcloud` inside your function and assign a new WordCloud object to it. You can pass the following code to the WordCloud object: 
  ```python
  wordcloud = WordCloud(width=800, height=400, background_color="white").generate_from_frequencies(dict(context_counter))
  ```
- After this we want to save the word cloud to a file. For this, you can use the `to_file` method of the wordcloud object. As a parameter, you can pass the filename. This looks like this: `wordcloud.to_file(filename)`.
- To know that the process is complete, you can print a message to the console: `print(f"Saved as {filename}")`.
- Call the function at the bottom of your document with the `context_counter` as input. 

Now you can see the result of the function in the wordcloud.png file. Play around with this with different persons and see what you can find out about the context of the persons in the data set. Are there any interesting words that appear with the persons? Does it make sense? 

### Some final thoughts about the task:
- This methods could be useful to get an overview of the data set and the persons in the data set. You can use this to get a first impression.
- For a small data set like this, it is not very useful. But if you have a big data set with many persons, this could be a good way to get an overview of the data set. Especially if it is too much data to read it all.
- Normally you would work with a better cleaned data set. But for this task, we had to work with the data set as it is. Data cleaning of historical data could fill an entire course on its own.
- You can't only work with digital methods. You always need to reflect on the results and think about what they mean. As a next step on this task, you would look for the most itneresting words of your wordcloud in the text context and try to understand why they appear with the person. Think about digital methods as a tool to help you understand and organize your data.

## Hints
### 1. Most important persons in the data set:
a)
- To define a default value for a parameter, you can use the following syntax: `def my_function(top_n=10)`.
- To define a doc object, you can use the following syntax: `doc = nlp(text)`.
- To iterate over the entities in the doc object, you can use the following syntax: `for ent in doc.ents:`.
- To check if an entity is a person, you can use the following syntax: `if ent.label_ == "PERSON":`.
- To append an entity to a list, you can use the following syntax: `persons.append(ent.text)`.
- To count the number of times each person appears in the data set, you can use the following syntax: 
  ```python
  from collections import Counter

  person_counts = Counter(persons)
  most_common_persons = person_counts.most_common(top_n)
  ```
- To read the content of a file, you can use the following syntax: 
  ```python
  with open("path/to/your/file.txt", "r") as file:
      text = file.read()
  ```
- You can call our function with the text and the a person_names list parameter: `context_counter = get_person_context(text, ["goode ollever", "goode"])`.

b)
- To iterate over a indexes with the range function, you can use the following syntax: `for i in range(len(persons)):`.
- With `i` you can access the current index of the persons list.
- You can reassign the value of a list at a specific index with the following syntax: `persons[i] = "new_name"`. 
- As a new value you can use the first name of the merge-list: `merge_list[0]`.

c)
- To remove an element from a list, you can use the following syntax: `my_list.remove("element")`.

### 2. Context of the persons:
a)
- To create a pattern list for the Matcher class, you can use the following syntax: `pattern = [{"LOWER": person.lower()}]`.
- To iterate over the token part-of-speech tags, you can use the following syntax: 
```python
for token in span:
    if token.pos_ in ["NOUN", "VERB", "ADJ"]:
        context_words.append(token.lemma_)
```

b) As already explained in 1a), you can use the Counter class to count the number of times each word appears in the context:
```python
context_counter = Counter(context_words)
return context_counter.most_common()
```

- The wordcloud function could look like this:
```python
def visualize_wordcloud(context_counter, filename="wordcloud.png"):
    wordcloud = WordCloud(width=800, height=400, background_color="white").generate_from_frequencies(dict(context_counter))
    
    wordcloud.to_file(filename)
    print(f"Saved as {filename}") 
```
