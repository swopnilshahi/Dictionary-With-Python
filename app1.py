import json
from difflib import get_close_matches

data = json.load(open("data.json"))  #load json file

def dictionary(word):  #creating function for dictionary
    word = word.lower()
    if word in data:
        return data[word] #returning the data
    elif len(get_close_matches(word, data.keys())) > 0:
        yn=input("Did you mean %s instead?? If yes then type Y if No then N :" % get_close_matches(word, data.keys())[0])
        if yn == "y" or "Y": 
            return data[get_close_matches(word, data.keys())[0]]  
        elif yn == "n" or "N":
            return print("There is no such word! Please double check it")
        else:
            return "Can't find"
    else:
        print("Data not found,Please Check your word")

user_input = input("Enter word: ")
output = dictionary(user_input)
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)