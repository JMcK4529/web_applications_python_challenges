class Artist:
    def __init__(self, id, name, genre):
        self.id = id
        self.name = name
        self.genre = genre

    def __repr__(self):
        return f"Artist({self.id}, {self.name}, {self.genre})"
    
    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
    def is_valid(self):
        for attr in [self.name, self.genre]:
            if attr in [None, ""]:
                return False
        return True

    def generate_errors(self):
        errors = []
        if self.name in [None, ""]:
            errors.append("Name can't be empty.")
        if self.genre in [None, ""]:
            errors.append("Genre can't be empty.")
        if len(errors) > 0:
            return " ".join(errors)
        return None