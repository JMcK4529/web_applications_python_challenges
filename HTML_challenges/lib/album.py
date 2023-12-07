class Album:
    def __init__(self, id, title, release_year, artist_id):
        self.id = id
        self.title = title
        self.release_year = release_year
        self.artist_id = artist_id

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
        
    def __repr__(self):
        return f"Album({self.id}, {self.title}, " + \
              f"{self.release_year}, {self.artist_id})"
    
    def is_valid(self):
        if None in [self.title, self.release_year, self.artist_id] or \
                    "" in [self.title, self.release_year, self.artist_id]:
            return False
        else:
            return True
    
    def generate_errors(self):
        if self.is_valid():
            return None
        errors = []
        if self.title in [None, ""]:
            errors.append("Title can't be blank.")
        if self.release_year in [None, ""]:
            errors.append("Release year can't be blank.")
        if self.artist_id in [None, ""]:
            errors.append("Artist ID can't be blank.")
        return "\n".join(errors)
        