class Movie:
    #Constructor of the class
    def __init__(self, title, duration, release) -> None:
        self.title = title
        self.duration = duration
        self.release = release
        print(f"The movie {self.title} has been created")

    def __str__(self) -> str:
        return f"{self.title} ({self.release})"

class Catalog:
    movies = []
    #Constructor of the class
    def __init__(self, movies=[]) -> None:
        self.movies = movies

    def add(self, m):
        self.movies.append(m)

    def show(self):
        for m in self.movies:
            print(m)

m = Movie("Doctor Strange", 115, 2017)
catalog1 = Catalog([m])

catalog1.show()

#add to the catalog at the same time that 
catalog1.add(Movie("Doctor Strange: Multiverse of Madness", 126, 2022))

catalog1.show()