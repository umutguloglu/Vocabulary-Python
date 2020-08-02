import json
import sys
# This part can be changed according to your preferences.
# Use "\33[0m" for no color option.
_Green="\33[32m"  #_Green="\33[0m"
_Yellow="\33[33m" #_Yellow="\33[0m"
_Cyan="\33[36m"   #_Cyan="\33[0m"
_NoColor="\33[0m"

def _control(new_Name,new_Def,new_Exp):
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
        desc=dict()
        desc["Definition"]=new_Def
        desc["Examples"]=new_Exp
        desc["Number of Repeats"]=0
        with open("sample.json", "w") as f:
            _dict["Words"][new_Name]=desc
            _dict["Number of Words"]=_dict["Number of Words"]
            json.dump(_dict,f,indent=4)
    elif cntrl=="w" :
        new_Name=input("Write the new name: ")
        for eachword in _dict["Words"]:
            if eachword==new_Name :
                print("This word is already exist in the dictionary.")
                sys.exit(1)
        return _control(new_Name,new_Def,new_Exp)
    elif cntrl=="d" :
        new_Def=input("Write the new name: ")
        return _control(new_Name,new_Def,new_Exp)
    elif cntrl=="e" :
        new_Exp=input("Write the new name: ")
        return _control(new_Name,new_Def,new_Exp)
    else :
        print("WARNİNG! You should choose one of the three options.")
        return _control(new_Name,new_Def,new_Exp)


new_Name="Umut"
new_Def="Human"
new_Exp="HomoSaphiens"

_control(new_Name,new_Def,new_Exp)
