import sqlite3
from Scripts.english_word import EnglishWord

class EnglishWord_List:
    def __init__(self):
        self.list = []

    # list = []

    # # appending instances to list
    # list.append(geeks('Akash', 2))
    # list.append(geeks('Deependra', 40))

    def GenerateList(self, level):
        conn = sqlite3.connect('data.db')
        # print("Opened database successfully")
        cursor = conn.execute(
            "SELECT id, name, meaning, discription, synonym, level from " + level)
        for row in cursor:
            new_word = EnglishWord(row[0],row[1],row[2],row[3],row[4],row[5])
            self.list.append(new_word) 

        print("Operation done successfully")
        conn.close()
