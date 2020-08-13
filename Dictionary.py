import json
from random import randint
import sys

# This part can be changed according to your preferences.
# Use "\33[0m" for no color option.
_Green="\33[32m"  #_Green="\33[0m"
_Yellow="\33[33m" #_Yellow="\33[0m"
_Cyan="\33[36m"   #_Cyan="\33[0m"
_Red="\33[31m"    #_Red="\33[0m"
_NoColor="\33[0m"
#------------------------------------------------------------------------------
def _takeName():
    new_Name=input(_Green + "The word you want to add is : ")
    return new_Name

def _takeDef():
    new_Def=input(_Yellow + "Definition : ")
    return new_Def

def _takeExp():
    new_Exp=input(_Cyan + "Example : ")
    return new_Exp

def _control(new_Name,new_Def,new_Exp): #Main part of adding
    print("")
    print(_Green,"The Word :", new_Name)
    print(_Yellow,"The Def. :", new_Def)
    print(_Cyan,"The Exp. :", new_Exp,_NoColor)
    cntrl=input("Press Enter if the word is okay to add.\n" +
    "1-) If the 'Word(Name)' is wrong, press 'w' and Enter. \n" +
    "2-) If the 'Definition' is wrong, press 'd' and Enter. \n" +
    "3-) If the 'Example' is wrong, press 'e' and Enter. \n" +
    "4-) To quit, press 'q' and Enter. \n")
    with open("Vocabulary.json", "r") as f:
        _dict=json.load(f)
    if cntrl=="" :
        for eachword in _dict["Words"]: #Controls whether the same word exists.
            if eachword==new_Name :
                print(_Red,"This word is already exist in the dictionary.",_NoColor)
                return _control(new_Name,new_Def,new_Exp)
        desc=dict()
        desc["Definition"]=new_Def
        desc["Example"]=new_Exp
        desc["Number of Repeats"]=0
        with open("Vocabulary.json", "w") as f:
            _dict["Number of Words"]=_dict["Number of Words"]+1
            _dict["Words"][new_Name]=desc
            json.dump(_dict,f,indent=4)
            print("Adding has been done succesfully.")
        sys.exit(1)
    elif cntrl=="w" :
        new_Name=input("Write the new name : ").capitalize()
        return _control(new_Name,new_Def,new_Exp)
    elif cntrl=="d" :
        new_Def=input("Write the new Definition : ").capitalize()
        return _control(new_Name,new_Def,new_Exp)
    elif cntrl=="e" :
        new_Exp=input("Write the new Example : ").capitalize()
        return _control(new_Name,new_Def,new_Exp)
    elif cntrl=="q" :
        sys.exit(1)
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
    with open("Vocabulary.json", "r") as f:
        _dict= json.load(f)
    _showColor(_dict,deleted_word)
    w=input("Press Enter to delete unnecessary word or press"+
    " something than enter not to delete : ")
    if w=="":
        for eachword in _dict["Words"]:
            if eachword==deleted_word :
                del _dict["Words"][deleted_word]
                _dict["Number of Words"]=_dict["Number of Words"]-1
                print(deleted_word,"is deleted.")
                with open("Vocabulary.json", "w") as f:
                    json.dump(_dict,f,indent=4)
                    return 0
        print("We could not find your word to delete! Try again.")
        return 0
    else:
        sys.exit(1)

def _length(_dict):
    if _dict["Number of Words"] == len(_dict["Words"]):
        return _dict["Number of Words"]
    else:
        print("There is a mistake in calculating length.")
        return -1

def _showColor(_dict,word):
    print(_Green,"Word : ", end="")
    print(word)
    print(_Yellow,"Def. : ", end="")
    print(_dict["Words"][word]["Definition"])
    print(_Cyan,"Example : ", end="")
    print(_dict["Words"][word]["Example"],end = "")
    print(_NoColor)

def _screening(_dict,wanted_word): #Screens a word.
    _showColor(_dict,wanted_word)
    _preRepeat=_dict["Words"][wanted_word]["Number of Repeats"]
    _dict["Words"][wanted_word]["Number of Repeats"]=_preRepeat+1
    print(_NoColor,"Reading has been done succesfully.")
    with open("Vocabulary.json", "w") as f:
        json.dump(_dict,f,indent=4)

