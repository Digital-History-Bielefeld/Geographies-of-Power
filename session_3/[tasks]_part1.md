# Modules, Packages, and Libraries

## Web Scraping with the BeautifulSoup Library 

You can install and import external libraries in Python to extend its functionality. One popular library for web scraping is BeautifulSoup. It allows you to extract data from HTML and XML files. BeautifulSoup creates a parse tree from the page source code, which you can navigate and search for specific elements. For this you need a basic understanding of HTML (you can find a tutorial in the Ressources section). For now, I tell you what to do, but if you are interested in web scraping, I recommend you to learn more about HTML and CSS.
Because BeautifulSoup just works with the HTML code of a website, you need to use the requests library to get the HTML code from a website first.

### 1. Installing Libraries

a) Take some minutes and check the documentation for the BeautifulSoup library: [BeautifulSoup Documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/). Try to understand how to install it and how to use it (not in detail, just a general overview).

b) We will use pip to install the library: https://www.crummy.com/software/BeautifulSoup/bs4/doc/#installing-beautiful-soup. Open your terminal and run the following command to install BeautifulSoup: `pip install beautifulsoup4`.

c) We also need to install the [`requests` library](https://requests.readthedocs.io/en/latest/user/install/#python-m-pip-install-requests), which allows us to send HTTP requests. Run the following command in your terminal: `pip -m install requests`.

Now you have installed two libraries: BeautifulSoup and requests. Congratulations! You are now ready to use them.

### 2. Use Requests to Get the HTML Code

a) Create a new python-file in the "Session 3"-folder. You can name it "web_scraping.py" for example.

b) Import the request library you just installed: `import requests`.

c) Define a function called `get_webpage_data`. The function should take a URL as an argument.

d) Use the requests library to get the HTML code from the URL. Save the response in a variable called `response`:
  
  ```python
  response = requests.get(url)
  ```
You can read how to do this in the [requests documentation](https://requests.readthedocs.io/en/latest/user/quickstart/#make-a-request).

e) Check if the request was successful. This is important because the website might not exist or the server might be down. You can check the status code with the request function `.raise_for_status()`. If the status code is not 200, raise an exception with the message "The website is not available.".

```python
response.raise_for_status()
```
f) Above your function definition, create a variable called `url` and assign a URL to it. You can use the URL of any website you want to scrape. In our case, we will use the URL of an example Salem Witchcraft case: "https://salem.lib.virginia.edu/n72.html"

g) Call the function with your url variable as an argument below the function definition.

**Optional:** You can print the html code with `print(response.text)` if you want to see it. Then the whole HTML code of the website will be printed in the console. To clean up your console after this, you can type `clear` and press enter.

### 3. Use BeautifulSoup to Parse the HTML Code

a) Import the BeautifulSoup library you just installed: `from bs4 import BeautifulSoup`. Do this under the import statement of the requests library.

b) To create a BeautifulSoup object, you need to pass the HTML code and a parser to the BeautifulSoup constructor. The parser is responsible for creating the parse tree. We will use the default parser, which is the Python built-in parser `html.parser`. Create a BeautifulSoup object and save it in a variable called `soup`:

```python
soup = BeautifulSoup(response.text, 'html.parser')
```
You can read more about this in the [BeautifulSoup documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#quick-start).

c) Now you have the HTML code of the website in a BeautifulSoup object. You can navigate and search for specific elements in the HTML code. For example, you can find all the links on the website with the `find_all` method. To do this, you need to know the HTML structure of the website. You can find the structure by inspecting the website in your browser.
In Firefox and Chrome, you can right-click on an element and select "Inspect Element" or "Inspect" to see the HTML code. Nearly every browser has a similar feature.
For our example, we first want to find the title of the website. For this you can use the bs function `soup.title.get_text()`. Save the return value in a variable called `title`.

d) Print the title like this: `print(f"Title: {title}")`.

e) Because we want to store the title in a txt file which is named after the title, we need to adjust the title-string. The filename should later look like this: "sources_full/SWP_No._072.txt"
  - First create a new folder in the main repository folder called "sources_full".
  - Create a variable called txt_file_path. 
  - Then first assign the folder path to it: `txt_file_path = "sources_full/"`.
  - Now you need to adjust the title-string. First we want to split the title-string at the colon. You can do this with the `split` method. You remember that split returns a list. We want to get the first element of this list, so we can use the index 0. Then this looks like this: `txt_file_path = "sources_full/" + title.split(":")[0]`. 
  - The file path would now look like this: "sources_full/SWP No. 072". We want to replace the spaces with underscores. You can do this with the `replace` method. The method takes two arguments: the string you want to replace and the string you want to replace it with. So you can adjust the file path like this: `txt_file_path = "sources_full/" + title.split(":")[0].replace(" ", "_")`.
  - As a last step you need to add the file extension ".txt" to the file path: `txt_file_path = "sources_full/" + title.split(":")[0].replace(" ", "_") + ".txt"`.
  - Now you have the correct file path, if you want, you can print the result and run the script to see if it is correct.

f) Now we want to get the essential text parts of the website. For this we use the `soup.find_all()`-method.
  - First we need to create an empty list called `content_parts`. In this list we will store the text parts.
  - Then we need for loop, to iterate over the elements we get with the `find_all`-method. You can do this like this: `for element in soup.find_all():`. In our case we need all the `p`-tags (because the text is in these paragraph-tags) and the `h1`-tag (because the paragraph-title is in this header-tag). You can pass the tags as a list to the `find_all`-method: `for element in soup.find_all(["p", "h1"]):`.
  - Inside the for loop you can get the text of the **element** with the `.get_text()`-method: `element.get_text()`. Store it inside a variable called `text_element`.
  - Then you can append the text_element to the content_parts-list: `content_parts.append(text_element)`.

g) Now you have all the text parts in the content_parts-list. But you want to write your content parts to a txt-file. So you need to join them together. You can do this with the `join`-method. The method takes a string as an argument, which will be inserted between the elements of the list. In our case you should use two newline character `"\n\n"` for this. The method looks like this: `content = "\n\n".join(content_parts)`.

h) As a next step you need to write the content to a txt-file. You can do this with the `open`-function. 
  - The function takes two arguments: the file path and the mode. You want to write to the file, so you should use the mode `"w"`. The function looks like this: `with open(txt_file_path, "w") as file:`.
  - Inside the `with`-block you can write the content to the file with the `write`-method: `file.write(content)`.

i) Now you have written the content to a txt-file. You can print a message to the console, that the file was created successfully: print(f"Data written to {txt_file_path}"). If you run the script now, you should see this message in the console. In your file system on the left, there should be a new file in the sources_full-folder with the title of the website as the file name.


### 4. More Practice (Optional)

You have just created your first web scraping script. If you work with digital methods, you usually need to scrape much more data. If you look at the Salem Witchcraft cases, you may notice that the url has always a similar structure. Our function is reusable for all the cases. So you can create a loop to scrape all the cases. You can do this like this:
- Define a for-loop that iterates over a range of numbers from 1 to 175. You can do this with the `range`-function.
- Inside the loop, you can create the url for each case with an f-string. Put the number of the case inside the f-string.
- Now we have the problem, that not all numbers are used for the cases. So you need to check if the url exists. You can do this with the `response.ok`-attribute. If the url exists, you can call the `get_webpage_data`-function with the url as an argument. This could look like this:

```python
for i in range(1, 175):
    url = f"https://salem.lib.virginia.edu/n{i}.html"
    if requests.get(url).ok:
        get_webpage_data(url)
```
