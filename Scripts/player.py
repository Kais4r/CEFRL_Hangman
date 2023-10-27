import sqlite3

class Player:
    def __init__(self, id, name, highestScore, level_A1, level_A2, level_B1, level_B2, level_C1, level_C2, proficiency):
        self.id = id
        self.name = name
        self.highestScore = highestScore
        self.level_A1 = level_A1
        self.level_A2 = level_A2
        self.level_B1 = level_B1
        self.level_B2 = level_B2
        self.level_C1 = level_C1
        self.level_C2 = level_C2
        self.proficiency = proficiency
    
    def AccessPlayerData(self, id):
        #Access PlayerData
        conn = sqlite3.connect('data.db')
        cursor = conn.execute("SELECT id, name, highestScore, level_A1, level_A2, level_B1, level_B2, level_C1, level_C2, proficiency from PLAYER where id = " + str(id))
        for row in cursor:
            # new_word = EnglishWord(row[0],row[1],row[2],row[3],row[4],row[5])
            # self.list.append(new_word)
            self.id = row[0]
            self.name = row[1]
            self.highestScore = row[2]
            self.level_A1 = row[3]
            self.level_A2 = row[4]
            self.level_B1 = row[5]
            self.level_B2 = row[6]
            self.level_C1 = row[7]
            self.level_C2 = row[8]
            self.proficiency = row[9]

        #print("row[1] = " + str(row[1]))
        conn.close()
    
    def UpdateHighestScore(self, score):
        self.highestScore = score

        conn = sqlite3.connect('data.db')
        cursor = conn.cursor()
        cursor.execute("UPDATE PLAYER SET highestScore = ? WHERE id = ?", (str(score), str(self.id)))

        conn.commit()
        print("Player data updated successfully")
        conn.close()
        