def _specificword(wanted_word):
    with open("Vocabulary.json", "r") as f:
        _dict= json.load(f)
        for eachword in _dict["Words"]:
            if eachword==wanted_word :
                _screening(_dict,wanted_word)
                return 0
        print("We could not find your word! Try again.")

def _random():
    with open("Vocabulary.json", "r") as f:
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

def _change(changed_word):
    with open("Vocabulary.json", "r") as f:
        _dict= json.load(f)
        for eachword in _dict["Words"]:
            if eachword==changed_word :
                print(_NoColor)
                change_option=input("\tWhat do you want to change?\n" +
                "1-) If the 'Word(Name)' is wrong, press 'w' and Enter. \n" +
                "2-) If the 'Definition' is wrong, press 'd' and Enter. \n" +
                "3-) If the 'Example' is wrong, press 'e' and Enter. \n" +
                "4-) If everything is okay, press Enter. \n")

                new_Name=changed_word
                new_Def=_dict["Words"][changed_word]["Definition"]
                new_Exp=_dict["Words"][changed_word]["Example"]

                if change_option=="" :
                    sys.exit(1)
                elif change_option=="w":
                    print(_Green,"The word is :",changed_word)
                    new_Name=input(" It should be : ").capitalize()
                    print(_NoColor)
                    del _dict["Words"][changed_word]
                    desc=dict()
                    desc["Definition"]=new_Def
                    desc["Example"]=new_Exp
                    desc["Number of Repeats"]=0
                    _dict["Words"][new_Name]=desc
                    with open("Vocabulary.json", "w") as f:
                        json.dump(_dict,f,indent=4)
                        print("The name is changed succesfully.")
                        return 1
                elif change_option=="d":
                    print(_Yellow,"The Definition is :",new_Def)
                    new_Def=input(" It should be : ").capitalize()
                    print(_NoColor)
                    _dict["Words"][new_Name]["Definition"]=new_Def
                    with open("Vocabulary.json", "w") as f:
                        json.dump(_dict,f,indent=4)
                        print("The Definition is changed succesfully.")
                        return 1
                elif change_option=="e":
                    print(_Cyan,"The Example is :",new_Exp)
                    new_Exp=input(" It should be : ").capitalize()
                    print(_NoColor)
                    _dict["Words"][new_Name]["Example"]=new_Exp
                    with open("Vocabulary.json", "w") as f:
                        json.dump(_dict,f,indent=4)
                        print("The Example is changed succesfully.")
                        return 1
                else :
                    print("WARNİNG! You should choose one of the three options.")
                    return _change(changed_word)
        print(_NoColor,"The word does no exist in the vocabulary. Try again! ")
        return 0


#-----------------------------------------------------------------------
_type=input("\n\tWelcome! What do you want?\n" +
"1-) To add word, press 'a' and Enter. \n" +
"2-) To look at a random word, press 'r' and Enter.\n" +
"3-) To look at a specific word, press 's' and Enter.\n"+
"4-) To delete a specific word, press 'd' and Enter.\n"+
"5-) To change something in a specific word, press 'c' and Enter.\n"+
"6-) To learn how many words are in the vocabulary, press 'h' and Enter.\n"+

"My choice is: "
)

if _type=="a" :
    _add()
    sys.exit(1)

elif _type=="r" :
    _random()
    sys.exit(1)

elif _type=="s" :
    wanted_word=input("The word you want to search is : ").capitalize()
    _specificword(wanted_word)
    sys.exit(1)

elif _type=="d" :
    deleted_word=input("The word you want to delete is : ").capitalize()
    _delete(deleted_word)
    sys.exit(1)

elif _type=="h" :
    with open("Vocabulary.json", "r") as f:
        dictionary= json.load(f)
        __length=_length(dictionary)
    print("There are",__length,"words in the vocabulary.")
    sys.exit(1)

elif _type=="c" :
    print(_Green)
    changed_word=input("The word you want to change is : ").capitalize()
    _change(changed_word)
    sys.exit(1)

else :
    print("WARNİNG! You should choose one of the three options. Try again !")
    sys.exit(1)
