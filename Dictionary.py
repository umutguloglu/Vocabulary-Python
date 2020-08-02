import json
from random import randint
import sys

# This part can be changed according to your preferences.
# Use "\33[0m" for no color option.
_Green="\33[32m"  #_Green="\33[0m"
_Yellow="\33[33m" #_Yellow="\33[0m"
_Cyan="\33[36m"   #_Cyan="\33[0m"
_NoColor="\33[0m"
#------------------------------------------------------------------------------

def _length(_dict):
    if _dict["Number of Words"] == len(_dict["Words"]):
        return _dict["Number of Words"]
    else:
        print("There is a mistake in calculating length.")
        return -1

def _screening(_dict,wanted_word):
    print(_Green,"Word : ", end="")
    print(wanted_word)
    print(_Yellow,"Def. : ", end="")
    print(_dict["Words"][wanted_word]["Definition"])
    print(_Cyan,"Example : ", end="")
    print(_dict["Words"][wanted_word]["Examples"])
    _preRepeat=_dict["Words"][wanted_word]["Number of Repeats"]
    _dict["Words"][wanted_word]["Number of Repeats"]=_preRepeat+1
    print(_NoColor,"Reading has been done succesfully.")
    with open("sample.json", "w") as f:
        json.dump(_dict,f,indent=4)

def _specificword(wanted_word):
    with open("sample.json", "r") as f:
        dictionary= json.load(f)
        for eachword in dictionary["Words"]:
            if eachword==wanted_word :
                _screening(dictionary,wanted_word)
                return 0
        print("We could not find your word! Try again.")

def _random():
    with open("sample.json", "r") as f:
        dictionary= json.load(f)
        __length=_length(dictionary)
        if __length==0 :
            print("There is not any word in the vocabulary yet.")
            return -1
        elif __length<0:
            print("Length is negative.")
            return -1
        else :
            number=randint(1,__length) - 1 # Array starts with 0.
            word=list(dictionary["Words"])[number]
            _screening(dictionary,word)


_type=input("\t\tWelcome! What do you want?\n" +
"1-) To add word, press 'a' and Enter. \n" +
"2-) To look at a random word, press 'r' and Enter.\n" +
"3-) To look at a specific word, press 's' and Enter.\n"+
"My choice is: "
)

if _type=="a" :
    pass
elif _type=="r" :
    _random()
    sys.exit(1)
elif _type=="s" :
    wanted_word=input("What is your word?\n")
    _specificword(wanted_word)
    sys.exit(1)
else :
    print("WARNİNG! You should choose one of the three options. Try again !")

"""
def _add():
    with open("sample.json", "a") as f:
        dictionary= json.load(f)
"""
























# Data to be written
"""
print(list(dictionary.values())[0])

with open("sample.json", "w") as osutfile:
    json.dump(dictionary, outfile)

a=input("Ahahaha ")
print(a)
"""
