def lowercase_and_without_whitespaces(text):
    text = text.lower()
    text = text.replace(" ", "")
    return text
    
    # You can also do it in one line:
    # return text.lower().replace(" ", "")  
