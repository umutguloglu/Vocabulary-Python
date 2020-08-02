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
def _takeName():
    new_Name=input("Word : ")
    return new_Name

def _takeDef():
    new_Def=input("Definition : ")
    return new_Def

def _takeExp():
    new_Exp=input("Example : ")
    return new_Exp

def _control(new_Name,new_Def,new_Exp): #Main part of adding
    print(_Green,"The Word :", new_Name)
    print(_Yellow,"The Def. :", new_Def)
    print(_Cyan,"The Exp. :", new_Exp,"\n",_NoColor)
    cntrl=input("\tPress Enter if the word is okay to add.\n" +
    "1-) If the 'Word(Name)' is wrong, press 'w' and Enter. \n" +
    "2-) If the 'Definition' is wrong, press 'd' and Enter. \n" +
    "3-) If the 'Example' is wrong, press 'e' and Enter. \n")
    with open("sample.json", "r") as f:
        _dict=json.load(f)
    if cntrl=="" :
        for eachword in _dict["Words"]: #Controls whether the same word exists.
            if eachword==new_Name :
                print("This word is already exist in the dictionary.")
                return _control(new_Name,new_Def,new_Exp)
        desc=dict()
        desc["Definition"]=new_Def
        desc["Examples"]=new_Exp
        desc["Number of Repeats"]=0
        with open("sample.json", "w") as f:
            _dict["Number of Words"]=_dict["Number of Words"]+1
            _dict["Words"][new_Name]=desc
            json.dump(_dict,f,indent=4)
    elif cntrl=="w" :
        new_Name=input("Write the new name: ").capitalize()
        return _control(new_Name,new_Def,new_Exp)
    elif cntrl=="d" :
        new_Def=input("Write the new name: ").capitalize()
        return _control(new_Name,new_Def,new_Exp)
    elif cntrl=="e" :
        new_Exp=input("Write the new name: ").capitalize()
        return _control(new_Name,new_Def,new_Exp)
    else :
        print("WARNİNG! You should choose one of the three options.")
        return _control(new_Name,new_Def,new_Exp)

def _add():     #Adds a Word
    new_Word=dict()
    new_Name=_takeName().capitalize()
    new_Def=_takeDef().capitalize()
    new_Exp=_takeExp().capitalize()
    _control(new_Name,new_Def,new_Exp)

def _delete(deleted_word):
    with open("sample.json", "r") as f:
        _dict= json.load(f)
    for eachword in _dict["Words"]:
        if eachword==deleted_word :
            del _dict["Words"][deleted_word]
            _dict["Number of Words"]=_dict["Number of Words"]-1
            print(deleted_word," is deleted.")
            with open("sample.json", "w") as f:
                json.dump(_dict,f,indent=4)
                return 0
    print("We could not find your word to delete! Try again.")
    return 0

def _length(_dict):
    if _dict["Number of Words"] == len(_dict["Words"]):
        return _dict["Number of Words"]
    else:
        print("There is a mistake in calculating length.")
        return -1

def _screening(_dict,wanted_word): #Screens a word.
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
        _dict= json.load(f)
        for eachword in _dict["Words"]:
            if eachword==wanted_word :
                _screening(_dict,wanted_word)
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

#-----------------------------------------------------------------------
_type=input("\t\tWelcome! What do you want?\n" +
"1-) To add word, press 'a' and Enter. \n" +
"2-) To look at a random word, press 'r' and Enter.\n" +
"3-) To look at a specific word, press 's' and Enter.\n"+
"4-) To delete a specific word, press 'd' and Enter.\n"+
"My choice is: "
)

if _type=="a" :
    _add()
    sys.exit(1)
elif _type=="r" :
    _random()
    sys.exit(1)
elif _type=="s" :
    wanted_word=input("What is your word?\n").capitalize()
    _specificword(wanted_word)
    sys.exit(1)
elif _type=="d" :
    deleted_word=input("Which word do you want to delete?").capitalize()
    _delete(deleted_word)
    sys.exit(1)
else :
    print("WARNİNG! You should choose one of the three options. Try again !")
    sys.exit(1)
