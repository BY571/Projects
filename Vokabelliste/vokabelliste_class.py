import pickle 
import pandas as pd
from googletrans import Translator
import datetime


class Vokabelliste:
    def __init__ (self, language = "englisch", output_language = "deutsch", list_ = []):
        self.language = language
        self.output_language = output_language
        self.list = list_
    

    def erweiter(self):
        print("Vokabelliste erweitern - aktuell {} Wörter enthalten.".format(len(self.list))) 
        while True:
            print("Zum Beenden - Q - Drücken!\n")
            print("Letzte Vokabel löschen - L - Drücken!\n")
            print("Bitte neue Vokabeln eingeben: ")
            a = input(":  ")
            if a.lower() == "q":
                break
            if a.lower() == "l" and self.list > 0:
                del self.list[:-1]
            self.list.append(a)
    
    def länge(self):
        """
        Gibt die länge der aktuellen Liste.
        """
        return len(self.list)
    
    def head(self):
        print(self.list)

    def print_last(self, n = 10):
        """
        Prints the last given words
        Input: nr of "n"  last words
        Out: "n" last words
        """
        print(self.list[len(self.list)-n:])

    def remove_word(self, element):
        """
        Removes the applied word in the list
        """
        if element in self.list: self.list.remove(element)

    def checking_for_multiple(self):
        """
        Prüft ob doppelte Einträge vorhanden sind- falls ja werden diese entfernt
        """
        self.list = list(set(self.list))
    
    def read_pkl_list(self, input_list):
        """
        Lädt eine vorhandene Liste
        """
        try:
            file = open(input_list, "rb")
            self.list = pickle.load(file)
        except:
            print("Liste konnte nicht geladen werden! \nBitte den Namen der Liste überprüfen.")

    def save_as_pkl(self, name = "Vokabelliste.pkl"):
        try:
            output = open(name, 'wb')
            pickle.dump(self.list, output)
            output.close()
            print("Liste wurde als {} gespeichert!".format(name))
        except:
            print("Liste konnte leider nicht gespeicher werden!")
    

    def read_txt_list(self, name):
        try:
            txt_file = open(name, 'r')
            self.list = [line.split(',') for line in txt_file.readlines()]
        except:
            print("Error - Check if Name is a string!")


    def combine_lists(self, liste2 = []):
        try:
            file = open(liste2, "rb")
            liste2 = pickle.load(file)
            for i in liste2:
                if not i in self.list:
                    self.list.append(i)
            print("Die Listen wurden kombiniert! Die kombinierte Liste hat nun: {} Einträge.".format(len(self.list)))
        except:
            print("Combining was incorrect! Check if input variable is a list!")

    def translate_export(self, excel = False, csv = True ):
        """
        Translates the list and exports it as excel or csv file
        Input: excel = bool (default = False), csv = bool (default = False)
        Out: Translated list in xlsx or csv format 
        """
        print("Translation has started: \n")
        # declare Translator
        translator = Translator()
        # define DataFrame
        df = pd.DataFrame(columns=[self.language, self.output_language])
        # read in the list
        df[self.language] = self.list
        #destination Language
        if self.output_language.lower() == "deutsch":
            dest ="de"
        if self.output_language.lower() == "spanisch":
            dest = "es"

        for i in range(len(df[self.language])):
            übersetzung = translator.translate(df[self.language][i], dest = dest)
            df[self.output_language][i] = übersetzung.text
        print("Alle Vokabeln übersetzt!\n")
        if excel == True and csv == False:
            df.to_excel("Übersetzungsliste_{}.xlsx".format(datetime.date.today()), index= False,header=False)
        if csv == True and excel == False:
            df.to_csv("Übersetzungsliste_{}.csv".format(datetime.date.today()), index= False, sep=",", header=False) 
        print("Übersetzung gespeichert!")



            
