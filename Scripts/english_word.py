class EnglishWord:
    def __init__(self, id, name, meaning, discription, synonym, level):
        self.id = id
        self.name = name
        self.meaning = meaning
        self.discription = discription
        self.synonym = synonym
        self.level = level
    def __str__(self):
        return f"{self.id},{self.name},{self.meaning},{self.discription},{self.synonym},{self.level}"