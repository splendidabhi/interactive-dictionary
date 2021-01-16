import json
from difflib import get_close_matches
data = json.load(open("data.json"))
def translate(word):
    word=word.lower()           #changes the upper case letter to lower case
    if word in data:
        return data[word]
    elif word.title() in data:  #if user entered "delhi" this will check for "Delhi" as well.
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word,data.keys())) > 0:
        yn=input("Did you mean %s instead ? Enter Y for YES, or N for NO : " % get_close_matches(word,data.keys())[0])
        if yn =="Y":
            return data[get_close_matches(word,data.keys())[0]]
        elif yn=="N":
            return("Sorry! The word does not exist double check it")
        else:
            return("SORRY! we didn't understand your query. Try New search")
    else:
        return "The word does not exist double check it "

word = input("Enter word : ")
output = translate(word)
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
