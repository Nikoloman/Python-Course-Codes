from io import open
import pickle

class Movie:

    # Constructor of class
    def __init__(self, tittle, duration, release) -> None:
        self.tittle = tittle
        self.duration = duration
        self.release = release
        print(f"The movie {self.tittle} has been created")

    def __str__(self) -> str:
        return f"{self.tittle} ({self.release})"

class Catalog:

    movies = []

    # Constructor of class
    def __init__(self, movies = []) -> None:
        self.load()
    
    def add(self, m):
        self.movies.append(m)
        self.save() # Automatic save

    def show(self):
        if len(self.movies) == 0:
            print("The catalog is empty")
            return
        for m in self.movies:
            print(m)

    def load(self):
        file = open("catalog.pckl", "ab+") # Append, binary, and Read
        file.seek(0)
        try:
            self.movies = pickle.load(file)
        except:
            print("The file is empty")
        finally:
            file.close()
            print(f"{len(self.movies)} movies has been loaded")

    def save(self):
        file = open("catalog.pckl", "wb")
        pickle.dump(self.movies, file)
        file.close() 