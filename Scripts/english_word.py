class EnglishWord:
    def __init__(self, id, name, meaning, description, synonym, level):
        self.id = id
        self.name = name
        self.meaning = meaning
        self.description = description
        self.synonym = synonym
        self.level = level
    def __str__(self):
        return f"{self.id},{self.name},{self.meaning},{self.description},{self.synonym},{self.level}"