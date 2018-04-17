import pickle
import pandas as pd
from googletrans import Translator
import datetime



# intro Main function:
def main():
    #Testing if there is any existing list
    try:
        file = open('list.pkl', "rb")
        old_list = pickle.load(file)
        print(len(old_list))
    except:
        print("Keine alte Liste vorhanden. Sicherstellen das Ordner/Liste vorhanden ist!")
        print("Erstellt automatisch nun eine neue Liste!")
        old_list = []
        #pass
    
    # Menu Loop
    while True:
        print("Hi, was willst du machen?:  \n")
        print("1) Neue Wörter zur Vokabelliste hinzufügen! (press: A)")
        print("2) Speichern der Vokabelliste! (press: B)")
        print("3) Liste Übersetzen und Übersetzungsliste speichern (press: T)")
        print("4) Liste ausgeben (press: O)")
        print("5) Nichts, Danke! (press: Q)")
#**************************************************************************************************
# USER INPUT
        userinput = input()
        # append the old list
        if userinput.lower() == "a":
            print("Erweitern deiner Vokabelliste wird ausgeführt ... ")
            new_list = liste_erweitern(old_list)
            print("Erweiterung der Liste abgeschlossen!\n")
            new_list = liste_prüfen(new_list)
            print("Deine Vokabelliste hat nun {} Einträge!", format(len(new_list)))
        # Saving the new-combined list
        if userinput.lower() == "b":
            try:
                output = open('list.pkl', 'wb')
                pickle.dump(new_list, output)
                output.close()
                print("\nVokabelliste wurde gespeichert!")
            except:
                print("Es wurden bisher keine neuen Vokabeln der Liste hinzugefügt!")
                #pass

        if userinput.lower() == "t":
            try:
                new_list
                if new_list and (len(old_list)>len(new_list)):
                    trans(old_list)
                if new_list and (len(old_list)< len(new_list)):
                    trans(new_list)
                else:
                    trans(old_list)
            except:
                trans(old_list)
            
        
        if userinput.lower() == "o":
            try:
                new_list

                if new_list and len(old_list)>len(new_list):
                    show_list(old_list)
                if new_list and len(old_list)< len(new_list):
                    show_list(new_list)
                else:
                    show_list(old_list)
            except:
                show_list(old_list)

        if userinput.lower() == "q":
            print("Tschüss!")
            break
        else:
            if userinput.lower() != "a" or "q" or "t" or "o" or "b":
                print("Fehlerhafte Eingabe!")

#**************************************************************************************************************
# ACTIONS and FUNCTIONS
def liste_erweitern(old_list):
    print("Erweitere nun deine Vokabelliste: \n")
    
    while True:
        print("In der liste befinden sich aktuell: %d - Woerter"% (len(old_list)))
        print("Beende die Eingabe neuer Vokabeln mit   >""Q""<   ")
        print("Du kannst deinen letzten Eintrag mit   >""L""<    löschen")
        print("Neues Wort eingeben (in Englisch!): \n")
        new = input()
        if new.lower() == "q":
            break
        if new.lower() == "l":
            del old_list[-1]
            pass
        old_list.append(new.lower())

    return(old_list)

def show_list(l):
    print(l)
    print("Die Liste enthält: {} Einträge.".format(len(l)))

def liste_prüfen(l):
    #set: sets list to a dic and removes doubble or multiple items - list: converts dic to a lost
    print("Vokabelliste wird auf mehrfacheinträge geprüft!")
    
    l = list(set(l))
    return l 

def trans(list):
    print("Übersetzung startet: \n")
    # declare Translator
    translator = Translator()
    # define DataFrame
    df = pd.DataFrame(columns=["Englisch", "Deutsch"])
    # read in the list
    df["Englisch"] = list
    for i in range(len(df["Englisch"])):
        #print(data["Englisch"][i])
        übersetzung = translator.translate(df["Englisch"][i],dest = "de")
        df["Deutsch"][i] = übersetzung.text
    print("Alle Vokabeln übersetzt!\n")
    print("Letzten Vokabeln\n", df.tail )
    df.to_excel("Übersetzungsliste_{}.xlsx".format(datetime.date.today()))
    print("Übersetzung gespeichert!")

if __name__ == "__main__":
    main()
