import requests
from bs4 import BeautifulSoup

url = "https://salem.lib.virginia.edu/n72.html"

def get_webpage_data(url):
  response = requests.get(url)
  response.raise_for_status()
  
  # print(response.text) #optional!

  soup = BeautifulSoup(response.text, 'html.parser')

  title = soup.title.get_text()
  print(f"Title: {title}")

  txt_file_path = "sources_full/" + title.split(":")[0].replace(" ", "_") + ".txt"

  content_parts = []
  for element in soup.find_all(['h1', 'p']):
      text_element = element.get_text()
      content_parts.append(text_element)
  
  content = "\n\n".join(content_parts)

  with open(txt_file_path, "w") as file:
      file.write(content)

  print(f"Data written to {txt_file_path}")


get_webpage_data(url)

##OPTIONAL
#
# for i in range(1, 175):
#     url = f"https://salem.lib.virginia.edu/n{i}.html"
#     if requests.get(url).ok:
#         get_webpage_data(url)


